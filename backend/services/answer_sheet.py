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

本模块已拆分为多个子模块，此处仅保留 AnswerSheetOrchestrator 编排层 + 模块级单例，
并 re-export 常用符号以保持向后兼容（外部代码无需改动导入路径）。

子模块结构：
- answer_sheet_models.py       : QuestionResult / PaperScanResult 数据类
- answer_sheet_text_utils.py   : 文本规范化 / Levenshtein / 作文检测
- answer_sheet_graders.py      : 三个题型批改函数（bubble/fill/essay）
- answer_sheet_attribution.py  : 错题归因回写
- answer_sheet.py（本文件）    : AnswerSheetOrchestrator 编排层 + 单例

复用清单：
- auto_grade(): backend/services/exam_service.py
- grading_service: backend/services/grader.py
- ocr_service: backend/services/ocr.py
- Exam/Question/ExamSubmission/Answer: backend/models/tables.py

模块级单例：answer_sheet_orchestrator = AnswerSheetOrchestrator()
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from backend.models.tables import (
    Exam, Question, ExamSubmission, Answer, RegisteredPerson, Student
)
from backend.services.paper_template import paper_template_service, QuestionRegionImage
from cv_engine.detectors.answer_card_detector import (  # noqa: F401
    answer_card_detector, AnswerCardResult,
)
from backend.services.answer_sheet_models import QuestionResult, PaperScanResult
from backend.services.answer_sheet_graders import (
    grade_bubble_question,
    grade_fill_question,
    grade_essay_question,
)
from backend.services.answer_sheet_attribution import attribute_and_persist_weakness

# 子模块 re-export（向后兼容：tests 与外部模块仍可直接从 answer_sheet 导入）
from backend.services.answer_sheet_text_utils import (  # noqa: F401
    _normalize_fill_text,
    _to_halfwidth,
    _levenshtein_distance,
    _levenshtein_similarity,
    _is_essay_question,
    _ESSAY_KEYWORDS,
    _FULLWIDTH_OFFSET,
)

logger = logging.getLogger(__name__)

__all__ = [
    "AnswerSheetOrchestrator",
    "answer_sheet_orchestrator",
    "QuestionResult",
    "PaperScanResult",
    "answer_card_detector",
    "AnswerCardResult",
    # 文本工具 re-export
    "_normalize_fill_text",
    "_to_halfwidth",
    "_levenshtein_distance",
    "_levenshtein_similarity",
    "_is_essay_question",
]


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
            attribution_summary = await attribute_and_persist_weakness(
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
            return await grade_bubble_question(question, region)
        elif region.region_type == "fill":
            return await grade_fill_question(question, region)
        elif region.region_type == "essay":
            return await grade_essay_question(question, region)
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

    # 向后兼容委托方法（原为内部实现，现委托给 answer_sheet_graders 模块级函数）
    # 保留以便外部测试与旧调用代码无需改动。
    async def _grade_bubble_question(
        self, question: Question, region: QuestionRegionImage
    ) -> QuestionResult:
        return await grade_bubble_question(question, region)

    async def _grade_fill_question(
        self, question: Question, region: QuestionRegionImage
    ) -> QuestionResult:
        return await grade_fill_question(question, region)

    async def _grade_essay_question(
        self, question: Question, region: QuestionRegionImage
    ) -> QuestionResult:
        return await grade_essay_question(question, region)

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

    def _get_student_name(self, db: Session, student_id: int) -> str:
        """获取学生姓名（通过 RegisteredPerson）"""
        person = db.query(RegisteredPerson).filter(RegisteredPerson.id == student_id).first()
        return person.name if person else f"用户#{student_id}"


# 模块级单例
answer_sheet_orchestrator = AnswerSheetOrchestrator()
