"""题库管理 API"""
import json
import logging
import random
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import QuestionBank, Exam, Question, RegisteredPerson

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/question-bank", tags=["question-bank"])


def _safe_json_loads(text: str | None):
    """安全解析 JSON 字符串，避免脏数据导致 500"""
    if not text:
        return None
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None


class QuestionBankCreate(BaseModel):
    type: str  # single/multi/judge/fill/essay
    content: str
    options: Optional[list[str]] = None
    answer: str
    score: float = 10.0
    category: Optional[str] = None
    tags: Optional[str] = None
    difficulty: int = 1


class QuestionBankOut(BaseModel):
    id: int
    type: str
    content: str
    options: Optional[list[str]]
    answer: str
    score: float
    category: Optional[str]
    tags: Optional[str]
    difficulty: int
    created_at: Optional[str] = None

    class Config:
        from_attributes = True


class ComposeExamRequest(BaseModel):
    title: str
    description: str = ""
    classroom_id: Optional[int] = None
    duration: int = 60
    total_score: float = 100.0
    question_ids: list[int] = []  # 手动指定的题目
    score_overrides: Optional[dict[int, float]] = None  # 分值覆盖 {question_id: score}
    template_id: Optional[int] = None  # 模板 ID（用于提取时长/总分默认值）
    random_config: Optional[dict] = None  # {"category": "数学", "difficulty": 2, "count": 10}
    exam_type: str = "computer"  # computer(机试)/paper(笔试)


@router.get("", response_model=list[QuestionBankOut])
def list_questions(
    type: Optional[str] = None,
    category: Optional[str] = None,
    difficulty: Optional[int] = None,
    keyword: Optional[str] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取题库列表"""
    query = db.query(QuestionBank)

    if current_user.role == "teacher":
        # 教师可以看到：自己创建的题目 + admin 创建的内置题目（如 TAL-SCQ5K）
        admin_ids = [p.id for p in db.query(RegisteredPerson).filter(RegisteredPerson.role == "admin").all()]
        query = query.filter(
            (QuestionBank.teacher_id == current_user.id) |
            (QuestionBank.teacher_id.in_(admin_ids))
        )
    # admin 可以看到所有题库题目

    if type:
        query = query.filter(QuestionBank.type == type)
    if category:
        query = query.filter(QuestionBank.category == category)
    if difficulty:
        query = query.filter(QuestionBank.difficulty == difficulty)
    if keyword:
        query = query.filter(QuestionBank.content.contains(keyword))

    query = query.order_by(QuestionBank.created_at.desc())
    result = []
    for q in query.all():
        result.append(QuestionBankOut(
            id=q.id,
            type=q.type,
            content=q.content,
            options=_safe_json_loads(q.options),
            answer=q.answer,
            score=q.score,
            category=q.category,
            tags=q.tags,
            difficulty=q.difficulty,
            created_at=q.created_at.isoformat() if q.created_at else None,
        ))
    return result


@router.post("", response_model=QuestionBankOut)
def create_question(
    data: QuestionBankCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """添加题目到题库"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以管理题库")

    q = QuestionBank(
        teacher_id=current_user.id,
        type=data.type,
        content=data.content,
        options=json.dumps(data.options) if data.options else None,
        answer=data.answer,
        score=data.score,
        category=data.category,
        tags=data.tags,
        difficulty=data.difficulty,
    )
    db.add(q)
    db.commit()
    db.refresh(q)

    return QuestionBankOut(
        id=q.id, type=q.type, content=q.content,
        options=_safe_json_loads(q.options),
        answer=q.answer, score=q.score, category=q.category,
        tags=q.tags, difficulty=q.difficulty,
        created_at=q.created_at.isoformat() if q.created_at else None,
    )


@router.delete("/{question_id}")
def delete_question(
    question_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除题库题目"""
    q = db.query(QuestionBank).filter(QuestionBank.id == question_id).first()
    if not q:
        raise HTTPException(404, "题目不存在")
    if q.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除")
    db.delete(q)
    db.commit()
    return {"success": True}


@router.get("/categories")
def list_categories(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取题库分类列表"""
    query = db.query(QuestionBank.category).filter(QuestionBank.category.isnot(None))
    if current_user.role == "teacher":
        query = query.filter(QuestionBank.teacher_id == current_user.id)
    # admin 可以看到所有分类
    categories = set(row[0] for row in query.distinct().all())
    return sorted(categories)


@router.get("/tags")
def list_tags(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取题库所有知识点标签（从 tags 字段提取唯一标签）"""
    query = db.query(QuestionBank.tags).filter(QuestionBank.tags.isnot(None), QuestionBank.tags != "")
    if current_user.role == "teacher":
        query = query.filter(QuestionBank.teacher_id == current_user.id)
    tags_set = set()
    for row in query.all():
        if row[0]:
            for tag in row[0].split(","):
                tag = tag.strip()
                if tag:
                    tags_set.add(tag)
    return sorted(tags_set)


# ── 智能换题 ──

class SwapQuestionRequest(BaseModel):
    """智能换题请求"""
    question_id: int        # 要替换的题目 ID（题库中的 ID）；0 表示题目不在题库中
    exclude_ids: list[int] = []  # 需要排除的题目 ID（如已在试卷中的题）
    type: Optional[str] = None   # 限定题型（默认同原题类型）
    difficulty: Optional[int] = None  # 限定难度（默认原题难度±1）
    category: Optional[str] = None   # 限定分类
    tags: Optional[str] = None       # 限定知识点标签
    # ── 新增：题目元数据（当 question_id=0 时使用，支持 AI 生成题的换题） ──
    question_type: Optional[str] = None       # 原题题型
    question_difficulty: Optional[int] = None  # 原题难度
    question_category: Optional[str] = None    # 原题分类
    question_tags: Optional[str] = None        # 原题标签
    question_content: Optional[str] = None     # 原题内容（用于日志）


class SwapQuestionResult(BaseModel):
    """智能换题结果"""
    original_id: int
    new_question: dict
    candidates_count: int  # 候选题总数


def _resolve_original_question(data: SwapQuestionRequest, db: Session, current_user: RegisteredPerson):
    """解析原题信息（支持题库 ID 和元数据两种来源）

    Returns:
        dict: {type, difficulty, category, tags, exclude_ids} 用于构建候选池
    """
    original = None
    if data.question_id and data.question_id > 0:
        original = db.query(QuestionBank).filter(QuestionBank.id == data.question_id).first()

    if original:
        return {
            "type": data.type or original.type,
            "difficulty": data.difficulty or original.difficulty,
            "category": data.category or original.category,
            "tags": data.tags or original.tags,
            "exclude_ids": [data.question_id] + data.exclude_ids,
        }
    else:
        # question_id=0 或题库中找不到 → 使用前端传入的元数据
        return {
            "type": data.type or data.question_type or "single",
            "difficulty": data.difficulty or data.question_difficulty or 2,
            "category": data.category or data.question_category,
            "tags": data.tags or data.question_tags,
            "exclude_ids": data.exclude_ids,  # 无 bank_id 可排除
        }


def _find_swap_candidates(params: dict, current_user: RegisteredPerson, db: Session, max_results: int = 20):
    """渐进式筛选换题候选

    策略（逐级放宽，直到找到候选或全部尝试完毕）：
    1. 同类型 + 同分类 + 难度±1 + 标签匹配
    2. 同类型 + 同分类 + 难度±2
    3. 同类型 + 难度±2
    4. 同类型（仅此一个条件）
    """
    q_type = params["type"]
    difficulty = params["difficulty"] or 2
    category = params.get("category")
    tags_str = params.get("tags")
    exclude_ids = params.get("exclude_ids", [])

    # 解析标签
    tag_list = []
    if tags_str:
        tag_list = [t.strip().lower() for t in tags_str.split(",") if t.strip()]

    # 4 级筛选策略
    strategies = [
        # 级别1：最严格 — 同类型 + 同分类 + 难度±1 + 标签匹配
        {"type": q_type, "diff_range": 1, "category": category, "tags": tag_list},
        # 级别2：放宽难度 — 同类型 + 同分类 + 难度±2
        {"type": q_type, "diff_range": 2, "category": category, "tags": None},
        # 级别3：去掉分类 — 同类型 + 难度±2
        {"type": q_type, "diff_range": 2, "category": None, "tags": None},
        # 级别4：仅同类型
        {"type": q_type, "diff_range": None, "category": None, "tags": None},
    ]

    for level, strategy in enumerate(strategies, 1):
        pool = db.query(QuestionBank)

        # 教师只能看到自己的题
        if current_user.role == "teacher":
            pool = pool.filter(QuestionBank.teacher_id == current_user.id)

        # 题型（始终限定）
        pool = pool.filter(QuestionBank.type == strategy["type"])

        # 难度范围
        if strategy["diff_range"] is not None:
            pool = pool.filter(QuestionBank.difficulty.between(
                difficulty - strategy["diff_range"],
                difficulty + strategy["diff_range"]
            ))

        # 分类
        if strategy["category"]:
            pool = pool.filter(QuestionBank.category == strategy["category"])

        # 排除已用题目
        if exclude_ids:
            pool = pool.filter(QuestionBank.id.notin_(exclude_ids))

        candidates = pool.all()

        # 标签匹配（在内存中做，更灵活）
        if strategy["tags"] and candidates:
            tag_matched = []
            for q in candidates:
                q_tags_lower = (q.tags or "").lower()
                if any(t in q_tags_lower for t in strategy["tags"]):
                    tag_matched.append(q)
            if tag_matched:
                candidates = tag_matched
            # 注意：标签匹配失败不降级，继续用无标签的候选

        if candidates:
            logger.info(
                f"[swap] level={level} found {len(candidates)} candidates, "
                f"type={q_type}, diff={difficulty}, category={category}"
            )
            return candidates[:max_results], level

    return [], 0


@router.post("/swap-question", response_model=SwapQuestionResult)
def swap_question(
    data: SwapQuestionRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """智能换题：从题库中匹配同类型/难度/知识点的题目替换原题"""
    params = _resolve_original_question(data, db, current_user)
    candidates, level = _find_swap_candidates(params, current_user, db, max_results=1)

    if not candidates:
        raise HTTPException(404, "没有找到合适的替换题，请先向题库中添加更多同类型题目")

    new_q = candidates[0]
    original_id = data.question_id or 0

    return SwapQuestionResult(
        original_id=original_id,
        new_question={
            "id": new_q.id,
            "type": new_q.type,
            "content": new_q.content,
            "options": _safe_json_loads(new_q.options),
            "answer": new_q.answer,
            "score": new_q.score,
            "category": new_q.category,
            "tags": new_q.tags,
            "difficulty": new_q.difficulty,
            "source": new_q.source,
            "analysis": new_q.analysis,
        },
        candidates_count=len(candidates),
    )


@router.post("/swap-question-candidates")
def swap_question_candidates(
    data: SwapQuestionRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """智能换题：返回多道候选题供教师选择（渐进式筛选）"""
    params = _resolve_original_question(data, db, current_user)
    candidates, match_level = _find_swap_candidates(params, current_user, db, max_results=20)

    result = []
    for q in candidates:
        result.append({
            "id": q.id,
            "type": q.type,
            "content": q.content,
            "options": _safe_json_loads(q.options),
            "answer": q.answer,
            "score": q.score,
            "category": q.category,
            "tags": q.tags,
            "difficulty": q.difficulty,
            "source": q.source,
            "analysis": q.analysis,
        })

    return {
        "original_id": data.question_id or 0,
        "candidates": result,
        "total": len(result),
        "match_level": match_level,  # 告知前端匹配级别（1=精确, 4=宽松）
    }


@router.post("/compose-exam")
def compose_exam(
    data: ComposeExamRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """从题库组卷创建考试"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建考试")

    # ── 从模板提取默认值 ──
    if data.template_id:
        from backend.models.tables import ExamTemplate
        tmpl = db.query(ExamTemplate).filter(ExamTemplate.id == data.template_id).first()
        if tmpl:
            if not data.duration or data.duration == 60:
                data.duration = tmpl.duration
            if not data.total_score or data.total_score == 100.0:
                data.total_score = tmpl.total_score

    selected_questions = []

    # 手动指定的题目（校验归属：教师只能选自己的题目，admin 可选所有）
    if data.question_ids:
        for qid in data.question_ids:
            q = db.query(QuestionBank).filter(QuestionBank.id == qid).first()
            if q:
                if current_user.role == "teacher" and q.teacher_id != current_user.id:
                    raise HTTPException(403, f"无权使用题目 #{qid}，该题目不属于你")
                selected_questions.append(q)

    # 随机抽题
    if data.random_config:
        cfg = data.random_config
        pool = db.query(QuestionBank)
        if current_user.role == "teacher":
            pool = pool.filter(QuestionBank.teacher_id == current_user.id)
        # admin 可以从全部题库抽题
        if cfg.get("category"):
            pool = pool.filter(QuestionBank.category == cfg["category"])
        if cfg.get("type"):
            pool = pool.filter(QuestionBank.type == cfg["type"])
        if cfg.get("difficulty"):
            pool = pool.filter(QuestionBank.difficulty == cfg["difficulty"])

        # 排除已手动选的
        if data.question_ids:
            pool = pool.filter(QuestionBank.id.notin_(data.question_ids))

        all_pool = pool.all()
        count = min(cfg.get("count", 10), len(all_pool))
        selected_questions.extend(random.sample(all_pool, count))

    if not selected_questions:
        raise HTTPException(400, "没有选中任何题目")

    # ── 计算各题实际分值（score_overrides 优先） ──
    effective_scores = {}
    for q in selected_questions:
        if data.score_overrides and q.id in data.score_overrides:
            effective_scores[q.id] = data.score_overrides[q.id]
        else:
            effective_scores[q.id] = q.score

    # 创建考试
    exam = Exam(
        title=data.title,
        description=data.description,
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        duration=data.duration,
        total_score=sum(effective_scores[q.id] for q in selected_questions),
        exam_type=data.exam_type,
    )
    db.add(exam)
    db.flush()

    for i, q in enumerate(selected_questions):
        question = Question(
            exam_id=exam.id,
            type=q.type,
            content=q.content,
            options=q.options,
            answer=q.answer,
            score=effective_scores[q.id],
            order=i + 1,
        )
        db.add(question)

    db.commit()
    return {"success": True, "exam_id": exam.id, "question_count": len(selected_questions)}
