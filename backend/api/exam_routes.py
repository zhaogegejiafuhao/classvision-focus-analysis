"""在线考试系统 API"""
import csv
import io
import json
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import Exam, Question, ExamSubmission, Answer, RegisteredPerson, Classroom, Student, Notification

router = APIRouter(prefix="/api/exams", tags=["exams"])


# ===== Pydantic 模型 =====
class QuestionCreate(BaseModel):
    type: str  # single/multi/judge/fill/essay
    content: str
    options: Optional[list[str]] = None  # 选择题选项
    answer: str
    score: float = 10.0


class ExamCreate(BaseModel):
    title: str
    description: str = ""
    classroom_id: Optional[int] = None
    duration: int = 60
    total_score: float = 100.0
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    questions: list[QuestionCreate] = []


class ExamOut(BaseModel):
    id: int
    title: str
    description: str
    classroom_id: Optional[int]
    classroom_name: Optional[str]
    teacher_id: int
    teacher_name: str
    duration: int
    total_score: float
    status: str
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    question_count: int

    class Config:
        from_attributes = True


class QuestionOut(BaseModel):
    id: int
    type: str
    content: str
    options: Optional[list[str]]
    score: float
    order: int

    class Config:
        from_attributes = True


class ExamDetailOut(ExamOut):
    questions: list[QuestionOut]


class AnswerSubmit(BaseModel):
    question_id: int
    content: str


class SubmissionOut(BaseModel):
    id: int
    exam_id: int
    student_id: int
    student_name: str
    score: Optional[float]
    status: str
    started_at: datetime
    submitted_at: Optional[datetime]

    class Config:
        from_attributes = True


# ===== 辅助函数 =====
def auto_grade(question: Question, answer_content: str) -> tuple[float, bool]:
    """自动评判题目"""
    if question.type == "single":
        # 单选题：答案为选项索引（如 "0", "1"）
        is_correct = answer_content.strip() == question.answer.strip()
        return (question.score if is_correct else 0), is_correct
    
    elif question.type == "multi":
        # 多选题：答案为逗号分隔的选项索引（如 "0,2,3"）
        student_answer = set(a.strip() for a in answer_content.split(",") if a.strip())
        correct_answer = set(a.strip() for a in question.answer.split(",") if a.strip())
        is_correct = student_answer == correct_answer
        return (question.score if is_correct else 0), is_correct
    
    elif question.type == "judge":
        # 判断题：答案为 "true" 或 "false"
        is_correct = answer_content.strip().lower() == question.answer.strip().lower()
        return (question.score if is_correct else 0), is_correct
    
    elif question.type == "fill":
        # 填空题：多空拆分匹配 + 数值/单位容差（A+B 方案）
        # 复用 backend.services.fill_grader.grade_fill_answer
        # auto_grade 只返回 (score, is_correct)；详细 detail 在 _grade_fill_question 中取
        from backend.services.fill_grader import grade_fill_answer
        score, is_correct, _detail = grade_fill_answer(
            answer_content, question.answer or "", question.score
        )
        return score, is_correct
    
    else:
        # 简答题：需要人工批改
        return 0, False


# ===== 教师端 API =====
@router.get("", response_model=list[ExamOut])
def list_exams(
    classroom_id: Optional[int] = None,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取考试列表"""
    query = db.query(Exam).options(
        joinedload(Exam.classroom),
        joinedload(Exam.teacher),
    )
    
    if current_user.role in ("teacher", "admin"):
        query = query.filter(Exam.teacher_id == current_user.id)
    else:
        # 学生查看分配的考试
        student = db.query(Student).filter(Student.person_id == current_user.id).first()
        if student:
            query = query.filter(Exam.classroom_id == student.classroom_id)
        else:
            return []
    
    if classroom_id:
        query = query.filter(Exam.classroom_id == classroom_id)
    
    query = query.order_by(Exam.created_at.desc())
    
    result = []
    for exam in query.all():
        classroom_name = exam.classroom.name if exam.classroom else None
        result.append(ExamOut(
            id=exam.id,
            title=exam.title,
            description=exam.description,
            classroom_id=exam.classroom_id,
            classroom_name=classroom_name,
            teacher_id=exam.teacher_id,
            teacher_name=exam.teacher.name,
            duration=exam.duration,
            total_score=exam.total_score,
            status=exam.status,
            start_time=exam.start_time,
            end_time=exam.end_time,
            question_count=len(exam.questions),
        ))
    return result


@router.post("", response_model=ExamDetailOut)
def create_exam(
    data: ExamCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """创建考试"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以创建考试")
    
    exam = Exam(
        title=data.title,
        description=data.description,
        classroom_id=data.classroom_id,
        teacher_id=current_user.id,
        duration=data.duration,
        total_score=data.total_score,
        start_time=data.start_time,
        end_time=data.end_time,
    )
    db.add(exam)
    db.flush()
    
    # 添加题目
    for i, q in enumerate(data.questions):
        question = Question(
            exam_id=exam.id,
            type=q.type,
            content=q.content,
            options=json.dumps(q.options) if q.options else None,
            answer=q.answer,
            score=q.score,
            order=i + 1,
        )
        db.add(question)
    
    db.commit()
    db.refresh(exam)
    
    classroom_name = exam.classroom.name if exam.classroom else None
    return ExamDetailOut(
        id=exam.id,
        title=exam.title,
        description=exam.description,
        classroom_id=exam.classroom_id,
        classroom_name=classroom_name,
        teacher_id=exam.teacher_id,
        teacher_name=current_user.name,
        duration=exam.duration,
        total_score=exam.total_score,
        status=exam.status,
        start_time=exam.start_time,
        end_time=exam.end_time,
        question_count=len(exam.questions),
        questions=[
            QuestionOut(
                id=q.id,
                type=q.type,
                content=q.content,
                options=json.loads(q.options) if q.options else None,
                score=q.score,
                order=q.order,
            ) for q in exam.questions
        ],
    )


# ===== 学生端路由（必须在 /{exam_id} 之前定义，避免路径冲突）=====
@router.get("/assigned", response_model=list[ExamOut])
def list_assigned_exams(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取分配给学生的考试"""
    if current_user.role == "student":
        my_classroom_ids = [
            s.classroom_id for s in
            db.query(Student.classroom_id).filter(Student.person_id == current_user.id).all()
            if s.classroom_id
        ]
        if not my_classroom_ids:
            return []
    else:
        return []
    
    exams = db.query(Exam).filter(
        Exam.classroom_id.in_(my_classroom_ids),
        Exam.status == "published",
    ).order_by(Exam.created_at.desc()).all()
    
    result = []
    for exam in exams:
        result.append(ExamOut(
            id=exam.id,
            title=exam.title,
            description=exam.description,
            classroom_id=exam.classroom_id,
            classroom_name=exam.classroom.name if exam.classroom else None,
            teacher_id=exam.teacher_id,
            teacher_name=exam.teacher.name,
            duration=exam.duration,
            total_score=exam.total_score,
            status=exam.status,
            start_time=exam.start_time,
            end_time=exam.end_time,
            question_count=len(exam.questions),
        ))
    return result


@router.get("/{exam_id}", response_model=ExamDetailOut)
def get_exam(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取考试详情"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    
    classroom_name = exam.classroom.name if exam.classroom else None
    return ExamDetailOut(
        id=exam.id,
        title=exam.title,
        description=exam.description,
        classroom_id=exam.classroom_id,
        classroom_name=classroom_name,
        teacher_id=exam.teacher_id,
        teacher_name=exam.teacher.name,
        duration=exam.duration,
        total_score=exam.total_score,
        status=exam.status,
        start_time=exam.start_time,
        end_time=exam.end_time,
        question_count=len(exam.questions),
        questions=[
            QuestionOut(
                id=q.id,
                type=q.type,
                content=q.content,
                options=json.loads(q.options) if q.options else None,
                score=q.score,
                order=q.order,
            ) for q in exam.questions
        ],
    )


@router.post("/{exam_id}/publish")
def publish_exam(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """发布考试"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权发布此考试")
    
    exam.status = "published"
    
    # 发送通知给学生
    if exam.classroom_id:
        students = db.query(Student).filter(Student.classroom_id == exam.classroom_id).all()
        for student in students:
            if student.person:
                notification = Notification(
                    title=f"考试通知：{exam.title}",
                    content=f"您有一个考试需要参加，时长 {exam.duration} 分钟。",
                    type="exam",
                    sender_id=current_user.id,
                    receiver_id=student.person_id,
                    classroom_id=exam.classroom_id,
                )
                db.add(notification)
    
    db.commit()
    return {"success": True}


@router.delete("/{exam_id}")
def delete_exam(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除考试"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权删除此考试")

    # 级联清理：先删子表数据
    for sub in exam.submissions:
        db.query(Answer).filter(Answer.submission_id == sub.id).delete()
    db.query(ExamSubmission).filter(ExamSubmission.exam_id == exam_id).delete()
    db.query(Question).filter(Question.exam_id == exam_id).delete()
    db.delete(exam)
    db.commit()
    return {"success": True}


@router.post("/{exam_id}/close")
def close_exam(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """关闭考试"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权关闭此考试")

    if exam.status != "published":
        raise HTTPException(400, "只能关闭已发布的考试")

    exam.status = "closed"
    exam.end_time = datetime.now()
    db.commit()
    return {"success": True}


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


@router.post("/{exam_id}/questions")
def add_question(
    exam_id: int,
    data: QuestionCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """向考试添加题目"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权修改此考试")
    
    if exam.status != "draft":
        raise HTTPException(400, "只能修改草稿状态的考试")
    
    # 获取当前最大顺序
    max_order = max((q.order for q in exam.questions), default=0)
    
    question = Question(
        exam_id=exam_id,
        type=data.type,
        content=data.content,
        options=json.dumps(data.options) if data.options else None,
        answer=data.answer,
        score=data.score,
        order=max_order + 1,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    
    return {
        "id": question.id,
        "type": question.type,
        "content": question.content,
        "options": json.loads(question.options) if question.options else None,
        "answer": question.answer,
        "score": question.score,
        "order": question.order,
    }


@router.delete("/{exam_id}/questions/{question_id}")
def delete_question(
    exam_id: int,
    question_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除考试题目"""
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")
    
    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权修改此考试")
    
    question = db.query(Question).filter(Question.id == question_id, Question.exam_id == exam_id).first()
    if not question:
        raise HTTPException(404, "题目不存在")
    
    db.delete(question)
    db.commit()
    return {"success": True}


@router.get("/{exam_id}/submissions", response_model=list[SubmissionOut])
def list_submissions(
    exam_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取考试提交列表"""
    exam = db.query(Exam).options(
        joinedload(Exam.submissions).joinedload(ExamSubmission.student),
    ).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(404, "考试不存在")

    if exam.teacher_id != current_user.id and current_user.role != "admin":
        raise HTTPException(403, "无权查看提交")
    
    result = []
    for sub in exam.submissions:
        result.append(SubmissionOut(
            id=sub.id,
            exam_id=sub.exam_id,
            student_id=sub.student_id,
            student_name=sub.student.name,
            score=sub.score,
            status=sub.status,
            started_at=sub.started_at,
            submitted_at=sub.submitted_at,
        ))
    return result


# ===== 学生端 API =====
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


# ===== 学生端 API =====
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


@router.post("/{exam_id}/submit")
def submit_exam(
    exam_id: int,
    answers: list[AnswerSubmit],
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """提交考试"""
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
    
    for ans in answers:
        question = db.query(Question).filter(Question.id == ans.question_id).first()
        if not question or question.exam_id != exam_id:
            continue
        
        # 自动评判
        score, is_correct = auto_grade(question, ans.content)
        if question.type == "essay":
            has_essay = True
            score = 0
            is_correct = None
        
        total_score += score
        
        answer = Answer(
            submission_id=submission.id,
            question_id=ans.question_id,
            content=ans.content,
            score=score,
            is_correct=is_correct,
        )
        db.add(answer)
    
    submission.score = total_score if not has_essay else None
    submission.status = "graded" if not has_essay else "submitted"
    submission.submitted_at = datetime.now()
    if not has_essay:
        submission.graded_at = datetime.now()
    
    db.commit()
    
    return {
        "success": True,
        "score": total_score if not has_essay else None,
        "has_essay": has_essay,
    }


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
            "correct_answer": question.answer if submission.status == "graded" else None,
            "score": ans.score,
            "is_correct": ans.is_correct,
        })

    return result


class AnswerGrade(BaseModel):
    answer_id: int
    score: float
    is_correct: Optional[bool] = None


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
            "correct_answer": question.answer if current_user.role != "student" or submission.status == "graded" else None,
            "score": ans.score,
            "is_correct": ans.is_correct,
        })

    return result