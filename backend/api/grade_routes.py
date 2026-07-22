"""综合成绩管理 API"""
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_owner_or_admin
from backend.models.tables import (
    GradeConfig, Classroom, Student, RegisteredPerson,
    Homework, HomeworkSubmission, Exam, ExamSubmission, Attendance, CheckinSession,
    UsualScore,
)

router = APIRouter(prefix="/api/grades", tags=["grades"])


class GradeConfigUpdate(BaseModel):
    homework_weight: float = 0.3
    exam_weight: float = 0.4
    attendance_weight: float = 0.1
    usual_weight: float = 0.2


@router.get("/config/{classroom_id}")
def get_grade_config(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取成绩权重配置"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    # 学生必须是课堂成员
    if current_user.role == "student":
        is_member = db.query(Student).filter(
            Student.classroom_id == classroom_id, Student.person_id == current_user.id
        ).first() is not None
        if not is_member:
            raise HTTPException(403, "无权访问该课堂")
    elif current_user.role == "teacher" and classroom.teacher_person_id != current_user.id:
        raise HTTPException(403, "无权访问该课堂")

    config = db.query(GradeConfig).filter(GradeConfig.classroom_id == classroom_id).first()
    if not config:
        # 返回默认配置
        return {
            "classroom_id": classroom_id,
            "homework_weight": 0.3,
            "exam_weight": 0.4,
            "attendance_weight": 0.1,
            "usual_weight": 0.2,
        }
    return {
        "classroom_id": config.classroom_id,
        "homework_weight": config.homework_weight,
        "exam_weight": config.exam_weight,
        "attendance_weight": config.attendance_weight,
        "usual_weight": config.usual_weight,
    }


@router.post("/config/{classroom_id}")
def save_grade_config(
    classroom_id: int,
    data: GradeConfigUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """保存成绩权重配置"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以配置成绩权重")
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_owner_or_admin(classroom.teacher_person_id, current_user)

    # 验证权重之和为1
    total = data.homework_weight + data.exam_weight + data.attendance_weight + data.usual_weight
    if abs(total - 1.0) > 0.01:
        raise HTTPException(400, f"权重之和应为1.0，当前为{total:.2f}")

    config = db.query(GradeConfig).filter(GradeConfig.classroom_id == classroom_id).first()
    if config:
        config.homework_weight = data.homework_weight
        config.exam_weight = data.exam_weight
        config.attendance_weight = data.attendance_weight
        config.usual_weight = data.usual_weight
    else:
        config = GradeConfig(
            classroom_id=classroom_id,
            homework_weight=data.homework_weight,
            exam_weight=data.exam_weight,
            attendance_weight=data.attendance_weight,
            usual_weight=data.usual_weight,
        )
        db.add(config)
    db.commit()
    return {"success": True}


@router.get("/report/{classroom_id}")
def get_grade_report(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取课堂综合成绩报告"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    # 学生必须是课堂成员
    if current_user.role == "student":
        is_member = db.query(Student).filter(
            Student.classroom_id == classroom_id, Student.person_id == current_user.id
        ).first() is not None
        if not is_member:
            raise HTTPException(403, "无权访问该课堂")
    elif current_user.role == "teacher" and classroom.teacher_person_id != current_user.id:
        raise HTTPException(403, "无权访问该课堂")

    # 获取权重配置
    config = db.query(GradeConfig).filter(GradeConfig.classroom_id == classroom_id).first()
    if not config:
        config = GradeConfig(homework_weight=0.3, exam_weight=0.4, attendance_weight=0.1, usual_weight=0.2)

    students = db.query(Student).filter(Student.classroom_id == classroom_id).all()
    homeworks = db.query(Homework).filter(Homework.classroom_id == classroom_id).all()
    exams = db.query(Exam).filter(Exam.classroom_id == classroom_id, Exam.status.in_(["published", "closed"])).all()
    checkin_sessions = db.query(CheckinSession).filter(CheckinSession.classroom_id == classroom_id).all()

    result = []
    for student in students:
        person = student.person
        if not person:
            continue

        # 作业平均分
        hw_scores = []
        for hw in homeworks:
            sub = db.query(HomeworkSubmission).filter(
                HomeworkSubmission.homework_id == hw.id,
                HomeworkSubmission.student_id == person.id,
                HomeworkSubmission.status == "graded",
            ).first()
            if sub and sub.score is not None:
                hw_scores.append(sub.score / (hw.total_score or 100) * 100)
        hw_avg = sum(hw_scores) / len(hw_scores) if hw_scores else 0

        # 考试平均分
        exam_scores = []
        for exam in exams:
            sub = db.query(ExamSubmission).filter(
                ExamSubmission.exam_id == exam.id,
                ExamSubmission.student_id == person.id,
                ExamSubmission.status == "graded",
            ).first()
            if sub and sub.score is not None:
                exam_scores.append(sub.score / (exam.total_score or 100) * 100)
        exam_avg = sum(exam_scores) / len(exam_scores) if exam_scores else 0

        # 考勤出勤率
        total_sessions = len(checkin_sessions)
        present_count = 0
        if total_sessions > 0:
            for session in checkin_sessions:
                att = db.query(Attendance).filter(
                    Attendance.checkin_session_id == session.id,
                    Attendance.student_id == student.id,
                    Attendance.status == "present",
                ).first()
                if att:
                    present_count += 1
        attendance_rate = (present_count / total_sessions * 100) if total_sessions > 0 else 100

        # 平时分：从 UsualScore 表读取，默认 80
        usual = db.query(UsualScore).filter(
            UsualScore.classroom_id == classroom_id,
            UsualScore.person_id == person.id,
        ).first()
        usual_score = usual.score if usual else 80.0

        # 综合成绩
        total_grade = (
            hw_avg * config.homework_weight
            + exam_avg * config.exam_weight
            + attendance_rate * config.attendance_weight
            + usual_score * config.usual_weight
        )

        result.append({
            "student_id": student.id,
            "person_id": person.id,
            "name": person.name,
            "homework_avg": round(hw_avg, 1),
            "exam_avg": round(exam_avg, 1),
            "attendance_rate": round(attendance_rate, 1),
            "usual_score": usual_score,
            "total_grade": round(total_grade, 1),
        })

    # 按综合成绩排序
    result.sort(key=lambda x: x["total_grade"], reverse=True)
    return {
        "config": {
            "homework_weight": config.homework_weight,
            "exam_weight": config.exam_weight,
            "attendance_weight": config.attendance_weight,
            "usual_weight": config.usual_weight,
        },
        "students": result,
    }


@router.put("/usual-score/{classroom_id}/{person_id}")
def update_usual_score(
    classroom_id: int,
    person_id: int,
    score: float,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """更新学生平时分"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以修改平时分")
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_owner_or_admin(classroom.teacher_person_id, current_user)
    if score < 0 or score > 100:
        raise HTTPException(400, "平时分应在0-100之间")

    # 持久化到 UsualScore 表
    usual = db.query(UsualScore).filter(
        UsualScore.classroom_id == classroom_id,
        UsualScore.person_id == person_id,
    ).first()
    if usual:
        usual.score = score
    else:
        usual = UsualScore(classroom_id=classroom_id, person_id=person_id, score=score)
        db.add(usual)
    db.commit()

    return {"success": True, "person_id": person_id, "usual_score": score}


@router.get("/trend/{student_id}")
def get_grade_trend(
    student_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取学生成绩趋势"""
    if current_user.role == "student" and current_user.id != student_id:
        raise HTTPException(403, "无权查看他人成绩")

    homework_subs = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.student_id == student_id,
        HomeworkSubmission.score.isnot(None),
    ).order_by(HomeworkSubmission.submitted_at.asc()).all()

    exam_subs = db.query(ExamSubmission).filter(
        ExamSubmission.student_id == student_id,
        ExamSubmission.score.isnot(None),
    ).order_by(ExamSubmission.submitted_at.asc()).all()

    trend = []
    for sub in homework_subs:
        hw = sub.homework
        trend.append({
            "type": "homework",
            "title": hw.title,
            "score": sub.score,
            "total_score": hw.total_score,
            "percentage": round(sub.score / hw.total_score * 100, 1) if hw.total_score else 0,
            "date": sub.submitted_at,
        })
    for sub in exam_subs:
        exam = sub.exam
        trend.append({
            "type": "exam",
            "title": exam.title,
            "score": sub.score,
            "total_score": exam.total_score,
            "percentage": round(sub.score / exam.total_score * 100, 1) if exam.total_score else 0,
            "date": sub.submitted_at,
        })

    trend.sort(key=lambda x: x["date"])
    for i, item in enumerate(trend):
        item["index"] = i + 1

    return {
        "trend": trend,
        "avg_homework": round(sum(t["percentage"] for t in trend if t["type"] == "homework") / max(1, sum(1 for t in trend if t["type"] == "homework")), 1),
        "avg_exam": round(sum(t["percentage"] for t in trend if t["type"] == "exam") / max(1, sum(1 for t in trend if t["type"] == "exam")), 1),
    }
