"""相似题生成 API"""
import logging
from fastapi import APIRouter, Depends, HTTPException

from backend.core.security import get_current_user
from backend.models.tables import RegisteredPerson
from backend.models.schemas import SimilarQuestionRequest, SimilarQuestionResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/similar-questions", tags=["similar-questions"])


@router.post("/generate", response_model=SimilarQuestionResponse)
async def generate_similar_questions(
    data: SimilarQuestionRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """生成相似练习题"""
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


@router.get("/model-router/stats")
def get_model_router_stats(
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """获取模型路由统计"""
    from backend.services.model_router import model_router
    return model_router.get_performance_stats()
