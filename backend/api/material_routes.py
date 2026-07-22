"""课件管理 API"""
import os
import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import CourseMaterial, RegisteredPerson, Classroom, Student

router = APIRouter(prefix="/api/materials", tags=["materials"])

UPLOAD_DIR = "uploads/materials"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".pptx", ".ppt", ".docx", ".doc", ".mp4", ".mp3", ".png", ".jpg", ".jpeg", ".txt", ".md"}
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB


@router.get("")
def list_materials(
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取课件列表"""
    query = db.query(CourseMaterial)
    if current_user.role == "teacher":
        query = query.filter(CourseMaterial.teacher_id == current_user.id)
    elif current_user.role == "student":
        # 学生只能看到自己所在课堂的课件
        my_classroom_ids = [
            s.classroom_id for s in
            db.query(Student.classroom_id).filter(Student.person_id == current_user.id).all()
            if s.classroom_id
        ]
        if classroom_id:
            if classroom_id not in my_classroom_ids:
                raise HTTPException(403, "无权访问该课堂的课件")
            query = query.filter(CourseMaterial.classroom_id == classroom_id)
        else:
            query = query.filter(CourseMaterial.classroom_id.in_(my_classroom_ids))
    if classroom_id and current_user.role != "student":
        query = query.filter(CourseMaterial.classroom_id == classroom_id)
    query = query.order_by(CourseMaterial.created_at.desc())

    return [
        {
            "id": m.id,
            "title": m.title,
            "description": m.description,
            "file_name": m.file_name,
            "file_size": m.file_size,
            "file_type": m.file_type,
            "classroom_id": m.classroom_id,
            "created_at": m.created_at.isoformat() if m.created_at else None,
        }
        for m in query.all()
    ]


@router.post("/upload")
async def upload_material(
    title: str = Form(...),
    classroom_id: Optional[int] = None,
    description: Optional[str] = None,
    file: UploadFile = File(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """上传课件"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以上传课件")

    # 检查文件扩展名
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, f"不支持的文件类型: {ext}")

    # 保存文件
    file_id = str(uuid.uuid4())
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(400, "文件过大，最大100MB")

    with open(save_path, "wb") as f:
        f.write(content)

    material = CourseMaterial(
        teacher_id=current_user.id,
        classroom_id=classroom_id,
        title=title,
        description=description,
        file_path=save_path,
        file_name=file.filename,
        file_size=len(content),
        file_type=ext.lstrip("."),
    )
    db.add(material)
    db.commit()
    db.refresh(material)

    return {"id": material.id, "title": material.title, "file_name": material.file_name}


@router.get("/{material_id}/download")
def download_material(
    material_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """下载课件"""
    material = db.query(CourseMaterial).filter(CourseMaterial.id == material_id).first()
    if not material:
        raise HTTPException(404, "课件不存在")

    # 校验课堂访问权限
    if material.classroom_id:
        classroom = db.query(Classroom).filter(Classroom.id == material.classroom_id).first()
        if classroom:
            if current_user.role == "student":
                is_member = db.query(Student).filter(
                    Student.classroom_id == material.classroom_id,
                    Student.person_id == current_user.id,
                ).first() is not None
                if not is_member:
                    raise HTTPException(403, "无权下载该课件")
            elif current_user.role == "teacher" and classroom.teacher_person_id != current_user.id:
                raise HTTPException(403, "无权下载该课件")

    if not os.path.exists(material.file_path):
        raise HTTPException(404, "文件不存在")

    return FileResponse(
        material.file_path,
        filename=material.file_name,
        media_type="application/octet-stream",
    )


@router.delete("/{material_id}")
def delete_material(
    material_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除课件"""
    material = db.query(CourseMaterial).filter(CourseMaterial.id == material_id).first()
    if not material:
        raise HTTPException(404, "课件不存在")
    if material.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除")

    # 删除文件
    if os.path.exists(material.file_path):
        os.remove(material.file_path)

    db.delete(material)
    db.commit()
    return {"success": True}
