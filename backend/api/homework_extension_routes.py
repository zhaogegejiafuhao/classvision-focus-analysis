"""作业延期申请路由（从 homework_routes.py 拆分）

涵盖：
- 学生提交延期申请
- 教师/学生查看延期申请列表
- 教师审批延期申请（通过后自动延长作业截止时间）
"""
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Homework, ExtensionRequest, RegisteredPerson, Notification,
)
from backend.api.homework_schemas import (
    ExtensionRequestCreate, ExtensionRequestOut, ExtensionReview,
)

router = APIRouter(prefix="/api/homework", tags=["homework"])


@router.get("/extensions", response_model=list[ExtensionRequestOut])
def list_extension_requests(
    status: Optional[str] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取延期申请列表"""
    query = db.query(ExtensionRequest)
    if current_user.role == "teacher":
        teacher_homework_ids = db.query(Homework.id).filter(Homework.teacher_id == current_user.id).all()
        hw_ids = [h[0] for h in teacher_homework_ids]
        query = query.filter(ExtensionRequest.homework_id.in_(hw_ids))
    elif current_user.role == "student":
        query = query.filter(ExtensionRequest.student_id == current_user.id)
    # admin 可以看到所有延期申请
    if status:
        query = query.filter(ExtensionRequest.status == status)
    query = query.order_by(ExtensionRequest.created_at.desc())

    result = []
    for ext in query.all():
        result.append(ExtensionRequestOut(
            id=ext.id,
            homework_id=ext.homework_id,
            homework_title=ext.homework.title,
            student_id=ext.student_id,
            student_name=ext.student.name,
            reason=ext.reason,
            original_deadline=ext.original_deadline,
            requested_deadline=ext.requested_deadline,
            status=ext.status,
            teacher_feedback=ext.teacher_feedback,
            created_at=ext.created_at,
            reviewed_at=ext.reviewed_at,
        ))
    return result


@router.post("/extensions", response_model=ExtensionRequestOut)
def create_extension_request(
    data: ExtensionRequestCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生提交延期申请"""
    homework = db.query(Homework).filter(Homework.id == data.homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")

    ext = ExtensionRequest(
        homework_id=data.homework_id,
        student_id=current_user.id,
        reason=data.reason,
        original_deadline=homework.deadline,
        requested_deadline=data.requested_deadline,
    )
    db.add(ext)
    db.commit()
    db.refresh(ext)

    return ExtensionRequestOut(
        id=ext.id,
        homework_id=ext.homework_id,
        homework_title=ext.homework.title,
        student_id=ext.student_id,
        student_name=ext.student.name,
        reason=ext.reason,
        original_deadline=ext.original_deadline,
        requested_deadline=ext.requested_deadline,
        status=ext.status,
        teacher_feedback=ext.teacher_feedback,
        created_at=ext.created_at,
        reviewed_at=ext.reviewed_at,
    )


@router.post("/extensions/{ext_id}/review")
def review_extension_request(
    ext_id: int,
    data: ExtensionReview,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师审批延期申请"""
    ext = db.query(ExtensionRequest).filter(ExtensionRequest.id == ext_id).first()
    if not ext:
        raise HTTPException(404, "延期申请不存在")

    if ext.homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权审批")

    ext.status = data.status
    ext.teacher_feedback = data.feedback
    ext.reviewed_at = datetime.now()

    if data.status == "approved":
        ext.homework.deadline = ext.requested_deadline

    notification = Notification(
        title=f"延期申请{'已通过' if data.status == 'approved' else '已拒绝'}：{ext.homework.title}",
        content=data.feedback or ("延期申请已通过" if data.status == "approved" else "延期申请已拒绝"),
        type="homework",
        sender_id=current_user.id,
        receiver_id=ext.student_id,
    )
    db.add(notification)
    db.commit()
    return {"success": True}
