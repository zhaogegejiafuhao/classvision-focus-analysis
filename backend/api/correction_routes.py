"""订正闭环 API（从原 correction_routes.py 拆分）

拆分后的模块：
- correction_routes.py：订正提交、订正对比、个性化订正（订正闭环工作流）
- mistake_book_routes.py：错题列表、错题详情、相似题生成（错题本浏览与练习）

本模块包含：
- POST /api/correction/submit                  学生提交订正作业
- GET  /api/correction/comparison/{correction_id}  获取订正前后对比
- POST /api/correction/personalized             获取分层个性化订正任务
"""
import base64
import json
import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_owner_or_admin
from backend.models.tables import (
    CorrectionRecord,
    GradingResult,
    Homework,
    HomeworkSubmission,
    RegisteredPerson,
)
from backend.models.schemas import (
    CorrectionComparisonOut,
    CorrectionSubmitRequest,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/correction", tags=["correction"])


@router.post("/submit")
async def submit_correction(
    data: CorrectionSubmitRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """学生提交订正作业

    修复要点：
    - 从 Homework 表取原题目和标准答案（不再传空字符串给LLM）
    - 支持文本订正（text字段），不强制走OCR
    - 空答案快速短路（避免无效LLM调用）
    - 复用原批改的 rubric
    """
    # 获取原始批改结果
    original = db.query(GradingResult).filter(
        GradingResult.submission_id == data.submission_id
    ).order_by(GradingResult.created_at.desc()).first()

    if not original:
        raise HTTPException(404, "未找到原始批改结果")

    submission = db.query(HomeworkSubmission).filter(
        HomeworkSubmission.id == data.submission_id
    ).first()
    if not submission:
        raise HTTPException(404, "提交不存在")

    # IDOR 防护：学生只能订正自己的提交，教师只能订正自己作业下的提交，管理员可操作所有
    homework = db.query(Homework).filter(Homework.id == submission.homework_id).first()
    if current_user.role == "student":
        if submission.student_id != current_user.id:
            raise HTTPException(403, "无权订正他人的提交")
    elif current_user.role == "teacher":
        if homework and homework.teacher_id != current_user.id:
            raise HTTPException(403, "无权订正其他教师的作业")

    # 从 Homework 表取原题目和标准答案
    original_question = homework.title if homework else ""
    original_standard = homework.description if homework else ""

    # 收集订正文本（优先 text 字段，其次走 OCR）
    from backend.services.grader import grading_service
    from backend.services.ocr import ocr_service

    correction_texts = []
    for corr in data.corrections:
        # 优先使用文本字段（避免OCR开销）
        if corr.get("text"):
            correction_texts.append(corr["text"])
        elif corr.get("image_base64"):
            try:
                image_bytes = base64.b64decode(corr["image_base64"])
                ocr_result = await ocr_service.recognize(image_bytes)
                if ocr_result and ocr_result.text:
                    correction_texts.append(ocr_result.text)
            except Exception as e:
                logger.warning(f"订正OCR失败: {e}")

    correction_answer = "\n".join(correction_texts).strip() if correction_texts else ""

    # 空答案快速短路：直接0分，不调用LLM
    if not correction_answer:
        logger.warning(f"[Correction] 订正答案为空，submission_id={data.submission_id}，直接判0分")
        correction_record = CorrectionRecord(
            submission_id=data.submission_id,
            original_score=original.score,
            correction_score=0,
            improved=False,
            knowledge_update=json.dumps({"improved": False, "reason": "empty_correction"}, ensure_ascii=False),
        )
        db.add(correction_record)
        db.commit()
        db.refresh(correction_record)
        return {
            "correction_id": correction_record.id,
            "original_score": original.score,
            "correction_score": 0,
            "improved": False,
            "message": "订正答案为空，请补交后重新提交",
        }

    # 复用原 rubric，对订正答案重新批改
    try:
        rubric = json.loads(original.rubric_json) if original.rubric_json else None
        new_result = await grading_service.grade_math(
            question=original_question,
            standard_answer=original_standard,
            student_answer_ocr=correction_answer,
            total_score=int(original.max_score),
            rubric=rubric,
        )
        new_score = new_result.get("suggested_score", 0) or new_result.get("grading", {}).get("total_score", 0)
        logger.info(f"[Correction] 订正批改完成: original={original.score} new={new_score} improved={new_score > original.score}")
    except Exception as e:
        logger.error(f"订正批改失败: {type(e).__name__}: {e}")
        new_score = 0

    # 保存订正记录
    correction_record = CorrectionRecord(
        submission_id=data.submission_id,
        original_score=original.score,
        correction_score=new_score,
        improved=new_score > original.score,
        knowledge_update=json.dumps({"improved": new_score > original.score}, ensure_ascii=False),
    )
    db.add(correction_record)
    db.commit()
    db.refresh(correction_record)

    return {
        "correction_id": correction_record.id,
        "original_score": original.score,
        "correction_score": new_score,
        "improved": new_score > original.score,
    }


@router.get("/comparison/{correction_id}")
def get_correction_comparison(
    correction_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取订正前后对比"""
    record = db.query(CorrectionRecord).filter(CorrectionRecord.id == correction_id).first()
    if not record:
        raise HTTPException(404, "订正记录不存在")

    # IDOR 防护：验证当前用户有权访问该订正记录
    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == record.submission_id).first()
    if submission:
        if current_user.role == "student" and submission.student_id != current_user.id:
            raise HTTPException(403, "无权查看他人的订正记录")
        if current_user.role == "teacher":
            homework = db.query(Homework).filter(Homework.id == submission.homework_id).first()
            if homework and homework.teacher_id != current_user.id:
                raise HTTPException(403, "无权查看其他教师的订正记录")

    return {
        "correction_id": record.id,
        "submission_id": record.submission_id,
        "original_score": record.original_score,
        "correction_score": record.correction_score,
        "improved": record.improved,
        "remaining_errors": json.loads(record.remaining_errors) if record.remaining_errors else [],
        "knowledge_update": json.loads(record.knowledge_update) if record.knowledge_update else {},
        "created_at": record.created_at.isoformat() if record.created_at else None,
    }


@router.post("/personalized")
def get_personalized_correction(
    student_id: int,
    analysis_type: str = "math",
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取分层个性化订正任务"""
    # IDOR 防护：学生只能查看自己的，教师只能查看自己作业下学生的，管理员可查看所有
    if current_user.role == "student":
        if student_id != current_user.id:
            raise HTTPException(403, "学生只能查看自己的个性化订正")
    elif current_user.role == "teacher":
        # 教师只能查看自己作业下提交的学生
        own_student_ids = {
            s.student_id for s in
            db.query(HomeworkSubmission).join(Homework, HomeworkSubmission.homework_id == Homework.id)
            .filter(Homework.teacher_id == current_user.id)
            .all()
        }
        if student_id not in own_student_ids:
            raise HTTPException(403, "无权查看该学生的个性化订正")

    from backend.services.correction import tier_classify, get_push_strategy
    from backend.models.tables import KnowledgeAnalysis

    # 获取最新分析
    analysis = db.query(KnowledgeAnalysis).filter(
        KnowledgeAnalysis.student_id == student_id,
        KnowledgeAnalysis.analysis_type == analysis_type,
    ).order_by(KnowledgeAnalysis.created_at.desc()).first()

    if not analysis:
        return {"student_id": student_id, "tier": "中等生", "tasks": []}

    weak_points = json.loads(analysis.weak_points_json) if analysis.weak_points_json else []

    # 将 weak_points list[dict] 转换为 tier_classify 所需的 dict[str, float] 格式
    weakness_scores = {}
    for wp in weak_points:
        if isinstance(wp, dict) and "knowledge_id" in wp and "weakness_score" in wp:
            weakness_scores[wp["knowledge_id"]] = wp["weakness_score"]

    tier_map = tier_classify(weakness_scores) if weakness_scores else {}

    # 取最常见的主导分层
    if tier_map:
        from collections import Counter
        tier_counter = Counter(tier_map.values())
        dominant_tier = tier_counter.most_common(1)[0][0]
    else:
        dominant_tier = "中等生"

    strategy = get_push_strategy(dominant_tier)

    return {
        "student_id": student_id,
        "tier": dominant_tier,
        "strategy": strategy,
        "weak_points": weak_points,
    }
