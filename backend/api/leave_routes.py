"""请假管理 API"""
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import LeaveRequest, RegisteredPerson, Classroom, Student, Notification, Attendance, CheckinSession

router = APIRouter(prefix="/api/leaves", tags=["leaves"])


class LeaveCreate(BaseModel):
    classroom_id: int
    start_date: datetime
    end_date: datetime
    leave_type: str = "sick"
    reason: str


class LeaveOut(BaseModel):
    id: int
    student_id: int
    student_name: str
    classroom_id: int
    classroom_name: str
    start_date: datetime
    end_date: datetime
    leave_type: str
    reason: str
    status: str
    teacher_feedback: Optional[str]
    created_at: datetime
    reviewed_at: Optional[datetime]

    class Config:
        from_attributes = True


class LeaveReview(BaseModel):
    status: str  # approved/rejected
    feedback: str = ""


@router.get("", response_model=list[LeaveOut])
def list_leaves(
    status: Optional[str] = None,
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取请假列表"""
    query = db.query(LeaveRequest)
    if current_user.role == "teacher":
        teacher_classroom_ids = db.query(Classroom.id).filter(Classroom.teacher_person_id == current_user.id).all()
        cids = [c[0] for c in teacher_classroom_ids]
        query = query.filter(LeaveRequest.classroom_id.in_(cids))
    elif current_user.role == "student":
        query = query.filter(LeaveRequest.student_id == current_user.id)
    if status:
        query = query.filter(LeaveRequest.status == status)
    if classroom_id:
        query = query.filter(LeaveRequest.classroom_id == classroom_id)
    query = query.order_by(LeaveRequest.created_at.desc())

    result = []
    for leave in query.all():
        result.append(LeaveOut(
            id=leave.id,
            student_id=leave.student_id,
            student_name=leave.student.name,
            classroom_id=leave.classroom_id,
            classroom_name=leave.classroom.name,
            start_date=leave.start_date,
            end_date=leave.end_date,
            leave_type=leave.leave_type,
            reason=leave.reason,
            status=leave.status,
            teacher_feedback=leave.teacher_feedback,
            created_at=leave.created_at,
            reviewed_at=leave.reviewed_at,
        ))
    return result


@router.post("", response_model=LeaveOut)
def create_leave(
    data: LeaveCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生提交请假申请"""
    leave = LeaveRequest(
        student_id=current_user.id,
        classroom_id=data.classroom_id,
        start_date=data.start_date,
        end_date=data.end_date,
        leave_type=data.leave_type,
        reason=data.reason,
    )
    db.add(leave)
    db.commit()
    db.refresh(leave)

    return LeaveOut(
        id=leave.id,
        student_id=leave.student_id,
        student_name=leave.student.name,
        classroom_id=leave.classroom_id,
        classroom_name=leave.classroom.name,
        start_date=leave.start_date,
        end_date=leave.end_date,
        leave_type=leave.leave_type,
        reason=leave.reason,
        status=leave.status,
        teacher_feedback=leave.teacher_feedback,
        created_at=leave.created_at,
        reviewed_at=leave.reviewed_at,
    )


@router.post("/{leave_id}/review")
def review_leave(
    leave_id: int,
    data: LeaveReview,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师审批请假"""
    leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    if not leave:
        raise HTTPException(404, "请假申请不存在")

    classroom = leave.classroom
    if classroom.teacher_person_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权审批")

    leave.status = data.status
    leave.teacher_feedback = data.feedback
    leave.reviewed_at = datetime.now()

    if data.status == "approved":
        student = db.query(Student).filter(Student.person_id == leave.student_id).first()
        if student:
            sessions = db.query(CheckinSession).filter(
                CheckinSession.classroom_id == leave.classroom_id,
                CheckinSession.start_time >= leave.start_date,
                CheckinSession.start_time <= leave.end_date,
            ).all()
            for session in sessions:
                existing = db.query(Attendance).filter(
                    Attendance.checkin_session_id == session.id,
                    Attendance.student_id == student.id,
                ).first()
                if not existing:
                    att = Attendance(
                        classroom_id=leave.classroom_id,
                        student_id=student.id,
                        checkin_session_id=session.id,
                        status="leave",
                        note=f"请假：{leave.reason[:50]}",
                    )
                    db.add(att)

    notification = Notification(
        title=f"请假申请{'已通过' if data.status == 'approved' else '已拒绝'}",
        content=data.feedback or ("请假已通过" if data.status == "approved" else "请假已拒绝"),
        type="attendance",
        sender_id=current_user.id,
        receiver_id=leave.student_id,
    )
    db.add(notification)
    db.commit()
    return {"success": True}
