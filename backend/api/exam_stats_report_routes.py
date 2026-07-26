"""考试统计、报告与导出路由（从 exam_routes.py 拆分）

涵盖：
- 考试统计分析（每题正确率、区分度、分数分布）
- 班级维度考试报告（含 AI 文案）
- 学生个人考试报告
- 试卷 HTML 导出 / 成绩 CSV 导出
"""
import csv
import io
import json
import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session, joinedload

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Answer, Exam, ExamSubmission, Question, RegisteredPerson,
)

logger = logging.getLogger("exam")

router = APIRouter(prefix="/api/exams", tags=["exams"])


# ===== 考试统计分析 =====
@router.get("/{exam_id}/stats")
def get_exam_stats(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取考试统计分析数据"""
    exam = db.query(Exam).options(
        joinedload(Exam.questions),
        joinedload(Exam.submissions),
    ).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    submissions = [s for s in exam.submissions if s.status in ("graded", "submitted")]

    if not submissions:
        return {
            "total_students": 0,
            "submitted_count": 0,
            "avg_score": 0,
            "max_score": 0,
            "min_score": 0,
            "pass_rate": 0,
            "score_distribution": [],
            "question_stats": [],
        }

    scores = [s.score or 0 for s in submissions]
    total_score = exam.total_score or 100
    pass_line = total_score * 0.6

    # 分数分布
    ranges = [(0, 60), (60, 70), (70, 80), (80, 90), (90, 101)]
    distribution = []
    for lo, hi in ranges:
        lo_scaled = lo * total_score / 100
        hi_scaled = hi * total_score / 100
        count = sum(1 for s in scores if lo_scaled <= s < hi_scaled)
        distribution.append({"range": f"{lo}-{hi}", "count": count})

    # 每题统计（批量查询避免 N+1）
    question_stats = []
    q_ids = [q.id for q in exam.questions]
    all_answers = db.query(Answer).filter(Answer.question_id.in_(q_ids)).all() if q_ids else []
    answers_by_q: dict[int, list[Answer]] = {}
    for a in all_answers:
        answers_by_q.setdefault(a.question_id, []).append(a)

    for q in sorted(exam.questions, key=lambda x: x.order):
        answers = answers_by_q.get(q.id, [])
        if not answers:
            continue
        correct_count = sum(1 for a in answers if a.is_correct == True)
        total = len(answers)
        avg_score = sum(a.score or 0 for a in answers) / total
        difficulty = 1 - (correct_count / total) if total > 0 else 0

        # 区分度：高分组答对率 - 低分组答对率
        sorted_subs = sorted(submissions, key=lambda s: s.score or 0, reverse=True)
        high_group = sorted_subs[:max(1, len(sorted_subs) // 3)]
        low_group = sorted_subs[-max(1, len(sorted_subs) // 3):]
        high_correct = sum(1 for s in high_group for a in answers if a.submission_id == s.id and a.is_correct == True)
        low_correct = sum(1 for s in low_group for a in answers if a.submission_id == s.id and a.is_correct == True)
        high_rate = high_correct / len(high_group) if high_group else 0
        low_rate = low_correct / len(low_group) if low_group else 0
        discrimination = high_rate - low_rate

        question_stats.append({
            "question_id": q.id,
            "order": q.order,
            "type": q.type,
            "content": q.content[:50],
            "score": q.score,
            "correct_rate": correct_count / total if total > 0 else 0,
            "avg_score": round(avg_score, 2),
            "difficulty": round(difficulty, 2),
            "discrimination": round(discrimination, 2),
        })

    return {
        "total_students": len(exam.classroom.students) if exam.classroom else 0,
        "submitted_count": len(submissions),
        "avg_score": round(sum(scores) / len(scores), 2),
        "max_score": max(scores),
        "min_score": min(scores),
        "pass_rate": round(sum(1 for s in scores if s >= pass_line) / len(scores) * 100, 1),
        "score_distribution": distribution,
        "question_stats": question_stats,
    }


# ===== 试卷 HTML 导出 =====
@router.get("/{exam_id}/paper-export")
def export_exam_paper(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """导出试卷为HTML(可打印为PDF)"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    questions = exam.questions
    type_names = {"single": "单选题", "multi": "多选题", "judge": "判断题", "fill": "填空题", "essay": "简答题"}

    # 按题型分组
    grouped = {}
    for q in sorted(questions, key=lambda x: x.order):
        t = type_names.get(q.type, q.type)
        if t not in grouped:
            grouped[t] = []
        options = json.loads(q.options) if q.options else None
        grouped[t].append({"content": q.content, "options": options, "score": q.score})

    # 生成HTML试卷
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{exam.title} - 试卷</title>
<style>
  @page {{ size: A4; margin: 2cm; }}
  body {{ font-family: "SimSun", "Microsoft YaHei", serif; font-size: 14px; line-height: 1.8; }}
  h1 {{ text-align: center; font-size: 20px; border-bottom: 2px solid #000; padding-bottom: 10px; }}
  .info {{ text-align: center; margin: 10px 0 20px; color: #666; }}
  .section {{ margin: 20px 0; }}
  .section-title {{ font-size: 16px; font-weight: bold; margin-bottom: 10px; }}
  .question {{ margin: 10px 0 10px 20px; }}
  .options {{ margin-left: 20px; }}
  .option {{ margin: 4px 0; }}
  .answer-line {{ border-bottom: 1px solid #ccc; display: inline-block; width: 200px; margin-left: 10px; }}
  .essay-space {{ height: 80px; border: 1px dashed #ccc; margin: 5px 0 5px 20px; }}
</style></head><body>
<h1>{exam.title}</h1>
<div class="info">考试时长：{exam.duration}分钟 &nbsp;|&nbsp; 总分：{exam.total_score}分 &nbsp;|&nbsp; 共{len(questions)}题</div>
<div class="info">姓名：__________ &nbsp;|&nbsp; 学号：__________ &nbsp;|&nbsp; 班级：__________</div>
"""

    for section_title, section_questions in grouped.items():
        html += f'<div class="section"><div class="section-title">{section_title}（共{len(section_questions)}题）</div>\n'
        for i, q in enumerate(section_questions, 1):
            html += f'<div class="question">{i}. {q["content"]}（{q["score"]}分）</div>\n'
            if q["options"]:
                html += '<div class="options">\n'
                for j, opt in enumerate(q["options"]):
                    label = chr(65 + j)  # A, B, C, D
                    html += f'<div class="option">{label}. {opt}</div>\n'
                html += '</div>\n'
            else:
                html += '<div class="essay-space"></div>\n'
        html += '</div>\n'

    html += '</body></html>'

    return StreamingResponse(
        io.BytesIO(html.encode("utf-8")),
        media_type="text/html; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename=exam_paper_{exam_id}.html"},
    )


# ===== 成绩 CSV 导出 =====
@router.get("/{exam_id}/export")
def export_exam_results(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """导出考试成绩为 CSV"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权导出")

    output = io.StringIO()
    output.write('\ufeff')  # BOM 头，防止中文乱码
    writer = csv.writer(output)
    writer.writerow(["学生", "得分", "状态", "提交时间"])

    for sub in exam.submissions:
        writer.writerow([
            sub.student.name,
            sub.score if sub.score is not None else "待批改",
            {"in_progress": "进行中", "submitted": "待批改", "graded": "已批改"}.get(sub.status, sub.status),
            sub.submitted_at.strftime("%Y-%m-%d %H:%M:%S") if sub.submitted_at else "",
        ])

    output.seek(0)
    filename = f"exam_results_{exam_id}.csv"
    return StreamingResponse(
        output,
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


# ===== 班级维度考试报告 =====
@router.post("/{exam_id}/report")
def generate_exam_report(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """生成考试报告（班级维度 + AI 文案）

    包含：参考人数、平均分、及格率、最高/最低分、每题正确率、知识点掌握度、AI 综合分析
    """
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以生成报告")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    submissions = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.status.in_(["graded", "submitted"]),
    ).all()

    if not submissions:
        raise HTTPException(400, "暂无已提交的答卷，无法生成报告")

    # ── 基础统计 ──
    total_count = len(submissions)
    scores = [s.score or 0 for s in submissions]
    avg_score = round(sum(scores) / total_count, 1) if total_count > 0 else 0
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0
    pass_rate = round(sum(1 for s in scores if s >= 60) / total_count * 100, 1) if total_count > 0 else 0

    # ── 每题统计 ──
    questions = db.query(Question).filter(Question.exam_id == exam_id).order_by(Question.order).all()
    question_stats = []
    for q in questions:
        answers = db.query(Answer).filter(Answer.question_id == q.id).all()
        if not answers:
            continue
        correct_count = sum(1 for a in answers if a.is_correct)
        total_answers = len(answers)
        avg_q_score = round(sum(a.score or 0 for a in answers) / total_answers, 1)
        question_stats.append({
            "question_id": q.id,
            "order": q.order,
            "type": q.type,
            "content": q.content[:60] + ("..." if len(q.content) > 60 else ""),
            "score": q.score,
            "correct_rate": round(correct_count / total_answers * 100, 1),
            "avg_score": avg_q_score,
        })

    # ── 分数段分布 ──
    score_ranges = {
        "90-100": sum(1 for s in scores if s >= 90),
        "80-89": sum(1 for s in scores if 80 <= s < 90),
        "70-79": sum(1 for s in scores if 70 <= s < 80),
        "60-69": sum(1 for s in scores if 60 <= s < 70),
        "0-59": sum(1 for s in scores if s < 60),
    }

    # ── AI 文案生成 ──
    ai_analysis = ""
    try:
        from backend.services.ollama_service import generate_report
        stats_for_ai = {
            "exam_title": exam.title,
            "total_count": total_count,
            "avg_score": avg_score,
            "max_score": max_score,
            "min_score": min_score,
            "pass_rate": pass_rate,
            "score_ranges": score_ranges,
            "question_stats": question_stats[:10],
        }
        ai_analysis = generate_report(stats_for_ai)
    except Exception as e:
        logger.warning(f"AI 报告生成失败: {e}")
        ai_analysis = "AI 分析生成失败，请查看上方数据统计。"

    return {
        "exam_id": exam_id,
        "exam_title": exam.title,
        "total_count": total_count,
        "avg_score": avg_score,
        "max_score": max_score,
        "min_score": min_score,
        "pass_rate": pass_rate,
        "score_ranges": score_ranges,
        "question_stats": question_stats,
        "ai_analysis": ai_analysis,
        "generated_at": datetime.now().isoformat(),
    }


# ===== 学生个人考试报告 =====
@router.get("/{exam_id}/student-report")
def get_student_exam_report(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前学生的考试个人报告

    包含：分数、错题、薄弱知识点、与班级均分对比
    """
    if current_user.role != "student":
        raise HTTPException(403, "仅学生可查看个人报告")

    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    submission = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.student_id == current_user.id,
    ).first()

    if not submission:
        raise HTTPException(404, "未找到你的答卷")

    # 班级均分
    all_submissions = db.query(ExamSubmission).filter(
        ExamSubmission.exam_id == exam_id,
        ExamSubmission.status.in_(["graded", "submitted"]),
    ).all()
    class_avg = round(sum(s.score or 0 for s in all_submissions) / len(all_submissions), 1) if all_submissions else 0

    # 我的错题
    wrong_answers = []
    for ans in submission.answers:
        if not ans.is_correct:
            q = ans.question
            wrong_answers.append({
                "question_id": q.id,
                "type": q.type,
                "content": q.content[:80],
                "my_answer": ans.content,
                "correct_answer": q.answer,
                "score": ans.score,
                "max_score": q.score,
            })

    # 薄弱知识点
    weak_points = []
    for wa in wrong_answers:
        q = db.query(Question).filter(Question.id == wa["question_id"]).first()
        if q and q.knowledge_points:
            kps = json.loads(q.knowledge_points) if q.knowledge_points else []
            weak_points.extend(kps)
    weak_points = list(set(weak_points))[:5]

    return {
        "exam_id": exam_id,
        "exam_title": exam.title,
        "my_score": submission.score or 0,
        "class_avg": class_avg,
        "diff_from_avg": round((submission.score or 0) - class_avg, 1),
        "total_questions": db.query(Question).filter(Question.exam_id == exam_id).count(),
        "correct_count": sum(1 for a in submission.answers if a.is_correct),
        "wrong_answers": wrong_answers,
        "weak_points": weak_points,
        "submitted_at": submission.submitted_at.isoformat() if submission.submitted_at else None,
    }
