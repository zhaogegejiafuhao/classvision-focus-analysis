"""课堂评价 API"""
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import ClassroomFeedback, RegisteredPerson, Classroom, Student

router = APIRouter(prefix="/api/feedback", tags=["feedback"])


class FeedbackCreate(BaseModel):
    classroom_id: int
    rating: int  # 1-5
    content: str = ""


class FeedbackOut(BaseModel):
    id: int
    classroom_id: int
    classroom_name: str
    student_id: int
    student_name: str
    rating: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


@router.get("/{classroom_id}", response_model=list[FeedbackOut])
def list_feedback(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取课堂评价列表"""
    feedbacks = db.query(ClassroomFeedback).filter(
        ClassroomFeedback.classroom_id == classroom_id
    ).order_by(ClassroomFeedback.created_at.desc()).all()

    result = []
    for fb in feedbacks:
        result.append(FeedbackOut(
            id=fb.id,
            classroom_id=fb.classroom_id,
            classroom_name=fb.classroom.name if fb.classroom else "",
            student_id=fb.student_id,
            student_name=fb.student.name,
            rating=fb.rating,
            content=fb.content,
            created_at=fb.created_at,
        ))
    return result


@router.get("/{classroom_id}/summary")
def get_feedback_summary(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取课堂评价汇总"""
    feedbacks = db.query(ClassroomFeedback).filter(
        ClassroomFeedback.classroom_id == classroom_id
    ).all()

    if not feedbacks:
        return {"avg_rating": 0, "total": 0, "distribution": {}}

    avg = sum(f.rating for f in feedbacks) / len(feedbacks)
    distribution = {}
    for i in range(1, 6):
        distribution[str(i)] = sum(1 for f in feedbacks if f.rating == i)

    return {
        "avg_rating": round(avg, 2),
        "total": len(feedbacks),
        "distribution": distribution,
    }


@router.post("", response_model=FeedbackOut)
def create_feedback(
    data: FeedbackCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生提交课堂评价"""
    if data.rating < 1 or data.rating > 5:
        raise HTTPException(400, "评分应在1-5之间")

    existing = db.query(ClassroomFeedback).filter(
        ClassroomFeedback.classroom_id == data.classroom_id,
        ClassroomFeedback.student_id == current_user.id,
    ).first()
    if existing:
        existing.rating = data.rating
        existing.content = data.content
        db.commit()
        db.refresh(existing)
        fb = existing
    else:
        fb = ClassroomFeedback(
            classroom_id=data.classroom_id,
            student_id=current_user.id,
            rating=data.rating,
            content=data.content,
        )
        db.add(fb)
        db.commit()
        db.refresh(fb)

    return FeedbackOut(
        id=fb.id,
        classroom_id=fb.classroom_id,
        classroom_name=fb.classroom.name if fb.classroom else "",
        student_id=fb.student_id,
        student_name=fb.student.name,
        rating=fb.rating,
        content=fb.content,
        created_at=fb.created_at,
    )


@router.delete("/{feedback_id}")
def delete_feedback(
    feedback_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除评价"""
    fb = db.query(ClassroomFeedback).filter(ClassroomFeedback.id == feedback_id).first()
    if not fb:
        raise HTTPException(404, "评价不存在")
    if fb.student_id != current_user.id and current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "无权删除")
    db.delete(fb)
    db.commit()
    return {"success": True}
