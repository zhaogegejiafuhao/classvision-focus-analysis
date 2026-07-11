from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_teacher_or_admin, assert_owner_or_admin
from backend.models.tables import Classroom, Student, AttentionRecord, ExamRiskRecord, Report, RegisteredPerson
from backend.models.schemas import StudentOut, StudentCreate, StudentUpdate, TimelinePoint, ReportOut, StudentPersonalReport, StudentClassroomAttention, ExamRiskOut
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
def get_students(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()

    # 学生只能看到自己的数据
    if current_user.role == "student":
        students = [s for s in students if s.person_id == current_user.id]

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
def create_report(
    classroom_id: int,
    force: bool = False,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    assert_teacher_or_admin(current_user)
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    existing = db.query(Report).filter(Report.classroom_id == classroom_id).first()
    if existing and not force:
        return existing
    if existing and force:
        db.delete(existing)
        db.commit()

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

    # 计算每个学生的平均注意力
    student_avg = {}
    for sid in student_ids:
        s_records = [r for r in records if r.student_id == sid]
        if s_records:
            student_avg[sid] = sum(r.attention_score for r in s_records) / len(s_records)

    # 注意力分布区间
    high_attention_count = sum(1 for v in student_avg.values() if v >= 75)
    medium_attention_count = sum(1 for v in student_avg.values() if 50 <= v < 75)
    low_attention_count = sum(1 for v in student_avg.values() if v < 50)

    # 学生注意力排行（Top5 / Bottom5）
    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()
    student_name_map = {s.id: s.name or f"学生{s.track_id}" for s in students}
    sorted_students = sorted(student_avg.items(), key=lambda x: x[1], reverse=True)
    top_students = "\n".join(
        f"- {student_name_map.get(sid, f'学生{sid}')}: {round(avg, 1)}%"
        for sid, avg in sorted_students[:5]
    ) or "暂无数据"
    bottom_students = "\n".join(
        f"- {student_name_map.get(sid, f'学生{sid}')}: {round(avg, 1)}%"
        for sid, avg in sorted_students[-5:][::-1]
    ) or "暂无数据"

    # 时间趋势（按分钟分组的平均注意力）
    time_rows = (
        db.query(
            func.strftime("%H:%M", AttentionRecord.timestamp).label("minute"),
            func.avg(AttentionRecord.attention_score).label("avg_att"),
        )
        .filter(AttentionRecord.classroom_id == classroom_id)
        .group_by("minute")
        .order_by("minute")
        .all()
    )
    if time_rows:
        time_trend = "\n".join(f"- {r.minute}: {round(r.avg_att, 1)}%" for r in time_rows)
    else:
        time_trend = "暂无数据"

    # 老师信息
    teacher_name = classroom.teacher
    if classroom.teacher_person_id:
        person = db.query(RegisteredPerson).filter(RegisteredPerson.id == classroom.teacher_person_id).first()
        if person:
            teacher_name = person.name

    stats = {
        "classroom_name": classroom.name,
        "teacher_name": teacher_name,
        "total_students": classroom.total_students,
        "avg_attention": classroom.avg_attention,
        "head_down_count": head_down_count,
        "head_turn_count": head_turn_count,
        "fatigue_count": fatigue_count,
        "duration": classroom.duration,
        "exam_mode": classroom.exam_mode,
        "high_attention_count": high_attention_count,
        "medium_attention_count": medium_attention_count,
        "low_attention_count": low_attention_count,
        "top_students": top_students,
        "bottom_students": bottom_students,
        "time_trend": time_trend,
    }

    content = generate_report(stats)
    report = Report(classroom_id=classroom_id, content=content)
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


@router.get("/classrooms/{classroom_id}/report", response_model=ReportOut)
def get_report(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    report = db.query(Report).filter(Report.classroom_id == classroom_id).first()
    if not report:
        raise HTTPException(404, "报告未生成")
    return report


@router.delete("/classrooms/{classroom_id}/report")
def delete_report(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除报告（创建者或管理员）"""
    report = db.query(Report).filter(Report.classroom_id == classroom_id).first()
    if not report:
        raise HTTPException(404, "报告不存在")
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    assert_owner_or_admin(classroom.teacher_person_id if classroom else None, current_user)
    db.delete(report)
    db.commit()
    return {"message": "报告已删除"}


# ===== 考试风险记录 =====

@router.get("/classrooms/{classroom_id}/exam-risks", response_model=list[ExamRiskOut])
def get_exam_risks(
    classroom_id: int,
    risk_level: str | None = Query(None),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取课堂的考试作弊风险记录（按风险等级可选过滤）"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    q = db.query(ExamRiskRecord).filter(ExamRiskRecord.classroom_id == classroom_id)
    if risk_level:
        q = q.filter(ExamRiskRecord.risk_level == risk_level)
    records = q.order_by(ExamRiskRecord.timestamp.desc()).all()

    student_cache = {}
    result = []
    for r in records:
        if r.student_id not in student_cache:
            s = db.query(Student).filter(Student.id == r.student_id).first()
            student_cache[r.student_id] = s.name or f"学生{s.track_id}" if s else "未知"
        result.append(ExamRiskOut(
            id=r.id,
            student_id=r.student_id,
            student_name=student_cache[r.student_id],
            risk_level=r.risk_level,
            gaze_deviation_duration=r.gaze_deviation_duration,
            head_down_duration=r.head_down_duration,
            head_turn_events=r.head_turn_events,
            cheating_object_nearby=r.cheating_object_nearby,
            attention_score=r.attention_score,
            timestamp=r.timestamp,
        ))
    return result


# ===== 学生管理 CRUD =====

@router.post("/classrooms/{classroom_id}/students", response_model=StudentOut)
def create_student(
    classroom_id: int,
    data: StudentCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """手动添加学生到课堂（教师/管理员）"""
    assert_teacher_or_admin(current_user)
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    student = Student(
        classroom_id=classroom_id,
        track_id=data.track_id,
        name=data.name,
        person_id=data.person_id,
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return StudentOut(
        id=student.id, track_id=student.track_id, name=student.name,
        avg_attention=0, head_down_count=0, blink_count=0, risk_level=None,
    )


@router.put("/classrooms/{classroom_id}/students/{student_id}", response_model=StudentOut)
def update_student(
    classroom_id: int,
    student_id: int,
    data: StudentUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """编辑学生信息（教师/管理员）"""
    assert_teacher_or_admin(current_user)
    student = db.query(Student).filter(
        Student.id == student_id, Student.classroom_id == classroom_id,
    ).first()
    if not student:
        raise HTTPException(404, "学生不存在")
    if data.name is not None:
        student.name = data.name
    if data.person_id is not None:
        student.person_id = data.person_id
    db.commit()
    db.refresh(student)

    records = db.query(AttentionRecord).filter(AttentionRecord.student_id == student_id).all()
    avg_att = sum(r.attention_score for r in records) / len(records) if records else 0
    head_down = 1 if any(abs(r.pitch) > 15 for r in records) else 0
    blinks = records[-1].blink_count if records else 0

    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    risk_level = None
    if classroom and classroom.exam_mode:
        latest_risk = (
            db.query(ExamRiskRecord)
            .filter(ExamRiskRecord.student_id == student_id)
            .order_by(ExamRiskRecord.timestamp.desc())
            .first()
        )
        risk_level = latest_risk.risk_level if latest_risk else "low"

    return StudentOut(
        id=student.id, track_id=student.track_id, name=student.name or f"学生{student.track_id}",
        avg_attention=round(avg_att, 1), head_down_count=head_down,
        blink_count=blinks, risk_level=risk_level,
    )


@router.delete("/classrooms/{classroom_id}/students/{student_id}")
def delete_student(
    classroom_id: int,
    student_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除学生（教师/管理员）级联删除注意力记录"""
    assert_teacher_or_admin(current_user)
    student = db.query(Student).filter(
        Student.id == student_id, Student.classroom_id == classroom_id,
    ).first()
    if not student:
        raise HTTPException(404, "学生不存在")
    db.query(AttentionRecord).filter(AttentionRecord.student_id == student_id).delete()
    db.query(ExamRiskRecord).filter(AttentionRecord.student_id == student_id).delete()
    db.delete(student)
    db.commit()
    return {"message": "学生已删除"}


# ===== 学生个人报告 =====

@router.get("/me/attention-history", response_model=StudentPersonalReport)
def get_my_attention_history(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前学生个人的注意力历史数据"""
    if current_user.role != "student":
        raise HTTPException(403, "仅学生可查看个人报告")

    # 找到该 person 关联的所有 student 记录
    my_students = db.query(Student).filter(Student.person_id == current_user.id).all()
    if not my_students:
        return StudentPersonalReport(
            student_name=current_user.name,
            total_classrooms=0,
            overall_avg_attention=0,
            best_classroom="",
            worst_classroom="",
            classrooms=[],
        )

    classroom_data = []
    for s in my_students:
        records = db.query(AttentionRecord).filter(AttentionRecord.student_id == s.id).all()
        if not records:
            continue
        avg_att = sum(r.attention_score for r in records) / len(records)
        head_down = sum(1 for r in records if abs(r.pitch) > 15)
        blinks = records[-1].blink_count if records else 0

        classroom = db.query(Classroom).filter(Classroom.id == s.classroom_id).first()
        if not classroom:
            continue

        # 时间线
        time_rows = (
            db.query(
                func.strftime("%H:%M", AttentionRecord.timestamp).label("minute"),
                func.avg(AttentionRecord.attention_score).label("avg_att"),
            )
            .filter(AttentionRecord.student_id == s.id)
            .group_by("minute")
            .order_by("minute")
            .all()
        )
        timeline = [
            TimelinePoint(timestamp=r.minute, avg_attention=round(r.avg_att, 1), student_count=1)
            for r in time_rows
        ]

        classroom_data.append(StudentClassroomAttention(
            classroom_id=classroom.id,
            classroom_name=classroom.name,
            teacher=classroom.teacher,
            avg_attention=round(avg_att, 1),
            head_down_count=head_down,
            blink_count=blinks,
            duration=classroom.duration,
            started_at=classroom.started_at,
            timeline=timeline,
        ))

    total = len(classroom_data)
    overall_avg = sum(c.avg_attention for c in classroom_data) / total if total else 0
    best = max(classroom_data, key=lambda c: c.avg_attention).classroom_name if classroom_data else ""
    worst = min(classroom_data, key=lambda c: c.avg_attention).classroom_name if classroom_data else ""

    return StudentPersonalReport(
        student_name=current_user.name,
        total_classrooms=total,
        overall_avg_attention=round(overall_avg, 1),
        best_classroom=best,
        worst_classroom=worst,
        classrooms=classroom_data,
    )
