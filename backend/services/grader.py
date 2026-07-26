"""ClassVision LLM批改层 - 对外统一接口

本模块已拆分为多个子模块，此处仅保留 GradingService 编排层 + 模块级单例，
并 re-export 常用符号以保持向后兼容（外部代码 `from backend.services.grader import grading_service` 不变）。

子模块结构：
- grader_prompts.py     : 所有 LLM 提示词与 Level 0 兜底 rubric
- rubric_generator.py   : LRUCache / rule_based_grade / RubricGenerator
- math_grader.py        : MathGrader（数学题过程分批改，并行竞速降级）
- essay_grader.py       : EssayGrader（语文作文四维批改）
- grader.py（本文件）   : GradingService 编排层 + 单例
"""
import logging
from typing import Optional

from backend.core.config import settings
from backend.services.geometry_analyzer import (
    GeometryAnalyzer,
    is_geometry_question,
    detect_geometry_with_llm_fallback,
)

# 子模块 re-export（向后兼容）
from backend.services.grader_prompts import (
    RUBRIC_GENERATION_PROMPT,
    MATH_GRADING_PROMPT,
    GEOMETRY_AUXILIARY_LINE_PROMPT_SECTION,
    COMMENT_GENERATION_PROMPT,
    ESSAY_OCR_LOW_CONFIDENCE_HINT,
    ESSAY_GRADING_PROMPT,
    ESSAY_COMMENT_GENERATION_PROMPT,
    FALLBACK_RUBRIC,
    FALLBACK_ESSAY_RUBRIC,
)
from backend.services.rubric_generator import (
    LRUCache,
    rule_based_grade,
    RubricGenerator,
    _rubric_cache,
)
from backend.services.math_grader import MathGrader
from backend.services.essay_grader import EssayGrader

logger = logging.getLogger(__name__)

__all__ = [
    # 编排层
    "GradingService",
    "grading_service",
    # 子模块 re-export
    "RubricGenerator",
    "MathGrader",
    "EssayGrader",
    "LRUCache",
    "rule_based_grade",
    "FALLBACK_RUBRIC",
    "FALLBACK_ESSAY_RUBRIC",
    # Prompt（便于外部测试/调试）
    "RUBRIC_GENERATION_PROMPT",
    "MATH_GRADING_PROMPT",
    "ESSAY_GRADING_PROMPT",
    "GEOMETRY_AUXILIARY_LINE_PROMPT_SECTION",
    "COMMENT_GENERATION_PROMPT",
    "ESSAY_OCR_LOW_CONFIDENCE_HINT",
    "ESSAY_COMMENT_GENERATION_PROMPT",
    # 几何工具
    "GeometryAnalyzer",
    "is_geometry_question",
    "detect_geometry_with_llm_fallback",
]


class GradingService:
    """批改服务 - 对外统一接口"""

    def __init__(self):
        self.rubric_generator = RubricGenerator()
        self.math_grader = MathGrader()
        self.geometry_analyzer = GeometryAnalyzer()
        self.essay_grader = EssayGrader()

    async def grade_math(
        self,
        question: str,
        standard_answer: str,
        student_answer_ocr: str,
        total_score: int,
        rubric: Optional[dict] = None,
        image_bytes: Optional[bytes] = None,
        confidence: float = 0.0,
    ) -> dict:
        """完整的数学题批改流程：rubric生成(如无) → 过程分判定 → 几何辅助线分析(可选) → 评语生成

        Args:
            question: 题目文本
            standard_answer: 标准答案
            student_answer_ocr: 学生解答（OCR提取）
            total_score: 题目总分
            rubric: 评分标准（可选，不传则自动生成）
            image_bytes: 学生手写图片字节（可选，用于几何辅助线分析）
            confidence: 置信度（0.0-1.0），用于动态模型路由决策

        Returns:
            dict: 完整批改结果
        """
        # 空答案快速短路：直接判0分，避免LLM把标准答案误判为学生答案
        if not student_answer_ocr or not student_answer_ocr.strip():
            logger.warning("[GradingService] 学生答案为空，跳过LLM批改，直接判0分")
            empty_rubric = rubric if rubric else FALLBACK_RUBRIC.copy()
            empty_grading = {
                "steps": [],
                "total_score": 0,
                "max_score": total_score,
                "error_type": "empty_answer",
                "error_cause": "未作答",
                "knowledge_points": [],
                "comment": "未作答",
                "grading_method": "empty_answer_short_circuit",
            }
            return {
                "rubric": empty_rubric,
                "grading": empty_grading,
                "comment": "未作答，本题判0分。请补交答案后重新批改。",
                "suggested_score": 0,
                "max_score": total_score,
                "confidence": 1.0,
                "flagged": False,
                "model_key": "rule_based",
            }

        # 极短答案（<5字符）也不调用LLM，避免误判
        stripped_answer = student_answer_ocr.strip()
        if len(stripped_answer) < 5 and not any(c.isdigit() for c in stripped_answer):
            logger.warning(f"[GradingService] 学生答案过短({len(stripped_answer)}字符)且无数字: {stripped_answer!r}，判0分")
            empty_rubric = rubric if rubric else FALLBACK_RUBRIC.copy()
            empty_grading = {
                "steps": [],
                "total_score": 0,
                "max_score": total_score,
                "error_type": "insufficient_answer",
                "error_cause": "答案不完整",
                "knowledge_points": [],
                "comment": "答案过短",
                "grading_method": "empty_answer_short_circuit",
            }
            return {
                "rubric": empty_rubric,
                "grading": empty_grading,
                "comment": "答案过短，无法判定解题过程，本题判0分。请补全解答过程后重新批改。",
                "suggested_score": 0,
                "max_score": total_score,
                "confidence": 1.0,
                "flagged": False,
                "model_key": "rule_based",
            }

        # 检测是否为几何题（三层检测：关键词+符号+LLM兜底）
        geometry_detected = await detect_geometry_with_llm_fallback(question)

        # Step 1: 柔性Rubric生成（如果未提供）
        if rubric is None:
            rubric = await self.rubric_generator.generate(
                question=question,
                standard_answer=standard_answer,
                total_score=total_score,
            )

        # Step 2: 基于rubric的过程分判定（集成动态模型路由）
        grading_result = await self.math_grader.grade(
            question=question,
            standard_answer=standard_answer,
            student_answer=student_answer_ocr,
            rubric=rubric,
            is_geometry=geometry_detected,
            confidence=confidence,
        )

        # Step 2.5: 几何辅助线分析（仅几何题且有图片时触发）
        geometry_analysis = None
        if geometry_detected and image_bytes:
            logger.info("[GradingService] 检测到几何题，启动辅助线分析...")
            try:
                geo_result = await self.geometry_analyzer.analyze(
                    question=question,
                    image_bytes=image_bytes,
                )
                geometry_analysis = geo_result.to_dict()
                logger.info(f"[GradingService] 辅助线分析完成: assessment={geo_result.assessment}")
            except Exception as e:
                logger.warning(f"[GradingService] 辅助线分析失败: {type(e).__name__}: {e}")

        # Step 3: 生成个性化评语（几何题时追加辅助线提示）
        error_steps = [
            {"step_id": s.get("step_id"), "content": s.get("content"), "reason": s.get("error_reason")}
            for s in grading_result.get("steps", [])
            if not s.get("correct", True)
        ]

        comment = await self.math_grader.generate_comment(
            question=question,
            score=grading_result.get("total_score", 0),
            max_score=grading_result.get("max_score", total_score),
            error_steps=error_steps,
            error_type=grading_result.get("error_type", "none"),
            knowledge_points=grading_result.get("knowledge_points", []),
        )

        # 几何题评语追加辅助线提示
        if geometry_analysis and geometry_analysis.get("hint"):
            comment = f"{comment} {geometry_analysis['hint']}"

        result = {
            "rubric": rubric,
            "grading": grading_result,
            "comment": comment,
            "suggested_score": grading_result.get("total_score", 0),
            "max_score": grading_result.get("max_score", total_score),
            "confidence": confidence if confidence > 0 else 0.85,
            "flagged": confidence < settings.GRADING_LOW_CONFIDENCE_THRESHOLD if confidence > 0 else False,
            "model_key": grading_result.get("_model_key", "standard"),
        }

        # 几何题时增加辅助线分析结果
        if geometry_analysis is not None:
            result["geometry_analysis"] = geometry_analysis

        return result

    async def grade_essay(
        self,
        question: str,
        standard_answer: str,
        student_answer_ocr: str,
        total_score: int,
        rubric: Optional[dict] = None,
        image_bytes: Optional[bytes] = None,
        confidence: float = 0.0,
    ) -> dict:
        """完整的语文作文批改流程：四维评分 → 综合评语

        Args:
            question: 作文题目
            standard_answer: 写作要求（参考）
            student_answer_ocr: 学生作文（OCR提取）
            total_score: 题目总分（默认100，支持按比例缩放四维）
            rubric: 评分标准（作文场景不使用，保留参数对齐签名）
            image_bytes: 学生手写图片字节（预留：未来用于 VL 识别书写）
            confidence: OCR置信度，作为书写维度弱信号

        Returns:
            dict: 与 grade_math() 同构的批改结果
        """
        # 空答案快速短路：直接判0分，避免LLM把标准答案误判为学生答案
        if not student_answer_ocr or not student_answer_ocr.strip():
            logger.warning("[GradingService] 作文答案为空，跳过LLM批改，直接判0分")
            empty_rubric = rubric if rubric else FALLBACK_ESSAY_RUBRIC.copy()
            scale = total_score / 100.0
            empty_dims = {}
            for dim_key, dim_meta in self.essay_grader.DIMENSION_WEIGHTS.items():
                new_max = round(dim_meta["max_score"] * scale, 1)
                empty_dims[dim_key] = {
                    "score": 0,
                    "max_score": new_max,
                    "comment": "未作答",
                    "error_cause": self.essay_grader._DIM_ERROR_MAP[dim_key],
                }
            empty_grading = {
                "dimensions": empty_dims,
                "steps": self.essay_grader._build_compatible_steps(empty_dims),
                "total_score": 0,
                "max_score": total_score,
                "primary_error_cause": "未作答",
                "error_type": "empty_answer",
                "error_cause": "未作答",
                "knowledge_points": ["内容", "结构", "语言"],
                "overall_comment": "未作答",
                "grading_method": "empty_answer_short_circuit",
                "_model_key": "rule_based",
            }
            return {
                "rubric": empty_rubric,
                "grading": empty_grading,
                "comment": "未作答，本篇作文判0分。请补交作文后重新批改。",
                "suggested_score": 0,
                "max_score": total_score,
                "confidence": 1.0,
                "flagged": False,
                "model_key": "rule_based",
            }

        # 极短作文（<50字符）：不足以构成完整作文，判低分
        stripped_answer = student_answer_ocr.strip()
        if len(stripped_answer) < 50:
            logger.warning(f"[GradingService] 作文过短({len(stripped_answer)}字符)，判低分")
            empty_rubric = rubric if rubric else FALLBACK_ESSAY_RUBRIC.copy()
            template_result = self.essay_grader._template_grade(question, student_answer_ocr, total_score, confidence)
            template_result["grading_method"] = "short_essay_short_circuit"
            template_result["_model_key"] = "rule_based"
            comment = template_result.get("overall_comment", "作文过短，建议补全后重新批改。")
            steps = self.essay_grader._build_compatible_steps(template_result.get("dimensions", {}))
            template_result["steps"] = steps
            return {
                "rubric": empty_rubric,
                "grading": template_result,
                "comment": comment,
                "suggested_score": template_result.get("total_score", 0) if isinstance(template_result.get("total_score"), (int, float)) else 0,
                "max_score": total_score,
                "confidence": confidence if confidence > 0 else 0.85,
                "flagged": False,
                "model_key": "rule_based",
            }

        # 四维评分（内部已含 primary→volcengine→template 三级降级）
        grading_result = await self.essay_grader.grade(
            question=question,
            standard_answer=standard_answer,
            student_answer=student_answer_ocr,
            rubric=rubric or FALLBACK_ESSAY_RUBRIC,
            total_score=total_score,
            confidence=confidence,
            image_bytes=image_bytes,
        )

        # 综合评语（基于四维详情，避免数学化术语）
        comment = await self.essay_grader.generate_comment(
            question=question,
            score=grading_result.get("total_score", 0),
            max_score=grading_result.get("max_score", total_score),
            dimensions=grading_result.get("dimensions", {}),
            error_cause=grading_result.get("error_cause", "none"),
            knowledge_points=grading_result.get("knowledge_points", []),
        )

        # 若 generate_comment 返回空（LLM 失败且降级也失败），用 overall_comment 兜底
        if not comment:
            comment = grading_result.get("overall_comment", "")

        return {
            "rubric": rubric or FALLBACK_ESSAY_RUBRIC,
            "grading": grading_result,
            "comment": comment,
            "suggested_score": grading_result.get("total_score", 0),
            "max_score": grading_result.get("max_score", total_score),
            "confidence": confidence if confidence > 0 else 0.85,
            "flagged": confidence < settings.GRADING_LOW_CONFIDENCE_THRESHOLD if confidence > 0 else False,
            "model_key": grading_result.get("_model_key", "standard"),
        }


# Module-level singleton
grading_service = GradingService()
