"""作业提交与批改路由（从 homework_routes.py 拆分）

涵盖：
- 学生提交作业（含重复提交覆盖）
- 教师查看提交列表、批改、打回
- 学生查看自己的提交
- 学生上传提交附件
"""
import os
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session, joinedload

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Homework, HomeworkSubmission, SubmissionAttachment,
    RegisteredPerson, Notification, GradingResult,
)
from backend.api.homework_schemas import (
    SubmissionCreate, SubmissionGrade, SubmissionOut,
)

router = APIRouter(prefix="/api/homework", tags=["homework"])

UPLOAD_DIR = "uploads/homework"


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


# ===== 学生提交附件 =====
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

    # 文件大小限制 (50MB)
    content = await file.read()
    if len(content) > 50 * 1024 * 1024:
        raise HTTPException(400, "文件过大，最大50MB")

    file_id = str(uuid.uuid4())
    safe_ext = os.path.splitext(os.path.basename(file.filename or "unnamed"))[1]
    save_path = os.path.join(UPLOAD_DIR, f"{file_id}{safe_ext}")
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
