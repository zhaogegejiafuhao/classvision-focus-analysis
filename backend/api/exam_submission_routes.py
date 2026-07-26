"""考试学生提交与教师批改路由（从 exam_routes.py 拆分）

涵盖：
- 学生上传答案图片
- 学生开始/提交考试（含主观题自动触发 AI 批改）
- 学生查看自己的考试结果
- 教师查看提交详情、批改简答题
"""
import json
import os
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session, joinedload

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Answer, Exam, ExamSubmission, Question, RegisteredPerson,
)
from backend.api.exam_schemas import AnswerGrade, AnswerSubmit, SubmissionOut
from backend.services.exam_service import auto_grade

router = APIRouter(prefix="/api/exams", tags=["exams"])

# 答案图片上传目录
ANSWER_UPLOAD_DIR = "uploads/exam_answers"


# ===== 学生端：答案图片上传 =====
@router.post("/answers/upload-image")
async def upload_answer_image(
    file: UploadFile = File(...),
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生上传答案图片（机试填空/简答的图片答案，或笔试的照片答案）"""
    if current_user.role != "student":
        raise HTTPException(403, "仅学生可上传答案图片")

    # 文件类型与大小校验
    ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".webp"}
    ext = os.path.splitext(file.filename or "unnamed")[1].lower()
    if ext not in ALLOWED_EXT:
        raise HTTPException(400, f"不支持的图片类型: {ext}，仅支持 jpg/png/webp")

    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(400, "图片过大，最大10MB")

    # 保存文件
    os.makedirs(ANSWER_UPLOAD_DIR, exist_ok=True)
    file_id = str(uuid.uuid4())
    save_path = os.path.join(ANSWER_UPLOAD_DIR, f"{file_id}{ext}")
    with open(save_path, "wb") as f:
        f.write(content)

    image_url = f"/uploads/exam_answers/{file_id}{ext}"
    return {"url": image_url, "filename": file.filename, "size": len(content)}


# ===== 学生端：开始考试 =====
@router.post("/{exam_id}/start")
def start_exam(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """开始考试"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.status != "published":
        raise HTTPException(400, "考试未发布")

    # 检查考试是否已结束
    if exam.end_time and datetime.now() > exam.end_time:
        raise HTTPException(400, "考试已结束")

    # 检查是否已开始
    existing = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.student_id == current_user.id,
    ).first()

    if existing:
        return {"submission_id": existing.id, "message": "考试已开始"}

    submission = ExamSubmission(
        exam_id=exam_id,
        student_id=current_user.id,
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)

    return {"submission_id": submission.id}


# ===== 学生端：提交考试 =====
@router.post("/{exam_id}/submit")
async def submit_exam(
    exam_id: int,
    answers: list[AnswerSubmit],
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """提交考试（含主观题时自动触发 AI 批改）"""
    submission = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.student_id == current_user.id,
    ).first()

    if not submission:
        raise HTTPException(404, "未开始考试")

    # 检查考试是否已结束
    if submission.exam.end_time and datetime.now() > submission.exam.end_time:
        # 自动将超时的提交标记为已提交
        if submission.status == "in_progress":
            submission.status = "timeout"
            submission.submitted_at = datetime.now()
            db.commit()
        raise HTTPException(400, "考试已结束，无法提交")

    if submission.status != "in_progress":
        raise HTTPException(400, "考试已提交")

    exam = submission.exam
    total_score = 0
    has_essay = False
    has_fill_with_images = False

    for ans in answers:
        question = db.query(Question).filter(Question.id == ans.question_id).first()
        if not question or question.exam_id != exam_id:
            continue

        # 自动评判（客观题）
        score, is_correct = auto_grade(question, ans.content)
        if question.type == "essay":
            has_essay = True
            score = 0
            is_correct = None
        elif question.type == "fill" and ans.image_urls:
            # 填空题带图片：作为主观题处理
            has_fill_with_images = True
            score = 0
            is_correct = None

        total_score += score

        answer = Answer(
            submission_id=submission.id,
            question_id=ans.question_id,
            content=ans.content,
            image_urls=json.dumps(ans.image_urls) if ans.image_urls else None,
            score=score,
            is_correct=is_correct,
        )
        db.add(answer)

    # 判定是否含主观题
    has_subjective = has_essay or has_fill_with_images

    if has_subjective:
        # 进入 AI 批改流程
        submission.score = None
        submission.status = "ai_grading"
        submission.submitted_at = datetime.now()
        db.commit()
        db.flush()  # 确保 answer.id 已生成

        # 标记主观题 answer 为 pending
        for ans in db.query(Answer).filter(
            Answer.submission_id == submission.id,
            Answer.is_correct.is_(None),
        ).all():
            ans.ai_status = "pending"
        db.commit()

        # 触发后台 AI 批改（fire-and-forget）
        from backend.services.exam_grader import trigger_ai_grading
        trigger_ai_grading(submission.id)

        return {
            "success": True,
            "score": None,
            "has_essay": has_essay,
            "has_subjective": True,
            "ai_grading_triggered": True,
        }
    else:
        # 纯客观题：直接 graded
        submission.score = total_score
        submission.status = "graded"
        submission.submitted_at = datetime.now()
        submission.graded_at = datetime.now()
        db.commit()

        return {
            "success": True,
            "score": total_score,
            "has_essay": False,
            "has_subjective": False,
            "ai_grading_triggered": False,
        }


# ===== 学生端：查看自己的考试结果 =====
@router.get("/my-result/{exam_id}")
def get_my_exam_result(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前学生的考试结果"""
    if current_user.role != "student":
        raise HTTPException(403, "仅学生可查看自己的考试结果")

    submission = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.student_id == current_user.id,
    ).first()

    if not submission:
        return {"submitted": False}

    result = {
        "submitted": True,
        "id": submission.id,
        "exam_id": submission.exam_id,
        "exam_title": submission.exam.title,
        "score": submission.score,
        "status": submission.status,
        "submitted_at": submission.submitted_at,
        "answers": [],
    }

    for ans in submission.answers:
        question = ans.question
        result["answers"].append({
            "question_id": ans.question_id,
            "question_content": question.content,
            "question_type": question.type,
            "options": json.loads(question.options) if question.options else None,
            "student_answer": ans.content,
            "image_urls": json.loads(ans.image_urls) if ans.image_urls else [],
            "correct_answer": question.answer if submission.status == "graded" else None,
            "score": ans.score,
            "is_correct": ans.is_correct,
        })

    return result


# ===== 教师端：批改简答题 =====
@router.post("/submissions/{submission_id}/grade-answers")
def grade_answers(
    submission_id: int,
    data: list[AnswerGrade],
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """批改简答题（教师端）"""
    submission = db.query(ExamSubmission).filter(ExamSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    if submission.exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权批改")

    total_score = 0
    for item in data:
        answer = db.query(Answer).filter(Answer.id == item.answer_id, Answer.submission_id == submission_id).first()
        if answer:
            answer.score = item.score
            answer.is_correct = item.is_correct
            total_score += item.score

    # 重新计算总分
    all_answers = db.query(Answer).filter(Answer.submission_id == submission_id).all()
    submission.score = sum(a.score or 0 for a in all_answers)
    submission.status = "graded"
    submission.graded_at = datetime.now()

    db.commit()
    return {"success": True, "total_score": submission.score}


# ===== 教师端：获取提交详情 =====
@router.get("/submissions/{submission_id}")
def get_submission(
    submission_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取提交详情"""
    submission = db.query(ExamSubmission).filter(ExamSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    # 权限检查
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权查看此提交")

    result = {
        "id": submission.id,
        "exam_id": submission.exam_id,
        "exam_title": submission.exam.title,
        "student_name": submission.student.name,
        "score": submission.score,
        "status": submission.status,
        "started_at": submission.started_at,
        "submitted_at": submission.submitted_at,
        "answers": [],
    }

    for ans in submission.answers:
        question = ans.question
        result["answers"].append({
            "answer_id": ans.id,
            "question_id": ans.question_id,
            "question_content": question.content,
            "question_type": question.type,
            "options": json.loads(question.options) if question.options else None,
            "student_answer": ans.content,
            "image_urls": json.loads(ans.image_urls) if ans.image_urls else [],
            "correct_answer": question.answer if current_user.role != "student" or submission.status == "graded" else None,
            "score": ans.score,
            "is_correct": ans.is_correct,
        })

    return result
