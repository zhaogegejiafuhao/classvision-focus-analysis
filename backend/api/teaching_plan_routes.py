"""教学计划/备课 API"""
import json
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import TeachingPlan, RegisteredPerson, Classroom, ClassroomMember

router = APIRouter(prefix="/api/teaching-plans", tags=["teaching-plans"])


def _safe_json_loads(text: str | None):
    """安全解析 JSON 字符串，避免脏数据导致 500"""
    if not text:
        return None
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None


class PlanCreate(BaseModel):
    title: str
    classroom_id: Optional[int] = None
    objectives: Optional[str] = None
    chapters: Optional[list] = None
    schedule: Optional[list] = None
    notes: Optional[str] = None


class PlanUpdate(BaseModel):
    title: Optional[str] = None
    objectives: Optional[str] = None
    chapters: Optional[list] = None
    schedule: Optional[list] = None
    notes: Optional[str] = None
    status: Optional[str] = None


@router.get("")
def list_plans(
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取教学计划列表"""
    query = db.query(TeachingPlan)
    if current_user.role == "teacher":
        query = query.filter(TeachingPlan.teacher_id == current_user.id)
    elif current_user.role == "student":
        # 学生只能看到自己所在课堂的教学计划
        my_classroom_ids = {
            m.classroom_id for m in
            db.query(ClassroomMember).filter(ClassroomMember.person_id == current_user.id).all()
        }
        if my_classroom_ids:
            query = query.filter(TeachingPlan.classroom_id.in_(my_classroom_ids))
        else:
            query = query.filter(TeachingPlan.teacher_id == -1)  # 无课堂，返回空
    if classroom_id:
        # 校验用户是否有权访问该课堂
        if current_user.role == "student":
            my_classroom_ids = {
                m.classroom_id for m in
                db.query(ClassroomMember).filter(ClassroomMember.person_id == current_user.id).all()
            }
            if classroom_id not in my_classroom_ids:
                raise HTTPException(403, "无权访问该课堂的教学计划")
        elif current_user.role == "teacher":
            cr = db.query(Classroom).filter(Classroom.id == classroom_id, Classroom.teacher_person_id == current_user.id).first()
            if not cr:
                raise HTTPException(403, "无权访问该课堂的教学计划")
        # admin 可以访问任何课堂的教学计划
        query = query.filter(TeachingPlan.classroom_id == classroom_id)
    query = query.order_by(TeachingPlan.updated_at.desc())

    result = []
    for p in query.all():
        result.append({
            "id": p.id,
            "title": p.title,
            "classroom_id": p.classroom_id,
            "objectives": p.objectives,
            "chapters": _safe_json_loads(p.chapters),
            "schedule": _safe_json_loads(p.schedule),
            "notes": p.notes,
            "status": p.status,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "updated_at": p.updated_at.isoformat() if p.updated_at else None,
        })
    return result


@router.post("")
def create_plan(
    data: PlanCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建教学计划"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建教学计划")

    plan = TeachingPlan(
        teacher_id=current_user.id,
        classroom_id=data.classroom_id,
        title=data.title,
        objectives=data.objectives,
        chapters=json.dumps(data.chapters) if data.chapters else None,
        schedule=json.dumps(data.schedule) if data.schedule else None,
        notes=data.notes,
    )
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return {"id": plan.id, "title": plan.title}


@router.put("/{plan_id}")
def update_plan(
    plan_id: int,
    data: PlanUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """更新教学计划"""
    plan = db.query(TeachingPlan).filter(TeachingPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(404, "计划不存在")
    if plan.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权修改")

    if data.title is not None:
        plan.title = data.title
    if data.objectives is not None:
        plan.objectives = data.objectives
    if data.chapters is not None:
        plan.chapters = json.dumps(data.chapters)
    if data.schedule is not None:
        plan.schedule = json.dumps(data.schedule)
    if data.notes is not None:
        plan.notes = data.notes
    if data.status is not None:
        plan.status = data.status

    db.commit()
    return {"success": True}


@router.delete("/{plan_id}")
def delete_plan(
    plan_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除教学计划"""
    plan = db.query(TeachingPlan).filter(TeachingPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(404, "计划不存在")
    if plan.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除")
    db.delete(plan)
    db.commit()
    return {"success": True}
