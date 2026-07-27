"""RAG 查询与索引管理 API（从原 rag_routes.py 拆分）

拆分后的模块：
- rag_routes.py：RAG 服务实例、状态查询、知识库检索、流式查询、索引重建、分块预览、历史索引
- rag_document_routes.py：知识文档上传/列表/更新/删除/文本块查看
- rag_conversation_routes.py：多轮对话会话 CRUD 与上下文查询
"""

import json
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.config import settings
from backend.core.security import get_current_user, assert_teacher_or_admin
from backend.models.tables import Report, ChatMessage, RegisteredPerson
from backend.models.schemas import RAGQueryRequest, RAGQueryResponse
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
def query_knowledge(
    request: RAGQueryRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """查询知识库（按用户可见性过滤，生成前过滤防止内容泄露）"""
    try:
        from backend.core.access import visible_doc_ids
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
    from backend.core.access import visible_doc_ids
    service = get_rag_service()
    visible_ids = visible_doc_ids(db, current_user)

    def event_stream():
        try:
            for event in service.stream_query(request.question, request.top_k, visible_doc_ids=visible_ids):
                yield f"data: {json.dumps(event, ensure_ascii=False)}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


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
        "indexed_chats": len(chat_contents),
        "total_chunks": len(all_chunks),
    }
