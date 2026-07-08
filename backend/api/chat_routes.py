from datetime import datetime
import os
import json
import tempfile

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.core.database import get_db
from backend.core.config import settings
from backend.models.tables import Classroom, ChatMessage, Report, Student, AttentionRecord, ExamRiskRecord
from backend.models.schemas import ChatRequest, ChatMessageOut
import requests

router = APIRouter(prefix="/api/classrooms", tags=["chat"])


def _build_system_prompt(classroom: Classroom, db: Session) -> str:
    """构建系统提示词，包含课堂数据"""
    stats = _get_classroom_stats(classroom, db)
    report_content = ""
    if classroom.report:
        report_content = classroom.report.content

    return f"""你是资深教学分析专家。基于以下课堂数据进行对话分析。

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

请根据用户的问题，结合以上数据进行分析和建议。回答要专业、客观、有针对性。"""


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


def _call_ollama(system_prompt: str, messages: list[dict]) -> str:
    """调用 Ollama API 生成回复"""
    url = f"{settings.OLLAMA_HOST}/api/chat"
    payload = {
        "model": settings.OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            *messages,
        ],
        "stream": False,
    }
    resp = requests.post(url, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.json()["message"]["content"]


def _ollama_stream(system_prompt: str, messages: list[dict]):
    """流式调用 Ollama，逐块 yield 文本增量"""
    url = f"{settings.OLLAMA_HOST}/api/chat"
    payload = {
        "model": settings.OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            *messages,
        ],
        "stream": True,
    }
    with requests.post(url, json=payload, stream=True, timeout=180) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            if data.get("done"):
                break
            delta = data.get("message", {}).get("content", "")
            if delta:
                yield delta


@router.post("/{classroom_id}/chat", response_model=ChatMessageOut)
def send_chat(
    classroom_id: int,
    data: ChatRequest,
    db: Session = Depends(get_db),
):
    """发送用户消息，返回 AI 回复"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 保存用户消息
    user_msg = ChatMessage(
        classroom_id=classroom_id,
        role="user",
        content=data.content,
    )
    db.add(user_msg)
    db.commit()

    # 获取历史对话
    history = db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.asc()).all()

    messages = [{"role": m.role, "content": m.content} for m in history]

    # 构建系统提示词
    system_prompt = _build_system_prompt(classroom, db)

    # RAG检索：自动从知识库中检索相关内容
    rag_context = ""
    try:
        from backend.api.rag_routes import get_rag_service
        rag_service = get_rag_service()
        rag_results = rag_service.query(data.content, top_k=3)
        if rag_results.get('retrieved_chunks'):
            rag_context = "\n\n--- 知识库参考内容 ---\n"
            for i, chunk in enumerate(rag_results['retrieved_chunks'], 1):
                rag_context += f"\n[参考{i}] (来源: {chunk['source']}, 相似度: {chunk['score']:.3f})\n{chunk['content']}\n"
    except Exception:
        pass  # RAG不可用时仍正常对话

    if rag_context:
        system_prompt += rag_context

    # 调用 Ollama
    try:
        ai_content = _call_ollama(system_prompt, messages)
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
):
    """流式对话：SSE 逐字返回 AI 回复"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 保存用户消息
    user_msg = ChatMessage(classroom_id=classroom_id, role="user", content=data.content)
    db.add(user_msg)
    db.commit()

    # 获取历史对话
    history = db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.asc()).all()
    messages = [{"role": m.role, "content": m.content} for m in history]

    # 构建系统提示词
    system_prompt = _build_system_prompt(classroom, db)

    # RAG 检索：用最近一轮问答 + 当前问题拼接，提升追问准确率
    try:
        from backend.api.rag_routes import get_rag_service
        rag_service = get_rag_service()
        recent = messages[-3:-1] if len(messages) >= 3 else messages[:-1]
        retrieval_query = " ".join([m["content"] for m in recent]) + " " + data.content
        rag_results = rag_service.query(retrieval_query[:500], top_k=3)
        if rag_results.get("retrieved_chunks"):
            rag_context = "\n\n--- 知识库参考内容 ---\n"
            for i, chunk in enumerate(rag_results["retrieved_chunks"], 1):
                rag_context += f"\n[参考{i}] (来源: {chunk['source']}, 相似度: {chunk['score']:.3f})\n{chunk['content']}\n"
            system_prompt += rag_context
    except Exception:
        pass  # RAG 不可用时仍正常对话

    def event_stream():
        full_content = ""
        try:
            for delta in _ollama_stream(system_prompt, messages):
                full_content += delta
                yield f"data: {json.dumps({'delta': delta}, ensure_ascii=False)}\n\n"
            # 流结束，保存 AI 消息
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
            if isinstance(e, requests.exceptions.ConnectionError):
                err_msg = "Ollama 服务未启动，请先运行 ollama serve 并拉取模型（ollama pull qwen3:4b）"
            else:
                err_msg = str(e)
            yield f"data: {json.dumps({'error': err_msg}, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@router.get("/{classroom_id}/chat/history", response_model=list[ChatMessageOut])
def get_chat_history(classroom_id: int, db: Session = Depends(get_db)):
    """获取对话历史"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    return db.query(ChatMessage).filter(
        ChatMessage.classroom_id == classroom_id
    ).order_by(ChatMessage.timestamp.asc()).all()


@router.get("/{classroom_id}/chat/export")
def export_chat_markdown(classroom_id: int, db: Session = Depends(get_db)):
    """导出对话记录为 Markdown 文件"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

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