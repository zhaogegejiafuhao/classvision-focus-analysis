"""消息通知 API"""
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import Notification, RegisteredPerson

router = APIRouter(prefix="/api/notifications", tags=["notifications"])


# ===== Pydantic 模型 =====
class NotificationCreate(BaseModel):
    title: str
    content: str
    type: str = "system"  # system/homework/exam/attendance
    receiver_id: Optional[int] = None  # NULL 表示全体
    classroom_id: Optional[int] = None


class NotificationOut(BaseModel):
    id: int
    title: str
    content: str
    type: str
    sender_id: Optional[int]
    sender_name: Optional[str]
    receiver_id: Optional[int]
    classroom_id: Optional[int]
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ===== API 端点 =====
@router.get("", response_model=list[NotificationOut])
def list_notifications(
    unread_only: bool = False,
    limit: int = 50,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前用户的通知列表"""
    query = db.query(Notification).filter(
        (Notification.receiver_id == current_user.id) | (Notification.receiver_id.is_(None))
    )
    if unread_only:
        query = query.filter(Notification.is_read == False)
    query = query.order_by(Notification.created_at.desc()).limit(limit)
    
    notifications = query.all()
    result = []
    for n in notifications:
        sender_name = n.sender.name if n.sender else None
        result.append(NotificationOut(
            id=n.id,
            title=n.title,
            content=n.content,
            type=n.type,
            sender_id=n.sender_id,
            sender_name=sender_name,
            receiver_id=n.receiver_id,
            classroom_id=n.classroom_id,
            is_read=n.is_read,
            created_at=n.created_at,
        ))
    return result


@router.get("/unread-count")
def get_unread_count(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取未读通知数量"""
    count = db.query(Notification).filter(
        (Notification.receiver_id == current_user.id) | (Notification.receiver_id.is_(None)),
        Notification.is_read == False,
    ).count()
    return {"unread_count": count}


@router.post("", response_model=NotificationOut)
def create_notification(
    data: NotificationCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建通知（教师/管理员）"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师和管理员可以发送通知")
    
    notification = Notification(
        title=data.title,
        content=data.content,
        type=data.type,
        sender_id=current_user.id,
        receiver_id=data.receiver_id,
        classroom_id=data.classroom_id,
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)
    
    sender_name = current_user.name
    return NotificationOut(
        id=notification.id,
        title=notification.title,
        content=notification.content,
        type=notification.type,
        sender_id=notification.sender_id,
        sender_name=sender_name,
        receiver_id=notification.receiver_id,
        classroom_id=notification.classroom_id,
        is_read=notification.is_read,
        created_at=notification.created_at,
    )


@router.post("/{notification_id}/read")
def mark_as_read(
    notification_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """标记通知为已读"""
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(404, "通知不存在")
    
    # 验证接收者：receiver_id=NULL（全体通知）任何人可标记，其余仅接收者本人
    if notification.receiver_id is not None and notification.receiver_id != current_user.id:
        raise HTTPException(403, "无权操作此通知")
    
    notification.is_read = True
    db.commit()
    return {"success": True}


@router.post("/read-all")
def mark_all_as_read(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """标记所有通知为已读"""
    db.query(Notification).filter(
        (Notification.receiver_id == current_user.id) | (Notification.receiver_id.is_(None)),
        Notification.is_read == False,
    ).update({"is_read": True})
    db.commit()
    return {"success": True}


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除通知"""
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(404, "通知不存在")
    
    # 验证权限：receiver_id=NULL（全体通知）仅管理员/发送者可删，其余仅接收者本人
    if notification.receiver_id is None:
        if current_user.role not in ("admin",) and notification.sender_id != current_user.id:
            raise HTTPException(403, "无权删除此全体通知")
    elif notification.receiver_id != current_user.id:
        raise HTTPException(403, "无权操作此通知")
    
    db.delete(notification)
    db.commit()
    return {"success": True}