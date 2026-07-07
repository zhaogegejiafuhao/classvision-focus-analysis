from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.tables import Classroom, Student, AttentionRecord, Report
from backend.models.schemas import StudentOut, TimelinePoint, ReportOut
from backend.services.ollama_service import generate_report

router = APIRouter(prefix="/api", tags=["stats"])


@router.get("/classrooms/{classroom_id}/timeline", response_model=list[TimelinePoint])
def get_timeline(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    rows = (
        db.query(
            func.strftime("%H:%M", AttentionRecord.timestamp).label("minute"),
            func.avg(AttentionRecord.attention_score).label("avg_attention"),
            func.count(func.distinct(AttentionRecord.student_id)).label("student_count"),
        )
        .filter(AttentionRecord.classroom_id == classroom_id)
        .group_by("minute")
        .order_by("minute")
        .all()
    )

    return [
        TimelinePoint(
            timestamp=r.minute,
            avg_attention=round(r.avg_attention, 1),
            student_count=r.student_count,
        )
        for r in rows
    ]


@router.get("/classrooms/{classroom_id}/students", response_model=list[StudentOut])
def get_students(classroom_id: int, db: Session = Depends(get_db)):
    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()
    result = []
    for s in students:
        records = db.query(AttentionRecord).filter(AttentionRecord.student_id == s.id).all()
        avg_att = sum(r.attention_score for r in records) / len(records) if records else 0
        head_down = 1 if any(abs(r.pitch) > 15 for r in records) else 0
        blinks = records[-1].blink_count if records else 0
        result.append(StudentOut(
            id=s.id, track_id=s.track_id, name=s.name or f"学生{s.track_id}",
            avg_attention=round(avg_att, 1), head_down_count=head_down, blink_count=blinks,
        ))
    return result


@router.post("/classrooms/{classroom_id}/report", response_model=ReportOut)
def create_report(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    existing = db.query(Report).filter(Report.classroom_id == classroom_id).first()
    if existing:
        return existing

    records = db.query(AttentionRecord).filter(AttentionRecord.classroom_id == classroom_id).all()

    student_ids = set(r.student_id for r in records)
    head_down_count = sum(
        1 for sid in student_ids
        if any(abs(r.pitch) > 15 for r in records if r.student_id == sid)
    )
    head_turn_count = sum(
        1 for sid in student_ids
        if any(abs(r.yaw) > 20 for r in records if r.student_id == sid)
    )
    fatigue_count = sum(
        1 for sid in student_ids
        if any(r.is_blinking for r in records if r.student_id == sid)
    )

    stats = {
        "total_students": classroom.total_students,
        "avg_attention": classroom.avg_attention,
        "head_down_count": head_down_count,
        "head_turn_count": head_turn_count,
        "fatigue_count": fatigue_count,
        "duration": classroom.duration,
    }

    content = generate_report(stats)
    report = Report(classroom_id=classroom_id, content=content)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


@router.get("/classrooms/{classroom_id}/report", response_model=ReportOut)
def get_report(classroom_id: int, db: Session = Depends(get_db)):
    report = db.query(Report).filter(Report.classroom_id == classroom_id).first()
    if not report:
        raise HTTPException(404, "报告未生成")
    return report
