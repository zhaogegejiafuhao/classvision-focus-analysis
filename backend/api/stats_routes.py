from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.tables import Classroom, Student, AttentionRecord, ExamRiskRecord, Report, RegisteredPerson
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


@router.get("/classrooms/{classroom_id}/heatmap")
def get_heatmap(classroom_id: int, db: Session = Depends(get_db)):
    """获取学生注意力热力图数据（学生x时间段的注意力矩阵）"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 获取所有学生
    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()
    student_map = {s.id: s.name or f"学生{s.track_id}" for s in students}

    # 获取所有时间点（按分钟分组）
    time_rows = (
        db.query(
            func.strftime("%H:%M", AttentionRecord.timestamp).label("minute"),
        )
        .filter(AttentionRecord.classroom_id == classroom_id)
        .group_by("minute")
        .order_by("minute")
        .all()
    )
    time_labels = [r.minute for r in time_rows]

    # 构建热力图数据矩阵
    heatmap_data = []
    for student_id, student_name in student_map.items():
        row_data = []
        for time_label in time_labels:
            avg_att = (
                db.query(func.avg(AttentionRecord.attention_score))
                .filter(
                    AttentionRecord.classroom_id == classroom_id,
                    AttentionRecord.student_id == student_id,
                    func.strftime("%H:%M", AttentionRecord.timestamp) == time_label,
                )
                .scalar() or 0
            )
            row_data.append(round(avg_att, 1))
        heatmap_data.append({
            "student_name": student_name,
            "data": row_data,
        })

    return {
        "time_labels": time_labels,
        "heatmap_data": heatmap_data,
    }


@router.get("/compare")
def compare_classrooms(
    classroom_ids: str,  # 逗号分隔的课堂ID，如 "1,2,3"
    db: Session = Depends(get_db),
):
    """多课堂对比数据"""
    ids = [int(x) for x in classroom_ids.split(",") if x.strip()]
    if not ids:
        raise HTTPException(400, "请提供课堂ID")

    classrooms = db.query(Classroom).filter(Classroom.id.in_(ids)).all()
    if not classrooms:
        raise HTTPException(404, "课堂不存在")

    result = []
    for c in classrooms:
        # 获取每个课堂的学生数和平均注意力
        student_count = db.query(Student).filter(Student.classroom_id == c.id).count()
        
        # 获取详细统计
        records = db.query(AttentionRecord).filter(AttentionRecord.classroom_id == c.id).all()
        student_ids = set(r.student_id for r in records)
        head_down_count = sum(
            1 for sid in student_ids
            if any(abs(r.pitch) > 15 for r in records if r.student_id == sid)
        )
        fatigue_count = sum(
            1 for sid in student_ids
            if any(r.is_blinking for r in records if r.student_id == sid)
        )

        # 获取老师信息
        teacher_name = c.teacher
        if c.teacher_person_id:
            person = db.query(RegisteredPerson).filter(RegisteredPerson.id == c.teacher_person_id).first()
            if person:
                teacher_name = person.name

        result.append({
            "id": c.id,
            "name": c.name,
            "teacher": teacher_name,
            "duration": c.duration,
            "avg_attention": round(c.avg_attention, 1),
            "total_students": student_count,
            "head_down_count": head_down_count,
            "fatigue_count": fatigue_count,
            "exam_mode": c.exam_mode,
            "started_at": c.started_at.strftime("%Y-%m-%d %H:%M"),
        })

    return {"classrooms": result}


@router.get("/classrooms/{classroom_id}/attendance")
def get_attendance(classroom_id: int, db: Session = Depends(get_db)):
    """获取课堂出席情况（基于人脸识别匹配）"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 获取课堂中的学生
    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()

    # 分类：已识别（有人脸匹配）vs 未识别
    identified = []
    unidentified = []

    for s in students:
        if s.person_id:
            person = db.query(RegisteredPerson).filter(RegisteredPerson.id == s.person_id).first()
            identified.append({
                "student_id": s.id,
                "track_id": s.track_id,
                "name": s.name or person.name if person else f"学生{s.track_id}",
                "person_id": s.person_id,
                "avg_attention": _get_student_avg_attention(s.id, db),
            })
        else:
            unidentified.append({
                "student_id": s.id,
                "track_id": s.track_id,
                "name": s.name or f"学生{s.track_id}",
                "avg_attention": _get_student_avg_attention(s.id, db),
            })

    # 获取已注册但未出席的学生
    all_registered = db.query(RegisteredPerson).filter(RegisteredPerson.role == "student").all()
    identified_ids = set(s["person_id"] for s in identified)
    absent = [
        {"id": p.id, "name": p.name}
        for p in all_registered if p.id not in identified_ids
    ]

    return {
        "total_students": len(students),
        "identified_count": len(identified),
        "unidentified_count": len(unidentified),
        "absent_count": len(absent),
        "identified": identified,
        "unidentified": unidentified,
        "absent": absent,
    }


def _get_student_avg_attention(student_id: int, db: Session) -> float:
    """获取学生的平均注意力"""
    avg = db.query(func.avg(AttentionRecord.attention_score)).filter(
        AttentionRecord.student_id == student_id
    ).scalar()
    return round(avg or 0, 1)


@router.get("/classrooms/{classroom_id}/students", response_model=list[StudentOut])
def get_students(classroom_id: int, db: Session = Depends(get_db)):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()
    result = []
    for s in students:
        records = db.query(AttentionRecord).filter(AttentionRecord.student_id == s.id).all()
        avg_att = sum(r.attention_score for r in records) / len(records) if records else 0
        head_down = 1 if any(abs(r.pitch) > 15 for r in records) else 0
        blinks = records[-1].blink_count if records else 0

        risk_level = None
        if classroom and classroom.exam_mode:
            latest_risk = (
                db.query(ExamRiskRecord)
                .filter(ExamRiskRecord.student_id == s.id)
                .order_by(ExamRiskRecord.timestamp.desc())
                .first()
            )
            risk_level = latest_risk.risk_level if latest_risk else "low"

        result.append(StudentOut(
            id=s.id, track_id=s.track_id, name=s.name or f"学生{s.track_id}",
            avg_attention=round(avg_att, 1), head_down_count=head_down,
            blink_count=blinks, risk_level=risk_level,
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
