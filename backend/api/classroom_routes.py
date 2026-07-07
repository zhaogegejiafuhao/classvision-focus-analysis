from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.tables import Classroom, Student, AttentionRecord
from backend.models.schemas import ClassroomCreate, ClassroomOut, ClassroomDetail, ClassroomEndOut

router = APIRouter(prefix="/api/classrooms", tags=["classrooms"])


@router.post("", response_model=ClassroomOut)
def create_classroom(data: ClassroomCreate, db: Session = Depends(get_db)):
    classroom = Classroom(name=data.name, teacher=data.teacher)
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom


@router.get("", response_model=list[ClassroomOut])
def list_classrooms(db: Session = Depends(get_db)):
    return db.query(Classroom).order_by(Classroom.started_at.desc()).all()


@router.get("/{classroom_id}", response_model=ClassroomDetail)
def get_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    records = db.query(AttentionRecord).filter(AttentionRecord.classroom_id == classroom_id).all()
    head_down_count = sum(1 for r in records if abs(r.pitch) > 15)
    head_turn_count = sum(1 for r in records if abs(r.yaw) > 20)
    fatigue_count = sum(1 for r in records if r.is_blinking)

    high = sum(1 for r in records if r.attention_score >= 60)
    medium = sum(1 for r in records if 30 <= r.attention_score < 60)
    low = sum(1 for r in records if r.attention_score < 30)

    classroom.stats = {
        "head_down_count": head_down_count,
        "head_turn_count": head_turn_count,
        "fatigue_count": fatigue_count,
        "attention_distribution": {"high": high, "medium": medium, "low": low},
    }
    return classroom


@router.put("/{classroom_id}/end", response_model=ClassroomEndOut)
def end_classroom(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    if classroom.ended_at:
        raise HTTPException(400, "课堂已结束")

    classroom.ended_at = datetime.now()
    if classroom.started_at:
        classroom.duration = int((classroom.ended_at - classroom.started_at).total_seconds() / 60)

    avg = db.query(func.avg(AttentionRecord.attention_score)).filter(
        AttentionRecord.classroom_id == classroom_id
    ).scalar()
    classroom.avg_attention = round(avg or 0, 1)

    classroom.total_students = db.query(Student).filter(
        Student.classroom_id == classroom_id
    ).count()

    db.commit()
    db.refresh(classroom)
    return classroom
