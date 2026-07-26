"""柔性 Rubric 生成器（从 grader.py 抽取）

包含：
- LRUCache：rubric 缓存
- rule_based_grade：Level 1 降级的关键词规则评分
- RubricGenerator：AI 推导评分标准（带 Level 0/1/2 降级）
"""
import hashlib
import logging
import re
from collections import OrderedDict
from typing import Optional

from backend.services.llm_utils import parse_llm_json
from backend.core.config import settings
from backend.services import async_llm
from backend.services.grader_prompts import (
    RUBRIC_GENERATION_PROMPT,
    FALLBACK_RUBRIC,
)

logger = logging.getLogger(__name__)


# ===== Rubric LRU 缓存 =====

class LRUCache:
    def __init__(self, maxsize=500):
        self._cache: OrderedDict = OrderedDict()
        self._maxsize = maxsize

    def get(self, key):
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        return None

    def put(self, key, value):
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._maxsize:
            self._cache.popitem(last=False)

    def clear(self):
        self._cache.clear()

    def __len__(self):
        return len(self._cache)


_rubric_cache = LRUCache(maxsize=500)


# ===== Level 1 降级：基于关键词的规则评分 =====

def rule_based_grade(question: str, student_answer: str, rubric: dict) -> dict:
    """Level 1降级：基于关键词的规则评分"""
    steps = []
    total_score = 0
    rubric_steps = rubric.get("steps", FALLBACK_RUBRIC["steps"])

    for rs in rubric_steps:
        score = 0
        correct = False
        keywords = rs.get("keywords", [])

        # 检查学生答案中是否包含关键词
        matched_keywords = [kw for kw in keywords if kw in student_answer]

        if matched_keywords:
            # 命中关键词数占比决定得分
            ratio = len(matched_keywords) / max(len(keywords), 1)
            score = round(rs.get("score", 1) * ratio, 1)
            correct = ratio >= 0.5

        steps.append({
            "step_id": rs["step_id"],
            "content": f"关键词匹配: {', '.join(matched_keywords)}" if matched_keywords else "未匹配到关键词",
            "correct": correct,
            "score": score,
            "rubric_ref": rs["step_id"],
            "error_reason": None if correct else "未检测到关键步骤",
        })
        total_score += score

    return {
        "steps": steps,
        "total_score": total_score,
        "max_score": sum(s.get("score", 0) for s in rubric_steps),
        "error_type": "rule_based",
        "error_cause": "none",
        "knowledge_points": [],
        "comment": "（降级评分：基于关键词匹配，建议教师复核）",
        "grading_method": "rule_based_fallback",
    }


# ===== Rubric 生成器 =====

class RubricGenerator:
    """柔性Rubric生成器"""

    # 简单计算题预设rubric（跳过LLM调用，加速响应）
    @staticmethod
    def _get_preset_rubric_for_simple_calc(question: str, total_score: int) -> Optional[dict]:
        """对纯算术表达式题目返回预设3步rubric，避免调用LLM

        判定条件：题目仅含数字、运算符、括号、空白，且不含字母（代数变量）。
        """
        stripped = question.strip()
        # 移除"计算："、"求值："等前缀
        for prefix in ("计算：", "计算:", "求值：", "求值:", "化简：", "化简:", "求解：", "求解:"):
            if stripped.startswith(prefix):
                stripped = stripped[len(prefix):].strip()
                break

        # 必须含数字
        if not any(c.isdigit() for c in stripped):
            return None
        # 排除含字母的代数表达式
        if re.search(r'[a-zA-Z]', stripped):
            return None
        # 排除含几何/证明/应用关键词
        for kw in ("证明", "求证", "三角形", "圆", "平行", "垂直", "应用", "工程", "方案"):
            if kw in question:
                return None
        # 长度限制
        if len(stripped) > 80:
            return None
        # 必须含运算符
        if not any(op in stripped for op in "+-×÷*/"):
            return None

        # 分配分数：乘除2/5，加减2/5，答案1/5
        s_mul_div = max(1, total_score * 2 // 5)
        s_add_sub = max(1, total_score * 2 // 5)
        s_answer = max(1, total_score - s_mul_div - s_add_sub)
        # 钳制总和等于 total_score
        while s_mul_div + s_add_sub + s_answer > total_score:
            if s_mul_div > 1:
                s_mul_div -= 1
            elif s_add_sub > 1:
                s_add_sub -= 1
            else:
                s_answer -= 1
        while s_mul_div + s_add_sub + s_answer < total_score:
            s_answer += 1

        logger.info(f"[RubricGenerator] 简单计算题使用预设rubric(3步): {s_mul_div}+{s_add_sub}+{s_answer}={total_score}")
        return {
            "steps": [
                {"step_id": "s1", "description": "先乘除：正确计算乘法和除法",
                 "score": s_mul_div, "required": True,
                 "keywords": ["×", "*", "÷", "/", "乘", "除"], "example": ""},
                {"step_id": "s2", "description": "后加减：正确计算加法和减法",
                 "score": s_add_sub, "required": True,
                 "keywords": ["+", "-", "加", "减"], "example": ""},
                {"step_id": "s3", "description": "得出最终答案",
                 "score": s_answer, "required": True,
                 "keywords": ["=", "答", "故", "因此"], "example": ""},
            ]
        }

    @staticmethod
    def _is_valid_rubric(result: dict, total_score: int, min_steps: int = 3) -> bool:
        """校验rubric结果是否有效

        有效条件：
        1. 是dict且包含 steps 字段（list）
        2. steps 数量 >= min_steps（默认3）
        3. 每个 step 有 score 字段
        4. 步骤分数总和接近 total_score（允许±2分误差）
        """
        if not result or not isinstance(result, dict):
            return False
        steps = result.get("steps", [])
        if not isinstance(steps, list) or len(steps) < min_steps:
            return False
        total = 0
        for s in steps:
            if not isinstance(s, dict):
                return False
            score = s.get("score", 0)
            if not isinstance(score, (int, float)):
                return False
            total += score
        # 允许±2分误差（LLM可能四舍五入）
        if abs(total - total_score) > 2:
            logger.warning(f"[RubricGenerator] rubric分数总和{total}与total_score{total_score}相差过大")
            return False
        return True

    def __init__(self):
        # No more self.sf_client / self.doubao_client
        pass

    async def generate(
        self, question: str, standard_answer: str, total_score: int, subject: str = "math", grade: int = 7
    ) -> dict:
        """AI自动推导评分标准（带降级）"""
        # 查缓存
        cache_key = hashlib.md5(f"{question}||{standard_answer}||{total_score}".encode()).hexdigest()
        cached = _rubric_cache.get(cache_key)
        if cached:
            logger.debug(f"[RubricGenerator] 命中缓存! key={cache_key[:8]}")
            return cached.copy()

        # 简单计算题预设rubric（跳过LLM，加速响应）
        if subject == "math":
            preset = self._get_preset_rubric_for_simple_calc(question, total_score)
            if preset is not None:
                _rubric_cache.put(cache_key, preset.copy())
                return preset

        prompt = RUBRIC_GENERATION_PROMPT.format(
            subject=subject,
            total_score=total_score,
            question=question,
            standard_answer=standard_answer,
        )

        # Try primary LLM (SiliconFlow via get_llm())
        try:
            logger.info("[RubricGenerator] 尝试主模型API...")
            result = await async_llm.async_chat_json(
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=1024,
                mode="deep",
            )
            # 校验rubric有效性
            if self._is_valid_rubric(result, total_score):
                _rubric_cache.put(cache_key, result.copy() if isinstance(result, dict) else result)
                logger.info(f"[RubricGenerator] 已缓存, key={cache_key[:8]}, 步骤数={len(result.get('steps', []))}, 当前缓存条数={len(_rubric_cache._cache)}")
                return result
            else:
                steps_count = len(result.get("steps", [])) if isinstance(result, dict) else 0
                logger.warning(f"[RubricGenerator] 主模型返回rubric无效(steps={steps_count}, 预期>={3})，降级...")
        except Exception as e:
            logger.warning(f"[RubricGenerator] 主模型失败: {type(e).__name__}, 降级...")

        # Try Volcengine fallback
        if settings.VOLCENGINE_API_KEY and settings.DOUBAO_ENDPOINT_ID:
            try:
                logger.info("[RubricGenerator] 降级到豆包...")
                resp = await async_llm.async_chat_with_provider(
                    provider_name="volcengine",
                    messages=[{"role": "user", "content": prompt}],
                    api_key=settings.VOLCENGINE_API_KEY,
                    base_url=settings.VOLCENGINE_BASE_URL,
                    model=settings.DOUBAO_ENDPOINT_ID,
                    temperature=0.1,
                    max_tokens=1024,
                )
                result = parse_llm_json(resp.get("content", ""))
                if self._is_valid_rubric(result, total_score):
                    _rubric_cache.put(cache_key, result.copy() if isinstance(result, dict) else result)
                    logger.info(f"[RubricGenerator] 已缓存(豆包), key={cache_key[:8]}, 步骤数={len(result.get('steps', []))}, 当前缓存条数={len(_rubric_cache._cache)}")
                    return result
                else:
                    logger.warning("[RubricGenerator] 豆包返回rubric也无效，使用规则兜底")
            except Exception as e:
                logger.error(f"[RubricGenerator] 豆包也失败: {type(e).__name__}: {e}")

        # Level 0 fallback
        logger.warning("[RubricGenerator] Level 0降级：使用规则兜底评分标准")
        return FALLBACK_RUBRIC.copy()
