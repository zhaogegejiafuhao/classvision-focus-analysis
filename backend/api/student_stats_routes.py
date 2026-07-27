"""学生管理与个人统计路由（从 stats_routes.py 拆分）

涵盖：
- 课堂内学生 CRUD（手动添加/编辑/删除）
- 学生个人注意力报告
- 学习行为画像分析
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_teacher_or_admin
from backend.core.access import assert_classroom_access
from backend.models.tables import (
    Classroom, Student, AttentionRecord, ExamRiskRecord, RegisteredPerson,
    HomeworkSubmission, ExamSubmission, Attendance, LeaveRequest,
)
from backend.models.schemas import (
    StudentOut, StudentCreate, StudentUpdate, TimelinePoint,
    StudentPersonalReport, StudentClassroomAttention,
)

router = APIRouter(prefix="/api", tags=["student-stats"])


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
    assert_classroom_access(classroom, current_user, db, teacher_only=True)
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
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_classroom_access(classroom, current_user, db, teacher_only=True)
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

    records = db.query(AttentionRecord).filter(AttentionRecord.student_record_id == student_id).all()
    avg_att = sum(r.attention_score for r in records) / len(records) if records else 0
    head_down = 1 if any(abs(r.pitch) > 15 for r in records) else 0
    blinks = records[-1].blink_count if records else 0

    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    risk_level = None
    if classroom and classroom.exam_mode:
        latest_risk = (
            db.query(ExamRiskRecord)
            .filter(ExamRiskRecord.student_record_id == student_id)
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
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_classroom_access(classroom, current_user, db, teacher_only=True)
    student = db.query(Student).filter(
        Student.id == student_id, Student.classroom_id == classroom_id,
    ).first()
    if not student:
        raise HTTPException(404, "学生不存在")
    db.query(AttentionRecord).filter(AttentionRecord.student_record_id == student_id).delete()
    db.query(ExamRiskRecord).filter(ExamRiskRecord.student_record_id == student_id).delete()
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
        records = db.query(AttentionRecord).filter(AttentionRecord.student_record_id == s.id).all()
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
            .filter(AttentionRecord.student_record_id == s.id)
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


# ===== 学习行为分析 =====

@router.get("/students/{student_id}/behavior")
def get_student_behavior(
    student_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取学生学习行为画像"""
    if current_user.role == "student" and current_user.id != student_id:
        raise HTTPException(403, "无权查看他人数据")

    student = db.query(Student).filter(Student.person_id == student_id).first()
    my_student_records = db.query(Student).filter(Student.person_id == student_id).all()
    my_student_ids = [s.id for s in my_student_records]

    # 作业行为
    homework_subs = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.student_id == student_id
    ).all()
    homework_total = len(homework_subs)
    homework_graded = sum(1 for s in homework_subs if s.status == "graded")
    homework_avg = sum(s.score or 0 for s in homework_subs if s.score) / max(1, homework_graded)

    # 考试行为
    exam_subs = db.query(ExamSubmission).filter(
        ExamSubmission.student_id == student_id
    ).all()
    exam_total = len(exam_subs)
    exam_avg = sum(s.score or 0 for s in exam_subs if s.score) / max(1, sum(1 for s in exam_subs if s.score))

    # 考勤行为（所有课堂的考勤记录）
    if my_student_ids:
        attendances = db.query(Attendance).filter(
            Attendance.student_record_id.in_(my_student_ids)
        ).all()
    else:
        attendances = []
    attendance_total = len(attendances)
    present_count = sum(1 for a in attendances if a.status == "present")
    late_count = sum(1 for a in attendances if a.status == "late")
    absent_count = sum(1 for a in attendances if a.status == "absent")
    leave_count = sum(1 for a in attendances if a.status == "leave")
    attendance_rate = present_count / max(1, attendance_total) * 100

    # 注意力行为（所有课堂的注意力记录）
    if my_student_ids:
        attention_records = db.query(AttentionRecord).filter(
            AttentionRecord.student_record_id.in_(my_student_ids)
        ).all()
    else:
        attention_records = []
    attention_avg = sum(r.attention_score for r in attention_records) / max(1, len(attention_records))

    # 活跃度评分（0-100）
    activity_score = min(100, (
        homework_total * 5 +
        exam_total * 10 +
        attendance_rate * 0.3 +
        attention_avg * 0.2
    ))

    # 请假次数
    leave_count_total = db.query(LeaveRequest).filter(
        LeaveRequest.student_id == student_id
    ).count()

    return {
        "student_id": student_id,
        "student_name": current_user.name if current_user.id == student_id else (student.person.name if student and student.person else f"学生{student_id}"),
        "homework": {
            "total": homework_total,
            "graded": homework_graded,
            "avg_score": round(homework_avg, 2),
            "submission_rate": round(homework_total / max(1, homework_total + homework_graded - homework_graded) * 100, 1) if homework_total else 0,
        },
        "exams": {
            "total": exam_total,
            "avg_score": round(exam_avg, 2),
        },
        "attendance": {
            "total": attendance_total,
            "present": present_count,
            "late": late_count,
            "absent": absent_count,
            "leave": leave_count,
            "rate": round(attendance_rate, 1),
        },
        "attention": {
            "avg_score": round(attention_avg, 2),
            "records": len(attention_records),
        },
        "leaves": leave_count_total,
        "activity_score": round(activity_score, 1),
    }
