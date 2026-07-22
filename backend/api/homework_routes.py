"""作业系统 API"""
import os
import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Homework, HomeworkAttachment, HomeworkSubmission, SubmissionAttachment,
    RegisteredPerson, Classroom, Student, Notification, ExtensionRequest, GradingResult
)

router = APIRouter(prefix="/api/homework", tags=["homework"])

UPLOAD_DIR = "uploads/homework"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ===== Pydantic 模型 =====
class HomeworkCreate(BaseModel):
    title: str
    description: str = ""
    classroom_id: Optional[int] = None
    deadline: Optional[datetime] = None
    total_score: float = 100.0


class HomeworkUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    total_score: Optional[float] = None
    status: Optional[str] = None


class HomeworkOut(BaseModel):
    id: int
    title: str
    description: str
    classroom_id: Optional[int]
    classroom_name: Optional[str]
    teacher_id: int
    teacher_name: str
    deadline: Optional[datetime]
    total_score: float
    status: str
    created_at: datetime
    submission_count: int = 0

    class Config:
        from_attributes = True


class SubmissionCreate(BaseModel):
    content: str = ""


class SubmissionGrade(BaseModel):
    score: float
    feedback: str = ""


class SubmissionOut(BaseModel):
    id: int
    homework_id: int
    student_id: int
    student_name: str
    content: str
    score: Optional[float]
    feedback: str
    status: str
    submitted_at: datetime
    graded_at: Optional[datetime]

    class Config:
        from_attributes = True


# ===== 延期申请模型 =====
class ExtensionRequestCreate(BaseModel):
    homework_id: int
    reason: str
    requested_deadline: datetime


class ExtensionRequestOut(BaseModel):
    id: int
    homework_id: int
    homework_title: str
    student_id: int
    student_name: str
    reason: str
    original_deadline: Optional[datetime]
    requested_deadline: datetime
    status: str
    teacher_feedback: Optional[str]
    created_at: datetime
    reviewed_at: Optional[datetime]

    class Config:
        from_attributes = True


class ExtensionReview(BaseModel):
    status: str  # approved/rejected
    feedback: str = ""


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
    ).filter(Homework.teacher_id == current_user.id)
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


# ===== 延期申请路由（必须在 /{homework_id} 之前）=====
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


@router.get("/{homework_id}/submissions", response_model=list[SubmissionOut])
def list_submissions(
    homework_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取作业的所有提交"""
    homework = db.query(Homework).options(
        joinedload(Homework.submissions).joinedload(HomeworkSubmission.student),
    ).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")
    
    if homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权查看提交")
    
    result = []
    for sub in homework.submissions:
        result.append(SubmissionOut(
            id=sub.id,
            homework_id=sub.homework_id,
            student_id=sub.student_id,
            student_name=sub.student.name,
            content=sub.content,
            score=sub.score,
            feedback=sub.feedback,
            status=sub.status,
            submitted_at=sub.submitted_at,
            graded_at=sub.graded_at,
        ))
    return result


@router.post("/submissions/{submission_id}/grade")
def grade_submission(
    submission_id: int,
    data: SubmissionGrade,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """批改作业"""
    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, "提交不存在")
    
    if submission.homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权批改")
    
    submission.score = data.score
    submission.feedback = data.feedback
    submission.status = "graded"
    submission.graded_at = datetime.now()

    # 同步创建 GradingResult 记录，使手动批改的作业也能进入错题本和知识归因
    grading_record = GradingResult(
        submission_id=submission_id,
        score=data.score,
        max_score=submission.homework.total_score,
        comment=data.feedback,
        model_key="manual",
        grading_method="manual",
        confirmed=True,
        confirmed_score=data.score,
    )
    db.add(grading_record)
    
    # 发送通知给学生
    notification = Notification(
        title=f"作业已批改：{submission.homework.title}",
        content=f"您的作业已批改，得分：{data.score}/{submission.homework.total_score}",
        type="homework",
        sender_id=current_user.id,
        receiver_id=submission.student_id,
    )
    db.add(notification)
    
    db.commit()
    return {"success": True}


# ===== 学生端 API =====
@router.post("/{homework_id}/submit", response_model=SubmissionOut)
def submit_homework(
    homework_id: int,
    data: SubmissionCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """提交作业"""
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")
    
    # 检查截止时间
    if homework.deadline and datetime.now() > homework.deadline:
        raise HTTPException(400, "作业已截止提交")
    
    # 检查是否已提交
    existing = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.homework_id == homework_id,
        HomeworkSubmission.student_id == current_user.id,
    ).first()
    
    if existing:
        # 更新提交
        existing.content = data.content
        existing.submitted_at = datetime.now()
        db.commit()
        db.refresh(existing)
        submission = existing
    else:
        # 新提交
        submission = HomeworkSubmission(
            homework_id=homework_id,
            student_id=current_user.id,
            content=data.content,
        )
        db.add(submission)
        db.commit()
        db.refresh(submission)
    
    return SubmissionOut(
        id=submission.id,
        homework_id=submission.homework_id,
        student_id=submission.student_id,
        student_name=current_user.name,
        content=submission.content,
        score=submission.score,
        feedback=submission.feedback,
        status=submission.status,
        submitted_at=submission.submitted_at,
        graded_at=submission.graded_at,
    )


@router.get("/submissions/{submission_id}", response_model=SubmissionOut)
def get_submission(
    submission_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取提交详情"""
    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, "提交不存在")
    
    # 权限检查
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权查看此提交")
    
    return SubmissionOut(
        id=submission.id,
        homework_id=submission.homework_id,
        student_id=submission.student_id,
        student_name=submission.student.name,
        content=submission.content,
        score=submission.score,
        feedback=submission.feedback,
        status=submission.status,
        submitted_at=submission.submitted_at,
        graded_at=submission.graded_at,
    )


@router.get("/my-submissions/{homework_id}")
def get_my_submission(
    homework_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前用户对指定作业的提交"""
    submission = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.homework_id == homework_id,
        HomeworkSubmission.student_id == current_user.id,
    ).first()
    
    if not submission:
        return {"submitted": False}
    
    return {
        "submitted": True,
        "submission": SubmissionOut(
            id=submission.id,
            homework_id=submission.homework_id,
            student_id=submission.student_id,
            student_name=current_user.name,
            content=submission.content,
            score=submission.score,
            feedback=submission.feedback,
            status=submission.status,
            submitted_at=submission.submitted_at,
            graded_at=submission.graded_at,
        )
    }


# ===== 附件 API =====
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

    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")
    content = await file.read()
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


@router.post("/submissions/{submission_id}/attachments")
async def upload_submission_attachment(
    submission_id: int,
    file: UploadFile = File(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生上传提交附件"""
    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, "提交不存在")
    if submission.student_id != current_user.id:
        raise HTTPException(403, "无权上传")

    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")
    content = await file.read()
    with open(save_path, "wb") as f:
        f.write(content)

    attachment = SubmissionAttachment(
        submission_id=submission_id,
        file_path=save_path,
        filename=file.filename,
        file_size=len(content),
    )
    db.add(attachment)
    db.commit()
    db.refresh(attachment)

    return {"id": attachment.id, "filename": attachment.filename, "file_size": attachment.file_size}


# ===== 作业打回重做 =====
@router.post("/submissions/{submission_id}/return")
def return_submission(
    submission_id: int,
    data: dict = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师打回作业让学生重做"""
    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    if submission.homework.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权打回")

    feedback = (data or {}).get("feedback", "请重做")
    submission.status = "returned"
    submission.feedback = feedback
    submission.graded_at = datetime.now()
    db.commit()

    notification = Notification(
        title=f"作业被打回：{submission.homework.title}",
        content=f"教师打回了您的作业，请根据反馈重做。反馈：{feedback}",
        type="homework",
        sender_id=current_user.id,
        receiver_id=submission.student_id,
    )
    db.add(notification)
    db.commit()

    return {"success": True}


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