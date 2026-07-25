"""在线考试系统 API"""
import csv
import io
import json
import os
import uuid
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import Exam, Question, ExamSubmission, Answer, RegisteredPerson, Classroom, Student, Notification

router = APIRouter(prefix="/api/exams", tags=["exams"])

# 答案图片上传目录
ANSWER_UPLOAD_DIR = "uploads/exam_answers"


# ===== Pydantic 模型 =====
class QuestionCreate(BaseModel):
    type: str  # single/multi/judge/fill/essay
    content: str
    options: Optional[list[str]] = None  # 选择题选项
    answer: str
    score: float = 10.0
    knowledge_points: Optional[list[str]] = None  # 知识点标签


class ExamCreate(BaseModel):
    title: str
    description: str = ""
    classroom_id: Optional[int] = None
    duration: int = 60
    total_score: float = 100.0
    exam_type: str = "computer"  # computer(机试)/paper(笔试)
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
    exam_type: str = "computer"
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
    knowledge_points: Optional[list[str]] = None

    class Config:
        from_attributes = True


class ExamDetailOut(ExamOut):
    questions: list[QuestionOut]


class AnswerSubmit(BaseModel):
    question_id: int
    content: str = ""
    image_urls: list[str] = []  # 图片URL列表


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
def _normalize_choice_answer(answer: str, option_count: int = 0) -> str:
    """将选择题答案统一为索引格式（"0","1","2"...）
    
    兼容多种格式：
    - 字母格式: "A","B","C","D" → "0","1","2","3"
    - 索引格式: "0","1","2","3" → 不变
    - 1-based: "1","2","3","4" → "0","1","2","3"（仅当 option_count 可用时）
    """
    a = answer.strip()
    if not a:
        return a
    # 单个字母 A-Z → 转为索引
    if len(a) == 1 and a.isalpha() and a.isupper():
        idx = ord(a) - ord('A')
        return str(idx)
    return a


def auto_grade(question: Question, answer_content: str) -> tuple[float, bool]:
    """自动评判题目"""
    if question.type == "single":
        # 单选题：兼容字母格式（A/B/C/D）和索引格式（0/1/2/3）
        student = _normalize_choice_answer(answer_content)
        correct = _normalize_choice_answer(question.answer or "", len(question.options or []))
        is_correct = student == correct
        return (question.score if is_correct else 0), is_correct
    
    elif question.type == "multi":
        # 多选题：兼容字母格式和索引格式
        student_parts = set(_normalize_choice_answer(a) for a in answer_content.split(",") if a.strip())
        correct_parts = set(_normalize_choice_answer(a) for a in (question.answer or "").split(",") if a.strip())
        is_correct = student_parts == correct_parts
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
    
    if current_user.role == "teacher":
        query = query.filter(Exam.teacher_id == current_user.id)
    # admin 可以看到所有考试
    elif current_user.role == "student":
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
            exam_type=getattr(exam, 'exam_type', 'computer'),
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
        exam_type=data.exam_type,
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
            knowledge_points=json.dumps(q.knowledge_points) if q.knowledge_points else None,
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
        exam_type=getattr(exam, 'exam_type', 'computer'),
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
                knowledge_points=json.loads(q.knowledge_points) if q.knowledge_points else None,
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
            exam_type=getattr(exam, 'exam_type', 'computer'),
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
        exam_type=getattr(exam, 'exam_type', 'computer'),
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
                knowledge_points=json.loads(q.knowledge_points) if q.knowledge_points else None,
            ) for q in exam.questions
        ],
    )


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
        knowledge_points=json.dumps(data.knowledge_points) if data.knowledge_points else None,
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
        "knowledge_points": json.loads(question.knowledge_points) if question.knowledge_points else None,
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
            "image_urls": json.loads(ans.image_urls) if ans.image_urls else [],
            "correct_answer": question.answer if current_user.role != "student" or submission.status == "graded" else None,
            "score": ans.score,
            "is_correct": ans.is_correct,
        })

    return result


# ===== 考试报告 =====

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
        import logging
        logging.getLogger("exam").warning(f"AI 报告生成失败: {e}")
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


# ============================================================
# AI 批改相关接口
# ============================================================


def _is_subjective_answer(ans: Answer, question: Question) -> bool:
    """判断是否为主观题答案（essay 或 fill 带图）"""
    if question.type == "essay":
        return True
    if question.type == "fill" and ans.image_urls:
        try:
            urls = json.loads(ans.image_urls)
            return bool(urls)
        except (json.JSONDecodeError, TypeError):
            return False
    return False


def _check_submission_completion(db: Session, submission: ExamSubmission):
    """检查 submission 的所有主观题是否都已确认，如是则锁定为 graded"""
    subjective_answers = []
    for ans in submission.answers:
        q = ans.question
        if q and _is_subjective_answer(ans, q):
            subjective_answers.append(ans)

    if not subjective_answers:
        return  # 没有主观题，无需处理

    all_confirmed = all(a.teacher_confirmed for a in subjective_answers)
    if all_confirmed:
        # 计算最终分数：客观题 score + 主观题 teacher_score（或 ai_score 兜底）
        total = 0.0
        for ans in submission.answers:
            q = ans.question
            if not q:
                continue
            if _is_subjective_answer(ans, q):
                # 主观题：优先 teacher_score，其次 ai_score
                total += ans.teacher_score if ans.teacher_score is not None else (ans.ai_score or 0)
            else:
                # 客观题：直接用 score
                total += ans.score or 0
        submission.score = total
        submission.status = "graded"
        submission.graded_at = datetime.now()
        db.commit()


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


class ConfirmAnswerRequest(BaseModel):
    teacher_score: Optional[float] = None
    teacher_comment: Optional[str] = None
    adopt_ai_score: bool = False  # True 时忽略 teacher_score，直接采用 ai_score


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


class ConfirmBatchRequest(BaseModel):
    answer_ids: list[int]
    adopt_ai_score: bool = True  # 默认采用 AI 分
    teacher_scores: Optional[dict[int, float]] = None  # adopt_ai_score=False 时使用


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


class ReviewSubmitItem(BaseModel):
    answer_id: int
    teacher_score: float
    teacher_comment: Optional[str] = None


class ReviewSubmitRequest(BaseModel):
    items: list[ReviewSubmitItem]


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
            _check_submission_completion(db, sub)

    return {
        "success": True,
        "confirmed_count": len(data.items),
        "affected_submissions": len(affected_submission_ids),
    }


# ============================================================
# 扩展功能：导出审核报告 + 审核统计仪表盘 + 批量操作增强
# ============================================================


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


class BatchSelectConfirmRequest(BaseModel):
    """批量选择确认请求：支持按题目/按提交/按状态筛选"""
    mode: str = "question"  # question=按题目, submission=按提交, status=按状态
    question_id: Optional[int] = None  # mode=question 时使用
    submission_id: Optional[int] = None  # mode=submission 时使用
    status_filter: Optional[str] = None  # mode=status 时: needs_review / unconfirmed / all
    adopt_ai_score: bool = True
    teacher_scores: Optional[dict[int, float]] = None


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
            _check_submission_completion(db, sub)

    return {
        "success": True,
        "confirmed_count": confirmed_count,
        "affected_submissions": len(affected_submission_ids),
        "mode": data.mode,
    }