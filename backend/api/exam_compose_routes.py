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
    QuestionBank, Exam, Question, RegisteredPerson, ExamTemplate,
)

logger = logging.getLogger(__name__)

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
        pool = pool.filter((QuestionBank.teacher_id == current_user.id) | (QuestionBank.is_builtin == True if hasattr(QuestionBank, 'is_builtin') else True))
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
      "difficulty": 2,
      "must_from_bank": true
    }
  ]
}

规则：
1. sections 中各 section 的 count × score_per 之和应接近 100 分
2. difficulty 取值 1-5（1=简单，5=困难）
3. must_from_bank=true 表示从题库匹配，false 表示 AI 生成新题
4. 如果题库中对应题型/难度/知识点的题目充足，设 must_from_bank=true
5. 如果题库不够，设 must_from_bank=false，AI 会补生成
6. type 只能是: single(单选), multi(多选), judge(判断), fill(填空), essay(简答)
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

    # ── 4. 按方案从题库匹配题目 ──
    selected_questions = []
    need_generate = []  # 需要 AI 生成的题目

    for section in plan["sections"]:
        q_type = section.get("type", "single")
        count = section.get("count", 5)
        score_per = section.get("score_per", 5)
        knowledge = section.get("knowledge", [])
        difficulty = section.get("difficulty", 2)
        must_from_bank = section.get("must_from_bank", True)

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
            # 题库不够，需要 AI 生成
            need_count = count - len(matched)
            need_generate.append({
                "type": q_type,
                "count": need_count,
                "score_per": score_per,
                "knowledge": knowledge,
                "difficulty": difficulty,
            })

    # ── 5. AI 生成缺口的题目 ──
    generated_questions = []
    if need_generate:
        gen_system = """你是一个出题专家。根据要求生成数学题目，输出 JSON 数组。
每道题的格式：
[{"type":"single","content":"题目内容","options":["A选项","B选项","C选项","D选项"],"answer":"A","score":5,"difficulty":2,"category":"分类","tags":"标签1,标签2","analysis":"解析"}]

对于 essay 类型，options 为 null。
对于 judge 类型，options 为 null，answer 为 "对" 或 "错"。
对于 fill 类型，options 为 null，answer 为填空答案。
只输出 JSON，不要其他文字。"""

        gen_prompt = f"""请根据以下要求生成题目：
{json.dumps(need_generate, ensure_ascii=False, indent=2)}

上下文：教师需求是 "{data.prompt}"
请确保题目与需求相关，难度和知识点匹配。"""

        try:
            gen_response = await _call_llm(gen_system, gen_prompt)
            gen_list = _parse_llm_json(gen_response)
            if isinstance(gen_list, list):
                for item in gen_list:
                    # 保存到题库
                    q = QuestionBank(
                        teacher_id=current_user.id,
                        type=item.get("type", "single"),
                        content=item.get("content", ""),
                        options=json.dumps(item.get("options"), ensure_ascii=False) if item.get("options") else None,
                        answer=item.get("answer", ""),
                        score=item.get("score", 5),
                        category=item.get("category", "AI生成"),
                        tags=item.get("tags", ""),
                        difficulty=item.get("difficulty", 2),
                        source="AI生成",
                        analysis=item.get("analysis", ""),
                    )
                    db.add(q)
                    db.flush()
                    generated_questions.append(q)
                db.commit()
        except Exception as e:
            logger.warning(f"AI 生成题目失败（不影响已匹配的题目）: {e}")

    # ── 6. 创建考试 ──
    all_selected = selected_questions + generated_questions
    if not all_selected:
        raise HTTPException(400, "没有匹配到任何题目，请调整需求或先导入题库")

    title = data.title or plan.get("title", "AI 生成考试")
    description = plan.get("description", f"AI 智能组卷，基于需求：{data.prompt}")
    total_score = sum(q.score for q in all_selected)

    exam = Exam(
        title=title,
        description=description,
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        duration=plan.get("duration", 90),
        total_score=total_score,
        status="draft",  # 草稿状态，等教师确认
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

    # 组装返回
    questions_preview = []
    for i, q in enumerate(all_selected):
        questions_preview.append({
            "order": i + 1,
            "id": q.id,
            "type": q.type,
            "content": q.content[:80] + ("..." if len(q.content) > 80 else ""),
            "score": q.score,
            "source": q.source or "题库",
        })

    return AIComposeResult(
        exam_id=exam.id,
        title=title,
        question_count=len(all_selected),
        total_score=total_score,
        questions=questions_preview,
    )
