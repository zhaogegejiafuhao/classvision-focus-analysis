"""语文作文四维批改引擎（从 grader.py 抽取）

内容40% + 结构20% + 语言25% + 书写15%。
输出结构兼容 MathGrader：含 steps/total_score/max_score/error_type/
error_cause/knowledge_points/_model_key，下游归因、错题本、导出无需改动。
额外输出 dimensions 字段供前端展示四维详情。
"""
import logging
from collections import OrderedDict
from typing import Optional

from backend.core.config import settings
from backend.services import async_llm
from backend.services.llm_utils import parse_llm_json
from backend.services.grader_prompts import (
    ESSAY_OCR_LOW_CONFIDENCE_HINT,
    ESSAY_GRADING_PROMPT,
    ESSAY_COMMENT_GENERATION_PROMPT,
)

logger = logging.getLogger(__name__)


class EssayGrader:
    """语文作文四维批改引擎（内容40%+结构20%+语言25%+书写15%）

    输出结构兼容 MathGrader：含 steps/total_score/max_score/error_type/
    error_cause/knowledge_points/_model_key，下游归因、错题本、导出无需改动。
    额外输出 dimensions 字段供前端展示四维详情。

    错因标签与 writing_graph.WRITING_ERROR_CAUSE_MAPPING 对齐：
    素材匮乏 / 逻辑断层 / 修辞单一 / 偏题跑题 / 书写潦草
    """

    DIMENSION_WEIGHTS = OrderedDict([
        ("content",     {"name": "内容", "max_score": 40}),
        ("structure",   {"name": "结构", "max_score": 20}),
        ("language",    {"name": "语言", "max_score": 25}),
        ("handwriting", {"name": "书写", "max_score": 15}),
    ])

    ESSAY_ERROR_CAUSES = ["素材匮乏", "逻辑断层", "修辞单一", "偏题跑题", "书写潦草"]

    # 维度→错因的默认映射（用于 _template_grade 降级时根据最低维度推算错因）
    _DIM_ERROR_MAP = {
        "content": "偏题跑题",
        "structure": "逻辑断层",
        "language": "修辞单一",
        "handwriting": "书写潦草",
    }

    # 维度→error_type 映射
    _DIM_ERROR_TYPE_MAP = {
        "content": "theme_deviation",
        "structure": "structure_issue",
        "language": "language_issue",
        "handwriting": "handwriting_issue",
    }

    def __init__(self):
        # No more self.qwen_client / self.doubao_client
        pass

    def _validate_error_cause(self, cause: str) -> str:
        """错因白名单校验，非法值降为 none"""
        if cause and cause in self.ESSAY_ERROR_CAUSES:
            return cause
        if cause and cause != "none":
            logger.warning(f"[EssayGrader] 非法 error_cause: {cause}，降级为 none")
        return "none"

    def _build_compatible_steps(self, dimensions: dict) -> list:
        """将四维结果转为 MathGrader 兼容的 steps 数组"""
        steps = []
        for dim_key, dim_meta in self.DIMENSION_WEIGHTS.items():
            dim_data = dimensions.get(dim_key, {})
            dim_score = float(dim_data.get("score", 0))
            dim_max = dim_meta["max_score"]
            dim_comment = dim_data.get("comment", "")
            dim_error_cause = dim_data.get("error_cause", "none")

            # correct 判定：得分率 >= 0.8 视为正确
            ratio = dim_score / dim_max if dim_max > 0 else 0
            correct = ratio >= 0.8

            steps.append({
                "step_id": f"dim_{dim_key}",
                "content": f"{dim_meta['name']}维度：{dim_comment}",
                "correct": correct,
                "score": dim_score,
                "rubric_ref": f"dim_{dim_key}",
                "error_reason": None if correct else (dim_error_cause if dim_error_cause != "none" else "维度得分偏低"),
                "max_score": dim_max,
            })
        return steps

    @staticmethod
    def _calc_essay_total(result: dict) -> float:
        """计算作文四维总分"""
        dims = result.get("dimensions", {})
        return sum(d.get("score", 0) for d in dims.values() if isinstance(d, dict))

    def _is_valid_essay_result(self, result: dict, student_answer: str) -> bool:
        """校验作文批改结果的合理性，防止LLM误判（如把正常作文判0分或说"无法辨识"）

        规则：
        1. 每个维度的score必须是数值且在0-max_score范围内
        2. 如果学生答案≥50字符但总分≤20/100，可能是误判（至少需要3个维度评语不含"无法辨识"）
        3. 如果评语中出现"无法辨识"但学生答案明显可读（≥30字符且含中文），也视为不合理
        """
        if not result or not isinstance(result, dict):
            return False

        dimensions = result.get("dimensions", {})
        if not dimensions or not isinstance(dimensions, dict):
            return False

        # 规则1：每个维度score必须是合理数值
        for dim_key, dim_data in dimensions.items():
            if not isinstance(dim_data, dict):
                return False
            score = dim_data.get("score")
            if not isinstance(score, (int, float)):
                return False
            max_score = self.DIMENSION_WEIGHTS.get(dim_key, {}).get("max_score", 100)
            if score < 0 or score > max_score:
                return False

        # 规则2：如果作文≥50字符但总分极低，检查是否误判
        total = self._calc_essay_total(result)
        answer_len = len(student_answer.strip()) if student_answer else 0
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in student_answer) if student_answer else False

        if answer_len >= 50 and has_chinese and total <= 20:
            # 检查评语中是否出现"无法辨识"
            all_comments = " ".join(
                d.get("comment", "") for d in dimensions.values() if isinstance(d, dict)
            )
            overall = result.get("overall_comment", "")
            combined = all_comments + overall
            if "无法辨识" in combined or "不可读" in combined or "无意义" in combined:
                logger.warning(f"[EssayGrader] 检测到误判：学生答案{answer_len}字符含中文，但评语说'无法辨识'，总分={total}")
                return False

        # 规则3：任何维度得分为0但答案明显有内容
        if answer_len >= 30 and has_chinese:
            zero_dims = sum(
                1 for d in dimensions.values()
                if isinstance(d, dict) and d.get("score", 0) == 0
            )
            if zero_dims >= 3:
                logger.warning(f"[EssayGrader] 检测到误判：学生答案{answer_len}字符含中文，但{zero_dims}个维度0分")
                return False

        return True

    def _normalize_to_total(self, raw_result: dict, total_score: int) -> dict:
        """将100分制四维分数归一化到题目总分（如 total_score=50 则按比例缩放）"""
        dimensions = raw_result.get("dimensions", {})
        if total_score == 100:
            # 无需缩放
            for dim_key in self.DIMENSION_WEIGHTS:
                dim_data = dimensions.get(dim_key, {})
                dim_data["max_score"] = self.DIMENSION_WEIGHTS[dim_key]["max_score"]
            total = sum(d.get("score", 0) for d in dimensions.values())
            raw_result["total_score"] = round(total, 1)
            raw_result["max_score"] = 100
            return raw_result

        # 按 total_score 缩放
        scale = total_score / 100.0
        new_dims = {}
        new_total = 0
        for dim_key, dim_meta in self.DIMENSION_WEIGHTS.items():
            dim_data = dimensions.get(dim_key, {})
            orig_max = dim_meta["max_score"]
            new_max = round(orig_max * scale, 1)
            new_score = round(float(dim_data.get("score", 0)) * scale, 1)
            # 钳制
            new_score = min(new_score, new_max)
            new_dims[dim_key] = {
                "score": new_score,
                "max_score": new_max,
                "comment": dim_data.get("comment", ""),
                "error_cause": self._validate_error_cause(dim_data.get("error_cause", "none")),
            }
            new_total += new_score

        raw_result["dimensions"] = new_dims
        raw_result["total_score"] = round(new_total, 1)
        raw_result["max_score"] = float(total_score)
        return raw_result

    def _template_grade(self, question: str, student_answer: str, total_score: int, confidence: float = 0.0) -> dict:
        """Level 2 降级：模板评分（基于文本长度/段落/置信度的启发式）"""
        text_len = len(student_answer)
        paragraphs = [p for p in student_answer.split("\n") if p.strip()]

        # 内容分：基于作文长度启发式
        if text_len < 200:
            content_ratio = 0.4
        elif text_len < 500:
            content_ratio = 0.6
        elif text_len < 800:
            content_ratio = 0.8
        else:
            content_ratio = 0.9

        # 结构分：基于段落分布
        if len(paragraphs) <= 1:
            structure_ratio = 0.3
        elif 2 <= len(paragraphs) <= 3:
            structure_ratio = 0.6
        elif 4 <= len(paragraphs) <= 6:
            structure_ratio = 0.85
        else:
            structure_ratio = 0.7

        # 语言分：默认
        language_ratio = 0.7

        # 书写分：基于 OCR 置信度
        if confidence > 0.85:
            handwriting_ratio = 0.9
        elif confidence > 0.7:
            handwriting_ratio = 0.7
        else:
            handwriting_ratio = 0.5

        scale = total_score / 100.0
        dimensions = {}
        ratios = {
            "content": content_ratio,
            "structure": structure_ratio,
            "language": language_ratio,
            "handwriting": handwriting_ratio,
        }
        for dim_key, dim_meta in self.DIMENSION_WEIGHTS.items():
            orig_max = dim_meta["max_score"]
            new_max = round(orig_max * scale, 1)
            new_score = round(orig_max * ratios[dim_key] * scale, 1)
            dimensions[dim_key] = {
                "score": new_score,
                "max_score": new_max,
                "comment": f"（降级评分：基于{dim_meta['name']}维度启发式规则，建议教师复核）",
                "error_cause": self._DIM_ERROR_MAP[dim_key] if ratios[dim_key] < 0.6 else "none",
            }

        # 选最低维度作为整体错因
        min_dim = min(ratios.items(), key=lambda x: x[1])[0]
        primary_error_cause = self._DIM_ERROR_MAP[min_dim] if ratios[min_dim] < 0.6 else "none"
        knowledge_points = [self.DIMENSION_WEIGHTS[min_dim]["name"]] if ratios[min_dim] < 0.8 else []

        return {
            "dimensions": dimensions,
            "primary_error_cause": primary_error_cause,
            "knowledge_points": knowledge_points,
            "overall_comment": f"（模板降级评分）本次作文得分偏低，主要薄弱维度为{self.DIMENSION_WEIGHTS[min_dim]['name']}，建议教师人工复核。",
        }

    async def _grade_with_fallback(self, prompt: str, question: str, student_answer: str, total_score: int) -> dict:
        """带降级的批改调用：primary → volcengine → template 三级降级"""
        # Level 0: Primary LLM
        try:
            logger.info("[EssayGrader] 尝试主模型评分...")
            result = await async_llm.async_chat_json(
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                max_tokens=2048,
                mode="deep",
            )
            if isinstance(result, dict) and "dimensions" in result:
                # 校验作文评分合理性
                if self._is_valid_essay_result(result, student_answer):
                    result["_model_key"] = "standard"
                    result["grading_method"] = "essay_llm"
                    logger.info(f"[EssayGrader] 主模型评分成功: primary_error_cause={result.get('primary_error_cause')}")
                    return result
                else:
                    logger.warning(f"[EssayGrader] 主模型评分不合理（可能误判），触发降级: total_score={self._calc_essay_total(result)}")
            else:
                logger.warning(f"[EssayGrader] 主模型返回结构异常: {str(result)[:100]}")
        except Exception as e:
            logger.warning(f"[EssayGrader] 主模型失败: {type(e).__name__}: {e}")

        # Level 1: Volcengine
        if settings.VOLCENGINE_API_KEY and settings.DOUBAO_ENDPOINT_ID:
            try:
                logger.info("[EssayGrader] 降级到豆包...")
                resp = await async_llm.async_chat_with_provider(
                    provider_name="volcengine",
                    messages=[{"role": "user", "content": prompt}],
                    api_key=settings.VOLCENGINE_API_KEY,
                    base_url=settings.VOLCENGINE_BASE_URL,
                    model=settings.DOUBAO_ENDPOINT_ID,
                    temperature=0.2,
                    max_tokens=2048,
                )
                result = parse_llm_json(resp.get("content", ""))
                if isinstance(result, dict) and "dimensions" in result:
                    if self._is_valid_essay_result(result, student_answer):
                        result["_model_key"] = "doubao"
                        result["grading_method"] = "essay_llm"
                        logger.info(f"[EssayGrader] 豆包评分成功: primary_error_cause={result.get('primary_error_cause')}")
                        return result
                    else:
                        logger.warning(f"[EssayGrader] 豆包评分也不合理，继续降级: total_score={self._calc_essay_total(result)}")
                else:
                    logger.warning(f"[EssayGrader] 豆包返回结构异常: {str(result)[:100]}")
            except Exception as e:
                logger.warning(f"[EssayGrader] 豆包失败: {type(e).__name__}: {e}")

        # Level 2: template fallback
        logger.warning("[EssayGrader] Level 2 降级：使用模板评分")
        template_result = self._template_grade(question, student_answer, total_score)
        template_result["_model_key"] = "template_fallback"
        template_result["grading_method"] = "essay_template_fallback"
        return template_result

    async def grade(
        self,
        question: str,
        standard_answer: str,
        student_answer: str,
        rubric: Optional[dict] = None,  # 接收但不使用，保持与 MathGrader.grade 签名兼容
        total_score: int = 100,
        confidence: float = 0.0,
        image_bytes: Optional[bytes] = None,  # 预留：未来用 VL 模型识别书写
        is_geometry: bool = False,  # 接收但不使用，保持签名兼容
    ) -> dict:
        """四维批改主入口

        Args:
            question: 作文题目
            standard_answer: 写作要求（参考）
            student_answer: 学生作文（OCR提取）
            rubric: 接收但不使用（保持签名兼容）
            total_score: 题目总分（默认100，若为50则按比例缩放四维）
            confidence: OCR置信度，作为书写维度弱信号
            image_bytes: 预留 VL 识别书写
            is_geometry: 接收但不使用（保持签名兼容）

        Returns:
            dict: 兼容 MathGrader 输出的批改结果，额外含 dimensions 字段
        """
        # OCR 置信度提示
        if confidence < 0.7:
            ocr_hint = ESSAY_OCR_LOW_CONFIDENCE_HINT.format(confidence=confidence)
        else:
            ocr_hint = ""

        # 截断超长作文（避免 prompt 过长）
        truncated_answer = student_answer[:3000] if len(student_answer) > 3000 else student_answer

        prompt = ESSAY_GRADING_PROMPT.format(
            question=question,
            standard_answer=standard_answer or "（无特殊要求）",
            student_answer=truncated_answer,
            ocr_confidence_hint=ocr_hint,
        )

        # 调用 LLM 评分
        raw_result = await self._grade_with_fallback(prompt, question, truncated_answer, total_score)

        # 校验并归一化
        dimensions = raw_result.get("dimensions", {})
        for dim_key in self.DIMENSION_WEIGHTS:
            if dim_key not in dimensions:
                logger.warning(f"[EssayGrader] LLM 输出缺失维度 {dim_key}，补默认值")
                dimensions[dim_key] = {
                    "score": 0,
                    "max_score": self.DIMENSION_WEIGHTS[dim_key]["max_score"],
                    "comment": "（LLM 未输出该维度，已补默认值）",
                    "error_cause": "none",
                }
            else:
                # 校验每个维度
                dim_data = dimensions[dim_key]
                dim_data["error_cause"] = self._validate_error_cause(dim_data.get("error_cause", "none"))
                # 分数钳制
                max_s = self.DIMENSION_WEIGHTS[dim_key]["max_score"]
                try:
                    s = float(dim_data.get("score", 0))
                except (TypeError, ValueError):
                    s = 0
                dim_data["score"] = max(0, min(s, max_s))
                dim_data["max_score"] = max_s
        raw_result["dimensions"] = dimensions

        # 归一化到题目总分
        raw_result = self._normalize_to_total(raw_result, total_score)

        # error_cause / error_type
        primary_error_cause = self._validate_error_cause(raw_result.get("primary_error_cause", "none"))
        raw_result["error_cause"] = primary_error_cause

        # error_type：根据 primary_error_cause 反推
        cause_to_type = {v: self._DIM_ERROR_TYPE_MAP[k] for k, v in self._DIM_ERROR_MAP.items()}
        raw_result["error_type"] = cause_to_type.get(primary_error_cause, "none")

        # knowledge_points
        if not raw_result.get("knowledge_points"):
            # 找得分率最低的维度
            min_dim = min(
                self.DIMENSION_WEIGHTS.keys(),
                key=lambda k: raw_result["dimensions"][k]["score"] / max(self.DIMENSION_WEIGHTS[k]["max_score"], 1)
            )
            raw_result["knowledge_points"] = [self.DIMENSION_WEIGHTS[min_dim]["name"]]
        else:
            # 清洗：只保留字符串
            kps = [str(k) for k in raw_result["knowledge_points"] if k]
            raw_result["knowledge_points"] = kps[:2]

        # 构造兼容 MathGrader 的 steps 数组
        raw_result["steps"] = self._build_compatible_steps(raw_result["dimensions"])

        # 保留 overall_comment 作为综合评语（如 LLM 已生成则直接用，否则由 generate_comment 生成）
        if not raw_result.get("comment"):
            raw_result["comment"] = raw_result.get("overall_comment", "")

        return raw_result

    async def generate_comment(
        self,
        question: str,
        score: float,
        max_score: float,
        dimensions: dict,
        error_cause: str,
        knowledge_points: list,
    ) -> str:
        """生成作文综合评语（基于四维详情，评语更贴合作文特性）"""
        # 准备四维详情
        dim_data = {}
        for dim_key, dim_meta in self.DIMENSION_WEIGHTS.items():
            d = dimensions.get(dim_key, {})
            dim_data[f"{dim_key}_score"] = d.get("score", 0)
            dim_data[f"{dim_key}_max"] = d.get("max_score", dim_meta["max_score"])
            dim_data[f"{dim_key}_comment"] = d.get("comment", "（无评语）")

        prompt = ESSAY_COMMENT_GENERATION_PROMPT.format(
            question=question,
            score=score,
            max_score=max_score,
            error_cause=error_cause,
            knowledge_points="、".join(knowledge_points) if knowledge_points else "无明显薄弱",
            **dim_data,
        )

        try:
            result = await async_llm.async_chat(
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=256,
                mode="deep",
            )
            return result.get("content", "")
        except Exception:
            # 降级为模板评语
            ratio = score / max_score if max_score > 0 else 0
            if ratio >= 0.85:
                return "本文整体表现优秀，继续保持。"
            elif ratio >= 0.6:
                weak = knowledge_points[0] if knowledge_points else "相关维度"
                return f"本文得分{score}/{max_score}，{weak}有待加强，建议针对性练习。"
            else:
                weak = knowledge_points[0] if knowledge_points else "整体结构"
                return f"本文得分{score}/{max_score}偏低，{weak}问题突出，请认真修改。"
