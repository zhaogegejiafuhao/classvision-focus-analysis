"""在线考试系统 API —— 核心 CRUD 与题目管理

已拆分到子模块（共用 prefix `/api/exams`）：
- exam_submission_routes.py    学生提交 / 批改流程
- exam_stats_report_routes.py  统计 / 报告 / 导出
- exam_ai_grading_routes.py    AI 批改进度 / 确认
- exam_schemas.py              Pydantic 模型
- exam_service.py              共享业务逻辑（auto_grade / is_subjective_answer / ...）

本文件保留：考试 CRUD、题目增删、提交列表查询。
"""
import json
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import (
    Answer, Exam, ExamSubmission, Question, RegisteredPerson, Student,
)
from backend.api.exam_schemas import (
    ExamCreate, ExamDetailOut, ExamOut, QuestionCreate, QuestionOut, SubmissionOut,
)

router = APIRouter(prefix="/api/exams", tags=["exams"])


# ===== 教师端：考试列表 =====
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


# ===== 教师端：创建考试 =====
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


# ===== 学生端：分配给我的考试（必须在 /{exam_id} 之前定义，避免路径冲突）=====
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


# ===== 考试详情 =====
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


# ===== 删除考试 =====
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


# ===== 关闭考试 =====
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


# ===== 题目管理：新增 =====
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


# ===== 题目管理：删除 =====
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


# ===== 教师端：考试提交列表 =====
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
