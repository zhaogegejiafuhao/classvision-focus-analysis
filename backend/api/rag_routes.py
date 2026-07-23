"""RAG API接口"""

import os
import json
import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.config import settings
from backend.core.security import get_current_user, assert_teacher_or_admin
from backend.core.access import visible_doc_ids, filter_visible_docs
from backend.models.tables import KnowledgeDocument, KnowledgeChunk, Report, ChatMessage, RegisteredPerson
from backend.models.schemas import RAGQueryRequest, RAGQueryResponse, KnowledgeDocumentOut
from rag.knowledge_base import KnowledgeBase, get_knowledge_base
from rag.rag_service import RAGService
from rag.conversation_service import ConversationService, is_followup, build_context_messages

router = APIRouter(prefix="/api/rag", tags=["rag"])

VALID_VISIBILITY = {"public", "staff", "private"}

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
def query_knowledge(
    request: RAGQueryRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """查询知识库（按用户可见性过滤，生成前过滤防止内容泄露）"""
    try:
        service = get_rag_service()
        visible_ids = visible_doc_ids(db, current_user)
        result = service.query(request.question, request.top_k, visible_doc_ids=visible_ids)
        return RAGQueryResponse(
            answer=result['answer'],
            sources=result['sources'],
            retrieved_chunks=result['retrieved_chunks'],
        )
    except Exception as e:
        raise HTTPException(500, f"RAG查询失败: {e}")


@router.post("/query/stream")
async def query_knowledge_stream(
    request: RAGQueryRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """流式查询知识库：SSE 逐字返回回答，生成前按可见性过滤防止内容泄露"""
    service = get_rag_service()
    visible_ids = visible_doc_ids(db, current_user)

    def event_stream():
        try:
            for event in service.stream_query(request.question, request.top_k, visible_doc_ids=visible_ids):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


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


@router.post("/rebuild")
def rebuild_index(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """从数据库重建索引：补充 document_id 元数据 + 清理已删除向量。

    旧索引（无 document_id）需执行一次本接口，后续删除才能生效。
    仅管理员/教师可操作。
    """
    assert_teacher_or_admin(current_user)
    service = get_rag_service()
    result = service.rebuild_index(db)
    return result


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


class ChunkPreviewRequest(BaseModel):
    text: str
    strategy: Optional[str] = None


@router.post("/chunk-preview")
def chunk_preview(
    req: ChunkPreviewRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """分块预览调试工具（WeKnora 风格）：离线调试，不写入数据库/索引

    支持粘贴 Markdown/纯文本片段，输出：
    - 生效策略标签及降级原因
    - 文档结构分析数据
    - 全量分块统计（均值/最值/标准差）
    - 单块详情（字符数/位置/层级面包屑/内容预览）
    - 父子分块预览（如果启用）
    """
    if not req.text or not req.text.strip():
        raise HTTPException(400, "请输入待测试文本")
    if len(req.text) > 65536:  # 64KB 限制
        raise HTTPException(400, "文本过长，最大 64KB")

    kb = get_knowledge_base()

    try:
        # 基础分块预览
        preview = kb.preview_chunks(req.text, strategy=req.strategy)

        # 父子分块预览（如果启用）
        parent_child_preview = None
        if settings.RAG_PARENT_CHILD_ENABLED:
            pc_result = kb.split_into_parent_child(req.text, strategy=req.strategy)
            parent_sizes = [len(p['content']) for p in pc_result['parents']]
            child_sizes = [len(c['content']) for c in pc_result['children']]
            import statistics
            parent_child_preview = {
                'parent_count': len(pc_result['parents']),
                'child_count': len(pc_result['children']),
                'parent_avg_chars': round(statistics.mean(parent_sizes), 1) if parent_sizes else 0,
                'child_avg_chars': round(statistics.mean(child_sizes), 1) if child_sizes else 0,
                'parents': [
                    {
                        'index': p['index'],
                        'chars': len(p['content']),
                        'content_preview': p['content'][:200] + ('...' if len(p['content']) > 200 else ''),
                    }
                    for p in pc_result['parents'][:20]  # 最多显示20个
                ],
                'children': [
                    {
                        'parent_index': c['parent_index'],
                        'chars': len(c['content']),
                        'content_preview': c['content'][:100] + ('...' if len(c['content']) > 100 else ''),
                    }
                    for c in pc_result['children'][:30]  # 最多显示30个
                ],
            }

        return {
            **preview,
            'parent_child': parent_child_preview,
            'config': {
                'chunk_size': settings.RAG_CHUNK_SIZE,
                'chunk_overlap': settings.RAG_CHUNK_OVERLAP,
                'strategy': settings.RAG_CHUNK_STRATEGY,
                'parent_child_enabled': settings.RAG_PARENT_CHILD_ENABLED,
                'parent_chunk_size': settings.RAG_PARENT_CHUNK_SIZE if settings.RAG_PARENT_CHILD_ENABLED else None,
                'child_chunk_size': settings.RAG_CHILD_CHUNK_SIZE if settings.RAG_PARENT_CHILD_ENABLED else None,
                'embedding_token_limit': settings.RAG_EMBEDDING_TOKEN_LIMIT,
            },
        }
    except Exception as e:
        raise HTTPException(500, f"分块预览失败: {e}")


@router.post("/index/history")
def index_history_data(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """索引历史课堂数据（报告和对话）— 仅管理员/教师可操作"""
    assert_teacher_or_admin(current_user)
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


# ===== 多轮对话 API =====

class ConversationCreateRequest(BaseModel):
    title: Optional[str] = "新对话"


class ConversationQueryRequest(BaseModel):
    question: str
    conversation_id: Optional[int] = None
    top_k: Optional[int] = None


class ConversationOut(BaseModel):
    id: int
    title: str
    state: str
    created_at: str
    updated_at: str
    message_count: int = 0

    model_config = {"from_attributes": True}


class MessageOut(BaseModel):
    id: int
    role: str
    content: str
    is_followup: bool
    timestamp: str

    model_config = {"from_attributes": True}


class ConversationQueryResponse(BaseModel):
    answer: str
    sources: list = []
    retrieved_chunks: list = []
    is_followup: bool = False
    conversation_id: int
    message_id: int


@router.get("/conversations", response_model=list[ConversationOut])
def list_conversations(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """列出当前用户的所有 RAG 对话会话"""
    svc = ConversationService(db)
    convs = svc.list_conversations(current_user.id)
    return [
        ConversationOut(
            id=c.id,
            title=c.title,
            state=c.state,
            created_at=c.created_at.isoformat(),
            updated_at=c.updated_at.isoformat(),
            message_count=len(c.messages),
        )
        for c in convs
    ]


@router.post("/conversations", response_model=ConversationOut)
def create_conversation(
    req: ConversationCreateRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建新对话会话"""
    svc = ConversationService(db)
    conv = svc.create_conversation(current_user.id, req.title)
    return ConversationOut(
        id=conv.id,
        title=conv.title,
        state=conv.state,
        created_at=conv.created_at.isoformat(),
        updated_at=conv.updated_at.isoformat(),
        message_count=0,
    )


@router.get("/conversations/{conv_id}/messages", response_model=list[MessageOut])
def get_conversation_messages(
    conv_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取对话历史消息"""
    svc = ConversationService(db)
    conv = svc.get_conversation(conv_id, current_user.id)
    if not conv:
        raise HTTPException(404, "对话不存在")
    messages = svc.get_history(conv_id)
    return [
        MessageOut(
            id=m.id,
            role=m.role,
            content=m.content,
            is_followup=m.is_followup,
            timestamp=m.timestamp.isoformat(),
        )
        for m in messages
    ]


@router.delete("/conversations/{conv_id}")
def delete_conversation(
    conv_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除对话会话"""
    svc = ConversationService(db)
    if not svc.delete_conversation(conv_id, current_user.id):
        raise HTTPException(404, "对话不存在")
    return {"message": "对话已删除"}


@router.post("/conversations/query", response_model=ConversationQueryResponse)
def conversation_query(
    req: ConversationQueryRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """多轮对话查询：支持上下文历史和追问识别

    流程：
    1. 如果无 conversation_id，创建新会话
    2. 判断是否为追问（基于关键词 + 历史对话）
    3. 追问：不检索，直接用历史上下文回答
    4. 新问题：混合检索 + 重排 + 带历史上下文生成
    5. 保存用户问题和 assistant 回答到会话
    """
    svc = ConversationService(db)

    # 获取或创建会话
    if req.conversation_id:
        conv = svc.get_conversation(req.conversation_id, current_user.id)
        if not conv:
            raise HTTPException(404, "对话不存在")
    else:
        conv = svc.create_conversation(current_user.id)

    # 判断是否为追问
    followup = is_followup(req.question, conv)

    # 构建历史上下文
    history = build_context_messages(conv)

    # 可见文档过滤
    visible_ids = visible_doc_ids(db, current_user)

    # 调用 RAG 服务（带上下文）
    rag_service = get_rag_service()
    result = rag_service.query_with_context(
        question=req.question,
        history_messages=history,
        is_followup_flag=followup,
        top_k=req.top_k,
        visible_doc_ids=visible_ids,
    )

    # 保存用户消息
    user_msg = svc.add_message(conv.id, "user", req.question, is_followup_flag=followup)
    # 保存 assistant 回答
    assistant_msg = svc.add_message(
        conv.id,
        "assistant",
        result['answer'],
        retrieved_chunks=result.get('retrieved_chunks', []),
        is_followup_flag=followup,
    )

    return ConversationQueryResponse(
        answer=result['answer'],
        sources=result.get('sources', []),
        retrieved_chunks=result.get('retrieved_chunks', []),
        is_followup=result.get('is_followup', False),
        conversation_id=conv.id,
        message_id=assistant_msg.id,
    )