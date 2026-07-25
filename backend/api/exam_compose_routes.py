"""AI 智能组卷 + 试卷模板管理 API

提供以下接口：
- POST /api/exam-templates                     创建试卷模板
- GET  /api/exam-templates                     获取模板列表（含内置）
- GET  /api/exam-templates/{id}                获取模板详情
- DELETE /api/exam-templates/{id}              删除自定义模板
- POST /api/question-bank/ai-compose           AI 智能组卷（自然语言→题库匹配+LLM补题）
"""
import json
import logging
import random
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    QuestionBank, Exam, Question, RegisteredPerson, ExamTemplate, Student, Notification,
)

logger = logging.getLogger(__name__)

_TYPE_MAP = {"single": "单选", "multi": "多选", "judge": "判断", "fill": "填空", "essay": "简答"}


def getTypeText(t: str) -> str:
    return _TYPE_MAP.get(t, t)


# ─── 试卷模板路由 ──────────────────────────────────────

template_router = APIRouter(prefix="/api/exam-templates", tags=["exam-templates"])


class ExamTemplateCreate(BaseModel):
    name: str
    description: str = ""
    total_score: float = 100.0
    duration: int = 90
    # [{"type":"single","count":10,"score_per":5,"knowledge":["极限"],"difficulty":2}, ...]
    structure: list[dict]


class ExamTemplateOut(BaseModel):
    id: int
    name: str
    description: str | None
    total_score: float
    duration: int
    structure: list[dict]
    is_builtin: bool
    created_by: int | None

    class Config:
        from_attributes = True


@template_router.get("", response_model=list[ExamTemplateOut])
def list_templates(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取试卷模板列表（内置 + 自己创建的）"""
    query = db.query(ExamTemplate)
    # 内置模板所有人可见，自定义模板只有创建者可见
    if current_user.role != "admin":
        query = query.filter(
            (ExamTemplate.is_builtin == True) | (ExamTemplate.created_by == current_user.id)
        )
    templates = query.order_by(ExamTemplate.is_builtin.desc(), ExamTemplate.created_at.desc()).all()
    result = []
    for t in templates:
        result.append(ExamTemplateOut(
            id=t.id, name=t.name, description=t.description,
            total_score=t.total_score, duration=t.duration,
            structure=json.loads(t.structure) if t.structure else [],
            is_builtin=t.is_builtin, created_by=t.created_by,
        ))
    return result


@template_router.post("", response_model=ExamTemplateOut)
def create_template(
    data: ExamTemplateCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建自定义试卷模板"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建模板")

    t = ExamTemplate(
        name=data.name,
        description=data.description,
        total_score=data.total_score,
        duration=data.duration,
        structure=json.dumps(data.structure, ensure_ascii=False),
        is_builtin=False,
        created_by=current_user.id,
    )
    db.add(t)
    db.commit()
    db.refresh(t)

    return ExamTemplateOut(
        id=t.id, name=t.name, description=t.description,
        total_score=t.total_score, duration=t.duration,
        structure=data.structure,
        is_builtin=t.is_builtin, created_by=t.created_by,
    )


@template_router.delete("/{template_id}")
def delete_template(
    template_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除自定义模板（内置模板不可删除）"""
    t = db.query(ExamTemplate).filter(ExamTemplate.id == template_id).first()
    if not t:
        raise HTTPException(404, "模板不存在")
    if t.is_builtin:
        raise HTTPException(400, "内置模板不可删除")
    if t.created_by != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除")
    db.delete(t)
    db.commit()
    return {"success": True}


# ─── AI 智能组卷路由 ────────────────────────────────────

compose_router = APIRouter(prefix="/api/question-bank", tags=["ai-compose"])


class AIComposeRequest(BaseModel):
    """AI 智能组卷请求"""
    prompt: str  # 自然语言描述，如"高数期中，5道单选 3道大题，覆盖极限和积分，难度中等"
    classroom_id: int | None = None  # 关联课堂
    template_id: int | None = None  # 可选：使用模板约束
    title: str = ""  # 考试标题（可选，AI 可自动生成）
    exam_type: str = "computer"  # computer(机试)/paper(笔试)


class AIComposeResult(BaseModel):
    """AI 智能组卷结果"""
    exam_id: int
    title: str
    question_count: int
    total_score: float
    questions: list[dict]  # 题目预览


# ─── LLM 调用 ──────────────────────────────────────────

async def _call_llm(system_prompt: str, user_prompt: str) -> str:
    """调用 LLM API — 复用项目 LLM Provider 配置"""
    from backend.core.config import settings

    provider = settings.LLM_PROVIDER
    api_key = settings.LLM_API_KEY

    # ── Ollama 本地模式 ──
    if provider == "ollama":
        import httpx as _httpx
        base_url = settings.OLLAMA_HOST
        model = settings.OLLAMA_MODEL
        async with _httpx.AsyncClient(timeout=120.0) as client:
            resp = await client.post(f"{base_url}/api/chat", json={
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "stream": False,
                "options": {"temperature": 0.3},
            })
            resp.raise_for_status()
            return resp.json()["message"]["content"]

    # ── OpenAI 兼容云端 API ──
    # 预置 URL
    preset_urls = {
        "openrouter": "https://openrouter.ai/api/v1",
        "dashscope": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "deepseek": "https://api.deepseek.com/v1",
        "siliconflow": "https://api.siliconflow.cn/v1",
    }
    base_url = settings.LLM_BASE_URL or preset_urls.get(provider, "https://api.openai.com/v1")
    model = settings.LLM_MODEL or "gpt-3.5-turbo"

    if not api_key:
        raise HTTPException(500, "未配置 LLM_API_KEY，请在 .env 中设置")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "max_tokens": 2000,
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(f"{base_url}/chat/completions", headers=headers, json=payload)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]


def _parse_llm_json(text: str) -> dict | None:
    """从 LLM 回复中提取 JSON"""
    # 尝试直接解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # 尝试提取 ```json ... ``` 代码块
    import re
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass
    # 尝试提取第一个 { ... }
    start = text.find("{")
    end = text.rfind("}") + 1
    if start >= 0 and end > start:
        try:
            return json.loads(text[start:end])
        except json.JSONDecodeError:
            pass
    return None


@compose_router.post("/ai-compose", response_model=AIComposeResult)
async def ai_compose_exam(
    data: AIComposeRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """AI 智能组卷：自然语言 → 题库匹配 + LLM 补题"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建考试")

    # ── 1. 获取模板约束（可选）──
    template_structure = None
    if data.template_id:
        tmpl = db.query(ExamTemplate).filter(ExamTemplate.id == data.template_id).first()
        if tmpl:
            template_structure = json.loads(tmpl.structure) if tmpl.structure else None

    # ── 2. 获取题库中可用题目的统计信息 ──
    pool = db.query(QuestionBank)
    if current_user.role == "teacher":
        # 教师可用：自己创建的 + admin 创建的内置题库
        admin_ids = [p.id for p in db.query(RegisteredPerson).filter(RegisteredPerson.role == "admin").all()]
        pool = pool.filter(
            (QuestionBank.teacher_id == current_user.id) |
            (QuestionBank.teacher_id.in_(admin_ids))
        )
    all_questions = pool.all()

    # 统计题库中各题型/难度/分类的题目数量
    stats = {"total": len(all_questions)}
    for q in all_questions:
        stats.setdefault(f"type_{q.type}", 0)
        stats[f"type_{q.type}"] += 1
        if q.category:
            stats.setdefault(f"cat_{q.category}", 0)
            stats[f"cat_{q.category}"] += 1
        stats.setdefault(f"diff_{q.difficulty}", 0)
        stats[f"diff_{q.difficulty}"] += 1
        if q.tags:
            for tag in q.tags.split(","):
                tag = tag.strip()
                if tag:
                    stats.setdefault(f"tag_{tag}", 0)
                    stats[f"tag_{tag}"] += 1

    # ── 3. 调用 LLM 解析自然语言 + 生成组卷方案 ──
    system_prompt = """你是一个智能组卷助手。根据教师的自然语言描述和题库统计信息，生成组卷方案。
所有题目必须从现有题库中抽取，不生成新题。如果某题型/难度/知识点的题目不足，请自动减少该部分的题目数量，并在其他部分补足。

你需要输出一个 JSON 对象，包含：
{
  "title": "考试标题",
  "description": "考试描述",
  "sections": [
    {
      "type": "single|multi|judge|fill|essay",
      "count": 5,
      "score_per": 5,
      "knowledge": ["知识点1", "知识点2"],
      "difficulty": 2
    }
  ]
}

规则：
1. sections 中各 section 的 count × score_per 之和应接近 100 分
2. difficulty 取值 1-5（1=简单，5=困难）
3. 所有题目均从题库中抽取，不生成新题
4. 如果题库中对应题型/难度/知识点的题目不足，请减少 count，不要超过题库实际数量
5. type 只能是: single(单选), multi(多选), judge(判断), fill(填空), essay(简答)
6. 请确保每个 section 的 count 不超过题库中该题型对应难度的题目数量
"""

    user_prompt = f"""教师需求：{data.prompt}

当前题库统计：
{json.dumps(stats, ensure_ascii=False, indent=2)}
"""

    if template_structure:
        user_prompt += f"\n模板约束结构：\n{json.dumps(template_structure, ensure_ascii=False, indent=2)}\n请按照模板结构的题型和数量来组卷，但可以根据教师需求微调难度和知识点。"

    try:
        llm_response = await _call_llm(system_prompt, user_prompt)
    except Exception as e:
        logger.error(f"LLM 调用失败: {e}")
        raise HTTPException(500, f"AI 组卷失败: {str(e)}")

    plan = _parse_llm_json(llm_response)
    if not plan or "sections" not in plan:
        logger.error(f"LLM 返回格式错误: {llm_response[:200]}")
        raise HTTPException(500, "AI 返回格式错误，请重试")

    # ── 4. 按方案从题库匹配题目（只从题库抽取，不生成新题）──
    selected_questions = []
    shortfall_info = []  # 记录不足的部分用于提示

    for section in plan["sections"]:
        q_type = section.get("type", "single")
        count = section.get("count", 5)
        score_per = section.get("score_per", 5)
        knowledge = section.get("knowledge", [])
        difficulty = section.get("difficulty", 2)

        # 从题库筛选
        candidates = [
            q for q in all_questions
            if q.type == q_type
            and q not in selected_questions
        ]
        # 难度筛选（±1 范围）
        if difficulty:
            diff_candidates = [q for q in candidates if abs(q.difficulty - difficulty) <= 1]
            if diff_candidates:
                candidates = diff_candidates
        # 知识点筛选
        if knowledge:
            knowledge_candidates = []
            for q in candidates:
                q_tags = (q.tags or "").lower() + " " + (q.category or "").lower()
                if any(k.lower() in q_tags for k in knowledge):
                    knowledge_candidates.append(q)
            if knowledge_candidates:
                candidates = knowledge_candidates

        matched = random.sample(candidates, min(count, len(candidates)))
        selected_questions.extend(matched)

        if len(matched) < count:
            shortfall_info.append(
                f"{getTypeText(q_type)}需{count}题但题库只有{len(candidates)}题（匹配到{len(matched)}题）"
            )

    # ── 5. 创建考试 ──
    all_selected = selected_questions
    if not all_selected:
        raise HTTPException(400, "题库中没有匹配到任何题目，请先导入题库或调整需求")

    title = data.title or plan.get("title", "AI 组卷")
    description = plan.get("description", f"AI 智能组卷，基于需求：{data.prompt}")
    if shortfall_info:
        description += f"\n\n⚠️ 题库不足提示：{'；'.join(shortfall_info)}"
    total_score = sum(q.score for q in all_selected)

    exam = Exam(
        title=title,
        description=description,
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        duration=plan.get("duration", 90),
        total_score=total_score,
        status="draft",  # 草稿状态，等教师确认
        exam_type=data.exam_type,
    )
    db.add(exam)
    db.flush()

    for i, q in enumerate(all_selected):
        question = Question(
            exam_id=exam.id,
            type=q.type,
            content=q.content,
            options=q.options,
            answer=q.answer,
            score=q.score,
            order=i + 1,
            knowledge_points=json.dumps([q.category] if q.category else [], ensure_ascii=False),
        )
        db.add(question)

    db.commit()

    # 组装返回（增加完整题目信息供审核）
    questions_preview = []
    for i, q in enumerate(all_selected):
        questions_preview.append({
            "order": i + 1,
            "bank_id": q.id,  # 题库中的原始 ID（用于换题）
            "type": q.type,
            "content": q.content,
            "options": json.loads(q.options) if q.options else None,
            "answer": q.answer,
            "score": q.score,  # AI 建议分值
            "suggested_score": q.score,  # 明确标注为建议分值
            "source": q.source or "题库",
            "category": q.category,
            "tags": q.tags,
            "difficulty": q.difficulty,
            "analysis": q.analysis,
        })

    return AIComposeResult(
        exam_id=exam.id,
        title=title,
        question_count=len(all_selected),
        total_score=total_score,
        questions=questions_preview,
    )


# ─── 考试审核与发布路由 ──────────────────────────────────

review_router = APIRouter(prefix="/api/exams", tags=["exam-review"])


class ExamPreviewResult(BaseModel):
    """考试预览结果"""
    exam_id: int
    title: str
    description: str
    status: str
    duration: int
    total_score: float
    classroom_id: int | None
    questions: list[dict]


@review_router.get("/{exam_id}/preview", response_model=ExamPreviewResult)
def preview_exam(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取 draft 考试的完整预览（审核确认前查看详情）"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权查看此考试")

    questions = db.query(Question).filter(Question.exam_id == exam_id).order_by(Question.order).all()

    questions_detail = []
    for q in questions:
        # 查找题库中的原始题目（用于换题参考）
        bank_q = db.query(QuestionBank).filter(
            QuestionBank.content == q.content,
            QuestionBank.type == q.type,
        ).first()

        questions_detail.append({
            "id": q.id,
            "bank_id": bank_q.id if bank_q else None,
            "order": q.order,
            "type": q.type,
            "content": q.content,
            "options": json.loads(q.options) if q.options else None,
            "answer": q.answer,
            "score": q.score,
            "suggested_score": q.score,
            "knowledge_points": json.loads(q.knowledge_points) if q.knowledge_points else [],
            "source": bank_q.source if bank_q else "题库",
            "category": bank_q.category if bank_q else None,
            "tags": bank_q.tags if bank_q else None,
            "difficulty": bank_q.difficulty if bank_q else None,
            "analysis": bank_q.analysis if bank_q else None,
        })

    return ExamPreviewResult(
        exam_id=exam.id,
        title=exam.title,
        description=exam.description or "",
        status=exam.status,
        duration=exam.duration,
        total_score=exam.total_score,
        classroom_id=exam.classroom_id,
        questions=questions_detail,
    )


class PublishExamRequest(BaseModel):
    """发布考试请求"""
    score_overrides: dict[int, float] | None = None  # 分值覆盖 {question_id: new_score}（Question表的ID）
    remove_question_ids: list[int] | None = None  # 要删除的题目 ID（Question表的ID）
    swap_questions: list[dict] | None = None  # 要替换的题目 [{"old_id": 1, "new_bank_id": 5}]
    title: str | None = None  # 更新标题
    duration: int | None = None  # 更新时长


@review_router.post("/{exam_id}/publish")
def publish_exam(
    exam_id: int,
    data: PublishExamRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """将 draft 考试发布（教师审核确认后调用）"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权发布此考试")
    if exam.status != "draft":
        raise HTTPException(400, f"考试当前状态为 {exam.status}，无法重复发布")

    # ── 1. 处理分值覆盖 ──
    if data.score_overrides:
        for q_id, new_score in data.score_overrides.items():
            q = db.query(Question).filter(Question.id == q_id, Question.exam_id == exam_id).first()
            if q:
                q.score = new_score

    # ── 2. 处理题目删除 ──
    if data.remove_question_ids:
        for q_id in data.remove_question_ids:
            q = db.query(Question).filter(Question.id == q_id, Question.exam_id == exam_id).first()
            if q:
                db.delete(q)

    # ── 3. 处理题目替换 ──
    if data.swap_questions:
        for swap in data.swap_questions:
            old_id = swap.get("old_id")
            new_bank_id = swap.get("new_bank_id")
            if old_id and new_bank_id:
                old_q = db.query(Question).filter(Question.id == old_id, Question.exam_id == exam_id).first()
                new_bank_q = db.query(QuestionBank).filter(QuestionBank.id == new_bank_id).first()
                if old_q and new_bank_q:
                    old_q.type = new_bank_q.type
                    old_q.content = new_bank_q.content
                    old_q.options = new_bank_q.options
                    old_q.answer = new_bank_q.answer
                    # 保留原题分值（教师可在 score_overrides 中单独调整）
                    old_q.knowledge_points = json.dumps(
                        [new_bank_q.category] if new_bank_q.category else [], ensure_ascii=False
                    )

    # ── 4. 更新标题/时长 ──
    if data.title:
        exam.title = data.title
    if data.duration:
        exam.duration = data.duration

    # ── 5. 重新计算总分和重排顺序 ──
    remaining_questions = db.query(Question).filter(Question.exam_id == exam_id).order_by(Question.order).all()
    for i, q in enumerate(remaining_questions):
        q.order = i + 1
    exam.total_score = sum(q.score for q in remaining_questions)
    exam.status = "published"

    # 发送通知给学生
    if exam.classroom_id:
        students = db.query(Student).filter(Student.classroom_id == exam.classroom_id).all()
        for student in students:
            if student.person:
                notification = Notification(
                    title=f"考试通知：{exam.title}",
                    content=f"您有一个考试需要参加，时长 {exam.duration} 分钟。",
                    type="exam",
                    sender_id=current_user.id,
                    receiver_id=student.person_id,
                    classroom_id=exam.classroom_id,
                )
                db.add(notification)

    db.commit()

    return {
        "success": True,
        "exam_id": exam.id,
        "title": exam.title,
        "status": "published",
        "question_count": len(remaining_questions),
        "total_score": exam.total_score,
    }
