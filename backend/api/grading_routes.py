"""AI智能批改 API"""
import json
import base64
import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user
from backend.models.tables import RegisteredPerson, HomeworkSubmission, GradingResult
from backend.models.schemas import AIGradeRequest, AIGradeResponse, GradingResultOut, GradeConfirmRequest
from backend.services.grader import grading_service
from backend.services.ocr import ocr_service
from backend.services.model_router import model_router

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/grading", tags=["grading"])


@router.post("/grade", response_model=AIGradeResponse)
async def ai_grade(
    data: AIGradeRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """AI批改单题（数学/作文）

    学生答案来源优先级：image_base64 (OCR) > student_text > submission.content
    submission_id 可选：若不传则不持久化批改结果到数据库（用于临时批改场景）
    """
    # 如果提供了 submission_id，从数据库查询提交记录（用于持久化批改结果）
    submission = None
    if data.submission_id:
        submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == data.submission_id).first()
        if not submission:
            raise HTTPException(404, "提交不存在")

    # 学生答案来源：优先使用请求中的 student_text，其次用 submission.content
    student_answer = data.student_text or (submission.content if submission else "") or ""
    confidence = 0.85
    image_bytes = None

    if data.image_base64:
        try:
            image_bytes = base64.b64decode(data.image_base64)
            ocr_result = await ocr_service.recognize(image_bytes)
            if ocr_result and ocr_result.text:
                student_answer = ocr_result.text
                confidence = ocr_result.confidence
        except Exception as e:
            logger.warning(f"OCR识别失败: {e}")

    # 根据题型调用不同批改引擎
    try:
        if data.subject_type == "essay":
            result = await grading_service.grade_essay(
                question=data.question,
                standard_answer=data.standard_answer,
                student_answer_ocr=student_answer,
                total_score=int(data.total_score),
                confidence=confidence,
                image_bytes=image_bytes,
            )
        else:
            result = await grading_service.grade_math(
                question=data.question,
                standard_answer=data.standard_answer,
                student_answer_ocr=student_answer,
                total_score=int(data.total_score),
                confidence=confidence,
                image_bytes=image_bytes,
            )
    except Exception as e:
        logger.error(f"AI批改失败: {e}")
        raise HTTPException(500, f"AI批改失败: {e}")

    # 保存批改结果到数据库（仅当有 submission_id 时）
    if submission:
        grading_record = GradingResult(
            submission_id=data.submission_id,
            rubric_json=json.dumps(result.get("rubric"), ensure_ascii=False) if result.get("rubric") else None,
            grading_json=json.dumps(result.get("grading"), ensure_ascii=False) if result.get("grading") else None,
            score=result.get("suggested_score", 0),
            max_score=result.get("max_score", data.total_score),
            comment=result.get("comment", ""),
            model_key=result.get("model_key", "standard"),
            grading_method=result.get("grading", {}).get("grading_method", "llm"),
            confidence=result.get("confidence", 0.85),
            error_type=result.get("grading", {}).get("error_type"),
            error_cause=result.get("grading", {}).get("error_cause"),
            knowledge_points=json.dumps(result.get("grading", {}).get("knowledge_points", []), ensure_ascii=False),
        )
        db.add(grading_record)
        db.commit()
        db.refresh(grading_record)

    return AIGradeResponse(
        submission_id=data.submission_id or 0,
        suggested_score=result.get("suggested_score", 0),
        max_score=result.get("max_score", data.total_score),
        comment=result.get("comment", ""),
        rubric=result.get("rubric"),
        grading=result.get("grading"),
        model_key=result.get("model_key", "standard"),
        confidence=result.get("confidence", 0.85),
        grading_method=result.get("grading", {}).get("grading_method", "llm"),
        error_type=result.get("grading", {}).get("error_type"),
        error_cause=result.get("grading", {}).get("error_cause"),
        knowledge_points=result.get("grading", {}).get("knowledge_points", []),
    )


@router.post("/batch")
async def batch_grade(
    homework_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """批量批改作业的所有提交"""
    from backend.models.tables import Homework
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if not homework:
        raise HTTPException(404, "作业不存在")

    submissions = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.homework_id == homework_id
    ).all()

    results = []
    for sub in submissions:
        try:
            # 简化批量批改：使用提交内容直接批改
            result = await grading_service.grade_math(
                question=homework.title,
                standard_answer=homework.description,
                student_answer_ocr=sub.content or "",
                total_score=int(homework.total_score),
            )
            results.append({
                "submission_id": sub.id,
                "student_id": sub.student_id,
                "suggested_score": result.get("suggested_score", 0),
                "status": "success",
            })
        except Exception as e:
            results.append({
                "submission_id": sub.id,
                "student_id": sub.student_id,
                "error": str(e),
                "status": "failed",
            })

    return {"homework_id": homework_id, "results": results}


@router.get("/result/{submission_id}")
def get_grading_result(
    submission_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取批改结果"""
    result = db.query(GradingResult).filter(
        GradingResult.submission_id == submission_id
    ).order_by(GradingResult.created_at.desc()).first()
    if not result:
        raise HTTPException(404, "批改结果不存在")

    return {
        "id": result.id,
        "submission_id": result.submission_id,
        "score": result.score,
        "max_score": result.max_score,
        "comment": result.comment,
        "rubric": json.loads(result.rubric_json) if result.rubric_json else None,
        "grading": json.loads(result.grading_json) if result.grading_json else None,
        "model_key": result.model_key,
        "grading_method": result.grading_method,
        "confidence": result.confidence,
        "error_type": result.error_type,
        "error_cause": result.error_cause,
        "knowledge_points": json.loads(result.knowledge_points) if result.knowledge_points else [],
        "confirmed": result.confirmed,
        "confirmed_score": result.confirmed_score,
        "created_at": result.created_at.isoformat() if result.created_at else None,
    }


@router.post("/confirm/{result_id}")
def confirm_grading(
    result_id: int,
    data: GradeConfirmRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """教师确认/修正AI批改结果"""
    if current_user.role not in ("teacher", "admin"):
        raise HTTPException(403, "只有教师可以确认批改结果")

    result = db.query(GradingResult).filter(GradingResult.id == result_id).first()
    if not result:
        raise HTTPException(404, "批改结果不存在")

    result.confirmed = True
    if data.confirmed_score is not None:
        result.confirmed_score = data.confirmed_score
        # 记录教师修正反馈给模型路由器
        is_accurate = abs(data.confirmed_score - result.score) / max(result.max_score, 1) < 0.15
        model_router.record_feedback(
            model_id=result.model_key,
            question_type="calculation",
            was_corrected=not is_accurate,
        )

    db.commit()
    return {"message": "批改结果已确认", "confirmed_score": result.confirmed_score or result.score}


@router.post("/ocr")
async def ocr_recognize(
    data: dict,
    current_user: RegisteredPerson = Depends(get_current_user),
):
    """单独OCR识别"""
    image_base64 = data.get("image_base64", "")
    if not image_base64:
        raise HTTPException(400, "image_base64 不能为空")
    try:
        image_bytes = base64.b64decode(image_base64)
        result = await ocr_service.recognize(image_bytes)
        return {
            "text": result.text if result else "",
            "confidence": result.confidence if result else 0,
            "engine": ",".join(result.engines_used) if result and result.engines_used else "none",
        }
    except Exception as e:
        raise HTTPException(500, f"OCR识别失败: {e}")
