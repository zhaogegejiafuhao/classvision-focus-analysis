"""订正闭环 API"""
import json
import logging
import base64
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_owner_or_admin
from backend.models.tables import RegisteredPerson, GradingResult, CorrectionRecord, HomeworkSubmission, Homework, SimilarQuestion
from backend.models.schemas import (
    CorrectionSubmitRequest,
    CorrectionComparisonOut,
    MistakeListResponse,
    MistakeListItem,
    MistakeDetail,
    MistakeCorrectionRecord,
    GenerateSimilarRequest,
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


def _parse_kp_list(raw: str | None) -> list[str]:
    """安全解析 knowledge_points JSON 字段为 list[str]"""
    if not raw:
        return []
    try:
        v = json.loads(raw)
        if isinstance(v, list):
            return [str(x) for x in v]
        if isinstance(v, str):
            return [v]
    except Exception:
        pass
    return []


@router.get("/list")
def list_mistakes(
    student_id: int | None = None,
    kp: str | None = None,
    page: int = 1,
    page_size: int = 20,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    """错题本列表：从 GradingResult 筛选 error_type 非空的记录

    - 学生角色：强制只能看自己的错题（student_id 被忽略）
    - 教师/管理员：可通过 student_id 指定学生，缺省则取自己
    - kp：知识点关键词，对 knowledge_points JSON 做 LIKE 过滤
    - 分页：page 从 1 开始，page_size 默认 20
    """
    # 角色权限控制
    if current_user.role == "student":
        target_student_id = current_user.id
    else:
        target_student_id = student_id or current_user.id

    if not target_student_id:
        raise HTTPException(400, "缺少 student_id 参数")

    # 单次三表 JOIN 查询，避免 N+1
    query = (
        db.query(GradingResult, HomeworkSubmission, Homework)
        .join(HomeworkSubmission, GradingResult.submission_id == HomeworkSubmission.id)
        .outerjoin(Homework, HomeworkSubmission.homework_id == Homework.id)
        .filter(
            GradingResult.error_type.isnot(None),
            GradingResult.error_type != "none",
            HomeworkSubmission.student_id == target_student_id,
        )
    )

    # 知识点 LIKE 过滤（JSON 字符串内嵌套匹配）
    if kp:
        query = query.filter(GradingResult.knowledge_points.like(f'%"{kp}"%'))

    total = query.count()
    offset = (page - 1) * page_size
    rows = (
        query.order_by(GradingResult.created_at.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

    items: list[dict] = []
    for grading, submission, homework in rows:
        items.append(
            {
                "grading_id": grading.id,
                "submission_id": grading.submission_id,
                "score": grading.score,
                "max_score": grading.max_score,
                "error_type": grading.error_type,
                "error_cause": grading.error_cause,
                "knowledge_points": _parse_kp_list(grading.knowledge_points),
                "created_at": grading.created_at,
                "homework_id": homework.id if homework else None,
                "homework_title": homework.title if homework else "",
            }
        )

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": items,
    }


@router.get("/{grading_id}")
def get_mistake_detail(
    grading_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    """错题详情：聚合原题+标准答案+学生作答+批改详情+订正历史"""
    grading = db.query(GradingResult).filter(GradingResult.id == grading_id).first()
    if not grading:
        raise HTTPException(404, "批改记录不存在")

    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == grading.submission_id).first()
    if not submission:
        raise HTTPException(404, "提交记录不存在")

    # 学生只能看自己的错题
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权访问该错题")
    # IDOR 防护：教师只能查看自己作业下的错题
    if current_user.role == "teacher":
        hw = db.query(Homework).filter(Homework.id == submission.homework_id).first()
        if hw and hw.teacher_id != current_user.id:
            raise HTTPException(403, "无权访问其他教师的错题")

    homework = (
        db.query(Homework).filter(Homework.id == submission.homework_id).first()
        if submission.homework_id
        else None
    )

    # 订正历史（按时间倒序）
    correction_records = (
        db.query(CorrectionRecord)
        .filter(CorrectionRecord.submission_id == submission.id)
        .order_by(CorrectionRecord.created_at.desc())
        .all()
    )

    # 解析 JSON 字段
    try:
        rubric = json.loads(grading.rubric_json) if grading.rubric_json else None
    except Exception:
        rubric = None
    try:
        grading_data = json.loads(grading.grading_json) if grading.grading_json else None
    except Exception:
        grading_data = None

    return {
        "grading_id": grading.id,
        "submission_id": grading.submission_id,
        "homework_id": homework.id if homework else None,
        "homework_title": homework.title if homework else "",
        "question_text": homework.title if homework else "",
        "standard_answer": homework.description if homework else "",
        "student_answer_ocr": submission.content or "",
        "rubric": rubric,
        "grading": grading_data,
        "score": grading.score,
        "max_score": grading.max_score,
        "comment": grading.comment or "",
        "error_type": grading.error_type,
        "error_cause": grading.error_cause,
        "knowledge_points": _parse_kp_list(grading.knowledge_points),
        "created_at": grading.created_at,
        "correction_records": [
            {
                "correction_id": cr.id,
                "correction_score": cr.correction_score,
                "original_score": cr.original_score,
                "improved": cr.improved,
                "created_at": cr.created_at,
            }
            for cr in correction_records
        ],
    }


@router.post("/{grading_id}/generate-similar")
async def generate_similar_from_mistake(
    grading_id: int,
    data: GenerateSimilarRequest,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """从错题一键生成相似题并持久化

    取 GradingResult → Homework 题目/标准答案 → knowledge_points →
    调 similar_question_service 生成 → 批量插入 SimilarQuestion
    """
    grading = db.query(GradingResult).filter(GradingResult.id == grading_id).first()
    if not grading:
        raise HTTPException(404, "批改记录不存在")

    submission = db.query(HomeworkSubmission).filter(HomeworkSubmission.id == grading.submission_id).first()
    if not submission:
        raise HTTPException(404, "提交记录不存在")

    # 学生只能给自己的错题生成
    if current_user.role == "student" and submission.student_id != current_user.id:
        raise HTTPException(403, "无权操作该错题")
    # IDOR 防护：教师只能给自己作业下的错题生成相似题
    if current_user.role == "teacher":
        hw = db.query(Homework).filter(Homework.id == submission.homework_id).first()
        if hw and hw.teacher_id != current_user.id:
            raise HTTPException(403, "无权操作其他教师的错题")

    # 确定目标学生
    target_student_id = submission.student_id or current_user.id

    # 取原题信息
    homework = db.query(Homework).filter(Homework.id == submission.homework_id).first() if submission.homework_id else None
    question_text = homework.title if homework else ""
    standard_answer = homework.description if homework else ""
    knowledge_points = _parse_kp_list(grading.knowledge_points)

    # 知识点标准化：用 ErrorMapper 映射到标准节点 ID
    knowledge_point_ids = []
    if knowledge_points:
        try:
            from backend.services.attribution import ErrorMapper
            mapper = ErrorMapper()
            for kp_text in knowledge_points:
                ids = await mapper.map_error(kp_text)
                knowledge_point_ids.extend(ids)
            knowledge_point_ids = list(set(knowledge_point_ids))  # 去重
        except Exception as e:
            logger.warning(f"ErrorMapper 标准化失败: {e}, 使用原始知识点")

    # 调用相似题服务
    from backend.services.similar_question import similar_question_service
    generated = await similar_question_service.generate_similar_questions(
        question=question_text,
        knowledge_points=knowledge_points,
        error_type=grading.error_type or "",
        tier=data.tier,
        count=data.count,
        standard_answer=standard_answer,
        knowledge_point_ids=knowledge_point_ids,
    )

    # 持久化
    persisted_items = []
    for q in generated:
        sq = SimilarQuestion(
            student_id=target_student_id,
            source_grading_id=grading_id,
            question_text=q.get("question_text", ""),
            standard_answer=q.get("standard_answer", ""),
            rubric_suggestion=json.dumps(q.get("rubric_suggestion", {}), ensure_ascii=False) if q.get("rubric_suggestion") else None,
            difficulty=q.get("difficulty", "中等"),
            variant_type=q.get("variant_type", "同类变式"),
            tier=data.tier,
            knowledge_point_ids=json.dumps(knowledge_point_ids or knowledge_points, ensure_ascii=False) if (knowledge_point_ids or knowledge_points) else None,
            mastery_status="pending",
        )
        db.add(sq)
        db.flush()  # 获取 id
        persisted_items.append({
            "similar_id": sq.id,
            "question_text": sq.question_text,
            "variant_type": sq.variant_type,
        })

    db.commit()

    logger.info(f"[generate-similar] grading_id={grading_id}, generated={len(persisted_items)}")

    return {
        "generated": len(persisted_items),
        "items": persisted_items,
    }
