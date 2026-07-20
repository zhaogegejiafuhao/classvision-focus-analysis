"""相似题生成 API"""
import json
import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import RegisteredPerson, SimilarQuestion, Classroom, Student
from backend.models.schemas import SimilarQuestionRequest, SimilarQuestionResponse, SimilarQuestionSubmitRequest

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/similar-questions", tags=["similar-questions"])


def _assert_can_access_student(current_user: RegisteredPerson, student_id: int, db: Session) -> None:
    """校验当前用户是否有权访问指定学生的数据。

    - admin：始终通过
    - student：仅能访问自己
    - teacher：学生必须在自己的课堂中
    """
    if current_user.role == "admin":
        return
    if current_user.role == "student":
        if student_id != current_user.id:
            raise HTTPException(403, "无权访问该学生的数据")
        return
    # teacher：学生必须在该教师所辖课堂中
    my_classroom_ids = {c.id for c in db.query(Classroom).filter(Classroom.teacher_person_id == current_user.id).all()}
    if not my_classroom_ids:
        raise HTTPException(403, "无权访问该学生的数据")
    student_in_my_class = (
        db.query(Student)
        .filter(Student.person_id == student_id, Student.classroom_id.in_(my_classroom_ids))
        .first()
    )
    if not student_in_my_class:
        raise HTTPException(403, "无权访问该学生的数据")


@router.post("/generate", response_model=SimilarQuestionResponse)
async def generate_similar_questions(
    data: SimilarQuestionRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """生成相似练习题（不持久化）"""
    try:
        from backend.services.similar_question import similar_question_service
        result = await similar_question_service.generate_similar_questions(
            question=data.question,
            knowledge_points=data.knowledge_points,
            error_type=data.error_type,
            tier=data.tier,
            count=data.count,
            standard_answer=data.standard_answer,
        )
        return SimilarQuestionResponse(questions=result)
    except Exception as e:
        logger.error(f"相似题生成失败: {e}")
        raise HTTPException(500, f"相似题生成失败: {e}")


@router.get("/list")
def list_similar_questions(
    student_id: int | None = None,
    status: str | None = None,
    page: int = 1,
    page_size: int = 20,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """已持久化相似题列表

    - 学生角色：只能看自己的
    - 教师：可通过 student_id 指定本课堂学生，否则返回本课堂所有学生
    - 管理员：可查看任意
    - status: pending/passed/failed，不传则返回全部
    """
    if current_user.role == "student":
        target_student_id = current_user.id
    elif current_user.role == "teacher":
        # 教师指定了 student_id，需校验该学生属于自己课堂
        if student_id is not None:
            _assert_can_access_student(current_user, student_id, db)
            target_student_id = student_id
        else:
            target_student_id = None  # 稍后用课堂过滤
    else:
        target_student_id = student_id or current_user.id

    query = db.query(SimilarQuestion)
    if target_student_id is not None:
        query = query.filter(SimilarQuestion.student_id == target_student_id)
    elif current_user.role == "teacher":
        # 教师未指定 student_id：只显示本课堂学生的相似题
        my_classroom_ids = {c.id for c in db.query(Classroom).filter(Classroom.teacher_person_id == current_user.id).all()}
        my_student_ids = {s.person_id for s in db.query(Student).filter(Student.classroom_id.in_(my_classroom_ids)).all() if s.person_id}
        if my_student_ids:
            query = query.filter(SimilarQuestion.student_id.in_(my_student_ids))
        else:
            query = query.filter(SimilarQuestion.student_id == -1)  # 无学生，返回空

    if status:
        query = query.filter(SimilarQuestion.mastery_status == status)

    total = query.count()
    offset = (page - 1) * page_size
    rows = (
        query.order_by(SimilarQuestion.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    items = []
    for sq in rows:
        items.append({
            "similar_id": sq.id,
            "student_id": sq.student_id,
            "source_grading_id": sq.source_grading_id,
            "question_text": sq.question_text,
            "standard_answer": sq.standard_answer,
            "difficulty": sq.difficulty,
            "variant_type": sq.variant_type,
            "tier": sq.tier,
            "mastery_status": sq.mastery_status,
            "created_at": sq.created_at,
        })

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": items,
    }


@router.post("/{similar_id}/submit")
async def submit_similar_answer(
    similar_id: int,
    data: SimilarQuestionSubmitRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """相似题练习提交：自动批改并更新 mastery_status

    逻辑：取 SimilarQuestion → 用 rubric_suggestion 调 grading_service.grade_math →
    score >= max_score * 0.8 判 passed → 更新 mastery_status/student_answer/practice_score/practiced_at
    """
    sq = db.query(SimilarQuestion).filter(SimilarQuestion.id == similar_id).first()
    if not sq:
        raise HTTPException(404, "相似题不存在")

    # 归属校验：学生仅操作自己的，教师仅操作本课堂学生的
    _assert_can_access_student(current_user, sq.student_id, db)

    if not data.answer_text.strip():
        raise HTTPException(400, "答案不能为空")

    # 解析 rubric_suggestion
    rubric = None
    if sq.rubric_suggestion:
        try:
            rubric = json.loads(sq.rubric_suggestion)
        except Exception:
            rubric = None

    # 调用批改服务
    from backend.services.grader import grading_service
    try:
        max_score = 10  # 默认满分10分
        if rubric and isinstance(rubric, dict) and "steps" in rubric:
            max_score = sum(s.get("score", 0) for s in rubric["steps"])
            if max_score <= 0:
                max_score = 10

        result = await grading_service.grade_math(
            question=sq.question_text,
            standard_answer=sq.standard_answer,
            student_answer_ocr=data.answer_text,
            total_score=max_score,
            rubric=rubric,
        )
        score = result.get("suggested_score", 0) or result.get("grading", {}).get("total_score", 0)
        grading_data = result.get("grading", {})
        comment = result.get("comment", "")
    except Exception as e:
        logger.error(f"相似题批改失败: {e}")
        score = 0
        grading_data = {}
        comment = f"批改失败: {type(e).__name__}"

    # 判断掌握状态
    mastery = "passed" if score >= max_score * 0.8 else "failed"

    # 更新记录
    sq.student_answer = data.answer_text
    sq.practice_score = score
    sq.mastery_status = mastery
    sq.practiced_at = datetime.now()

    # 回写 KnowledgeAnalysis.correction_status_json（知识点掌握反馈）
    _update_knowledge_mastery(sq, db)

    db.commit()

    logger.info(f"[similar-submit] id={similar_id}, score={score}/{max_score}, mastery={mastery}")

    return {
        "similar_id": sq.id,
        "score": score,
        "max_score": max_score,
        "mastery_status": mastery,
        "grading": grading_data,
        "comment": comment,
    }


@router.get("/{similar_id}")
def get_similar_question(
    similar_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取单条已持久化相似题详情"""
    sq = db.query(SimilarQuestion).filter(SimilarQuestion.id == similar_id).first()
    if not sq:
        raise HTTPException(404, "相似题不存在")

    # 归属校验：学生仅访问自己的，教师仅访问本课堂学生的
    _assert_can_access_student(current_user, sq.student_id, db)

    rubric = None
    if sq.rubric_suggestion:
        try:
            rubric = json.loads(sq.rubric_suggestion)
        except Exception:
            rubric = None

    kp_ids = []
    if sq.knowledge_point_ids:
        try:
            kp_ids = json.loads(sq.knowledge_point_ids)
        except Exception:
            kp_ids = []

    return {
        "similar_id": sq.id,
        "student_id": sq.student_id,
        "source_grading_id": sq.source_grading_id,
        "question_text": sq.question_text,
        "standard_answer": sq.standard_answer,
        "rubric_suggestion": rubric,
        "difficulty": sq.difficulty,
        "variant_type": sq.variant_type,
        "tier": sq.tier,
        "knowledge_point_ids": kp_ids,
        "mastery_status": sq.mastery_status,
        "student_answer": sq.student_answer,
        "practice_score": sq.practice_score,
        "created_at": sq.created_at,
        "practiced_at": sq.practiced_at,
    }


@router.get("/model-router/stats")
def get_model_router_stats(
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """获取模型路由统计"""
    from backend.services.model_router import model_router
    return model_router.get_performance_stats()


def _update_knowledge_mastery(sq: SimilarQuestion, db: Session):
    """相似题练习结果回写 KnowledgeAnalysis.correction_status_json

    逻辑：查找该学生最近的 KnowledgeAnalysis，在 correction_status 中
    更新相关知识点的订正状态。
    """
    from backend.models.tables import KnowledgeAnalysis

    ka = (
        db.query(KnowledgeAnalysis)
        .filter(
            KnowledgeAnalysis.student_id == sq.student_id,
            KnowledgeAnalysis.analysis_type == "math",
        )
        .order_by(KnowledgeAnalysis.created_at.desc())
        .first()
    )
    if not ka:
        return

    # 解析 correction_status_json
    try:
        correction_status = json.loads(ka.correction_status_json) if ka.correction_status_json else {}
    except Exception:
        correction_status = {}

    # 更新相关知识点
    kp_ids = []
    if sq.knowledge_point_ids:
        try:
            kp_ids = json.loads(sq.knowledge_point_ids)
        except Exception:
            kp_ids = []

    for kp in kp_ids:
        if kp in correction_status:
            if sq.mastery_status == "passed":
                correction_status[kp] = "mastered"
            elif correction_status.get(kp) != "mastered":
                correction_status[kp] = "practicing"

    # 写回
    ka.correction_status_json = json.dumps(correction_status, ensure_ascii=False)
