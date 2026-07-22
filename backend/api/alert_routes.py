"""教学预警系统 API"""
from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    RegisteredPerson, Student, Classroom,
    Homework, HomeworkSubmission,
    Exam, ExamSubmission,
    Attendance, CheckinSession,
    Notification, ClassroomMember,
)

router = APIRouter(prefix="/api/alerts", tags=["alerts"])


@router.get("")
def get_alerts(
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取教学预警列表"""
    alerts = []

    # 确定查询范围（按角色校验课堂归属）
    if classroom_id:
        # 指定课堂时，校验用户是否有权访问该课堂
        if current_user.role == "student":
            member = db.query(ClassroomMember).filter(
                ClassroomMember.classroom_id == classroom_id,
                ClassroomMember.person_id == current_user.id,
            ).first()
            if not member:
                raise HTTPException(403, "无权访问该课堂的告警")
        elif current_user.role == "teacher":
            cr = db.query(Classroom).filter(
                Classroom.id == classroom_id,
                Classroom.teacher_person_id == current_user.id,
            ).first()
            if not cr:
                raise HTTPException(403, "无权访问该课堂的告警")
        classrooms = db.query(Classroom).filter(Classroom.id == classroom_id).all()
    elif current_user.role == "teacher":
        classrooms = db.query(Classroom).filter(Classroom.teacher_person_id == current_user.id).all()
    elif current_user.role == "student":
        # 学生只能看自己所在课堂的告警
        my_classroom_ids = {
            m.classroom_id for m in
            db.query(ClassroomMember).filter(ClassroomMember.person_id == current_user.id).all()
        }
        if my_classroom_ids:
            classrooms = db.query(Classroom).filter(Classroom.id.in_(my_classroom_ids)).all()
        else:
            classrooms = []
    else:
        classrooms = db.query(Classroom).limit(20).all()

    for classroom in classrooms:
        students = db.query(Student).filter(Student.classroom_id == classroom.id).all()

        for student in students:
            if not student.person:
                continue

            # 1. 出勤率预警
            sessions = db.query(CheckinSession).filter(CheckinSession.classroom_id == classroom.id).all()
            if len(sessions) >= 3:
                present = 0
                for s in sessions:
                    att = db.query(Attendance).filter(
                        Attendance.checkin_session_id == s.id,
                        Attendance.student_record_id == student.id,
                        Attendance.status == "present",
                    ).first()
                    if att:
                        present += 1
                rate = present / len(sessions)
                if rate < 0.6:
                    alerts.append({
                        "type": "attendance",
                        "level": "high" if rate < 0.4 else "medium",
                        "student_id": student.id,
                        "student_name": student.person.name,
                        "classroom_id": classroom.id,
                        "classroom_name": classroom.name,
                        "message": f"出勤率仅{rate * 100:.0f}%，低于60%预警线",
                        "value": round(rate * 100, 1),
                    })

            # 2. 作业未交预警
            homeworks = db.query(Homework).filter(Homework.classroom_id == classroom.id).all()
            unsubmitted = 0
            for hw in homeworks:
                sub = db.query(HomeworkSubmission).filter(
                    HomeworkSubmission.homework_id == hw.id,
                    HomeworkSubmission.student_id == student.person_id,
                ).first()
                if not sub and hw.deadline and hw.deadline < datetime.now():
                    unsubmitted += 1
            if unsubmitted >= 3:
                alerts.append({
                    "type": "homework",
                    "level": "high" if unsubmitted >= 5 else "medium",
                    "student_id": student.id,
                    "student_name": student.person.name,
                    "classroom_id": classroom.id,
                    "classroom_name": classroom.name,
                    "message": f"已有{unsubmitted}次作业未提交",
                    "value": unsubmitted,
                })

            # 3. 考试成绩预警
            exams = db.query(Exam).filter(
                Exam.classroom_id == classroom.id,
                Exam.status.in_(["published", "closed"]),
            ).all()
            fail_count = 0
            for exam in exams:
                sub = db.query(ExamSubmission).filter(
                    ExamSubmission.exam_id == exam.id,
                    ExamSubmission.student_id == student.person_id,
                    ExamSubmission.status == "graded",
                ).first()
                if sub and sub.score is not None:
                    if sub.score < exam.total_score * 0.6:
                        fail_count += 1
            if fail_count >= 2:
                alerts.append({
                    "type": "exam",
                    "level": "high" if fail_count >= 3 else "medium",
                    "student_id": student.id,
                    "student_name": student.person.name,
                    "classroom_id": classroom.id,
                    "classroom_name": classroom.name,
                    "message": f"已有{fail_count}次考试不及格",
                    "value": fail_count,
                })

    # 按预警级别排序
    level_order = {"high": 0, "medium": 1, "low": 2}
    alerts.sort(key=lambda x: (level_order.get(x["level"], 3), x.get("value", 0)), reverse=False)

    return {"total": len(alerts), "high": sum(1 for a in alerts if a["level"] == "high"), "alerts": alerts}
