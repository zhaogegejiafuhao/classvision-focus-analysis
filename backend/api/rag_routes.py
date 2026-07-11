"""RAG API接口"""

import os
import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.config import settings
from backend.core.security import get_current_user, assert_teacher_or_admin
from backend.models.tables import KnowledgeDocument, KnowledgeChunk, Report, ChatMessage, RegisteredPerson
from backend.models.schemas import RAGQueryRequest, RAGQueryResponse, KnowledgeDocumentOut
from rag.knowledge_base import KnowledgeBase, get_knowledge_base
from rag.rag_service import RAGService

router = APIRouter(prefix="/api/rag", tags=["rag"])

# RAG服务实例（懒加载）
_rag_service: RAGService | None = None


def get_rag_service() -> RAGService:
    """获取RAG服务实例"""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service


@router.get("/status")
def get_rag_status():
    """获取RAG索引状态"""
    try:
        service = get_rag_service()
        return service.get_status()
    except Exception as e:
        return {"error": str(e), "total_vectors": 0}


@router.post("/query", response_model=RAGQueryResponse)
def query_knowledge(request: RAGQueryRequest, db: Session = Depends(get_db)):
    """查询知识库"""
    try:
        service = get_rag_service()
        result = service.query(request.question, request.top_k)
        return RAGQueryResponse(
            answer=result['answer'],
            sources=result['sources'],
            retrieved_chunks=result['retrieved_chunks'],
        )
    except Exception as e:
        raise HTTPException(500, f"RAG查询失败: {e}")


@router.post("/query/stream")
async def query_knowledge_stream(request: RAGQueryRequest):
    """流式查询知识库：SSE 逐字返回回答，先发检索到的参考来源"""
    service = get_rag_service()

    def event_stream():
        try:
            for event in service.stream_query(request.question, request.top_k):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@router.post("/upload")
async def upload_knowledge(
    file: UploadFile = File(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """上传知识文档（教师/管理员）"""
    assert_teacher_or_admin(current_user)
    # 检查文件类型
    allowed_types = ['.pdf', '.txt', '.md', '.docx', '.pptx']
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_types:
        raise HTTPException(400, f"不支持的文件类型: {ext}")

    # 保存文件
    save_dir = settings.RAG_KNOWLEDGE_DIR
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, file.filename)

    with open(file_path, 'wb') as f:
        content = await file.read()
        f.write(content)

    # 解析文件
    kb = get_knowledge_base()
    chunks = kb.process_file(file_path)

    if not chunks:
        raise HTTPException(400, "文件解析失败，没有提取到文本")

    # 先保存到数据库，拿到 doc.id
    doc = KnowledgeDocument(
        filename=file.filename,
        file_path=file_path,
        file_type=ext.replace('.', ''),
        total_chunks=len(chunks),
        indexed=True,
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    # 添加到 FAISS 索引（带 document_id，便于后续删除）
    service = get_rag_service()
    service.add_knowledge(chunks, source=file.filename, document_id=doc.id)

    # 保存文本块到数据库
    for i, chunk in enumerate(chunks):
        chunk_record = KnowledgeChunk(
            document_id=doc.id,
            chunk_index=i,
            content=chunk,
            embedding_stored=True,
        )
        db.add(chunk_record)
    db.commit()

    return {
        "id": doc.id,
        "filename": file.filename,
        "total_chunks": len(chunks),
        "indexed": True,
    }


@router.get("/documents", response_model=List[KnowledgeDocumentOut])
def list_documents(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取所有知识文档"""
    return db.query(KnowledgeDocument).order_by(KnowledgeDocument.created_at.desc()).all()


@router.put("/documents/{document_id}")
def update_document(
    document_id: int,
    filename: str = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """重命名知识文档（教师/管理员）"""
    assert_teacher_or_admin(current_user)
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(404, "文档不存在")
    if filename:
        doc.filename = filename
    db.commit()
    db.refresh(doc)
    return doc


@router.delete("/documents/{document_id}")
def delete_document(
    document_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除知识文档（教师/管理员）"""
    assert_teacher_or_admin(current_user)
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(404, "文档不存在")

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


@router.post("/rebuild")
def rebuild_index(db: Session = Depends(get_db)):
    """从数据库重建索引：补充 document_id 元数据 + 清理已删除向量。

    旧索引（无 document_id）需执行一次本接口，后续删除才能生效。
    """
    service = get_rag_service()
    result = service.rebuild_index(db)
    return result


@router.get("/documents/{document_id}/chunks")
def get_document_chunks(document_id: int, db: Session = Depends(get_db)):
    """获取文档的文本块列表，用于预览解析结果"""
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(404, "文档不存在")
    chunks = db.query(KnowledgeChunk).filter(
        KnowledgeChunk.document_id == document_id
    ).order_by(KnowledgeChunk.chunk_index).all()
    return {
        "document": {"id": doc.id, "filename": doc.filename, "total_chunks": doc.total_chunks},
        "chunks": [{"index": c.chunk_index, "content": c.content} for c in chunks],
    }


@router.post("/index/history")
def index_history_data(db: Session = Depends(get_db)):
    """索引历史课堂数据（报告和对话）"""
    # 获取所有报告
    reports = db.query(Report).all()
    report_contents = [r.content for r in reports if r.content]

    # 获取所有对话
    messages = db.query(ChatMessage).all()
    chat_contents = [m.content for m in messages if m.content]

    # 合并内容
    all_contents = report_contents + chat_contents

    if not all_contents:
        return {"message": "没有历史数据需要索引"}

    # 分块并索引
    kb = get_knowledge_base()
    all_chunks = []
    for content in all_contents:
        chunks = kb.split_into_chunks(content)
        all_chunks.extend(chunks)

    # 添加到索引
    service = get_rag_service()
    service.add_knowledge(all_chunks, source="历史数据")

    return {
        "indexed_reports": len(report_contents),
        "indexed_messages": len(chat_contents),
        "total_chunks": len(all_chunks),
    }