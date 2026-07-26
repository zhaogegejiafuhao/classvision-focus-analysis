"""数学题过程分批改引擎（从 grader.py 抽取）

集成动态模型路由 + 并行竞速降级策略。
"""
import asyncio
import json
import logging
import time

from backend.core.config import settings
from backend.services import async_llm
from backend.services.llm_utils import parse_llm_json
from backend.services.model_router import model_router, MODELS
from backend.services.grader_prompts import (
    MATH_GRADING_PROMPT,
    GEOMETRY_AUXILIARY_LINE_PROMPT_SECTION,
    COMMENT_GENERATION_PROMPT,
)
from backend.services.rubric_generator import rule_based_grade

logger = logging.getLogger(__name__)


class MathGrader:
    """数学题过程分批改引擎（集成动态模型路由）"""

    def __init__(self):
        # No more self.doubao_client / self.qwen_client
        self.router = model_router

    def _get_model_and_mode(self, model_key: str):
        """根据路由key获取模型名和调用模式"""
        model_name = MODELS.get(model_key, MODELS["standard"])
        if model_key == "lightweight":
            return model_name, "fast"
        else:
            return model_name, "deep"

    async def grade(
        self,
        question: str,
        standard_answer: str,
        student_answer: str,
        rubric: dict,
        is_geometry: bool = False,
        confidence: float = 0.0,
    ) -> dict:
        """基于rubric的过程分批改（集成动态模型路由，带降级）

        Args:
            question: 题目文本
            standard_answer: 标准答案
            student_answer: 学生解答（OCR提取）
            rubric: 评分标准
            is_geometry: 是否为几何题
            confidence: 置信度（0.0-1.0），用于动态路由决策

        Returns:
            dict: 批改结果，含 steps/total_score/max_score 等
        """
        rubric_json = json.dumps(rubric.get("steps", []), ensure_ascii=False)

        # 几何题时追加辅助线评估指令
        geometry_section = GEOMETRY_AUXILIARY_LINE_PROMPT_SECTION if is_geometry else ""

        prompt = MATH_GRADING_PROMPT.format(
            question=question,
            rubric_json=rubric_json,
            standard_answer=standard_answer,
            student_answer=student_answer,
            geometry_section=geometry_section,
        )

        # 动态路由选择模型
        try:
            model_key = self.router.route(
                question=question,
                confidence=confidence,
                is_geometry=is_geometry,
            )
            logger.info(f"[MathGrader] 动态路由选择模型: {model_key} ({MODELS.get(model_key, model_key)})")
        except Exception as e:
            logger.warning(f"[MathGrader] 路由异常，使用默认模型: {type(e).__name__}: {e}")
            model_key = "standard"

        model_name, mode = self._get_model_and_mode(model_key)

        # 根据路由结果调用对应模型，失败降级
        result = await self._grade_with_fallback(model_name, mode, model_key, prompt, question, student_answer, rubric)

        # 在结果中记录使用的模型key（供后续反馈追踪）
        result["_model_key"] = model_key

        # 计算总过程分
        steps = result.get("steps", [])
        total_score = sum(s.get("score", 0) for s in steps)
        max_score = sum(s.get("score", 0) for s in rubric.get("steps", []))

        result["total_score"] = total_score
        result["max_score"] = max_score

        return result

    async def _call_model_unified(
        self,
        model_key: str,
        prompt: str,
    ) -> dict:
        """统一模型调用封装（屏蔽 SiliconFlow / 火山引擎差异）

        Args:
            model_key: 模型路由key（multimodal / standard / lightweight / long_context）
            prompt: 批改提示词

        Returns:
            dict: LLM返回的JSON解析结果

        Raises:
            Exception: 调用失败时抛出
        """
        model_name = MODELS.get(model_key, MODELS["standard"])

        # multimodal 是豆包endpoint ID，必须走火山引擎API
        if model_key == "multimodal" and settings.VOLCENGINE_API_KEY and settings.DOUBAO_ENDPOINT_ID:
            resp = await async_llm.async_chat_with_provider(
                provider_name="volcengine",
                messages=[{"role": "user", "content": prompt}],
                api_key=settings.VOLCENGINE_API_KEY,
                base_url=settings.VOLCENGINE_BASE_URL,
                model=settings.DOUBAO_ENDPOINT_ID,
                temperature=0.1,
                max_tokens=2048,
            )
            return parse_llm_json(resp.get("content", ""))

        # 其他模型走 SiliconFlow API（async_chat_json自动解析JSON）
        mode = "fast" if model_key == "lightweight" else "deep"
        return await async_llm.async_chat_json(
            messages=[{"role": "user", "content": prompt}],
            model=model_name,
            temperature=0.1,
            max_tokens=2048,
            mode=mode,
        )

    async def _grade_with_fallback(
        self,
        primary_model: str,
        primary_mode: str,
        primary_key: str,
        prompt: str,
        question: str,
        student_answer: str,
        rubric: dict,
    ) -> dict:
        """带降级的批改调用（并行竞速版）

        策略：
          1. 并行启动主模型 + 备选模型（standard + 豆包），用 asyncio.wait FIRST_COMPLETED 竞速
          2. 任一模型返回 **有效** 结果立即采用，取消其他任务
          3. 所有模型失败或返回无效 → 最后用 rule_based 兜底

        相比串行降级，并行可将几何题从 208s 降至 ~90s（取最快模型耗时）。

        Args:
            primary_model: 首选模型名称（保留兼容，实际用 primary_key 路由）
            primary_mode: 首选调用模式（保留兼容）
            primary_key: 首选模型路由key
            prompt: 批改提示词
            question: 题目
            student_answer: 学生答案
            rubric: 评分标准

        Returns:
            dict: 批改结果
        """
        rubric_steps = rubric.get("steps", []) if isinstance(rubric, dict) else []
        rubric_step_count = len(rubric_steps) if rubric_steps else 0
        min_expected_steps = max(1, (rubric_step_count + 1) // 2) if rubric_step_count > 0 else 1

        # 构建候选模型列表（去重，保持优先级：主模型 -> standard -> 豆包）
        candidates = [primary_key]
        if primary_key != "standard":
            candidates.append("standard")
        # 豆包作为最后兜底（仅在配置可用时加入）
        has_volcengine = bool(settings.VOLCENGINE_API_KEY and settings.DOUBAO_ENDPOINT_ID)
        if has_volcengine and "multimodal" not in candidates:
            candidates.append("multimodal")
        # 去重（避免 primary_key == standard 时重复）
        seen = set()
        candidates = [c for c in candidates if not (c in seen or seen.add(c))]

        logger.info(f"[MathGrader] 并行批改启动，候选模型: {candidates}")

        # 嵌套函数：调用单个模型，成功返回 (key, result)，失败抛异常
        async def _try_model(key: str) -> tuple[str, dict]:
            t0 = time.time()
            result = await self._call_model_unified(key, prompt)
            elapsed = time.time() - t0
            if not self._is_valid_grading_result(result, rubric_step_count, min_expected_steps):
                steps_count = len(result.get("steps", [])) if isinstance(result, dict) else 0
                raise ValueError(f"steps过少({steps_count}/{rubric_step_count}, 期望>={min_expected_steps})")
            logger.info(f"[MathGrader] 模型 {key} 返回有效结果 (耗时 {elapsed:.1f}s)")
            return key, result

        # 用独立字典维护 task -> key 映射，不被 pop 破坏
        task_to_key = {
            asyncio.ensure_future(_try_model(key)): key
            for key in candidates
        }

        # 竞速：任一任务返回有效结果就采用，取消其他任务
        win_result = None
        try:
            while task_to_key:
                done, pending = await asyncio.wait(
                    task_to_key.keys(),
                    return_when=asyncio.FIRST_COMPLETED,
                )
                for done_task in done:
                    key = task_to_key.pop(done_task)
                    try:
                        win_key, result = done_task.result()
                        # 找到有效结果，取消所有未完成任务并返回
                        for p in pending:
                            p.cancel()
                        for t in list(task_to_key.keys()):
                            t.cancel()
                        result["_model_key"] = win_key
                        win_result = result
                        break
                    except Exception as e:
                        logger.warning(f"[MathGrader] 模型 {key} 失败/无效: {type(e).__name__}: {e}，等待其他模型...")
                if win_result is not None:
                    break
        except Exception as e:
            logger.error(f"[MathGrader] 并行批改异常: {type(e).__name__}: {e}")

        if win_result is not None:
            return win_result

        # 所有模型都失败 → rule_based 兜底
        logger.warning("[MathGrader] 所有模型均失败或返回无效，使用规则评分兜底")
        return rule_based_grade(question, student_answer, rubric)

    @staticmethod
    def _is_valid_grading_result(result: dict, rubric_step_count: int, min_expected_steps: int) -> bool:
        """校验LLM批改结果是否有效

        有效条件（必须同时满足）：
        1. 是dict且包含 steps 字段（list），且 steps 数量 >= min_expected_steps
        2. 每个step有score字段（数字）

        注意：error_cause 不作为豁免条件。即使识别出错因，
        如果步骤数过少仍判无效（因为评分不完整，学生得分会失真）。

        Args:
            result: LLM返回的解析后字典
            rubric_step_count: rubric中的步骤总数
            min_expected_steps: 最少期望的步骤数

        Returns:
            bool: 结果是否有效
        """
        if not result or not isinstance(result, dict):
            return False

        # steps 字段必须存在且为list
        steps = result.get("steps", [])
        if not isinstance(steps, list):
            return False
        if len(steps) == 0:
            return False

        # 每个 step 必须有 score 字段（数字）
        for s in steps:
            if not isinstance(s, dict):
                return False
            score = s.get("score")
            if not isinstance(score, (int, float)):
                return False

        # 如果 rubric 有步骤，steps 数量应至少达到 min_expected_steps
        if rubric_step_count > 0 and len(steps) < min_expected_steps:
            return False

        return True

    async def generate_comment(
        self,
        question: str,
        score: float,
        max_score: float,
        error_steps: list,
        error_type: str,
        knowledge_points: list,
    ) -> str:
        """生成个性化评语"""
        prompt = COMMENT_GENERATION_PROMPT.format(
            question=question,
            score=score,
            max_score=max_score,
            error_steps=json.dumps(error_steps, ensure_ascii=False),
            error_type=error_type,
            knowledge_points="、".join(knowledge_points),
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
            if score == max_score:
                return "解答完全正确，继续保持！"
            return f"本次得分{score}/{max_score}，请注意{knowledge_points[0] if knowledge_points else '相关知识点'}的巩固练习。"
