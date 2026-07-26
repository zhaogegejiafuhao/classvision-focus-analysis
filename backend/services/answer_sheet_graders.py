"""答题卡单题批改函数（从 answer_sheet.py 抽取）

按 region_type 分发的三个独立批改函数：
- grade_bubble_question: 单选/多选/判断题（气泡检测 → 精细化判分）
- grade_fill_question:   填空题（OCR + 规范化 + 精确/模糊匹配）
- grade_essay_question:  大题/作文（OCR + LLM 智能批改）

这三个函数原为 AnswerSheetOrchestrator 的方法，但均不使用 self，
故抽取为模块级 async 函数，降低编排器复杂度。
"""
from __future__ import annotations

import logging
from typing import Optional

from backend.models.tables import Question
from backend.services.paper_template import QuestionRegionImage
from backend.services.answer_sheet_models import QuestionResult
from backend.services.answer_sheet_text_utils import (
    _normalize_fill_text,
    _levenshtein_similarity,
    _is_essay_question,
)
from cv_engine.detectors.answer_card_detector import answer_card_detector, AnswerCardResult

logger = logging.getLogger(__name__)


async def grade_bubble_question(
    question: Question, region: QuestionRegionImage
) -> QuestionResult:
    """单选/多选/判断题：答题卡气泡检测 → 转 content → 精细化判分

    Phase 4-3 改进：
    1. 单选题多涂判错（多涂 → 0 分，避免误取第一个）
    2. 判断题多涂判错（同上）
    3. 多选题部分分：
       - 完全相等 → 满分
       - 少选但不错选（student ⊂ correct）→ 按比例给半分（ratio × 0.5 × 满分）
       - 错选/多选/未填涂 → 0 分
    4. 置信度基于相关气泡的"决策清晰度"（替代固定 0.9）：
       - 同时存在已填涂与未填涂气泡时，取 (已填涂均值 + (1-未填涂均值)) / 2
       - 仅已填涂/仅未填涂时取对应均值或其补
       - 无气泡时降级为 0.5

    复用：
    - answer_card_detector.detect()  (cv_engine/detectors/answer_card_detector.py)
    - auto_grade()  (backend/services/exam_service.py)，仅在单选/判断的正常分支调用
    """
    from backend.services.exam_service import auto_grade

    # 调用气泡检测器（标准模板）
    detect_result: AnswerCardResult = answer_card_detector.detect(
        region.image_bytes, template_type="standard_5x10x4"
    )

    if detect_result.error:
        return QuestionResult(
            question_id=question.id,
            question_type=question.type,
            question_content=question.content[:80],
            region_type="bubble",
            student_answer="",
            standard_answer=question.answer,
            score=0,
            max_score=question.score,
            is_correct=None,
            error=f"气泡检测失败: {detect_result.error}",
        )

    # 从检测结果中提取该题的答案
    # detect_result.answers: {question_index: [option_indices]}
    # 由于每个 region 只切分了一道题，取第一个非空题的答案
    student_options: list[int] = []
    question_index: Optional[int] = None
    if detect_result.answers:
        question_index = sorted(detect_result.answers.keys())[0]
        student_options = list(detect_result.answers[question_index])

    # ============ Phase 4-3-4：基于 fill_ratio 计算识别置信度 ============
    if question_index is not None:
        related_bubbles = [b for b in detect_result.bubbles if b.question_index == question_index]
    else:
        related_bubbles = list(detect_result.bubbles)  # 兜底：使用全部气泡

    filled_ratios = [b.fill_ratio for b in related_bubbles if b.filled]
    unfilled_ratios = [b.fill_ratio for b in related_bubbles if not b.filled]
    if filled_ratios and unfilled_ratios:
        # 决策最清晰：已填涂高、未填涂低，平均之
        confidence = (sum(filled_ratios) / len(filled_ratios)
                      + (1 - sum(unfilled_ratios) / len(unfilled_ratios))) / 2
    elif filled_ratios:
        confidence = sum(filled_ratios) / len(filled_ratios)
    elif unfilled_ratios:
        confidence = 1 - sum(unfilled_ratios) / len(unfilled_ratios)
    else:
        confidence = 0.5
    confidence = max(0.0, min(1.0, confidence))

    avg_fill_ratio = (
        sum(b.fill_ratio for b in related_bubbles) / len(related_bubbles)
        if related_bubbles else 0.0
    )

    # ============ Phase 4-3：精细化判分 ============
    # 单选题：多涂判错；空答判错；正常调 auto_grade
    if question.type == "single":
        if len(student_options) > 1:
            content = ",".join(str(o) for o in student_options)
            score, is_correct, comment = 0.0, False, f"单选题多涂（{len(student_options)} 个选项），判错"
        elif not student_options:
            content, score, is_correct, comment = "", 0.0, False, "未填涂"
        else:
            content = str(student_options[0])
            score, is_correct = auto_grade(question, content)
            comment = ""

    # 判断题：多涂判错；空答判错；正常映射 0=true / 1=false 后调 auto_grade
    elif question.type == "judge":
        if len(student_options) > 1:
            content = ",".join(str(o) for o in student_options)
            score, is_correct, comment = 0.0, False, f"判断题多涂（{len(student_options)} 个选项），判错"
        elif not student_options:
            content, score, is_correct, comment = "", 0.0, False, "未填涂"
        else:
            # 选项 0 = true，选项 1 = false（如需调整可读取 Question.answer 前缀映射）
            content = "true" if student_options[0] == 0 else "false"
            score, is_correct = auto_grade(question, content)
            comment = ""

    # 多选题：完全相等满分；少选但不错选按比例给半分；其他 0 分
    else:  # multi
        content = ",".join(str(o) for o in student_options)
        try:
            student_set = set(student_options)
            correct_set = set(int(a.strip()) for a in (question.answer or "").split(",") if a.strip())
        except (ValueError, AttributeError):
            student_set, correct_set = set(student_options), set()

        if not student_set:
            score, is_correct, comment = 0.0, False, "未填涂"
        elif student_set == correct_set:
            score, is_correct, comment = float(question.score), True, ""
        elif student_set < correct_set and correct_set:
            # 少选但不错选：ratio × 0.5 × 满分（如满分2选对1/2 → 0.5分）
            ratio = len(student_set) / len(correct_set)
            score = round(float(question.score) * ratio * 0.5, 2)
            is_correct = False
            comment = f"少选（选对 {len(student_set)}/{len(correct_set)}），给 {round(ratio * 50)}% 部分分"
        else:
            wrong = sorted(student_set - correct_set)
            score, is_correct, comment = 0.0, False, f"错选/多选选项 {wrong}，0 分"

    return QuestionResult(
        question_id=question.id,
        question_type=question.type,
        question_content=question.content[:80],
        region_type="bubble",
        student_answer=content,
        standard_answer=question.answer,
        score=score,
        max_score=question.score,
        is_correct=is_correct,
        confidence=round(confidence, 3),
        comment=comment,
        grading_detail={
            "bubbles_detected": len(detect_result.bubbles),
            "bubbles_filled": sum(1 for b in detect_result.bubbles if b.filled),
            "skew_angle": detect_result.skew_angle,
            "avg_fill_ratio": round(avg_fill_ratio, 3),
            "student_options": student_options,
            "debug_image_b64": detect_result.debug_image_b64,
        },
    )


async def grade_fill_question(
    question: Question, region: QuestionRegionImage
) -> QuestionResult:
    """填空题：OCR 识别 + 字符串规范化 + 精确匹配 + 模糊匹配二次确认

    Phase 2 实现：
    1. 调 ocr_service.recognize(region.image_bytes) 获取学生答案文本 + 置信度
    2. 文本规范化（去空白/换行、全角转半角、统一大小写、去首尾标点）
    3. 调 auto_grade(question, normalized_text) fill 分支做精确匹配
    4. 若判错且 confidence > 0.85，做 Levenshtein 相似度二次确认（>=0.85 视为正确）
    5. 若 confidence < 0.4 或 needs_manual_input，标记为"需人工复核"
    """
    # 1. OCR 识别
    try:
        from backend.services.ocr import ocr_service
        ocr_result = await ocr_service.recognize(region.image_bytes)
    except Exception as e:
        logger.exception(f"[AnswerSheet] 填空题 {question.id} OCR 异常: {e}")
        return QuestionResult(
            question_id=question.id,
            question_type=question.type,
            question_content=question.content[:80],
            region_type="fill",
            student_answer="",
            standard_answer=question.answer,
            score=0,
            max_score=question.score,
            is_correct=None,
            confidence=0.0,
            error=f"OCR 调用失败: {type(e).__name__}: {e}",
        )

    raw_text = ocr_result.text or ""
    confidence = float(ocr_result.confidence or 0.0)

    # 2. 文本规范化
    normalized = _normalize_fill_text(raw_text)
    standard_normalized = _normalize_fill_text(question.answer or "")

    # 3. needs_manual_input 处理
    if ocr_result.needs_manual_input or confidence < 0.4 or not normalized:
        return QuestionResult(
            question_id=question.id,
            question_type=question.type,
            question_content=question.content[:80],
            region_type="fill",
            student_answer=raw_text,
            standard_answer=question.answer,
            score=0,
            max_score=question.score,
            is_correct=None,
            confidence=confidence,
            ocr_text=raw_text,
            comment="OCR 置信度过低或识别失败，需人工复核",
            error="OCR 低置信度" if confidence < 0.4 else "OCR 双引擎均失败",
        )

    # 4. 填空题判分（A+B 方案：多空拆分 + 数值/单位容差）
    from backend.services.fill_grader import grade_fill_answer
    score, is_correct, fill_detail = grade_fill_answer(
        normalized, question.answer or "", float(question.score)
    )

    # 5. 模糊匹配二次确认（仅当判错且 OCR 置信度较高时；仅单空场景适用）
    # 多空场景下整体字符串的 Levenshtein 相似度意义不大，跳过
    fuzzy_matched = False
    fuzzy_similarity = 0.0
    if (not is_correct
            and confidence > 0.85
            and standard_normalized
            and not fill_detail.get("is_multi_blank")):
        fuzzy_similarity = _levenshtein_similarity(normalized, standard_normalized)
        if fuzzy_similarity >= 0.85:
            # 模糊匹配视为正确
            score = float(question.score)
            is_correct = True
            fuzzy_matched = True

    # 6. 构建评语
    comment_parts = []
    if is_correct:
        if fuzzy_matched:
            comment_parts.append(f"答案基本正确（相似度 {fuzzy_similarity:.2f}，模糊匹配通过）")
        elif fill_detail.get("is_multi_blank"):
            comment_parts.append(
                f"多空全对（{fill_detail['correct_count']}/{fill_detail['blank_count']} 空）"
            )
        else:
            method = fill_detail["per_blank"][0]["method"] if fill_detail.get("per_blank") else "exact"
            method_zh = {"exact": "精确匹配", "numeric": "数值相等", "unit": "单位等价"}.get(method, "匹配")
            comment_parts.append(f"答案正确（{method_zh}）")
    else:
        if fill_detail.get("is_multi_blank"):
            comment_parts.append(
                f"多空部分对（{fill_detail['correct_count']}/{fill_detail['blank_count']} 空，"
                f"得 {score}/{question.score} 分）"
            )
        else:
            comment_parts.append(f"答案错误（OCR 置信度 {confidence:.2f}，相似度 {fuzzy_similarity:.2f}）")
    if confidence < 0.7:
        comment_parts.append("OCR 置信度偏低，建议人工复核")

    return QuestionResult(
        question_id=question.id,
        question_type=question.type,
        question_content=question.content[:80],
        region_type="fill",
        student_answer=normalized,
        standard_answer=question.answer,
        score=score,
        max_score=question.score,
        is_correct=is_correct,
        confidence=confidence,
        ocr_text=raw_text,
        comment="；".join(comment_parts),
        grading_detail={
            "ocr_engines": ocr_result.engines_used,
            "ocr_confidence": round(confidence, 3),
            "fuzzy_similarity": round(fuzzy_similarity, 3),
            "fuzzy_matched": fuzzy_matched,
            "normalized_student": normalized,
            "normalized_standard": standard_normalized,
            "fill_grading": fill_detail,
        },
    )


async def grade_essay_question(
    question: Question, region: QuestionRegionImage
) -> QuestionResult:
    """大题/作文：OCR + LLM 智能批改（Phase 3 实现）

    流程：
    1. 调 ocr_service.recognize(region.image_bytes) 获取学生答案文本 + 置信度
    2. 根据 _is_essay_question(question.content) 路由：
       - 作文：grading_service.grade_essay() + writing_kg 写作能力归因
       - 数学解答题：grading_service.grade_math()
    3. 把 LLM 返回的 suggested_score / comment 写入 QuestionResult
    4. 作文场景调 writing_kg.map_error_cause_to_dimension/nodes/suggestion 做能力归因

    复用：
    - ocr_service: backend/services/ocr.py
    - grading_service: backend/services/grader.py
    - writing_kg: backend/services/writing_graph.py
    """
    # 1. OCR 识别
    try:
        from backend.services.ocr import ocr_service
        ocr_result = await ocr_service.recognize(region.image_bytes)
    except Exception as e:
        logger.exception(f"[AnswerSheet] 大题 {question.id} OCR 异常: {e}")
        return QuestionResult(
            question_id=question.id,
            question_type=question.type,
            question_content=question.content[:80],
            region_type="essay",
            student_answer="",
            standard_answer=question.answer,
            score=0,
            max_score=question.score,
            is_correct=None,
            confidence=0.0,
            error=f"OCR 调用失败: {type(e).__name__}: {e}",
        )

    raw_text = ocr_result.text or ""
    confidence = float(ocr_result.confidence or 0.0)

    # 2. OCR 低置信度 / 识别失败处理
    if ocr_result.needs_manual_input or (not raw_text.strip() and confidence < 0.4):
        return QuestionResult(
            question_id=question.id,
            question_type=question.type,
            question_content=question.content[:80],
            region_type="essay",
            student_answer=raw_text,
            standard_answer=question.answer,
            score=0,
            max_score=question.score,
            is_correct=None,
            confidence=confidence,
            ocr_text=raw_text,
            comment="OCR 识别失败或置信度过低，需人工复核",
            error="OCR 低置信度或失败" if confidence < 0.4 else "OCR 双引擎均失败",
        )

    # 3. 路由：作文 vs 数学解答题
    is_essay = _is_essay_question(question.content)
    logger.info(
        f"[AnswerSheet] 大题 {question.id} 路由: "
        f"is_essay={is_essay}, content_head={question.content[:30]!r}"
    )

    try:
        from backend.services.grader import grading_service
        if is_essay:
            llm_result = await grading_service.grade_essay(
                question=question.content,
                standard_answer=question.answer or "",
                student_answer_ocr=raw_text,
                total_score=int(question.score),
                confidence=confidence,
                image_bytes=region.image_bytes,
            )
        else:
            llm_result = await grading_service.grade_math(
                question=question.content,
                standard_answer=question.answer or "",
                student_answer_ocr=raw_text,
                total_score=int(question.score),
                confidence=confidence,
                image_bytes=region.image_bytes,
            )
    except Exception as e:
        logger.exception(f"[AnswerSheet] 大题 {question.id} LLM 批改异常: {e}")
        return QuestionResult(
            question_id=question.id,
            question_type=question.type,
            question_content=question.content[:80],
            region_type="essay",
            student_answer=raw_text,
            standard_answer=question.answer,
            score=0,
            max_score=question.score,
            is_correct=None,
            confidence=confidence,
            ocr_text=raw_text,
            error=f"LLM 批改失败: {type(e).__name__}: {e}",
        )

    # 4. 提取批改结果
    suggested_score = float(llm_result.get("suggested_score", 0) or 0)
    max_score = float(llm_result.get("max_score", question.score) or question.score)
    grading = llm_result.get("grading", {}) or {}
    comment = llm_result.get("comment", "") or ""
    error_cause = grading.get("error_cause", "none")
    knowledge_points = grading.get("knowledge_points", []) or []
    model_key = llm_result.get("model_key", "standard")
    grading_method = grading.get("grading_method", "llm")

    # is_correct 判定：得分率 >= 0.8 视为正确
    ratio = suggested_score / max_score if max_score > 0 else 0
    is_correct = ratio >= 0.8

    # 5. 写作能力归因（仅作文场景，且有错因）
    writing_attribution = None
    if is_essay and error_cause and error_cause != "none":
        try:
            from backend.services.writing_graph import writing_kg
            dimension = writing_kg.map_error_cause_to_dimension(error_cause)
            fine_nodes = writing_kg.map_error_cause_to_nodes(error_cause)
            suggestion = writing_kg.get_error_cause_suggestion(error_cause)
            writing_attribution = {
                "error_cause": error_cause,
                "dimension": dimension,
                "fine_nodes": fine_nodes,
                "knowledge_points": knowledge_points,
                "suggestion": suggestion,
            }
            # 把改进建议追加到评语
            if suggestion:
                comment = f"{comment}\n\n【改进建议】{suggestion}"
        except Exception as e:
            logger.warning(f"[AnswerSheet] 大题 {question.id} 写作归因失败: {type(e).__name__}: {e}")

    # 6. 构建详细批改信息
    grading_detail = {
        "is_essay": is_essay,
        "model_key": model_key,
        "grading_method": grading_method,
        "grading": grading,
        "error_cause": error_cause,
        "knowledge_points": knowledge_points,
    }
    if writing_attribution:
        grading_detail["writing_attribution"] = writing_attribution

    logger.info(
        f"[AnswerSheet] 大题 {question.id} 批改完成: "
        f"is_essay={is_essay}, score={suggested_score}/{max_score}, "
        f"model={model_key}, error_cause={error_cause}"
    )

    return QuestionResult(
        question_id=question.id,
        question_type=question.type,
        question_content=question.content[:80],
        region_type="essay",
        student_answer=raw_text,
        standard_answer=question.answer,
        score=suggested_score,
        max_score=max_score,
        is_correct=is_correct,
        confidence=confidence,
        ocr_text=raw_text,
        comment=comment,
        grading_detail=grading_detail,
    )
