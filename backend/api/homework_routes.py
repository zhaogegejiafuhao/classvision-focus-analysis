"""作业系统 API —— 作业 CRUD 与教师附件（从原 homework_routes.py 拆分）

拆分后的模块：
- homework_routes.py：作业增删改查 + 教师附件上传/下载
- homework_submission_routes.py：学生提交、教师批改、打回、学生附件
- homework_extension_routes.py：延期申请提交与审批
"""
import os
import uuid
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Homework, HomeworkAttachment, HomeworkSubmission, SubmissionAttachment,
    RegisteredPerson, Classroom, Student, Notification, ExtensionRequest, GradingResult,
)
from backend.api.homework_schemas import (
    HomeworkCreate, HomeworkUpdate, HomeworkOut,
)

router = APIRouter(prefix="/api/homework", tags=["homework"])

UPLOAD_DIR = "uploads/homework"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ===== 教师端 API =====
@router.get("", response_model=list[HomeworkOut])
def list_homework(
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取作业列表（教师创建的）"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以查看作业列表")

    query = db.query(Homework).options(
        joinedload(Homework.classroom),
        joinedload(Homework.submissions),
    )
    if current_user.role == "teacher":
        query = query.filter(Homework.teacher_id == current_user.id)
    # admin 可以看到所有作业
    if classroom_id:
        query = query.filter(Homework.classroom_id == classroom_id)
    query = query.order_by(Homework.created_at.desc())

    result = []
    for hw in query.all():
        classroom_name = hw.classroom.name if hw.classroom else None
        submission_count = len(hw.submissions)
        result.append(HomeworkOut(
            id=hw.id,
            title=hw.title,
            description=hw.description,
            classroom_id=hw.classroom_id,
            classroom_name=classroom_name,
            teacher_id=hw.teacher_id,
            teacher_name=current_user.name,
            deadline=hw.deadline,
            total_score=hw.total_score,
            status=hw.status,
            created_at=hw.created_at,
            submission_count=submission_count,
        ))
    return result


@router.post("", response_model=HomeworkOut)
def create_homework(
    data: HomeworkCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建作业"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建作业")

    homework = Homework(
        title=data.title,
        description=data.description,
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        deadline=data.deadline,
        total_score=data.total_score,
    )
    db.add(homework)
    db.commit()
    db.refresh(homework)

    # 发送通知给学生
    if data.classroom_id:
        classroom = db.query(Classroom).filter(Classroom.id == data.classroom_id).first()
        if classroom:
            students = db.query(Student).filter(Student.classroom_id == data.classroom_id).all()
            for student in students:
                if student.person:
                    notification = Notification(
                        title=f"新作业：{data.title}",
                        content=f"您有一个新作业需要完成，截止时间：{data.deadline.strftime('%Y-%m-%d %H:%M') if data.deadline else '无截止时间'}",
                        type="homework",
                        sender_id=current_user.id,
                        receiver_id=student.person_id,
                        classroom_id=data.classroom_id,
                    )
                    db.add(notification)
            db.commit()

    classroom_name = homework.classroom.name if homework.classroom else None
    return HomeworkOut(
        id=homework.id,
        title=homework.title,
        description=homework.description,
        classroom_id=homework.classroom_id,
        classroom_name=classroom_name,
        teacher_id=homework.teacher_id,
        teacher_name=current_user.name,
        deadline=homework.deadline,
        total_score=homework.total_score,
        status=homework.status,
        created_at=homework.created_at,
        submission_count=0,
    )


# ===== 学生端路由（必须在 /{homework_id} 之前定义，避免路径冲突）=====
@router.get("/assigned", response_model=list[HomeworkOut])
def list_assigned_homework(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取分配给学生的作业"""
    if current_user.role == "student":
        my_classroom_ids = [
            s.classroom_id for s in
            db.query(Student.classroom_id).filter(Student.person_id == current_user.id).all()
            if s.classroom_id
        ]
        if not my_classroom_ids:
            return []
    else:
        my_classroom_ids = None

    query = db.query(Homework).options(
        joinedload(Homework.classroom),
        joinedload(Homework.submissions),
    ).filter(Homework.status == "open")
    if my_classroom_ids:
        query = query.filter(or_(Homework.classroom_id.in_(my_classroom_ids), Homework.classroom_id.is_(None)))

    query = query.order_by(Homework.deadline.asc().nullslast(), Homework.created_at.desc())

    result = []
    for hw in query.all():
        classroom_name = hw.classroom.name if hw.classroom else None
        submission_count = len(hw.submissions)
        result.append(HomeworkOut(
            id=hw.id, title=hw.title, description=hw.description,
            classroom_id=hw.classroom_id, classroom_name=classroom_name,
            teacher_id=hw.teacher_id, teacher_name=hw.teacher.name,
            deadline=hw.deadline, total_score=hw.total_score,
            status=hw.status, created_at=hw.created_at, submission_count=submission_count,
        ))
    return result


@router.get("/{homework_id}", response_model=HomeworkOut)
def get_homework(
    homework_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取作业详情"""
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")

    classroom_name = homework.classroom.name if homework.classroom else None
    submission_count = len(homework.submissions)
    return HomeworkOut(
        id=homework.id,
        title=homework.title,
        description=homework.description,
        classroom_id=homework.classroom_id,
        classroom_name=classroom_name,
        teacher_id=homework.teacher_id,
        teacher_name=homework.teacher.name,
        deadline=homework.deadline,
        total_score=homework.total_score,
        status=homework.status,
        created_at=homework.created_at,
        submission_count=submission_count,
    )


@router.put("/{homework_id}", response_model=HomeworkOut)
def update_homework(
    homework_id: int,
    data: HomeworkUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """更新作业"""
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")
    if homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权修改此作业")

    if data.title is not None:
        homework.title = data.title
    if data.description is not None:
        homework.description = data.description
    if data.deadline is not None:
        homework.deadline = data.deadline
    if data.total_score is not None:
        homework.total_score = data.total_score
    if data.status is not None:
        homework.status = data.status

    db.commit()
    db.refresh(homework)

    classroom_name = homework.classroom.name if homework.classroom else None
    submission_count = len(homework.submissions)
    return HomeworkOut(
        id=homework.id,
        title=homework.title,
        description=homework.description,
        classroom_id=homework.classroom_id,
        classroom_name=classroom_name,
        teacher_id=homework.teacher_id,
        teacher_name=homework.teacher.name,
        deadline=homework.deadline,
        total_score=homework.total_score,
        status=homework.status,
        created_at=homework.created_at,
        submission_count=submission_count,
    )


@router.delete("/{homework_id}")
def delete_homework(
    homework_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除作业"""
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")
    if homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除此作业")

    # 级联清理：先删子表数据
    for sub in homework.submissions:
        db.query(GradingResult).filter(GradingResult.submission_id == sub.id).delete()
        db.query(SubmissionAttachment).filter(SubmissionAttachment.submission_id == sub.id).delete()
    db.query(HomeworkSubmission).filter(HomeworkSubmission.homework_id == homework_id).delete()
    db.query(HomeworkAttachment).filter(HomeworkAttachment.homework_id == homework_id).delete()
    db.query(ExtensionRequest).filter(ExtensionRequest.homework_id == homework_id).delete()
    db.delete(homework)
    db.commit()
    return {"success": True}


# ===== 教师附件 API =====
@router.post("/{homework_id}/attachments")
async def upload_homework_attachment(
    homework_id: int,
    file: UploadFile = File(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """上传作业附件（教师）"""
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")
    if homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权上传附件")

    # 文件大小限制 (50MB)
    content = await file.read()
    if len(content) > 50 * 1024 * 1024:
        raise HTTPException(400, "文件过大，最大50MB")

    file_id = str(uuid.uuid4())
    safe_ext = os.path.splitext(os.path.basename(file.filename or "unnamed"))[1]
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}{safe_ext}")
    with open(save_path, "wb") as f:
        f.write(content)

    attachment = HomeworkAttachment(
        homework_id=homework_id,
        file_path=save_path,
        filename=file.filename,
        file_size=len(content),
    )
    db.add(attachment)
    db.commit()
    db.refresh(attachment)

    return {"id": attachment.id, "filename": attachment.filename, "file_size": attachment.file_size}


@router.get("/attachments/{attachment_id}/download")
def download_homework_attachment(
    attachment_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """下载作业附件"""
    attachment = db.query(HomeworkAttachment).filter(HomeworkAttachment.id == attachment_id).first()
    if not attachment:
        raise HTTPException(404, "附件不存在")
    if not os.path.exists(attachment.file_path):
        raise HTTPException(404, "文件不存在")
    return FileResponse(attachment.file_path, filename=attachment.filename)
