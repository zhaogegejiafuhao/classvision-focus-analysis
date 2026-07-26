"""考试 AI 批改路由（从 exam_routes.py 拆分）

涵盖：
- 查询 AI 批改进度（前端轮询）
- 教师重新触发 AI 批改
- 教师确认单题 / 批量确认
"""
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import Answer, ExamSubmission, RegisteredPerson
from backend.api.exam_schemas import ConfirmAnswerRequest, ConfirmBatchRequest
from backend.services.exam_service import (
    is_subjective_answer as _is_subjective_answer,
    check_submission_completion as _check_submission_completion,
)

router = APIRouter(prefix="/api/exams", tags=["exams"])


# ===== 查询 AI 批改进度 =====
@router.get("/submissions/{submission_id}/ai-progress")
def get_ai_grading_progress(
    submission_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """查询 AI 批改进度（前端轮询）"""
    submission = db.query(ExamSubmission).filter(
        ExamSubmission.id == submission_id
    ).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    # 权限检查
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权查看")
    if (current_user.role == "teacher"
            and submission.exam.teacher_id != current_user.id
            and current_user.role != "admin"):
        raise HTTPException(403, "无权查看")

    from backend.services.exam_grader import get_grading_progress
    task_info = get_grading_progress(submission_id)

    # 统计 answer 维度进度
    answers = db.query(Answer).filter(Answer.submission_id == submission_id).all()
    subjective = []
    for a in answers:
        q = a.question
        if q and _is_subjective_answer(a, q):
            subjective.append(a)

    graded = [a for a in subjective if a.ai_status == "graded"]
    failed = [a for a in subjective if a.ai_status == "failed"]
    processing = [a for a in subjective if a.ai_status == "processing"]
    pending = [a for a in subjective if a.ai_status == "pending"]

    return {
        "submission_id": submission_id,
        "submission_status": submission.status,  # ai_grading / ai_graded / graded
        "task_running": task_info["running"],
        "total_subjective": len(subjective),
        "graded": len(graded),
        "failed": len(failed),
        "processing": len(processing),
        "pending": len(pending),
        "progress_pct": round(len(graded) / max(len(subjective), 1) * 100, 1),
        "needs_review_count": sum(1 for a in graded if a.needs_review),
        "teacher_confirmed_count": sum(1 for a in subjective if a.teacher_confirmed),
    }


# ===== 重新触发 AI 批改 =====
@router.post("/submissions/{submission_id}/regrade")
def regrade_submission(
    submission_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """重新触发 AI 批改（教师对结果不满意时）

    仅重置未确认的主观题；已确认的题不会被重新批改。
    """
    submission = db.query(ExamSubmission).filter(
        ExamSubmission.id == submission_id
    ).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    if submission.exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作")

    # 重置未确认的主观题 answer
    reset_count = 0
    for ans in submission.answers:
        q = ans.question
        if q and _is_subjective_answer(ans, q) and not ans.teacher_confirmed:
            ans.ai_status = "pending"
            ans.ai_score = None
            ans.ai_comment = None
            ans.ai_confidence = None
            ans.ai_grading_json = None
            ans.ai_rubric_json = None
            ans.ai_graded_at = None
            ans.ai_error = None
            ans.ocr_text = None
            ans.ocr_confidence = None
            ans.ocr_engines = None
            ans.needs_review = False
            reset_count += 1

    if reset_count == 0:
        raise HTTPException(400, "没有可重新批改的题目（全部已确认）")

    submission.status = "ai_grading"
    db.commit()

    # 触发后台 AI 批改
    from backend.services.exam_grader import trigger_ai_grading
    trigger_ai_grading(submission.id)

    return {
        "success": True,
        "reset_count": reset_count,
        "message": f"已重置 {reset_count} 道题，AI 重新批改中",
    }


# ===== 教师确认单题 =====
@router.post("/submissions/{submission_id}/answers/{answer_id}/confirm")
def confirm_answer(
    submission_id: int,
    answer_id: int,
    data: ConfirmAnswerRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师确认单题（含覆盖分数/评语）"""
    submission = db.query(ExamSubmission).filter(
        ExamSubmission.id == submission_id
    ).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    if submission.exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作")

    answer = db.query(Answer).filter(
        Answer.id == answer_id,
        Answer.submission_id == submission_id,
    ).first()
    if not answer:
        raise HTTPException(404, "答案不存在")

    # 计算最终分数
    if data.adopt_ai_score:
        if answer.ai_score is None:
            raise HTTPException(400, "AI 分数不存在，无法采用")
        final_score = answer.ai_score
    else:
        if data.teacher_score is None:
            raise HTTPException(400, "请提供 teacher_score 或 adopt_ai_score=true")
        final_score = data.teacher_score

    # 题目满分校验
    max_score = answer.question.score if answer.question else 100
    if final_score < 0 or final_score > max_score:
        raise HTTPException(400, f"分数应在 0-{max_score} 之间")

    answer.teacher_confirmed = True
    answer.teacher_score = final_score
    answer.teacher_comment = data.teacher_comment
    answer.confirmed_at = datetime.now()
    # 同步到 answer.score（用于统一查询）
    answer.score = final_score
    answer.is_correct = final_score >= max_score * 0.6  # 60% 及格
    db.commit()

    # 检查 submission 是否全部确认完毕
    db.refresh(submission)
    _check_submission_completion(db, submission)

    return {
        "success": True,
        "answer_id": answer_id,
        "teacher_score": final_score,
        "submission_status": submission.status,
    }


# ===== 批量确认答案 =====
@router.post("/submissions/{submission_id}/confirm-batch")
def confirm_answers_batch(
    submission_id: int,
    data: ConfirmBatchRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """批量确认答案（一键采用 AI 分或批量指定分数）"""
    submission = db.query(ExamSubmission).filter(
        ExamSubmission.id == submission_id
    ).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    if submission.exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作")

    if not data.answer_ids:
        raise HTTPException(400, "answer_ids 不能为空")

    confirmed_count = 0
    for answer_id in data.answer_ids:
        answer = db.query(Answer).filter(
            Answer.id == answer_id,
            Answer.submission_id == submission_id,
        ).first()
        if not answer:
            continue
        if answer.teacher_confirmed:
            continue  # 已确认的跳过

        # 计算分数
        if data.adopt_ai_score:
            if answer.ai_score is None:
                continue  # 无 AI 分的跳过
            final_score = answer.ai_score
        else:
            ts = (data.teacher_scores or {}).get(answer_id)
            if ts is None:
                continue
            final_score = ts

        # 满分校验
        max_score = answer.question.score if answer.question else 100
        if final_score < 0 or final_score > max_score:
            continue

        answer.teacher_confirmed = True
        answer.teacher_score = final_score
        answer.confirmed_at = datetime.now()
        answer.score = final_score
        answer.is_correct = final_score >= max_score * 0.6
        confirmed_count += 1

    db.commit()

    # 检查 submission 是否全部确认完毕
    db.refresh(submission)
    _check_submission_completion(db, submission)

    return {
        "success": True,
        "confirmed_count": confirmed_count,
        "submission_status": submission.status,
    }
