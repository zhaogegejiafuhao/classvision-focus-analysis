"""考勤签到系统 API"""
import csv
import io
import random
import string
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_, func as sa_func

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import CheckinSession, Attendance, RegisteredPerson, Classroom, Student, Notification

router = APIRouter(prefix="/api/checkin", tags=["checkin"])


# ===== Pydantic 模型 =====
class CheckinSessionCreate(BaseModel):
    classroom_id: int
    type: str = "normal"  # normal/encrypted


class CheckinSubmit(BaseModel):
    session_id: int
    code: Optional[str] = None  # 加密签到时需要


class CheckinSessionOut(BaseModel):
    id: int
    classroom_id: int
    classroom_name: str
    teacher_id: int
    teacher_name: str
    type: str
    code: Optional[str]
    status: str
    start_time: datetime
    end_time: Optional[datetime]
    checked_count: int
    total_count: int

    class Config:
        from_attributes = True


class AttendanceOut(BaseModel):
    id: int
    student_id: int
    student_name: str
    status: str
    checkin_time: Optional[datetime]
    note: Optional[str]

    class Config:
        from_attributes = True


# ===== 教师端 API =====
@router.post("/sessions", response_model=CheckinSessionOut)
def create_session(
    data: CheckinSessionCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建签到会话"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建签到")
    
    # 检查课堂是否存在
    classroom = db.query(Classroom).filter(Classroom.id == data.classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    
    # 权限检查：教师只能为自己创建的课堂签到
    if current_user.role == "teacher" and classroom.teacher_person_id != current_user.id:
        raise HTTPException(403, "只能为自己创建的课堂发起签到")
    
    # 检查是否已有进行中的签到
    active = db.query(CheckinSession).filter(
        CheckinSession.classroom_id == data.classroom_id,
        CheckinSession.status == "active",
    ).first()
    if active:
        raise HTTPException(400, "该课堂已有进行中的签到")
    
    # 生成加密签到的验证码
    code = None
    if data.type == "encrypted":
        code = ''.join(random.choices(string.digits, k=6))
    
    session = CheckinSession(
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        type=data.type,
        code=code,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    
    # 获取课堂学生总数
    students = db.query(Student).filter(Student.classroom_id == data.classroom_id).all()
    total_count = len(students)
    
    # 发送通知给学生
    for student in students:
        if student.person:
            notification = Notification(
                title=f"签到提醒：{classroom.name}",
                content=f"教师发起了{'加密' if data.type == 'encrypted' else '普通'}签到，请及时完成签到。",
                type="attendance",
                sender_id=current_user.id,
                receiver_id=student.person_id,
                classroom_id=data.classroom_id,
            )
            db.add(notification)
    db.commit()
    
    return CheckinSessionOut(
        id=session.id,
        classroom_id=session.classroom_id,
        classroom_name=classroom.name,
        teacher_id=session.teacher_id,
        teacher_name=current_user.name,
        type=session.type,
        code=session.code,
        status=session.status,
        start_time=session.start_time,
        end_time=session.end_time,
        checked_count=0,
        total_count=total_count,
    )


@router.get("/sessions", response_model=list[CheckinSessionOut])
def list_sessions(
    classroom_id: Optional[int] = None,
    status: Optional[str] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取签到会话列表"""
    query = db.query(CheckinSession).options(
        joinedload(CheckinSession.classroom),
        joinedload(CheckinSession.teacher),
    )
    
    if current_user.role == "teacher":
        query = query.filter(CheckinSession.teacher_id == current_user.id)
    
    if classroom_id:
        query = query.filter(CheckinSession.classroom_id == classroom_id)
    if status:
        query = query.filter(CheckinSession.status == status)
    
    query = query.order_by(CheckinSession.created_at.desc())
    
    sessions = query.all()
    # 批量查询学生总数和签到数，避免 N+1
    session_ids = [s.id for s in sessions]
    classroom_ids = list(set(s.classroom_id for s in sessions))
    student_counts = {cid: db.query(Student).filter(Student.classroom_id == cid).count() for cid in classroom_ids}
    checked_counts = dict(
        db.query(Attendance.checkin_session_id, sa_func.count(Attendance.id))
        .filter(Attendance.checkin_session_id.in_(session_ids), Attendance.status == "present")
        .group_by(Attendance.checkin_session_id).all()
    ) if session_ids else {}
    
    result = []
    for session in sessions:
        classroom_name = session.classroom.name if session.classroom else ""
        teacher_name = session.teacher.name if session.teacher else ""
        total_count = student_counts.get(session.classroom_id, 0)
        checked_count = checked_counts.get(session.id, 0)
        
        result.append(CheckinSessionOut(
            id=session.id,
            classroom_id=session.classroom_id,
            classroom_name=classroom_name,
            teacher_id=session.teacher_id,
            teacher_name=teacher_name,
            type=session.type,
            code=session.code,
            status=session.status,
            start_time=session.start_time,
            end_time=session.end_time,
            checked_count=checked_count,
            total_count=total_count,
        ))
    return result


@router.get("/sessions/{session_id}", response_model=CheckinSessionOut)
def get_session(
    session_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取签到详情"""
    session = db.query(CheckinSession).filter(CheckinSession.id == session_id).first()
    if not session:
        raise HTTPException(404, "签到会话不存在")
    
    # 权限检查：教师只能看自己课堂的，学生只能看自己参与的课堂
    if current_user.role == "teacher":
        if session.teacher_id != current_user.id and current_user.role != "admin":
            raise HTTPException(403, "无权查看此签到会话")
    elif current_user.role == "student":
        student = db.query(Student).filter(Student.person_id == current_user.id).first()
        if not student or student.classroom_id != session.classroom_id:
            raise HTTPException(403, "无权查看此签到会话")
    
    classroom_name = session.classroom.name if session.classroom else ""
    teacher_name = session.teacher.name if session.teacher else ""
    students = db.query(Student).filter(Student.classroom_id == session.classroom_id).all()
    total_count = len(students)
    checked_count = db.query(Attendance).filter(
        Attendance.checkin_session_id == session.id,
        Attendance.status == "present",
    ).count()
    
    return CheckinSessionOut(
        id=session.id,
        classroom_id=session.classroom_id,
        classroom_name=classroom_name,
        teacher_id=session.teacher_id,
        teacher_name=teacher_name,
        type=session.type,
        code=session.code,
        status=session.status,
        start_time=session.start_time,
        end_time=session.end_time,
        checked_count=checked_count,
        total_count=total_count,
    )


@router.post("/sessions/{session_id}/close")
def close_session(
    session_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """结束签到"""
    session = db.query(CheckinSession).filter(CheckinSession.id == session_id).first()
    if not session:
        raise HTTPException(404, "签到会话不存在")
    
    if session.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权结束此签到")
    
    session.status = "closed"
    session.end_time = datetime.now()
    
    # 将未签到的学生标记为缺勤
    students = db.query(Student).filter(Student.classroom_id == session.classroom_id).all()
    for student in students:
        existing = db.query(Attendance).filter(
            Attendance.checkin_session_id == session.id,
            Attendance.student_id == student.id,
        ).first()
        if not existing:
            attendance = Attendance(
                classroom_id=session.classroom_id,
                student_id=student.id,
                checkin_session_id=session.id,
                status="absent",
                note="未签到",
            )
            db.add(attendance)
    
    db.commit()
    return {"success": True}


@router.get("/sessions/{session_id}/attendances", response_model=list[AttendanceOut])
def get_attendances(
    session_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取签到记录"""
    session = db.query(CheckinSession).filter(CheckinSession.id == session_id).first()
    if not session:
        raise HTTPException(404, "签到会话不存在")
    
    # 权限检查：教师只能看自己课堂的，学生只能看自己参与的课堂
    if current_user.role == "teacher":
        if session.teacher_id != current_user.id and current_user.role != "admin":
            raise HTTPException(403, "无权查看此签到记录")
    elif current_user.role == "student":
        student = db.query(Student).filter(Student.person_id == current_user.id).first()
        if not student or student.classroom_id != session.classroom_id:
            raise HTTPException(403, "无权查看此签到记录")
    
    attendances = db.query(Attendance).filter(Attendance.checkin_session_id == session_id).all()
    result = []
    for att in attendances:
        student_name = att.student.person.name if att.student and att.student.person else f"学生{att.student_id}"
        result.append(AttendanceOut(
            id=att.id,
            student_id=att.student_id,
            student_name=student_name,
            status=att.status,
            checkin_time=att.checkin_time,
            note=att.note,
        ))
    return result


@router.get("/sessions/{session_id}/export")
def export_attendance(
    session_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """导出签到记录为 CSV"""
    session = db.query(CheckinSession).filter(CheckinSession.id == session_id).first()
    if not session:
        raise HTTPException(404, "签到会话不存在")

    if session.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权导出")

    attendances = db.query(Attendance).filter(Attendance.checkin_session_id == session_id).all()

    output = io.StringIO()
    output.write('\ufeff')  # BOM 头，防止中文乱码
    writer = csv.writer(output)
    writer.writerow(["学生ID", "姓名", "状态", "签到时间", "备注"])
    for att in attendances:
        student_name = att.student.person.name if att.student and att.student.person else f"学生{att.student_id}"
        status_text = "已签到" if att.status == "present" else "缺勤"
        writer.writerow([
            att.student_id,
            student_name,
            status_text,
            att.checkin_time.strftime("%Y-%m-%d %H:%M:%S") if att.checkin_time else "",
            att.note or "",
        ])

    output.seek(0)
    filename = f"checkin_{session_id}.csv"
    return StreamingResponse(
        output,
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


# ===== 学生端 API =====
@router.get("/active")
def get_active_checkin(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前课堂进行中的签到"""
    # 权限检查：学生只能查自己参与的课堂
    if current_user.role == "student":
        is_member = db.query(Student).filter(
            Student.person_id == current_user.id,
            Student.classroom_id == classroom_id,
        ).first() is not None
        if not is_member:
            raise HTTPException(403, "无权查看该课堂签到")
    
    session = db.query(CheckinSession).filter(
        CheckinSession.classroom_id == classroom_id,
        CheckinSession.status == "active",
    ).first()
    
    if not session:
        return {"active": False}
    
    # 检查学生是否已签到
    student = db.query(Student).filter(
        Student.person_id == current_user.id,
        Student.classroom_id == classroom_id,
    ).first()
    if not student:
        return {"active": False, "message": "您不是该课堂的学生"}
    
    attendance = db.query(Attendance).filter(
        Attendance.checkin_session_id == session.id,
        Attendance.student_id == student.id,
    ).first()
    
    return {
        "active": True,
        "session_id": session.id,
        "type": session.type,
        "checked": attendance is not None and attendance.status == "present",
    }


@router.post("/submit")
def submit_checkin(
    data: CheckinSubmit,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生签到"""
    session = db.query(CheckinSession).filter(CheckinSession.id == data.session_id).first()
    if not session:
        raise HTTPException(404, "签到会话不存在")
    
    if session.status != "active":
        raise HTTPException(400, "签到已结束")
    
    # 获取学生信息（特定课堂的学生记录）
    student = db.query(Student).filter(
        Student.person_id == current_user.id,
        Student.classroom_id == session.classroom_id,
    ).first()
    if not student:
        raise HTTPException(403, "您不属于该课堂")
    
    # 加密签到验证
    if session.type == "encrypted":
        if not data.code or data.code != session.code:
            raise HTTPException(400, "验证码错误")
    
    # 检查是否已签到
    existing = db.query(Attendance).filter(
        Attendance.checkin_session_id == session.id,
        Attendance.student_id == student.id,
    ).first()
    
    if existing and existing.status == "present":
        raise HTTPException(400, "您已签到")
    
    if existing:
        existing.status = "present"
        existing.checkin_time = datetime.now()
        existing.checkin_code = data.code
    else:
        attendance = Attendance(
            classroom_id=session.classroom_id,
            student_id=student.id,
            checkin_session_id=session.id,
            status="present",
            checkin_time=datetime.now(),
            checkin_code=data.code,
        )
        db.add(attendance)
    
    db.commit()
    return {"success": True, "message": "签到成功"}


@router.get("/history")
def get_checkin_history(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取学生的签到历史"""
    my_student_ids = [
        s[0] for s in
        db.query(Student.id).filter(Student.person_id == current_user.id).all()
    ]
    if not my_student_ids:
        return []
    
    attendances = db.query(Attendance).filter(
        Attendance.student_id.in_(my_student_ids)
    ).order_by(Attendance.created_at.desc()).all()
    
    result = []
    for att in attendances:
        session = att.checkin_session
        classroom_name = session.classroom.name if session and session.classroom else ""
        result.append({
            "id": att.id,
            "classroom_name": classroom_name,
            "status": att.status,
            "checkin_time": att.checkin_time,
        })
    return result