"""RAG 知识文档管理 API（从 rag_routes.py 拆分）

包含文档的上传、列表、更新、删除和文本块查看。
"""
import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.config import settings
from backend.core.security import get_current_user
from backend.core.access import visible_doc_ids, filter_visible_docs
from backend.models.tables import KnowledgeDocument, KnowledgeChunk, RegisteredPerson
from backend.models.schemas import KnowledgeDocumentOut
from rag.knowledge_base import get_knowledge_base

from backend.api.rag_routes import get_rag_service

router = APIRouter(prefix="/api/rag", tags=["rag"])

VALID_VISIBILITY = {"public", "staff", "private"}


@router.post("/upload")
async def upload_knowledge(
    file: UploadFile = File(...),
    visibility: str = Form("private"),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """上传知识文档（所有角色可上传，学生只能 private，支持父子分块）"""
    if visibility not in VALID_VISIBILITY:
        raise HTTPException(400, f"无效的可见性，可选: {VALID_VISIBILITY}")
    # 学生只能上传 private
    if current_user.role == "student" and visibility != "private":
        raise HTTPException(403, "学生只能上传私有文档")
    # 检查文件类型
    allowed_types = ['.pdf', '.txt', '.md', '.docx', '.pptx']
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_types:
        raise HTTPException(400, f"不支持的文件类型: {ext}")

    # 保存文件（使用安全的文件名，防止路径遍历）
    save_dir = settings.RAG_KNOWLEDGE_DIR
    os.makedirs(save_dir, exist_ok=True)
    # 仅取文件名部分，移除路径分隔符
    safe_filename = os.path.basename(file.filename or "unnamed")
    file_id = str(uuid.uuid4())
    ext = os.path.splitext(safe_filename)[1].lower()
    file_path = os.path.join(save_dir, f"{file_id}{ext}")

    with open(file_path, 'wb') as f:
        content = await file.read()
        f.write(content)

    # 解析文件
    kb = get_knowledge_base()
    service = get_rag_service()

    if settings.RAG_PARENT_CHILD_ENABLED:
        # 父子分块模式
        full_text = None
        if ext == '.pdf':
            full_text = kb.parse_pdf(file_path)
        elif ext == '.txt':
            full_text = kb.parse_txt(file_path)
        elif ext == '.md':
            full_text = kb.parse_md(file_path)
        elif ext == '.docx':
            full_text = kb.parse_docx(file_path)
        elif ext == '.pptx':
            full_text = kb.parse_pptx(file_path)

        if not full_text:
            raise HTTPException(400, "文件解析失败，没有提取到文本")

        result = kb.split_into_parent_child(full_text)
        parents = result['parents']
        children = result['children']

        if not children:
            raise HTTPException(400, "文件解析失败，没有提取到文本")

        # 先保存文档到数据库
        doc = KnowledgeDocument(
            filename=file.filename,
            file_path=file_path,
            file_type=ext.replace('.', ''),
            total_chunks=len(parents) + len(children),
            indexed=True,
            uploaded_by=current_user.id,
            visibility=visibility,
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)

        # 先存父分块到数据库，拿到 DB id
        parent_db_ids = []
        for p_idx, parent in enumerate(parents):
            parent_record = KnowledgeChunk(
                document_id=doc.id,
                chunk_index=p_idx,
                content=parent['content'],
                embedding_stored=False,  # 父分块不进 FAISS
                is_parent=True,
            )
            db.add(parent_record)
            db.flush()
            parent_db_ids.append(parent_record.id)

        # 再存子分块到数据库
        for c_idx, child in enumerate(children):
            p_idx = child['parent_index']
            parent_db_id = parent_db_ids[p_idx] if p_idx < len(parent_db_ids) else None
            db.add(KnowledgeChunk(
                document_id=doc.id,
                chunk_index=len(parents) + c_idx,
                content=child['content'],
                embedding_stored=True,
                is_parent=False,
                parent_chunk_id=parent_db_id,
            ))
        db.commit()

        # 添加到索引（子分块进 FAISS + BM25，父分块进 parent_store）
        service.add_knowledge_parent_child(
            parents, children, source=file.filename, document_id=doc.id
        )

        return {
            "id": doc.id,
            "filename": file.filename,
            "total_chunks": len(parents) + len(children),
            "parent_chunks": len(parents),
            "child_chunks": len(children),
            "indexed": True,
            "visibility": visibility,
            "uploaded_by": current_user.id,
        }
    else:
        # 单层分块模式（向后兼容）
        chunks_meta = kb.process_file_with_metadata(file_path)

        if not chunks_meta:
            raise HTTPException(400, "文件解析失败，没有提取到文本")

        doc = KnowledgeDocument(
            filename=file.filename,
            file_path=file_path,
            file_type=ext.replace('.', ''),
            total_chunks=len(chunks_meta),
            indexed=True,
            uploaded_by=current_user.id,
            visibility=visibility,
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)

        # 添加到 FAISS + BM25 索引
        service.add_knowledge(chunks_meta, source=file.filename, document_id=doc.id)

        # 保存文本块到数据库
        for i, chunk in enumerate(chunks_meta):
            chunk_record = KnowledgeChunk(
                document_id=doc.id,
                chunk_index=i,
                content=chunk['content'],
                embedding_stored=True,
            )
            db.add(chunk_record)
        db.commit()

        return {
            "id": doc.id,
            "filename": file.filename,
            "total_chunks": len(chunks_meta),
            "indexed": True,
            "visibility": visibility,
            "uploaded_by": current_user.id,
        }


@router.get("/documents", response_model=List[KnowledgeDocumentOut])
def list_documents(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前用户可见的知识文档"""
    q = db.query(KnowledgeDocument)
    q = filter_visible_docs(q, current_user)
    docs = q.order_by(KnowledgeDocument.created_at.desc()).all()

    # 批量获取上传者姓名
    uploader_ids = {d.uploaded_by for d in docs if d.uploaded_by}
    uploader_map = {}
    if uploader_ids:
        persons = db.query(RegisteredPerson).filter(RegisteredPerson.id.in_(uploader_ids)).all()
        uploader_map = {p.id: p.name for p in persons}

    result = []
    for d in docs:
        result.append(KnowledgeDocumentOut(
            id=d.id,
            filename=d.filename,
            file_type=d.file_type,
            total_chunks=d.total_chunks,
            indexed=d.indexed,
            created_at=d.created_at,
            uploaded_by=d.uploaded_by,
            uploader_name=uploader_map.get(d.uploaded_by, None),
            visibility=d.visibility or "private",
        ))
    return result


@router.put("/documents/{document_id}")
def update_document(
    document_id: int,
    filename: str = None,
    visibility: str = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """重命名或修改可见性（上传者或管理员）"""
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(404, "文档不存在")
    # 权限：上传者本人或 admin
    if doc.uploaded_by != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "仅上传者或管理员可修改")
    if filename:
        doc.filename = filename
    if visibility:
        if visibility not in VALID_VISIBILITY:
            raise HTTPException(400, f"无效的可见性，可选: {VALID_VISIBILITY}")
        if current_user.role == "student" and visibility != "private":
            raise HTTPException(403, "学生文档只能为私有")
        doc.visibility = visibility
    db.commit()
    db.refresh(doc)
    return doc


@router.delete("/documents/{document_id}")
def delete_document(
    document_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除知识文档（上传者或管理员）"""
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(404, "文档不存在")
    # 权限：上传者本人或 admin
    if doc.uploaded_by != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "仅上传者或管理员可删除")

    # 软删除 FAISS 索引中的向量
    removed = 0
    try:
        service = get_rag_service()
        removed = service.remove_document(document_id)
    except Exception as e:
        print(f"软删除索引向量失败: {e}")

    # 删除文件
    if os.path.exists(doc.file_path):
        os.remove(doc.file_path)

    # 删除数据库记录
    db.query(KnowledgeChunk).filter(KnowledgeChunk.document_id == document_id).delete()
    db.delete(doc)
    db.commit()

    return {"message": "文档已删除", "vectors_removed": removed}


@router.get("/documents/{document_id}/chunks")
def get_document_chunks(
    document_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取文档的文本块列表，用于预览解析结果"""
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(404, "文档不存在")
    # 可见性校验：非管理员必须对文档有可见权限
    visible_ids = visible_doc_ids(db, current_user)
    if document_id not in visible_ids:
        raise HTTPException(403, "无权访问该文档")
    chunks = db.query(KnowledgeChunk).filter(
        KnowledgeChunk.document_id == document_id
    ).order_by(KnowledgeChunk.chunk_index).all()
    return {
        "document": {"id": doc.id, "filename": doc.filename, "total_chunks": doc.total_chunks},
        "chunks": [
            {
                "index": c.chunk_index,
                "content": c.content,
                "is_parent": c.is_parent,
                "parent_chunk_id": c.parent_chunk_id,
            }
            for c in chunks
        ],
    }
