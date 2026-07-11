from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_teacher_or_admin, assert_owner_or_admin
from backend.models.tables import Classroom, Student, AttentionRecord, ExamRiskRecord, RegisteredPerson, Report, ChatMessage
from backend.models.schemas import ClassroomCreate, ClassroomUpdate, ClassroomOut, ClassroomDetail, ClassroomEndOut

router = APIRouter(prefix="/api/classrooms", tags=["classrooms"])


@router.post("", response_model=ClassroomOut)
def create_classroom(
    data: ClassroomCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    assert_teacher_or_admin(current_user)
    teacher_person_id = data.teacher_person_id
    if teacher_person_id is None and current_user.role in ("teacher", "admin"):
        teacher_person_id = current_user.id
    classroom = Classroom(
        name=data.name,
        teacher=data.teacher,
        exam_mode=data.exam_mode,
        teacher_person_id=teacher_person_id,
    )
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom


@router.get("", response_model=list[ClassroomOut])
def list_classrooms(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return db.query(Classroom).order_by(Classroom.started_at.desc()).all()


@router.get("/{classroom_id}", response_model=ClassroomDetail)
def get_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    records = db.query(AttentionRecord).filter(
        AttentionRecord.classroom_id == classroom_id
    ).all()

    student_ids = db.query(func.distinct(AttentionRecord.student_id)).filter(
        AttentionRecord.classroom_id == classroom_id
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

    high = sum(1 for r in records if r.attention_score >= 60)
    medium = sum(1 for r in records if 30 <= r.attention_score < 60)
    low = sum(1 for r in records if r.attention_score < 30)

    stats = {
        "head_down_count": head_down_count,
        "head_turn_count": head_turn_count,
        "fatigue_count": fatigue_count,
        "attention_distribution": {"high": high, "medium": medium, "low": low},
    }

    if classroom.exam_mode:
        risk_counts = (
            db.query(ExamRiskRecord.risk_level, func.count())
            .filter(ExamRiskRecord.classroom_id == classroom_id)
            .group_by(ExamRiskRecord.risk_level)
            .all()
        )
        stats["risk_distribution"] = {level: count for level, count in risk_counts}

    classroom.stats = stats
    return classroom


@router.put("/{classroom_id}", response_model=ClassroomOut)
def update_classroom(
    classroom_id: int,
    data: ClassroomUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """编辑课堂（创建者或管理员）"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_owner_or_admin(classroom.teacher_person_id, current_user)

    if data.name is not None:
        classroom.name = data.name
    if data.teacher is not None:
        classroom.teacher = data.teacher
    if data.exam_mode is not None:
        classroom.exam_mode = data.exam_mode
    if data.teacher_person_id is not None:
        classroom.teacher_person_id = data.teacher_person_id

    db.commit()
    db.refresh(classroom)
    return classroom


@router.delete("/{classroom_id}")
def delete_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除课堂（创建者或管理员）级联删除关联数据"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_owner_or_admin(classroom.teacher_person_id, current_user)

    db.query(AttentionRecord).filter(AttentionRecord.classroom_id == classroom_id).delete()
    db.query(ExamRiskRecord).filter(ExamRiskRecord.classroom_id == classroom_id).delete()
    db.query(ChatMessage).filter(ChatMessage.classroom_id == classroom_id).delete()
    db.query(Report).filter(Report.classroom_id == classroom_id).delete()
    db.query(Student).filter(Student.classroom_id == classroom_id).delete()
    db.delete(classroom)
    db.commit()
    return {"message": "课堂已删除"}


@router.put("/{classroom_id}/end", response_model=ClassroomEndOut)
def end_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
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
