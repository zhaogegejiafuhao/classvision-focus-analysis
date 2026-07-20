"""答题卡整卷批改编排器——协调各题型处理流程，复用现有批改能力

核心数据流：
    扫描件图片
        ↓
    PaperTemplateService.extract_regions()  按模板切分各题
        ↓
    分题型处理：
      - bubble (单选/多选/判断): AnswerCardDetector.detect() → 转 content → auto_grade()
      - fill   (填空题, Phase 2): ocr_service.recognize() → auto_grade() fill分支
      - essay  (大题, Phase 3): ocr_service.recognize() → grading_service.grade_math/grade_essay()
        ↓
    持久化到 Answer + ExamSubmission 表
        ↓
    返回 PaperScanResult（题目级结果 + 汇总报告）

复用清单：
- auto_grade(): backend/api/exam_routes.py L95
- grading_service: backend/services/grader.py
- ocr_service: backend/services/ocr.py
- Exam/Question/ExamSubmission/Answer: backend/models/tables.py

模块级单例：answer_sheet_orchestrator = AnswerSheetOrchestrator()
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from backend.models.tables import (
    Exam, Question, ExamSubmission, Answer, RegisteredPerson, Student
)
from backend.services.paper_template import paper_template_service, QuestionRegionImage
from cv_engine.detectors.answer_card_detector import answer_card_detector, AnswerCardResult

logger = logging.getLogger(__name__)


@dataclass
class QuestionResult:
    """单题批改结果"""
    question_id: int
    question_type: str           # single/multi/judge/fill/essay
    question_content: str        # 题目内容（前 80 字）
    region_type: str             # bubble/fill/essay
    student_answer: str          # 识别出的学生答案文本
    standard_answer: str         # 标准答案
    score: float                 # 得分
    max_score: float             # 满分
    is_correct: Optional[bool]   # 是否正确（None 表示未批改）
    comment: str = ""            # 评语
    confidence: float = 1.0      # 识别置信度
    ocr_text: Optional[str] = None  # OCR 识别的原始文本（填空/大题）
    grading_detail: Optional[dict] = None  # LLM 批改完整结果（大题）
    error: Optional[str] = None  # 处理失败原因


@dataclass
class PaperScanResult:
    """整卷扫描批改结果"""
    submission_id: int
    exam_id: int
    student_id: int
    student_name: str
    total_score: float
    max_score: float
    question_results: list[QuestionResult] = field(default_factory=list)
    summary: dict = field(default_factory=dict)  # 汇总统计
    debug_image_b64: str = ""                    # 答题卡调试可视化图
    attribution: dict = field(default_factory=dict)  # 错题归因回写摘要


class AnswerSheetOrchestrator:
    """整卷批改编排器

    使用方式：
        result = await answer_sheet_orchestrator.scan_and_grade(
            db, exam_id=1, student_id=2, paper_image_bytes=img_bytes
        )
    """

    async def scan_and_grade(
        self,
        db: Session,
        exam_id: int,
        student_id: int,
        paper_image_bytes: bytes,
    ) -> PaperScanResult:
        """主入口：扫描整卷 → 识别各题 → 批改 → 持久化 → 返回报告

        Args:
            db: 数据库会话
            exam_id: 考试 ID
            student_id: 学生 ID（RegisteredPerson.id）
            paper_image_bytes: 整卷扫描件字节

        Returns:
            PaperScanResult
        """
        # 1. 校验考试存在
        exam = db.query(Exam).filter(Exam.id == exam_id).first()
        if not exam:
            raise ValueError(f"考试 {exam_id} 不存在")

        # 2. 查询学生姓名
        student_name = self._get_student_name(db, student_id)

        # 3. 创建 ExamSubmission（标记为已提交待批改）
        submission = ExamSubmission(
            exam_id=exam_id,
            student_id=student_id,
            status="submitted",
            started_at=datetime.now(),
            submitted_at=datetime.now(),
        )
        db.add(submission)
        db.flush()  # 获取 submission.id

        # 4. 按模板切分各题区域
        try:
            region_images = paper_template_service.extract_regions(db, exam_id, paper_image_bytes)
        except ValueError as e:
            db.rollback()
            raise ValueError(f"试卷模板切分失败: {e}")

        if not region_images:
            db.rollback()
            raise ValueError("未切分到任何题目区域，请检查试卷模板配置")

        # 5. 查询题目信息（用于获取标准答案和分值）
        question_ids = [ri.question_id for ri in region_images]
        questions = db.query(Question).filter(Question.id.in_(question_ids)).all()
        question_map = {q.id: q for q in questions}

        # 6. 逐题批改
        question_results: list[QuestionResult] = []
        for region in region_images:
            question = question_map.get(region.question_id)
            if not question:
                question_results.append(QuestionResult(
                    question_id=region.question_id,
                    question_type="unknown",
                    question_content="(题目已删除)",
                    region_type=region.region_type,
                    student_answer="",
                    standard_answer="",
                    score=0,
                    max_score=0,
                    is_correct=None,
                    error="题目不存在",
                ))
                continue

            try:
                result = await self._grade_single_question(question, region)
            except Exception as e:
                logger.exception(f"[AnswerSheet] 题目 {question.id} 批改异常: {e}")
                result = QuestionResult(
                    question_id=question.id,
                    question_type=question.type,
                    question_content=question.content[:80],
                    region_type=region.region_type,
                    student_answer="",
                    standard_answer=question.answer,
                    score=0,
                    max_score=question.score,
                    is_correct=None,
                    error=f"{type(e).__name__}: {e}",
                )

            question_results.append(result)

        # 7. 持久化到 Answer 表
        self._persist_answers(db, submission.id, question_results)

        # 8. 更新 ExamSubmission 总分
        total_score = sum(r.score for r in question_results)
        max_score = sum(r.max_score for r in question_results)
        submission.score = total_score
        submission.status = "graded"
        submission.graded_at = datetime.now()
        db.commit()
        db.refresh(submission)

        # 9. 构建汇总报告
        summary = self._build_report(question_results)

        # 10. 寻找调试图（取第一个 bubble 题型的）
        debug_b64 = ""
        for r in question_results:
            if r.grading_detail and r.grading_detail.get("debug_image_b64"):
                debug_b64 = r.grading_detail["debug_image_b64"]
                break

        logger.info(
            f"[AnswerSheet] 扫描批改完成: exam_id={exam_id}, student_id={student_id}, "
            f"submission_id={submission.id}, total={total_score}/{max_score}"
        )

        # 11. 错题归因回写（写入 KnowledgeAnalysis 表，失败不阻塞主流程）
        attribution_summary: dict = {}
        try:
            attribution_summary = await self._attribute_and_persist_weakness(
                db, student_id, question_results
            )
        except Exception as e:
            logger.warning(f"[AnswerSheet] 归因回写整体失败: {type(e).__name__}: {e}")
            attribution_summary = {"error": str(e)}

        return PaperScanResult(
            submission_id=submission.id,
            exam_id=exam_id,
            student_id=student_id,
            student_name=student_name,
            total_score=total_score,
            max_score=max_score,
            question_results=question_results,
            summary=summary,
            debug_image_b64=debug_b64,
            attribution=attribution_summary,
        )

    # ============ 单题批改分发 ============

    async def _grade_single_question(
        self, question: Question, region: QuestionRegionImage
    ) -> QuestionResult:
        """根据 region_type 分发到对应处理路径"""
        if region.region_type == "bubble":
            return await self._grade_bubble_question(question, region)
        elif region.region_type == "fill":
            return await self._grade_fill_question(question, region)
        elif region.region_type == "essay":
            return await self._grade_essay_question(question, region)
        else:
            return QuestionResult(
                question_id=question.id,
                question_type=question.type,
                question_content=question.content[:80],
                region_type=region.region_type,
                student_answer="",
                standard_answer=question.answer,
                score=0,
                max_score=question.score,
                is_correct=None,
                error=f"未知 region_type: {region.region_type}",
            )

    async def _grade_bubble_question(
        self, question: Question, region: QuestionRegionImage
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
        - auto_grade()  (backend/api/exam_routes.py L95)，仅在单选/判断的正常分支调用
        """
        from backend.api.exam_routes import auto_grade

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

    async def _grade_fill_question(
        self, question: Question, region: QuestionRegionImage
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

    async def _grade_essay_question(
        self, question: Question, region: QuestionRegionImage
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

    # ============ 持久化与汇总 ============

    def _persist_answers(self, db: Session, submission_id: int, results: list[QuestionResult]) -> None:
        """把批改结果写入 Answer 表

        复用 Answer 模型（backend/models/tables.py L461）
        """
        for r in results:
            answer = Answer(
                submission_id=submission_id,
                question_id=r.question_id,
                content=r.student_answer,
                score=r.score,
                is_correct=r.is_correct,
            )
            db.add(answer)
        db.flush()

    def _build_report(self, results: list[QuestionResult]) -> dict:
        """构建汇总报告"""
        total = len(results)
        correct = sum(1 for r in results if r.is_correct is True)
        wrong = sum(1 for r in results if r.is_correct is False)
        ungraded = sum(1 for r in results if r.is_correct is None)

        # 按题型分组统计
        by_type: dict[str, dict] = {}
        for r in results:
            t = r.question_type
            if t not in by_type:
                by_type[t] = {"total": 0, "correct": 0, "wrong": 0, "score": 0.0, "max_score": 0.0}
            by_type[t]["total"] += 1
            by_type[t]["score"] += r.score
            by_type[t]["max_score"] += r.max_score
            if r.is_correct is True:
                by_type[t]["correct"] += 1
            elif r.is_correct is False:
                by_type[t]["wrong"] += 1

        # 错题列表
        wrong_list = [
            {
                "question_id": r.question_id,
                "question_content": r.question_content,
                "student_answer": r.student_answer,
                "standard_answer": r.standard_answer,
                "error": r.error,
            }
            for r in results if r.is_correct is False
        ]

        return {
            "total_questions": total,
            "correct_count": correct,
            "wrong_count": wrong,
            "ungraded_count": ungraded,
            "accuracy": correct / total if total > 0 else 0,
            "by_type": by_type,
            "wrong_list": wrong_list,
        }

    async def _attribute_and_persist_weakness(
        self,
        db: Session,
        student_id: int,
        question_results: list[QuestionResult],
    ) -> dict:
        """错题归因回写：把批改结果交给归因服务，写入 KnowledgeAnalysis 表

        流程：
        1. 收集错题（is_correct=False 或部分得分），按 region_type 分组：
           - bubble/fill 数学错题 → knowledge_attribution_service（基于 knowledge_graph）
           - essay 作文错题 → writing_attribution_service（基于 writing_graph）
        2. 数学题：用 ErrorMapper.map_by_keywords(question_content) 把题目映射到 KG 节点
        3. 作文题：用 error_cause 直接映射到写作 DAG 节点
        4. 调归因服务的 analyze 方法，得到雷达图 + 薄弱点
        5. 序列化写入 KnowledgeAnalysis 表（math/writing 各一条）

        Returns:
            归因回写摘要 {math_report_saved: bool, writing_report_saved: bool, ...}
        """
        from datetime import date as date_cls
        from backend.models.tables import KnowledgeAnalysis

        today = date_cls.today()
        result_summary = {
            "math_report_saved": False,
            "writing_report_saved": False,
            "math_error_count": 0,
            "writing_error_count": 0,
            "error": None,
        }

        # 收集错题
        math_error_texts: list[tuple[str, str, float]] = []  # (question_content, error_cause, weight)
        writing_errors: list[tuple[str, str, float]] = []  # (essay_title, error_cause, weight)

        for r in question_results:
            # 跳过未批改或全对的题
            if r.is_correct is True:
                continue
            # 计算错误权重：完全错=1.0, 部分对=0.5
            if r.is_correct is False:
                weight = 1.0
            else:  # None（未批改）
                continue

            # 得分率 < 0.5 视为完全错，0.5-0.8 视为部分错
            if r.max_score > 0:
                ratio = r.score / r.max_score
                if ratio >= 0.5:
                    weight = 0.5

            # 获取 error_cause 和 grading_detail
            grading_detail = r.grading_detail or {}
            error_cause = grading_detail.get("error_cause", "") or ""

            if r.region_type == "essay":
                # 作文题：检查 is_essay 标记
                is_essay = grading_detail.get("is_essay", False)
                if is_essay and error_cause and error_cause != "none":
                    writing_errors.append((r.question_content, error_cause, weight))
            else:
                # 数学/选择/填空题：用题目内容做关键词匹配
                # 只对有 LLM 批改结果（含 error_cause）的题做归因
                if error_cause and error_cause != "none":
                    math_error_texts.append((r.question_content, error_cause, weight))
                elif r.region_type in ("bubble", "fill"):
                    # 选择/填空题没有 LLM 错因，用题目内容做关键词匹配后归因
                    math_error_texts.append((r.question_content, "知识缺失", weight))

        result_summary["math_error_count"] = len(math_error_texts)
        result_summary["writing_error_count"] = len(writing_errors)

        # 数学题归因
        if math_error_texts:
            try:
                from backend.services.attribution import (
                    knowledge_attribution_service, ErrorEvent,
                )
                # 用 ErrorMapper 把题目内容映射到 KG 节点
                error_events: list[ErrorEvent] = []
                for content, cause, weight in math_error_texts:
                    node_ids = knowledge_attribution_service.error_mapper.map_by_keywords(content)
                    if not node_ids:
                        # 关键词未命中，跳过该题（避免慢速 LLM 调用）
                        continue
                    # 一个题目可能匹配多个节点，分摊权重
                    per_node_weight = weight / len(node_ids)
                    for nid in node_ids:
                        error_events.append(ErrorEvent(
                            knowledge_node_id=nid,
                            error_weight=per_node_weight,
                            timestamp=today,
                            question_content=content[:80],
                            error_cause=cause,
                        ))

                if error_events:
                    report = await knowledge_attribution_service.analyze(
                        errors=error_events,
                        reference_date=today,
                    )
                    # 序列化写入 KnowledgeAnalysis 表
                    radar_json = json.dumps(report.radar, ensure_ascii=False)
                    weak_points_data = [
                        {
                            "knowledge_id": wp.knowledge_id,
                            "knowledge_name": wp.knowledge_name,
                            "weakness_score": wp.weakness_score,
                            "error_count": wp.error_count,
                            "suggestion": wp.suggestion,
                            "error_cause_distribution": wp.error_cause_distribution,
                        }
                        for wp in report.weak_points
                    ]
                    weak_points_json = json.dumps(weak_points_data, ensure_ascii=False)
                    correction_status_json = json.dumps(report.correction_status, ensure_ascii=False)

                    ka = KnowledgeAnalysis(
                        student_id=student_id,
                        analysis_type="math",
                        radar_json=radar_json,
                        weak_points_json=weak_points_json,
                        correction_status_json=correction_status_json,
                    )
                    db.add(ka)
                    db.commit()
                    result_summary["math_report_saved"] = True
                    logger.info(
                        f"[AnswerSheet] 数学归因完成: student_id={student_id}, "
                        f"error_events={len(error_events)}, weak_points={len(report.weak_points)}"
                    )
            except Exception as e:
                logger.warning(f"[AnswerSheet] 数学归因失败: {type(e).__name__}: {e}")
                result_summary["error"] = f"math: {type(e).__name__}: {e}"

        # 作文题归因
        if writing_errors:
            try:
                from backend.services.attribution import (
                    writing_attribution_service, WritingErrorEvent,
                )
                writing_events = [
                    WritingErrorEvent(
                        error_cause=cause,
                        error_weight=weight,
                        timestamp=today,
                        essay_title=title[:50],
                    )
                    for title, cause, weight in writing_errors
                ]
                report = await writing_attribution_service.analyze(
                    writing_errors=writing_events,
                    student_id=str(student_id),
                    reference_date=today,
                )
                # 序列化写入 KnowledgeAnalysis 表
                radar_json = json.dumps(report.radar, ensure_ascii=False)
                weak_dims_data = [
                    {
                        "dimension_id": wd.dimension_id,
                        "dimension_name": wd.dimension_name,
                        "weakness_score": wd.weakness_score,
                        "sub_weaknesses": wd.sub_weaknesses,
                        "error_causes": wd.error_causes,
                        "suggestion": wd.suggestion,
                    }
                    for wd in report.weak_dimensions
                ]
                weak_points_json = json.dumps({
                    "weak_dimensions": weak_dims_data,
                    "error_cause_distribution": report.error_cause_distribution,
                    "overall_suggestion": report.overall_suggestion,
                }, ensure_ascii=False)

                ka = KnowledgeAnalysis(
                    student_id=student_id,
                    analysis_type="writing",
                    radar_json=radar_json,
                    weak_points_json=weak_points_json,
                    correction_status_json=None,
                )
                db.add(ka)
                db.commit()
                result_summary["writing_report_saved"] = True
                logger.info(
                    f"[AnswerSheet] 写作归因完成: student_id={student_id}, "
                    f"writing_errors={len(writing_events)}, weak_dims={len(report.weak_dimensions)}"
                )
            except Exception as e:
                logger.warning(f"[AnswerSheet] 写作归因失败: {type(e).__name__}: {e}")
                prev = result_summary.get("error") or ""
                result_summary["error"] = f"{prev}writing: {type(e).__name__}: {e}".strip()

        return result_summary

    def _get_student_name(self, db: Session, student_id: int) -> str:
        """获取学生姓名（通过 RegisteredPerson）"""
        person = db.query(RegisteredPerson).filter(RegisteredPerson.id == student_id).first()
        return person.name if person else f"用户#{student_id}"


# ============ 模块级辅助函数（填空题 OCR 判分用）============

# 全角→半角字符映射表（数字、字母、标点）
_FULLWIDTH_OFFSET = 0xFEE0  # 全角字符到半角的偏移量（除空格外）

def _normalize_fill_text(text: str) -> str:
    """填空题文本规范化

    用于 OCR 识别后与学生标准答案的比对，提高匹配率：
    1. 去除首尾空白和内部换行
    2. 全角字符转半角（数字、字母、标点）
    3. 统一小写
    4. 去除首尾的中英文标点
    5. 合并连续空白为单个空格
    """
    if not text:
        return ""
    # 1. 去换行
    s = text.replace("\r", " ").replace("\n", " ")
    # 2. 全角转半角
    s = _to_halfwidth(s)
    # 3. 小写
    s = s.lower()
    # 4. 去首尾标点（中英文）
    s = s.strip(" \t\"'.,;:!?，。；：！？、…—·（()[]【】「」『』")
    # 5. 合并连续空白
    s = " ".join(s.split())
    return s


def _to_halfwidth(s: str) -> str:
    """全角字符转半角

    全角空格 (U+3000) → 半角空格
    全角字符 (U+FF01..U+FF5E) → 减去 0xFEE0 转为对应半角
    """
    if not s:
        return s
    result = []
    for ch in s:
        code = ord(ch)
        if code == 0x3000:  # 全角空格
            result.append(" ")
        elif 0xFF01 <= code <= 0xFF5E:  # 全角字符范围
            result.append(chr(code - _FULLWIDTH_OFFSET))
        else:
            result.append(ch)
    return "".join(result)


def _levenshtein_distance(s1: str, s2: str) -> int:
    """Levenshtein 编辑距离（DP 实现）"""
    if len(s1) < len(s2):
        return _levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def _levenshtein_similarity(s1: str, s2: str) -> float:
    """基于 Levenshtein 距离的相似度 [0.0, 1.0]

    similarity = 1 - distance / max(len(s1), len(s2))
    空字符串返回 0.0
    """
    if not s1 and not s2:
        return 1.0
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    dist = _levenshtein_distance(s1, s2)
    return 1.0 - dist / max_len


# ============ 模块级辅助函数（大题/作文 OCR + LLM 批改用）============

# 作文题关键词（出现任一即认定为作文，路由到 grade_essay）
_ESSAY_KEYWORDS: tuple[str, ...] = (
    "作文", "写一篇", "题材", "文体",
    "不少于", "字数", "根据要求写作", "阅读下面的文字",
    "命题作文", "材料作文", "话题作文", "半命题作文",
    "写话", "写一段话",
)


def _is_essay_question(content: str) -> bool:
    """检测题目是否为语文作文（vs 数学/理科解答题）

    判定规则：题目内容包含作文相关关键词 → 视为作文
    用于在 _grade_essay_question 中决定路由到 grade_essay 还是 grade_math。

    Args:
        content: 题目内容文本

    Returns:
        True 表示认定为作文题，False 表示数学/理科解答题
    """
    if not content:
        return False
    text = content.lower()
    for kw in _ESSAY_KEYWORDS:
        if kw in text:
            return True
    # 特殊模式："以...为题"（支持全角／半角引号、书名号）
    import re
    if re.search(r"以[\"\"''《「『].{1,30}[\"\"''》」』]为题", content):
        return True
    return False


# 模块级单例
answer_sheet_orchestrator = AnswerSheetOrchestrator()
