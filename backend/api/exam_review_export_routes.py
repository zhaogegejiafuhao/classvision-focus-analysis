"""考试审核报告导出与统计路由（从 exam_review_routes.py 拆分）

拆分后的模块：
- exam_review_routes.py：审核数据查询、提交、批量确认（工作流）
- exam_review_export_routes.py：HTML 报告导出、审核统计仪表盘（导出/统计）
"""
import json
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Exam,
    ExamSubmission,
    Question,
    RegisteredPerson,
)

router = APIRouter(prefix="/api/exams", tags=["exam-review-export"])


@router.get("/{exam_id}/review/export")
def export_review_report(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """导出审核报告为 HTML（可打印为 PDF）

    包含：每题的学生答案 + AI 评分/评语 + 教师评分/评语
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师可导出")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作")

    # 复用 review 数据获取逻辑
    questions = db.query(Question).filter(
        Question.exam_id == exam_id
    ).order_by(Question.id).all()

    submissions = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.status.in_(["submitted", "ai_grading", "ai_graded", "graded"]),
    ).order_by(ExamSubmission.submitted_at).all()

    student_ids = {s.student_id for s in submissions}
    students = db.query(RegisteredPerson).filter(
        RegisteredPerson.id.in_(student_ids)
    ).all() if student_ids else []
    student_map = {s.id: s for s in students}

    type_names = {"single": "单选题", "multi": "多选题", "judge": "判断题", "fill": "填空题", "essay": "简答题"}

    # 生成 HTML 报告
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{exam.title} - AI 审核报告</title>
<style>
  @page {{ size: A4; margin: 1.5cm; }}
  body {{ font-family: "Microsoft YaHei", "SimSun", sans-serif; font-size: 12px; line-height: 1.6; }}
  h1 {{ text-align: center; font-size: 18px; border-bottom: 2px solid #1890ff; padding-bottom: 8px; }}
  .meta {{ text-align: center; color: #666; margin: 8px 0 16px; }}
  .question-section {{ margin: 16px 0; page-break-inside: avoid; }}
  .question-title {{ font-size: 14px; font-weight: bold; background: #f0f9ff; padding: 6px 10px; border-left: 3px solid #1890ff; }}
  .standard-answer {{ color: #52c41a; font-size: 11px; margin: 4px 0 8px 10px; }}
  table {{ width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 11px; }}
  th, td {{ border: 1px solid #e8e8e8; padding: 6px 8px; text-align: left; vertical-align: top; }}
  th {{ background: #fafafa; font-weight: 600; white-space: nowrap; }}
  .ai-score {{ color: #1890ff; }}
  .teacher-score {{ color: #52c41a; font-weight: bold; }}
  .needs-review {{ background: #fff2f0; }}
  .confirmed {{ background: #f6ffed; }}
  .comment {{ font-size: 10px; color: #666; max-width: 200px; word-break: break-all; }}
  .tag {{ display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 10px; margin-right: 4px; }}
  .tag-blue {{ background: #e6f7ff; color: #1890ff; }}
  .tag-green {{ background: #f6ffed; color: #52c41a; }}
  .tag-red {{ background: #fff2f0; color: #ff4d4f; }}
  .tag-orange {{ background: #fff7e6; color: #fa8c16; }}
</style></head><body>
<h1>{exam.title} - AI 审核报告</h1>
<div class="meta">总分 {exam.total_score} 分 | 提交 {len(submissions)} 份 | 生成时间 {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>
"""

    for idx, q in enumerate(questions):
        if q.type not in ("essay", "fill"):
            continue

        # 收集该题答案
        rows = []
        for sub in submissions:
            for ans in sub.answers:
                if ans.question_id != q.id:
                    continue
                if q.type == "fill" and not (ans.image_urls and json.loads(ans.image_urls)):
                    continue
                student = student_map.get(sub.student_id)
                rows.append((ans, student, sub))

        if not rows:
            continue

        html += f"""
<div class="question-section">
  <div class="question-title">第 {idx + 1} 题 [{type_names.get(q.type, q.type)}]（{q.score} 分）</div>
  <div style="margin: 4px 0 4px 10px">{q.content[:200]}</div>
  <div class="standard-answer">标准答案：{q.answer or '（无）'}</div>
  <table>
    <tr>
      <th style="width:60px">学生</th>
      <th style="width:120px">学生答案</th>
      <th style="width:60px">AI 评分</th>
      <th style="width:80px">AI 评语</th>
      <th style="width:50px">置信度</th>
      <th style="width:60px">教师评分</th>
      <th style="width:80px">教师评语</th>
      <th style="width:50px">状态</th>
    </tr>
"""

        for ans, student, sub in rows:
            name = student.name if student else f"用户{sub.student_id}"
            content = (ans.content or "")[:80]
            if not content and ans.image_urls:
                content = "（图片答案）"
            ai_score = f"{ans.ai_score}" if ans.ai_score is not None else "-"
            ai_comment = (ans.ai_comment or "")[:60]
            confidence = f"{ans.ai_confidence * 100:.0f}%" if ans.ai_confidence else "-"
            teacher_score = f"{ans.teacher_score}" if ans.teacher_score is not None else "-"
            teacher_comment = (ans.teacher_comment or "")[:60]

            # 状态标签
            if ans.teacher_confirmed:
                status_html = '<span class="tag tag-green">已确认</span>'
                row_class = "confirmed"
            elif ans.needs_review:
                status_html = '<span class="tag tag-red">需审核</span>'
                row_class = "needs-review"
            elif ans.ai_status == "graded":
                status_html = '<span class="tag tag-blue">待审核</span>'
                row_class = ""
            elif ans.ai_status == "failed":
                status_html = '<span class="tag tag-orange">失败</span>'
                row_class = "needs-review"
            else:
                status_html = '<span class="tag tag-orange">批改中</span>'
                row_class = ""

            html += f"""    <tr class="{row_class}">
      <td>{name}</td>
      <td>{content}</td>
      <td class="ai-score">{ai_score}</td>
      <td class="comment">{ai_comment}</td>
      <td>{confidence}</td>
      <td class="teacher-score">{teacher_score}</td>
      <td class="comment">{teacher_comment}</td>
      <td>{status_html}</td>
    </tr>
"""

        html += "  </table>\n</div>\n"

    html += "</body></html>"

    return StreamingResponse(
        iter([html]),
        media_type="text/html",
        headers={"Content-Disposition": f"inline; filename=review_report_{exam_id}.html"},
    )


@router.get("/{exam_id}/review/stats")
def get_review_stats(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """审核统计仪表盘数据

    返回：
    - 整体进度（已确认/总数/百分比）
    - 各题维度：AI 平均分、教师平均分、偏差、需审核数
    - AI 置信度分布
    - 教师修正分布（教师分 vs AI 分的差异统计）
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "仅教师可查看")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权操作")

    # 复用 review 数据
    questions = db.query(Question).filter(
        Question.exam_id == exam_id
    ).order_by(Question.id).all()

    submissions = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.status.in_(["submitted", "ai_grading", "ai_graded", "graded"]),
    ).all()

    student_ids = {s.student_id for s in submissions}
    students = db.query(RegisteredPerson).filter(
        RegisteredPerson.id.in_(student_ids)
    ).all() if student_ids else []
    student_map = {s.id: s for s in students}

    # 整体统计
    total_answers = 0
    confirmed_answers = 0
    needs_review_count = 0
    all_confidence = []
    all_ai_scores = []
    all_teacher_scores = []
    all_deviations = []

    # 各题统计
    question_stats = []

    for q in questions:
        if q.type not in ("essay", "fill"):
            continue

        q_ai_scores = []
        q_teacher_scores = []
        q_confirmed = 0
        q_needs_review = 0
        q_confidence = []
        q_deviations = []
        q_status_dist = {"graded": 0, "failed": 0, "pending": 0, "processing": 0, "confirmed": 0}

        for sub in submissions:
            for ans in sub.answers:
                if ans.question_id != q.id:
                    continue
                if q.type == "fill" and not (ans.image_urls and json.loads(ans.image_urls)):
                    continue

                total_answers += 1

                if ans.teacher_confirmed:
                    confirmed_answers += 1
                    q_confirmed += 1
                    q_status_dist["confirmed"] += 1

                if ans.needs_review:
                    needs_review_count += 1
                    q_needs_review += 1

                if ans.ai_score is not None:
                    q_ai_scores.append(ans.ai_score)
                    all_ai_scores.append(ans.ai_score)

                if ans.ai_confidence is not None:
                    q_confidence.append(ans.ai_confidence)
                    all_confidence.append(ans.ai_confidence)

                if ans.teacher_score is not None:
                    q_teacher_scores.append(ans.teacher_score)
                    all_teacher_scores.append(ans.teacher_score)

                if ans.ai_score is not None and ans.teacher_score is not None:
                    dev = ans.teacher_score - ans.ai_score
                    q_deviations.append(dev)
                    all_deviations.append(dev)

                if ans.ai_status in q_status_dist:
                    q_status_dist[ans.ai_status] += 1

        question_stats.append({
            "question_id": q.id,
            "question_type": q.type,
            "max_score": q.score,
            "total_answers": len(q_ai_scores) + q_status_dist.get("pending", 0),
            "confirmed": q_confirmed,
            "needs_review": q_needs_review,
            "ai_avg": round(sum(q_ai_scores) / len(q_ai_scores), 1) if q_ai_scores else None,
            "teacher_avg": round(sum(q_teacher_scores) / len(q_teacher_scores), 1) if q_teacher_scores else None,
            "deviation_avg": round(sum(q_deviations) / len(q_deviations), 1) if q_deviations else None,
            "confidence_avg": round(sum(q_confidence) / len(q_confidence), 2) if q_confidence else None,
            "status_dist": q_status_dist,
        })

    # 置信度分布
    confidence_dist = {"high": 0, "medium": 0, "low": 0}
    for c in all_confidence:
        if c >= 0.85:
            confidence_dist["high"] += 1
        elif c >= 0.6:
            confidence_dist["medium"] += 1
        else:
            confidence_dist["low"] += 1

    # 修正分布
    deviation_dist = {"no_change": 0, "minor": 0, "major": 0}
    for d in all_deviations:
        if abs(d) < 0.5:
            deviation_dist["no_change"] += 1
        elif abs(d) < 3:
            deviation_dist["minor"] += 1
        else:
            deviation_dist["major"] += 1

    return {
        "exam_id": exam_id,
        "exam_title": exam.title,
        "total_submissions": len(submissions),
        "total_subjective_answers": total_answers,
        "confirmed_answers": confirmed_answers,
        "needs_review_count": needs_review_count,
        "confirm_progress_pct": round(confirmed_answers / max(total_answers, 1) * 100, 1),
        "ai_avg_score": round(sum(all_ai_scores) / len(all_ai_scores), 1) if all_ai_scores else None,
        "teacher_avg_score": round(sum(all_teacher_scores) / len(all_teacher_scores), 1) if all_teacher_scores else None,
        "avg_deviation": round(sum(all_deviations) / len(all_deviations), 2) if all_deviations else None,
        "confidence_dist": confidence_dist,
        "deviation_dist": deviation_dist,
        "question_stats": question_stats,
    }
