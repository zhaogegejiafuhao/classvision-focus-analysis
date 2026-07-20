"""相似题生成 API"""
import json
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import RegisteredPerson, SimilarQuestion
from backend.models.schemas import SimilarQuestionRequest, SimilarQuestionResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/similar-questions", tags=["similar-questions"])


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
    - 教师/管理员：可通过 student_id 指定学生
    - status: pending/passed/failed，不传则返回全部
    """
    if current_user.role == "student":
        target_student_id = current_user.id
    else:
        target_student_id = student_id or current_user.id

    query = db.query(SimilarQuestion).filter(SimilarQuestion.student_id == target_student_id)

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

    if current_user.role == "student" and sq.student_id != current_user.id:
        raise HTTPException(403, "无权访问该相似题")

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
