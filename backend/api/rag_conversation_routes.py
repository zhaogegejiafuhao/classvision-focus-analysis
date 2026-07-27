"""RAG 多轮对话 API（从 rag_routes.py 拆分）

包含对话会话的 CRUD 和多轮对话查询（支持上下文历史和追问识别）。
"""
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.core.access import visible_doc_ids
from backend.models.tables import RegisteredPerson
from rag.conversation_service import ConversationService, is_followup, build_context_messages

from backend.api.rag_routes import get_rag_service

router = APIRouter(prefix="/api/rag", tags=["rag"])


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
