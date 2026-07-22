"""题库管理 API"""
import json
import random
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import QuestionBank, Exam, Question, RegisteredPerson

router = APIRouter(prefix="/api/question-bank", tags=["question-bank"])


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
    random_config: Optional[dict] = None  # {"category": "数学", "difficulty": 2, "count": 10}


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
        query = query.filter(QuestionBank.teacher_id == current_user.id)
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
            options=json.loads(q.options) if q.options else None,
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
        options=json.loads(q.options) if q.options else None,
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


@router.post("/compose-exam")
def compose_exam(
    data: ComposeExamRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """从题库组卷创建考试"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建考试")

    selected_questions = []

    # 手动指定的题目
    if data.question_ids:
        for qid in data.question_ids:
            q = db.query(QuestionBank).filter(QuestionBank.id == qid).first()
            if q:
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

    # 创建考试
    exam = Exam(
        title=data.title,
        description=data.description,
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        duration=data.duration,
        total_score=sum(q.score for q in selected_questions),
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
            score=q.score,
            order=i + 1,
        )
        db.add(question)

    db.commit()
    return {"success": True, "exam_id": exam.id, "question_count": len(selected_questions)}
