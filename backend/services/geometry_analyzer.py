"""希沃智教π 几何辅助线溯源分析（降级版）

Phase 2 - 7.2.7 CapGeo几何辅助线溯源
功能：VL模型识别学生辅助线 → LLM匹配标准方案 → 输出辅助线评估与提示
降级策略：VL模型不可用时跳过辅助线分析，返回默认结果

已迁移至 ClassVision backend，使用 async_llm 适配层替代直接 AsyncOpenAI 调用。
"""
import base64
import json
import logging
from dataclasses import dataclass
from typing import Optional

from backend.core.config import settings
from backend.services.llm_utils import parse_llm_json
from backend.services import async_llm

logger = logging.getLogger(__name__)


# ===== 几何题关键词 =====

# 几何符号（用于 OCR 文本级检测，定义在前以便 is_geometry_question 复用）
GEOMETRY_SYMBOLS = ["△", "∠", "⊥", "∥", "⊙", "○", "π", "≈", "≡", "∟", "⌒", "∵", "∴", "≌", "∽", "≅"]
GEOMETRY_LATEX = [r"\triangle", r"\angle", r"\perp", r"\parallel", r"\circ", r"\odot", r"\cong", r"\sim"]

GEOMETRY_KEYWORDS = [
    # 中文术语
    "三角形", "全等", "相似", "四边形", "圆", "证明", "求证", "辅助线",
    "平行", "垂直", "角平分线", "中垂线", "中线", "高线",
    "菱形", "矩形", "正方形", "梯形", "弦", "切线", "弧",
    "几何", "顶点", "底边", "腰", "斜边", "直角边", "内角", "外角",
    "全等三角形", "相似三角形", "等腰", "等边", "直角三角形",
    "圆心", "半径", "直径", "周长", "面积", "勾股", "勾股定理",
]

# 模糊词：单独出现不足以判定为几何题，但若出现则触发Layer 3 LLM确认
GEOMETRY_AMBIGUOUS_HINTS = [
    "如图", "所示", "连接", "延长", "交于", "过点", "作图",
    "求∠", "求证", "试证", "证:", "证：",
]


def is_geometry_question(question: str) -> bool:
    """判断题目是否为几何题（Layer 1 + Layer 2 同步快速检测）

    Layer 1: 关键词匹配（中文术语）
    Layer 2: 几何符号 + LaTeX 公式检测

    本函数为同步、零成本检测，覆盖绝大多数明确几何题。
    对于模糊情况（如仅含"如图"），请使用 detect_geometry_with_llm_fallback()。

    Args:
        question: 题目文本

    Returns:
        bool: 是否为明确的几何题
    """
    # Layer 1: 关键词匹配
    if any(kw in question for kw in GEOMETRY_KEYWORDS):
        return True
    # Layer 2: 几何符号检测（△ ∠ ⊥ ∥ ⊙ ○ ⌒ 等）
    if any(sym in question for sym in GEOMETRY_SYMBOLS):
        return True
    # Layer 2.5: LaTeX 几何命令
    if any(cmd in question for cmd in GEOMETRY_LATEX):
        return True
    return False


def has_geometry_ambiguous_hints(question: str) -> bool:
    """判断题目是否含几何模糊词（需触发 Layer 3 LLM 确认）

    Returns:
        bool: 是否含"如图"、"所示"等模糊词，但 Layer 1+2 未命中
    """
    return any(hint in question for hint in GEOMETRY_AMBIGUOUS_HINTS)


async def detect_geometry_with_llm_fallback(question: str) -> bool:
    """三层几何题检测（Layer 3 LLM 兜底）

    流程：
      1. Layer 1+2 同步快速检测（关键词 + 符号 + LaTeX）
         - 命中 → 立即返回 True（零延迟）
      2. Layer 3 LLM 兜底
         - 仅当 Layer 1+2 未命中 **且** 含模糊词（如"如图"、"求证"）时才调用 LLM
         - LLM 返回 False 或超时 → 返回 False
      3. 既无明确特征也无模糊词 → 直接返回 False（不调用 LLM）

    设计权衡：
      - 明确几何题零延迟识别（绝大多数情况）
      - 仅在边界情况调用 LLM，避免常规请求多一次 LLM 延迟
      - LLM 用 max_tokens=8 / temperature=0 做纯分类，单次调用 ~1-3s
    """
    # Layer 1 + 2: 同步快速检测
    if is_geometry_question(question):
        return True

    # 没有模糊词 → 直接返回 False，避免不必要的 LLM 调用
    if not has_geometry_ambiguous_hints(question):
        return False

    # Layer 3: LLM 兜底确认（仅对含模糊词的边界情况）
    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "你是数学题目分类器。判断给定题目是否为几何题"
                    "（涉及图形、三角形、四边形、圆、角度、证明、辅助线等）。"
                    "严格只输出一个词：true 或 false。"
                ),
            },
            {"role": "user", "content": f"题目：{question[:500]}\n\n是否为几何题？"},
        ]
        result = await async_llm.async_chat(
            messages=messages,
            temperature=0.0,
            max_tokens=8,
            mode="fast",  # 用快速模型降低延迟
        )
        content = (result.get("content") or "").strip().lower()
        # 容忍各种"是"的回复
        is_geo = content.startswith("true") or content.startswith("是") or content == "yes"
        logger.info(
            f"[detect_geometry_with_llm_fallback] LLM判定: is_geometry={is_geo}, "
            f"原文='{content[:20]}', 题目='{question[:30]}...'"
        )
        return is_geo
    except Exception as e:
        logger.warning(f"[detect_geometry_with_llm_fallback] LLM几何检测失败: {type(e).__name__}: {e}")
        # LLM 失败时，有模糊词也保守判为几何题（几何题检测漏了影响辅助线分析，误判影响不大）
        return True


async def detect_geometry_enhanced(
    question_text: str,
    question_image_bytes: bytes | None = None,
) -> dict:
    """三层增强版几何检测

    Layer 1: 关键词匹配（零成本）
    Layer 2: 几何符号 + LaTeX公式检测（零额外成本，复用OCR结果）
    Layer 3: VL模型图片级检测（可选，需API Key）

    Returns:
        dict: {
            "is_geometry": bool,
            "source": str,  # "keyword"|"symbol"|"vl"|"none"
            "hints": list[str],
            "sources": dict,  # 各层检测结果
            "combined_score": float,
        }
    """
    sources = {}
    hints = []

    # Layer 1: 关键词匹配
    keyword_hit = is_geometry_question(question_text)
    sources["keyword_match"] = keyword_hit
    if keyword_hit:
        matched = [kw for kw in GEOMETRY_KEYWORDS if kw in question_text]
        hints.append(f"关键词命中：{', '.join(matched)}")

    # Layer 2: OCR文本中的几何符号检测
    symbol_hits = [s for s in GEOMETRY_SYMBOLS if s in question_text]
    sources["ocr_symbol_match"] = len(symbol_hits) > 0
    if symbol_hits:
        hints.append(f"检测到几何符号：{', '.join(symbol_hits)}")

    # Layer 2.5: LaTeX公式中的几何命令检测
    formula_hit = any(cmd in question_text for cmd in GEOMETRY_LATEX)
    sources["formula_geometry"] = formula_hit
    if formula_hit:
        hints.append("检测到LaTeX几何公式")

    # Layer 3: VL模型图片级检测（仅在Layer1+2都未命中时调用）
    vl_detected = False
    if question_image_bytes and not keyword_hit and not symbol_hits and not formula_hit:
        try:
            if settings.VOLCENGINE_API_KEY and settings.DOUBAO_ENDPOINT_ID:
                vl_detected = await _vl_detect_geometry(question_image_bytes)
                sources["vl_model_detection"] = vl_detected
                if vl_detected:
                    hints.append("VL模型检测：图片包含几何图形")
            else:
                logger.debug("[detect_geometry_enhanced] VL模型未配置（VOLCENGINE_API_KEY或DOUBAO_ENDPOINT_ID为空），跳过VL检测")
                sources["vl_model_detection"] = False
        except Exception as e:
            logger.warning(f"VL模型几何检测失败: {type(e).__name__}: {e}")
            sources["vl_model_detection"] = False
    elif not (keyword_hit or symbol_hits or formula_hit):
        sources["vl_model_detection"] = False

    # 综合判定：任一层检测到即为几何题
    is_geometry = keyword_hit or len(symbol_hits) > 0 or formula_hit or vl_detected

    # 来源标记
    if keyword_hit:
        source = "keyword"
    elif symbol_hits:
        source = "symbol"
    elif formula_hit:
        source = "formula"
    elif vl_detected:
        source = "vl"
    else:
        source = "none"

    # 综合置信度
    score = 0.0
    if keyword_hit: score += 0.4
    if symbol_hits: score += 0.3
    if formula_hit: score += 0.15
    if vl_detected: score += 0.15

    return {
        "is_geometry": is_geometry,
        "source": source,
        "hints": hints,
        "sources": sources,
        "combined_score": min(score, 1.0),
    }


async def _vl_detect_geometry(image_bytes: bytes) -> bool:
    """使用VL模型检测图片是否包含几何图形

    通过 async_llm.async_chat_with_provider 调用火山引擎豆包VL模型。
    """
    try:
        b64 = base64.b64encode(image_bytes).decode()
        messages = [{
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
                {"type": "text", "text": "请判断这张图片是否包含几何图形（三角形、四边形、圆、角度标注、辅助线等）。严格输出JSON：{\"is_geometry\": true或false, \"reason\": \"简要说明\"}"},
            ],
        }]
        result = await async_llm.async_chat_with_provider(
            provider_name="volcengine",
            messages=messages,
            api_key=settings.VOLCENGINE_API_KEY,
            base_url=settings.VOLCENGINE_BASE_URL,
            model=settings.DOUBAO_ENDPOINT_ID,
            temperature=0.1,
            max_tokens=128,
        )
        content = result.get("content", "")
        parsed = json.loads(content)
        return bool(parsed.get("is_geometry", False))
    except Exception as e:
        logger.warning(f"VL几何检测失败: {e}")
        return False


# ===== 数据类 =====

@dataclass
class GeometryAnalysisResult:
    """几何辅助线分析结果"""
    has_auxiliary_line: bool          # 学生是否画了辅助线
    auxiliary_line_desc: str          # 辅助线描述
    standard_line_desc: str           # 标准辅助线描述
    assessment: str                   # 辅助线正确|辅助线方向偏差|缺失关键辅助线|辅助线多余
    hint: str                         # 辅助线提示

    def to_dict(self) -> dict:
        """转换为字典格式"""
        return {
            "has_auxiliary_line": self.has_auxiliary_line,
            "auxiliary_line_desc": self.auxiliary_line_desc,
            "standard_line_desc": self.standard_line_desc,
            "assessment": self.assessment,
            "hint": self.hint,
        }


# ===== Prompt 模板 =====

VL_AUXILIARY_LINE_PROMPT = """你是一位几何教学专家，请仔细观察这张学生手写几何题图片，判断学生是否画了辅助线。

辅助线通常表现为：
1. 用虚线表示的线段
2. 延长线（将某条边延长至某点）
3. 连接两点的线段（如连接对角线）
4. 作垂线、平行线、角平分线等构造线
5. 用不同颜色或不同线型标注的线条

请输出JSON格式：
{{"has_auxiliary_line": true或false, "auxiliary_line_desc": "描述学生画的辅助线，如'连接了AC，作了BD的垂线'，若没有则填'无'"}}

严格输出JSON，不要输出其他内容。"""

LLM_AUXILIARY_LINE_EVAL_PROMPT = """你是一位几何教学专家，请根据题目和标准解法，判断学生辅助线的正确性。

## 题目
{question}

## 学生画的辅助线
{auxiliary_line_desc}

请分析：
1. 这道题的标准辅助线方案是什么
2. 学生的辅助线与标准方案的匹配程度
3. 给出评估结论

评估结论只能从以下4种选择其一：
- 辅助线正确：学生的辅助线与标准方案一致
- 辅助线方向偏差：学生画了辅助线但方向或位置不太对
- 缺失关键辅助线：学生没有画必要的辅助线
- 辅助线多余：学生画了不需要的辅助线

严格输出JSON格式，不要输出其他内容：
{{"standard_line_desc": "标准辅助线描述", "assessment": "辅助线正确|辅助线方向偏差|缺失关键辅助线|辅助线多余", "hint": "给学生的辅助线提示，如'建议连接AC构造全等三角形'"}}"""


# ===== 几何辅助线分析器 =====

class GeometryAnalyzer:
    """几何辅助线分析器（降级版）

    Step 1: VL模型（豆包）识别学生是否画了辅助线
    Step 2: LLM匹配标准辅助线方案并评估
    降级策略：VL模型不可用时跳过辅助线分析，返回默认结果

    使用 async_llm 适配层替代直接 AsyncOpenAI 客户端。
    """

    def __init__(self):
        # 延迟检查VL可用性（VOLCENGINE_API_KEY + DOUBAO_ENDPOINT_ID 非空即可用）
        self._vl_available = bool(settings.VOLCENGINE_API_KEY and settings.DOUBAO_ENDPOINT_ID)

    async def analyze(self, question: str, image_bytes: bytes) -> GeometryAnalysisResult:
        """分析几何辅助线（降级版）

        Args:
            question: 题目文本
            image_bytes: 学生手写图片字节数据

        Returns:
            GeometryAnalysisResult: 辅助线分析结果
        """
        # 前置检查：VL模型是否可用
        if not self._vl_available:
            logger.warning("[GeometryAnalyzer] VL模型不可用（缺少VOLCENGINE_API_KEY或DOUBAO_ENDPOINT_ID），跳过辅助线分析")
            return self._default_result()

        # Step 1: VL模型识别辅助线
        auxiliary_line_desc = ""
        has_auxiliary_line = False

        try:
            logger.info("[GeometryAnalyzer] Step 1: VL模型识别辅助线...")
            vl_result = await self._vl_detect_auxiliary_line(image_bytes)
            has_auxiliary_line = vl_result.get("has_auxiliary_line", False)
            auxiliary_line_desc = vl_result.get("auxiliary_line_desc", "无")
            logger.info(f"[GeometryAnalyzer] VL识别结果: has_auxiliary_line={has_auxiliary_line}, desc={auxiliary_line_desc[:50]}")
        except Exception as e:
            logger.warning(f"[GeometryAnalyzer] VL模型调用失败: {type(e).__name__}: {e}, 跳过辅助线分析")
            return self._default_result()

        # Step 2: LLM匹配标准方案并评估
        try:
            logger.info("[GeometryAnalyzer] Step 2: LLM评估辅助线...")
            eval_result = await self._llm_evaluate_auxiliary_line(question, auxiliary_line_desc)

            # 校验assessment值是否合法
            assessment = eval_result.get("assessment", "")
            valid_assessments = ["辅助线正确", "辅助线方向偏差", "缺失关键辅助线", "辅助线多余"]
            if assessment not in valid_assessments:
                logger.warning(f"[GeometryAnalyzer] LLM返回的assessment不合法: {assessment}，使用默认值")
                assessment = "缺失关键辅助线" if not has_auxiliary_line else "辅助线方向偏差"

            return GeometryAnalysisResult(
                has_auxiliary_line=has_auxiliary_line,
                auxiliary_line_desc=auxiliary_line_desc,
                standard_line_desc=eval_result.get("standard_line_desc", ""),
                assessment=assessment,
                hint=eval_result.get("hint", ""),
            )
        except Exception as e:
            logger.warning(f"[GeometryAnalyzer] LLM评估失败: {type(e).__name__}: {e}, 返回基础结果")
            return GeometryAnalysisResult(
                has_auxiliary_line=has_auxiliary_line,
                auxiliary_line_desc=auxiliary_line_desc,
                standard_line_desc="",
                assessment="缺失关键辅助线" if not has_auxiliary_line else "辅助线方向偏差",
                hint="",
            )

    async def _vl_detect_auxiliary_line(self, image_bytes: bytes) -> dict:
        """使用VL模型识别学生是否画了辅助线

        通过 async_llm.async_chat_with_provider 调用火山引擎豆包VL模型。

        Args:
            image_bytes: 图片字节数据

        Returns:
            dict: {"has_auxiliary_line": bool, "auxiliary_line_desc": str}
        """
        img_b64 = base64.b64encode(image_bytes).decode()

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"},
                    },
                    {
                        "type": "text",
                        "text": VL_AUXILIARY_LINE_PROMPT,
                    },
                ],
            }
        ]

        result = await async_llm.async_chat_with_provider(
            provider_name="volcengine",
            messages=messages,
            api_key=settings.VOLCENGINE_API_KEY,
            base_url=settings.VOLCENGINE_BASE_URL,
            model=settings.DOUBAO_ENDPOINT_ID,
            temperature=0.1,
            max_tokens=512,
        )

        content = result.get("content", "")
        return parse_llm_json(content)

    async def _llm_evaluate_auxiliary_line(self, question: str, auxiliary_line_desc: str) -> dict:
        """使用LLM匹配标准辅助线方案并评估

        通过 async_llm.async_chat_json 调用默认深度模型。

        Args:
            question: 题目文本
            auxiliary_line_desc: 学生辅助线描述

        Returns:
            dict: {"standard_line_desc": str, "assessment": str, "hint": str}
        """
        prompt = LLM_AUXILIARY_LINE_EVAL_PROMPT.format(
            question=question,
            auxiliary_line_desc=auxiliary_line_desc,
        )

        return await async_llm.async_chat_json(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=512,
            mode="deep",
        )

    @staticmethod
    def _default_result() -> GeometryAnalysisResult:
        """降级时返回的默认结果（VL模型不可用）"""
        return GeometryAnalysisResult(
            has_auxiliary_line=False,
            auxiliary_line_desc="（VL模型不可用，跳过辅助线识别）",
            standard_line_desc="",
            assessment="缺失关键辅助线",
            hint="",
        )


# ===== 模块级单例 =====
geometry_analyzer = GeometryAnalyzer()
