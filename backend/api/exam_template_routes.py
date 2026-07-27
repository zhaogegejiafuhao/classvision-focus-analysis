"""试卷模板管理路由（从 exam_compose_routes.py 拆分）

提供试卷模板的 CRUD 接口：
- GET    /api/exam-templates           获取模板列表（内置 + 自己创建的）
- POST   /api/exam-templates           创建自定义模板
- DELETE /api/exam-templates/{id}      删除自定义模板（内置不可删）
"""
import json

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import ExamTemplate, RegisteredPerson

router = APIRouter(prefix="/api/exam-templates", tags=["exam-templates"])


class ExamTemplateCreate(BaseModel):
    name: str
    description: str = ""
    total_score: float = 100.0
    duration: int = 90
    # [{"type":"single","count":10,"score_per":5,"knowledge":["极限"],"difficulty":2}, ...]
    structure: list[dict]


class ExamTemplateOut(BaseModel):
    id: int
    name: str
    description: str | None
    total_score: float
    duration: int
    structure: list[dict]
    is_builtin: bool
    created_by: int | None

    class Config:
        from_attributes = True


@router.get("", response_model=list[ExamTemplateOut])
def list_templates(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取试卷模板列表（内置 + 自己创建的）"""
    query = db.query(ExamTemplate)
    # 内置模板所有人可见，自定义模板只有创建者可见
    if current_user.role != "admin":
        query = query.filter(
            (ExamTemplate.is_builtin == True) | (ExamTemplate.created_by == current_user.id)
        )
    templates = query.order_by(ExamTemplate.is_builtin.desc(), ExamTemplate.created_at.desc()).all()
    result = []
    for t in templates:
        result.append(ExamTemplateOut(
            id=t.id, name=t.name, description=t.description,
            total_score=t.total_score, duration=t.duration,
            structure=json.loads(t.structure) if t.structure else [],
            is_builtin=t.is_builtin, created_by=t.created_by,
        ))
    return result


@router.post("", response_model=ExamTemplateOut)
def create_template(
    data: ExamTemplateCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建自定义试卷模板"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建模板")

    t = ExamTemplate(
        name=data.name,
        description=data.description,
        total_score=data.total_score,
        duration=data.duration,
        structure=json.dumps(data.structure, ensure_ascii=False),
        is_builtin=False,
        created_by=current_user.id,
    )
    db.add(t)
    db.commit()
    db.refresh(t)

    return ExamTemplateOut(
        id=t.id, name=t.name, description=t.description,
        total_score=t.total_score, duration=t.duration,
        structure=data.structure,
        is_builtin=t.is_builtin, created_by=t.created_by,
    )


@router.delete("/{template_id}")
def delete_template(
    template_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除自定义模板（内置模板不可删除）"""
    t = db.query(ExamTemplate).filter(ExamTemplate.id == template_id).first()
    if not t:
        raise HTTPException(404, "模板不存在")
    if t.is_builtin:
        raise HTTPException(400, "内置模板不可删除")
    if t.created_by != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除")
    db.delete(t)
    db.commit()
    return {"success": True}
