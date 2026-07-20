"""ClassVision LLM批改层 - 柔性Rubric + 过程分判定"""
import asyncio
import json
import logging
import re
import hashlib
import time
from collections import OrderedDict
from typing import Optional

from backend.services.llm_utils import parse_llm_json
from backend.core.config import settings
from backend.services.geometry_analyzer import GeometryAnalyzer, is_geometry_question, detect_geometry_with_llm_fallback
from backend.services.model_router import DynamicModelRouter, model_router, MODELS
from backend.services import async_llm
from backend.services.llm_client import LLMError

logger = logging.getLogger(__name__)


# ===== Prompt 模板 =====

RUBRIC_GENERATION_PROMPT = """你是一位资深的{subject}教师，请为以下题目推导步骤评分标准。

## 题目（{total_score}分）
{question}

## 标准答案
{standard_answer}

请推导评分标准，输出JSON：
1. 列出解题关键步骤（3-6步），每步描述应具体明确
2. 为每个步骤分配分值（总和={total_score}），前序步骤分值稍多、末尾步骤稍少
3. 标注 required（true=必须项，没写直接0分 / false=加分项）
4. 提供该步骤的关键词匹配列表和示例表达

【注意】至少生成3个步骤，确保评分粒度足够细。对于简单计算题，拆分为：列式→计算→结果三步。

严格输出以下JSON格式，不要输出其他内容：
{{"steps": [{{"step_id": "s1", "description": "...", "score": N, "required": true, "keywords": ["..."], "example": "..."}}]}}"""

MATH_GRADING_PROMPT = """你是一位专业的数学教师，请基于以下评分标准对学生解答进行逐步批改。

【重要】学生的解答文本是可正常阅读的，请仔细阅读后给出评分。不要说"无法辨识"——文本是清晰可读的。

## 题目
{question}

## 评分标准（Rubric）
{rubric_json}

## 标准答案
{standard_answer}

## 学生解答
{student_answer}
{geometry_section}

## 批改要求
请逐步骤判定：
1. 匹配每个rubric步骤，判断学生是否完成
2. 对每个步骤给出correct/partial/missing判定和得分
3. 评分锚点：
   - 完全正确：给该步骤满分
   - 部分正确（思路对但计算错）：给该步骤一半分数
   - 完全错误或缺失：给0分
4. 指出具体错误原因（如有）
5. 生成一句个性化评语（结合错因与知识薄弱点）
6. 对每个错误步骤标注错因标签（从以下6种选择：计算粗心、概念混淆、审题不清、辅助线缺失、逻辑跳步、知识缺失）
7. 如果学生答案与标准答案完全一致，所有步骤应标记为correct，error_cause填"none"

严格输出以下JSON格式，不要输出其他内容：
{{"steps": [{{"step_id": "s1", "content": "学生写的步骤内容", "correct": true, "score": N, "rubric_ref": "s1", "error_reason": null}}], "error_type": "calculation_error|concept_error|process_error|none", "error_cause": "计算粗心|概念混淆|审题不清|辅助线缺失|逻辑跳步|知识缺失|none", "knowledge_points": ["知识点1"], "comment": "个性化评语"}}"""

# 几何题辅助线评估指令（追加到MATH_GRADING_PROMPT的geometry_section占位符）
GEOMETRY_AUXILIARY_LINE_PROMPT_SECTION = """
## 几何辅助线评估提示
本题是几何证明/计算题，请特别关注以下方面：
- 学生是否画了辅助线（如虚线、延长线、连接线等）
- 辅助线是否正确（方向、位置是否合理）
- 是否缺失关键辅助线
- 辅助线使用情况应反映在错因标签中（如"辅助线缺失"）
- 评语中需包含辅助线相关的提示或建议
"""

COMMENT_GENERATION_PROMPT = """基于以下批改结果，生成一句简短个性化评语。

题目：{question}
学生得分：{score}/{max_score}
错误步骤：{error_steps}
错因类型：{error_type}
薄弱知识点：{knowledge_points}

要求：评语要具体指出问题并给出改进建议，不要空泛鼓励。"""


# ===== 作文批改 Prompt =====

ESSAY_OCR_LOW_CONFIDENCE_HINT = """**提示**：本次文本识别置信度较低（{confidence:.2f}），书写维度评分时适当关注，但其他维度仍以文本实际内容为准。"""

ESSAY_GRADING_PROMPT = """你是一位资深的语文作文阅卷老师，请按中考作文四维评分标准对以下学生作文进行评分。

【重要】下面的学生作文文本是完整的、可正常阅读的中文文本，请仔细阅读全文后给出评分。不要说"无法辨识"或"内容不可读"——文本内容是清晰可读的，你应当基于文本实际内容进行评分。

## 作文题目
{question}

## 写作要求（参考）
{standard_answer}

## 学生作文
{student_answer}

{ocr_confidence_hint}

## 评分标准（总分100分）
请按以下四个维度独立评分，评分要参考以下锚点：
- 内容：切题且素材丰富=28-40分；切题但素材一般=20-27分；偏题=10-19分；严重跑题=0-9分
- 结构：结构完整且层次清晰=14-20分；结构基本完整=10-13分；结构混乱=5-9分；无结构=0-4分
- 语言：流畅且有修辞=18-25分；通顺但平淡=12-17分；有语病=6-11分；不通顺=0-5分
- 书写：无错别字=12-15分；少量错别字=8-11分；较多错别字=4-7分；大量错别字=0-3分

1. **内容**（满分40分）：审题立意是否准确、主题是否明确、素材是否丰富贴切、思想感情是否真实健康
2. **结构**（满分20分）：篇章布局是否合理、段落过渡是否自然、开头结尾是否呼应、详略是否得当
3. **语言**（满分25分）：用词是否准确丰富、修辞是否恰当、句式是否有变化、是否通顺流畅
4. **书写**（满分15分）：是否有错别字、语句是否通顺（基于文本质量推断书写规范性）

## 评分要求
- 必须仔细阅读学生作文全文后再评分，评语要引用原文片段佐证
- 每个维度从以下5种错因中选1种最贴切的（无错填"none"）：素材匮乏、逻辑断层、修辞单一、偏题跑题、书写潦草
- 选出最主要的一个错因作为整体错因（primary_error_cause）
- 列出最薄弱的1-2个维度名称作为knowledge_points（从"内容/结构/语言/书写"中选）

严格输出以下JSON格式，不要输出其他内容：
{{"dimensions": {{"content": {{"score": N, "max_score": 40, "comment": "...", "error_cause": "偏题跑题|素材匮乏|none"}}, "structure": {{"score": N, "max_score": 20, "comment": "...", "error_cause": "逻辑断层|none"}}, "language": {{"score": N, "max_score": 25, "comment": "...", "error_cause": "修辞单一|none"}}, "handwriting": {{"score": N, "max_score": 15, "comment": "...", "error_cause": "书写潦草|none"}}}}, "primary_error_cause": "素材匮乏|逻辑断层|修辞单一|偏题跑题|书写潦草|none", "knowledge_points": ["薄弱维度1"], "overall_comment": "综合评语"}}"""

ESSAY_COMMENT_GENERATION_PROMPT = """基于以下作文四维批改结果，生成一段简短的个性化评语。

## 作文题目
{question}

## 总得分
{score}/{max_score}

## 四维详情
- 内容（{content_score}/{content_max}）：{content_comment}
- 结构（{structure_score}/{structure_max}）：{structure_comment}
- 语言（{language_score}/{language_max}）：{language_comment}
- 书写（{handwriting_score}/{handwriting_max}）：{handwriting_comment}

## 主要错因
{error_cause}

## 薄弱维度
{knowledge_points}

## 要求
1. 评语要贴合语文作文特性，避免出现"步骤评分""推理过程"等数学化术语
2. 先肯定优点，再指出最关键的1-2个改进方向
3. 不要超过100字，简洁有力，给出可操作的修改建议"""

# Level 0降级：作文四维占位 rubric（供题库存储使用）
FALLBACK_ESSAY_RUBRIC = {
    "type": "essay",
    "dimensions": [
        {"step_id": "dim_content", "description": "内容", "score": 40, "required": True, "keywords": [], "example": ""},
        {"step_id": "dim_structure", "description": "结构", "score": 20, "required": True, "keywords": [], "example": ""},
        {"step_id": "dim_language", "description": "语言", "score": 25, "required": True, "keywords": [], "example": ""},
        {"step_id": "dim_handwriting", "description": "书写", "score": 15, "required": True, "keywords": [], "example": ""},
    ],
}


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

# Level 0降级：规则兜底评分标准（所有LLM失败时使用）
FALLBACK_RUBRIC = {
    "steps": [
        {"step_id": "s1", "description": "列式/建立方程", "score": 2, "required": True, "keywords": ["设", "令", "因为", "所以", "="], "example": ""},
        {"step_id": "s2", "description": "计算过程", "score": 2, "required": True, "keywords": ["代入", "化简", "解得", "计算"], "example": ""},
        {"step_id": "s3", "description": "最终答案", "score": 1, "required": True, "keywords": ["答", "故", "因此"], "example": ""},
    ]
}


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
