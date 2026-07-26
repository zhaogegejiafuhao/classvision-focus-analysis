"""答题卡答题卡查询入口路由（从 answer_sheet_routes.py 拆分）"""
import os
import json
import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import func as sa_func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_owner_or_admin
from backend.models.tables import RegisteredPerson, Exam, Question
from backend.services.answer_sheet import answer_sheet_orchestrator
from backend.services.paper_template import paper_template_service
from cv_engine.detectors.answer_card_detector import answer_card_detector

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/answer-sheet", tags=["answer-sheet"])

SCAN_UPLOAD_DIR = "uploads/answer_sheets"
os.makedirs(SCAN_UPLOAD_DIR, exist_ok=True)


@router.get("/exams")
def list_exams_for_scan(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取可扫描批改的考试列表（含模板配置状态）"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用")

    # 查询当前教师的所有考试
    query = db.query(Exam)
    if current_user.role == "teacher":
        query = query.filter(Exam.teacher_id == current_user.id)
    exams = query.order_by(Exam.created_at.desc()).all()

    # 批量查询模板配置状态和题目数量（避免 N+1）
    from backend.models.tables import PaperTemplate
    exam_ids = [e.id for e in exams]
    template_exam_ids = {
        row.exam_id for row in
        db.query(PaperTemplate.exam_id).filter(PaperTemplate.exam_id.in_(exam_ids)).all()
    } if exam_ids else set()
    question_counts = dict(
        db.query(Question.exam_id, sa_func.count(Question.id))
        .filter(Question.exam_id.in_(exam_ids))
        .group_by(Question.exam_id).all()
    ) if exam_ids else {}

    result = []
    for e in exams:
        result.append({
            "id": e.id,
            "title": e.title,
            "status": e.status,
            "total_score": e.total_score,
            "question_count": question_counts.get(e.id, 0),
            "has_template": e.id in template_exam_ids,
            "created_at": e.created_at.isoformat() if e.created_at else None,
        })

    return result



@router.get("/exams/{exam_id}/questions")
def list_exam_questions(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取考试的题目列表（用于模板编辑器中选择题号）"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师/管理员可调用")

    # 校验考试归属
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, f"考试 {exam_id} 不存在")
    assert_owner_or_admin(exam.teacher_id, current_user)

    questions = db.query(Question).filter(Question.exam_id == exam_id).order_by(Question.order).all()
    return [
        {
            "id": q.id,
            "order": q.order,
            "type": q.type,
            "content": q.content[:100] + ("..." if len(q.content) > 100 else ""),
            "score": q.score,
            "answer": q.answer,
        }
        for q in questions
    ]

