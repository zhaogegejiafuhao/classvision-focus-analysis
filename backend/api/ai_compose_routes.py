"""AI 智能组卷路由（从 exam_compose_routes.py 拆分）

提供自然语言→题库匹配+LLM补题的智能组卷接口：
- POST /api/question-bank/ai-compose   AI 智能组卷

流程：自然语言描述 → LLM 解析生成组卷方案 → 从题库匹配题目 → 创建 draft 考试
"""
import json
import logging
import random

import httpx
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Exam,
    ExamTemplate,
    Question,
    QuestionBank,
    RegisteredPerson,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/question-bank", tags=["ai-compose"])

_TYPE_MAP = {"single": "单选", "multi": "多选", "judge": "判断", "fill": "填空", "essay": "简答"}


def getTypeText(t: str) -> str:
    return _TYPE_MAP.get(t, t)


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


@router.post("/ai-compose", response_model=AIComposeResult)
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
