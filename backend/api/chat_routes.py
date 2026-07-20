from datetime import datetime
import os
import json
import re
import tempfile

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.core.database import get_db
from backend.core.config import settings
from backend.core.security import get_current_user
from backend.api.stats_routes import _assert_classroom_access
from backend.models.tables import Classroom, ChatMessage, Report, Student, AttentionRecord, ExamRiskRecord, RegisteredPerson
from backend.models.schemas import ChatRequest, ChatMessageOut
from backend.services.llm_client import get_llm, LLMError

router = APIRouter(prefix="/api/classrooms", tags=["chat"])

# 课堂对话最大历史轮数（防止 token 爆炸）
MAX_CLASSROOM_HISTORY_TURNS = 10



def _build_system_prompt(classroom: Classroom, db: Session) -> str:
    """构建系统提示词，包含课堂数据"""
    stats = _get_classroom_stats(classroom, db)
    report_content = ""
    if classroom.report:
        report_content = classroom.report.content

    return f"""你是资深教学分析专家。基于以下课堂数据进行对话分析。

【权威数据 — 以下课堂数据来自数据库，是唯一事实依据，不得编造或修改】

课堂数据：
- 课堂名称：{classroom.name}
- 教师：{classroom.teacher}
- 总人数：{classroom.total_students}
- 平均注意力：{classroom.avg_attention}分
- 课堂时长：{classroom.duration}分钟
- 低头人次：{stats['head_down_count']}
- 转头人次：{stats['head_turn_count']}
- 疲劳人次：{stats['fatigue_count']}
- 考场模式：{classroom.exam_mode}

已生成的分析报告：
{report_content}

【回答规则】
1. 只回答当前用户问题，不要描述思考过程（如"首先我需要..."、"让我分析..."），不要在回答开头重复或引用历史对话中的内容
2. 引用课堂数据时，必须使用以上权威数据，不得编造或使用历史对话中的数字
3. 区分两类问题：
   - 课堂数据查询：用户询问当前课堂的具体数据（如人数、注意力分、低头人次等），必须用以上权威数据回答；如果数据项不在列表中，说明"当前数据中未提供此信息"
   - 通用知识问题：用户询问方法论、技术原理、改进建议等通用问题（如"注意力检测的方法有哪些""如何提高学生注意力"），基于你的专业知识回答，无需引用课堂数据
4. 知识库参考内容（如有）仅为辅助线索，可用于补充通用知识
5. 回答要专业、客观、有针对性，控制在300字以内"""


def _get_classroom_stats(classroom: Classroom, db: Session) -> dict:
    """获取课堂统计数据"""
    records = db.query(AttentionRecord).filter(
        AttentionRecord.classroom_id == classroom.id
    ).all()

    student_ids = db.query(func.distinct(AttentionRecord.student_id)).filter(
        AttentionRecord.classroom_id == classroom.id
    ).all()

    head_down_count = 0
    head_turn_count = 0
    fatigue_count = 0
    for (sid,) in student_ids:
        student_records = [r for r in records if r.student_id == sid]
        if any(abs(r.pitch) > 15 for r in student_records):
            head_down_count += 1
        if any(abs(r.yaw) > 20 for r in student_records):
            head_turn_count += 1
        if any(r.is_blinking for r in student_records):
            fatigue_count += 1

    return {
        "head_down_count": head_down_count,
        "head_turn_count": head_turn_count,
        "fatigue_count": fatigue_count,
    }


def _call_llm(system_prompt: str, messages: list[dict], mode: str = "fast") -> str:
    """调用 LLM 生成回复"""
    llm = get_llm(mode)
    num_predict = 1536 if mode == "deep" else 1280
    full_messages = [{"role": "system", "content": system_prompt}, *messages]
    # 只在 Ollama 下启用 think（云端 API 不支持）
    think = settings.LLM_PROVIDER == "ollama"
    result = llm.chat(full_messages, max_tokens=num_predict, think=think, temperature=0.7)
    return result["content"]


def _llm_stream(system_prompt: str, messages: list[dict], mode: str = "fast"):
    """流式调用 LLM，逐块 yield content 增量"""
    llm = get_llm(mode)
    num_predict = 1536 if mode == "deep" else 1280
    full_messages = [{"role": "system", "content": system_prompt}, *messages]
    think = settings.LLM_PROVIDER == "ollama"
    for chunk in llm.stream(full_messages, max_tokens=num_predict, think=think, temperature=0.7):
        if chunk["done"]:
            break
        content = chunk["content"]
        if content:
            yield content


@router.post("/{classroom_id}/chat", response_model=ChatMessageOut)
def send_chat(
    classroom_id: int,
    data: ChatRequest,
    db: Session = Depends(get_db),
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """发送用户消息，返回 AI 回复"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    _assert_classroom_access(classroom, current_user, db)

    # 保存用户消息
    user_msg = ChatMessage(
        classroom_id=classroom_id,
        role="user",
        content=data.content,
    )
    db.add(user_msg)
    db.commit()

    # 获取历史对话（仅保留最近 MAX_CLASSROOM_HISTORY_TURNS 轮，防止 token 爆炸）
    history = db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.desc()).limit(MAX_CLASSROOM_HISTORY_TURNS * 2).all()
    history = list(reversed(history))

    messages = [{"role": m.role, "content": m.content} for m in history]

    # 构建系统提示词
    system_prompt = _build_system_prompt(classroom, db)

    # RAG检索：按当前用户可见性过滤，防止私有文档内容泄露
    rag_context = ""
    try:
        from backend.api.rag_routes import get_rag_service, _visible_doc_ids
        rag_service = get_rag_service()
        visible_ids = _visible_doc_ids(db, current_user)
        rag_results = rag_service.retrieve_only(
            data.content, top_k=3, visible_doc_ids=visible_ids, mode=data.mode,
        )
        if rag_results.get('retrieved_chunks'):
            rag_context = "\n\n--- 知识库参考内容 ---\n"
            for i, chunk in enumerate(rag_results['retrieved_chunks'], 1):
                rag_context += f"\n[参考{i}] (来源: {chunk['source']}, 相似度: {chunk['score']:.3f})\n{chunk['content']}\n"
    except Exception as e:
        import logging
        logging.getLogger("chat").warning("RAG retrieve failed: %s", e, exc_info=True)

    if rag_context:
        system_prompt += "\n\n【辅助线索 — 以下知识库参考内容来自RAG检索，仅供参考，不能替代上述权威课堂数据】"
        system_prompt += rag_context

    # 调用 LLM
    try:
        ai_content = _call_llm(system_prompt, messages, mode=data.mode)
    except Exception as e:
        raise HTTPException(500, f"AI 服务异常: {e}")

    # 保存 AI 回复
    ai_msg = ChatMessage(
        classroom_id=classroom_id,
        role="assistant",
        content=ai_content,
    )
    db.add(ai_msg)
    db.commit()
    db.refresh(ai_msg)

    return ai_msg


@router.post("/{classroom_id}/chat/stream")
async def chat_stream(
    classroom_id: int,
    data: ChatRequest,
    db: Session = Depends(get_db),
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """流式对话：SSE 逐字返回 AI 回复"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    _assert_classroom_access(classroom, current_user, db)

    # 保存用户消息
    user_msg = ChatMessage(classroom_id=classroom_id, role="user", content=data.content)
    db.add(user_msg)
    db.commit()

    # 获取历史对话（仅保留最近 MAX_CLASSROOM_HISTORY_TURNS 轮，防止 token 爆炸）
    history = db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.desc()).limit(MAX_CLASSROOM_HISTORY_TURNS * 2).all()
    messages = [{"role": m.role, "content": m.content} for m in reversed(history)]

    # 构建系统提示词
    system_prompt = _build_system_prompt(classroom, db)

    # RAG 检索：只用当前用户输入做检索（避免历史消息污染检索 query）
    try:
        from backend.api.rag_routes import get_rag_service, _visible_doc_ids
        rag_service = get_rag_service()
        visible_ids = _visible_doc_ids(db, current_user)
        rag_results = rag_service.retrieve_only(
            data.content, top_k=3, visible_doc_ids=visible_ids, mode=data.mode,
        )
        if rag_results.get("retrieved_chunks"):
            rag_context = "\n\n【辅助线索 — 以下知识库参考内容来自RAG检索，仅供参考，不能替代上述权威课堂数据】\n"
            for i, chunk in enumerate(rag_results["retrieved_chunks"], 1):
                rag_context += f"\n[参考{i}] (来源: {chunk['source']}, 相似度: {chunk['score']:.3f})\n{chunk['content']}\n"
            system_prompt += rag_context
    except Exception as e:
        import logging
        logging.getLogger("chat").warning("RAG retrieve failed: %s", e, exc_info=True)

    def event_stream():
        full_content = ""
        try:
            for delta in _llm_stream(system_prompt, messages, mode=data.mode):
                full_content += delta
                yield f"data: {json.dumps({'delta': delta}, ensure_ascii=False)}\n\n"
            ai_msg = ChatMessage(
                classroom_id=classroom_id,
                role="assistant",
                content=full_content,
            )
            db.add(ai_msg)
            db.commit()
            db.refresh(ai_msg)
            yield f"data: {json.dumps({'done': True, 'id': ai_msg.id, 'content': full_content}, ensure_ascii=False)}\n\n"
        except Exception as e:
            if full_content:
                db.add(ChatMessage(classroom_id=classroom_id, role="assistant", content=full_content))
                db.commit()
            if isinstance(e, LLMError):
                err_msg = "LLM 服务异常，请检查配置或稍后重试"
            else:
                err_msg = str(e)
            yield f"data: {json.dumps({'error': err_msg}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@router.get("/{classroom_id}/chat/history", response_model=list[ChatMessageOut])
def get_chat_history(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取对话历史"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    _assert_classroom_access(classroom, current_user, db)

    return db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.asc()).all()


@router.get("/{classroom_id}/chat/export")
def export_chat_markdown(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """导出对话记录为 Markdown 文件"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    _assert_classroom_access(classroom, current_user, db)

    messages = db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.asc()).all()

    # 构建 Markdown 内容
    lines = [
        f"# {classroom.name} 课堂对话记录",
        f"",
        f"**教师**: {classroom.teacher}",
        f"**时长**: {classroom.duration} 分钟",
        f"**平均注意力**: {classroom.avg_attention} 分",
        f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"",
        "---",
        f"",
    ]

    # 如果有报告，先放报告内容
    if classroom.report:
        lines.extend([
            "## AI 分析报告",
            "",
            classroom.report.content,
            "",
            "---",
            "",
        ])

    # 对话内容
    lines.append("## 对话记录")
    lines.append("")

    role_labels = {"user": "用户", "assistant": "AI"}

    for msg in messages:
        time_str = msg.timestamp.strftime('%H:%M:%S')
        lines.append(f"### {role_labels[msg.role]} ({time_str})")
        lines.append("")
        lines.append(msg.content)
        lines.append("")
        lines.append("---")
        lines.append("")

    md_content = "\n".join(lines)

    # 写入临时文件，用 FileResponse 返回（支持中文文件名）
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{classroom.name}_完整分析报告_{timestamp}.md"
    
    # 创建临时文件
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, f"classvision_export_{timestamp}.md")
    
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return FileResponse(
        path=temp_path,
        media_type="text/markdown",
        filename=filename,
    )