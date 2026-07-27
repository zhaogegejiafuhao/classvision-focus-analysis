"""考试审核工作流路由（从原 exam_review_routes.py 拆分）

拆分后的模块：
- exam_review_routes.py：审核数据查询、提交、批量确认（工作流）
- exam_review_export_routes.py：HTML 报告导出、审核统计仪表盘（导出/统计）

本模块包含：
- GET  /{exam_id}/review              获取审核数据
- POST /{exam_id}/review/submit       提交审核结果
- POST /{exam_id}/review/batch-confirm 批量确认
"""

import json
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Answer,
    Exam,
    ExamSubmission,
    Question,
    RegisteredPerson,
)
from backend.services.exam_service import check_submission_completion

router = APIRouter(prefix="/api/exams", tags=["exam-review"])


# ===== Pydantic 请求模型 =====


class ReviewSubmitItem(BaseModel):
    answer_id: int
    teacher_score: float
    teacher_comment: Optional[str] = None


class ReviewSubmitRequest(BaseModel):
    items: list[ReviewSubmitItem]


class BatchSelectConfirmRequest(BaseModel):
    """批量选择确认请求：支持按题目/按提交/按状态筛选"""

    mode: str = "question"  # question=按题目, submission=按提交, status=按状态
    question_id: Optional[int] = None  # mode=question 时使用
    submission_id: Optional[int] = None  # mode=submission 时使用
    status_filter: Optional[str] = None  # mode=status 时: needs_review / unconfirmed / all
    adopt_ai_score: bool = True
    teacher_scores: Optional[dict[int, float]] = None


# ===== 路由 =====


@router.get("/{exam_id}/review")
def get_exam_review_data(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取考试审核数据（按题目聚合所有学生答案，供教师横向对比审核）

    返回结构：
    {
      exam_id, exam_title, exam_total_score,
      total_submissions, ai_grading_count, ai_graded_count, graded_count,
      review_progress: {confirmed, pending},
      questions: [
        {
          question_id, question_type, question_content, max_score, standard_answer,
          answers: [
            {answer_id, submission_id, student_name, student_avatar,
             content, image_urls, ai_status, ai_score, ai_confidence, ai_comment,
             ai_grading, ai_rubric, ocr_text, needs_review,
             teacher_confirmed, teacher_score, teacher_comment}
          ]
        }
      ]
    }
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师可审核")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权审核此考试")

    # 拉取所有题目（按 id 排序）
    questions = db.query(Question).filter(
        Question.exam_id == exam_id
    ).order_by(Question.id).all()

    # 拉取所有提交（按提交时间排序）
    submissions = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.status.in_(["submitted", "ai_grading", "ai_graded", "graded"]),
    ).order_by(ExamSubmission.submitted_at).all()

    # 构建学生姓名映射
    student_ids = {s.student_id for s in submissions}
    students = db.query(RegisteredPerson).filter(
        RegisteredPerson.id.in_(student_ids)
    ).all() if student_ids else []
    student_map = {s.id: s for s in students}

    # 按题目聚合答案
    question_list = []
    confirmed_total = 0
    pending_total = 0

    for q in questions:
        # 仅主观题纳入审核
        if q.type not in ("essay", "fill"):
            continue

        # 收集该题所有学生的答案
        answer_list = []
        for sub in submissions:
            for ans in sub.answers:
                if ans.question_id != q.id:
                    continue
                # fill 题仅带图片的算主观
                if q.type == "fill" and not (ans.image_urls and json.loads(ans.image_urls)):
                    continue

                student = student_map.get(sub.student_id)
                answer_list.append({
                    "answer_id": ans.id,
                    "submission_id": sub.id,
                    "student_id": sub.student_id,
                    "student_name": student.name if student else f"用户{sub.student_id}",
                    "student_avatar": getattr(student, "avatar", None) if student else None,
                    "content": ans.content,
                    "image_urls": json.loads(ans.image_urls) if ans.image_urls else [],
                    "ai_status": ans.ai_status,
                    "ai_score": ans.ai_score,
                    "ai_confidence": ans.ai_confidence,
                    "ai_comment": ans.ai_comment,
                    "ai_grading": json.loads(ans.ai_grading_json) if ans.ai_grading_json else None,
                    "ai_rubric": json.loads(ans.ai_rubric_json) if ans.ai_rubric_json else None,
                    "ai_model_key": ans.ai_model_key,
                    "ocr_text": ans.ocr_text,
                    "ocr_confidence": ans.ocr_confidence,
                    "needs_review": ans.needs_review,
                    "teacher_confirmed": ans.teacher_confirmed,
                    "teacher_score": ans.teacher_score,
                    "teacher_comment": ans.teacher_comment,
                    "submission_status": sub.status,
                })

                if ans.teacher_confirmed:
                    confirmed_total += 1
                else:
                    pending_total += 1

        if not answer_list:
            continue  # 该题无人作答

        question_list.append({
            "question_id": q.id,
            "question_type": q.type,
            "question_content": q.content,
            "max_score": q.score,
            "standard_answer": q.answer,
            "answers": answer_list,
        })

    # 统计 submission 状态分布
    status_counts = {"submitted": 0, "ai_grading": 0, "ai_graded": 0, "graded": 0}
    for s in submissions:
        if s.status in status_counts:
            status_counts[s.status] += 1

    return {
        "exam_id": exam_id,
        "exam_title": exam.title,
        "exam_total_score": exam.total_score,
        "total_submissions": len(submissions),
        "status_counts": status_counts,
        "review_progress": {
            "confirmed": confirmed_total,
            "pending": pending_total,
            "total": confirmed_total + pending_total,
        },
        "questions": question_list,
    }


@router.post("/{exam_id}/review/submit")
def submit_exam_review(
    exam_id: int,
    data: ReviewSubmitRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师提交全部审核结果，锁定分数

    接收所有主观题的最终分数，批量写回并锁定 submission 为 graded。
    适用于教师完成全部审核后的"提交全部审核"按钮。
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师可审核")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权审核此考试")

    if not data.items:
        raise HTTPException(400, "审核项不能为空")

    # 按 answer_id 索引
    answer_ids = [item.answer_id for item in data.items]
    answers = db.query(Answer).filter(Answer.id.in_(answer_ids)).all()
    answer_map = {a.id: a for a in answers}

    # 收集受影响的 submission_ids
    affected_submission_ids = set()

    for item in data.items:
        answer = answer_map.get(item.answer_id)
        if not answer:
            continue

        # 满分校验
        max_score = answer.question.score if answer.question else 100
        if item.teacher_score < 0 or item.teacher_score > max_score:
            raise HTTPException(400, f"答案 {item.answer_id} 分数应在 0-{max_score} 之间")

        answer.teacher_confirmed = True
        answer.teacher_score = item.teacher_score
        answer.teacher_comment = item.teacher_comment
        answer.confirmed_at = datetime.now()
        answer.score = item.teacher_score
        answer.is_correct = item.teacher_score >= max_score * 0.6
        affected_submission_ids.add(answer.submission_id)

    db.commit()

    # 检查每个受影响的 submission 是否全部确认完毕
    for sid in affected_submission_ids:
        sub = db.query(ExamSubmission).filter(ExamSubmission.id == sid).first()
        if sub:
            check_submission_completion(db, sub)

    return {
        "success": True,
        "confirmed_count": len(data.items),
        "affected_submissions": len(affected_submission_ids),
    }


@router.post("/{exam_id}/review/batch-confirm")
def batch_select_confirm(
    exam_id: int,
    data: BatchSelectConfirmRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """批量选择确认（增强版）

    支持三种筛选模式：
    - mode=question + question_id: 确认某题所有学生的答案
    - mode=submission + submission_id: 确认某学生所有主观题答案
    - mode=status + status_filter: 按 needs_review/unconfirmed 筛选
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师可操作")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作")

    # 收集目标答案
    target_answers = []
    submissions = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.status.in_(["submitted", "ai_grading", "ai_graded", "graded"]),
    ).all()

    for sub in submissions:
        for ans in sub.answers:
            if ans.teacher_confirmed:
                continue  # 跳过已确认
            q = ans.question
            if not q:
                continue

            # 仅主观题
            is_subjective = False
            if q.type == "essay":
                is_subjective = True
            elif q.type == "fill" and ans.image_urls:
                try:
                    urls = json.loads(ans.image_urls)
                    if urls:
                        is_subjective = True
                except (json.JSONDecodeError, TypeError):
                    pass

            if not is_subjective:
                continue

            # 按模式筛选
            if data.mode == "question":
                if data.question_id and ans.question_id != data.question_id:
                    continue
            elif data.mode == "submission":
                if data.submission_id and ans.submission_id != data.submission_id:
                    continue
            elif data.mode == "status":
                if data.status_filter == "needs_review" and not ans.needs_review:
                    continue
                elif data.status_filter == "unconfirmed":
                    pass  # 已被 teacher_confirmed 过滤
                elif data.status_filter == "all":
                    pass

            target_answers.append(ans)

    # 批量确认
    confirmed_count = 0
    affected_submission_ids = set()

    for ans in target_answers:
        if data.adopt_ai_score:
            if ans.ai_score is None:
                continue  # 无 AI 分跳过
            final_score = ans.ai_score
        else:
            ts = (data.teacher_scores or {}).get(ans.id)
            if ts is None:
                continue
            final_score = ts

        max_score = ans.question.score if ans.question else 100
        if final_score < 0 or final_score > max_score:
            continue

        ans.teacher_confirmed = True
        ans.teacher_score = final_score
        ans.confirmed_at = datetime.now()
        ans.score = final_score
        ans.is_correct = final_score >= max_score * 0.6
        affected_submission_ids.add(ans.submission_id)
        confirmed_count += 1

    db.commit()

    # 检查 submission 完成度
    for sid in affected_submission_ids:
        sub = db.query(ExamSubmission).filter(ExamSubmission.id == sid).first()
        if sub:
            check_submission_completion(db, sub)

    return {
        "success": True,
        "confirmed_count": confirmed_count,
        "affected_submissions": len(affected_submission_ids),
        "mode": data.mode,
    }
