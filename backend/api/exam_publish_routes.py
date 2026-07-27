"""考试预览与发布路由（从 exam_compose_routes.py 拆分）

AI 组卷生成 draft 考试后，教师审核确认前的预览与发布接口：
- GET  /api/exams/{exam_id}/preview    获取 draft 考试完整预览
- POST /api/exams/{exam_id}/publish     发布考试（含分值覆盖/题目删除/替换/重排）

注：原 exam_compose_routes.py 中的 review_router 在此重命名为 publish_router，
避免与 exam_review_routes.py（审核工作流）的概念混淆；tag 也从 "exam-review"
改为 "exam-publish" 以区分。
"""
import json

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Exam,
    Notification,
    Question,
    QuestionBank,
    RegisteredPerson,
    Student,
)

router = APIRouter(prefix="/api/exams", tags=["exam-publish"])


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


@router.get("/{exam_id}/preview", response_model=ExamPreviewResult)
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


@router.post("/{exam_id}/publish")
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
