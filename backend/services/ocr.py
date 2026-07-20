"""希沃智教π OCR识别层 - 双引擎置信度融合"""
import asyncio
import base64
import hashlib
import logging
import httpx
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)

from backend.core.config import settings

# PaddleOCR 可选依赖，缺失时优雅降级
try:
    from paddleocr import PaddleOCR
    PADDLEOCR_AVAILABLE = True
except ImportError:
    PADDLEOCR_AVAILABLE = False


@dataclass
class OCRResult:
    """单引擎OCR识别结果"""
    text: str
    confidence: float
    engine: str  # baidu_ocr | paddleocr_vl
    formulas: list[str] = field(default_factory=list)  # LaTeX公式列表
    regions: list[dict] = field(default_factory=list)  # [{bbox, text, confidence}]


@dataclass
class FusedOCRResult:
    """双引擎融合后的OCR结果"""
    text: str
    confidence: float
    formulas: list[str]
    regions: list[dict]
    engines_used: list[str]
    per_engine_results: dict[str, OCRResult]
    needs_manual_input: bool = False


# ============ 文字块阅读顺序排序（C 方案：OCR 顺序稳定化）============

def _sort_blocks_by_reading_order(blocks: list[dict]) -> list[list[dict]]:
    """把文字块按阅读顺序分行排序：从上到下分行，行内从左到右

    输入 blocks: [{bbox: [x1, y1, x2, y2], text, confidence}, ...]
    输出：二维列表，外层是行（按 y 升序），内层是行内块（按 x 升序）

    分行策略：
    1. 先按 top(y1) 升序排序
    2. 用第一个块的 top 作为当前行基准，行高 = 该块 height
    3. 后续块若 |top - 当前行基准| < 行高 × 0.5，归入当前行；否则开新行
    4. 行内按 left(x1) 升序排序
    """
    if not blocks:
        return []

    # 提取位置信息
    enriched = []
    for b in blocks:
        x1, y1, x2, y2 = b["bbox"]
        enriched.append({
            **b,
            "_top": y1,
            "_left": x1,
            "_width": max(x2 - x1, 1),
            "_height": max(y2 - y1, 1),
        })

    # 按 top 排序
    enriched.sort(key=lambda x: x["_top"])

    # 分行
    lines: list[list[dict]] = []
    current_line = [enriched[0]]
    line_top = enriched[0]["_top"]
    line_height = enriched[0]["_height"]

    for it in enriched[1:]:
        if abs(it["_top"] - line_top) < line_height * 0.5:
            current_line.append(it)
            line_height = max(line_height, it["_height"])
        else:
            current_line.sort(key=lambda x: x["_left"])
            lines.append(current_line)
            current_line = [it]
            line_top = it["_top"]
            line_height = it["_height"]

    current_line.sort(key=lambda x: x["_left"])
    lines.append(current_line)
    return lines


def _concat_blocks_to_text(blocks: list[dict]) -> str:
    """把文字块按阅读顺序拼接为文本

    - 行内：根据相邻块的水平间距决定是否插入空格
      间距 > 上一个块的字符平均宽度 × 0.5 时插入空格
      （让 'x' '=' '5' 三个紧邻块拼成 'x=5'，让 'hello' 'world' 拼成 'hello world'）
    - 行间：用 '\\n' 分隔
    """
    if not blocks:
        return ""

    lines = _sort_blocks_by_reading_order(blocks)
    line_texts = []
    for line in lines:
        if not line:
            continue
        # 行内拼接
        parts = [line[0]["text"]]
        for prev, curr in zip(line[:-1], line[1:]):
            gap = curr["_left"] - (prev["_left"] + prev["_width"])
            char_width = max(prev["_width"] / max(len(prev["text"]), 1), 1)
            if gap > char_width * 0.5:
                parts.append(" " + curr["text"])
            else:
                parts.append(curr["text"])
        line_texts.append("".join(parts))

    return "\n".join(line_texts)


class BaiduOCREngine:
    """百度智能云手写OCR API"""

    OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
    TOKEN_URL = "https://aip.baidubce.com/oauth/2.0/token"
    _token_cache: dict = {}

    async def _get_access_token(self) -> str:
        if "token" in self._token_cache:
            return self._token_cache["token"]

        async with httpx.AsyncClient() as client:
            resp = await client.post(
                self.TOKEN_URL,
                params={
                    "grant_type": "client_credentials",
                    "client_id": settings.BAIDU_OCR_API_KEY,
                    "client_secret": settings.BAIDU_OCR_SECRET_KEY,
                },
            )
            data = resp.json()
            self._token_cache["token"] = data["access_token"]
            return data["access_token"]

    async def recognize(self, image_bytes: bytes) -> OCRResult:
        """识别图片中的手写文字"""
        if not settings.BAIDU_OCR_API_KEY:
            return OCRResult(text="", confidence=0.0, engine="baidu_ocr")

        token = await self._get_access_token()
        img_b64 = base64.b64encode(image_bytes).decode()

        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                self.OCR_URL,
                params={"access_token": token},
                data={"image": img_b64, "language_type": "CHN_ENG"},
            )
            data = resp.json()

        words_result = data.get("words_result", [])
        regions = []
        total_conf = 0.0

        for item in words_result:
            word = item.get("words", "")
            loc = item.get("location", {})
            conf = item.get("probability", {}).get("average", 0.5)
            total_conf += conf
            regions.append({
                "bbox": [loc.get("left", 0), loc.get("top", 0),
                         loc.get("left", 0) + loc.get("width", 0),
                         loc.get("top", 0) + loc.get("height", 0)],
                "text": word,
                "confidence": round(conf, 3),
            })

        # C 方案：按阅读顺序排序后再拼接（百度 OCR 每条 word 通常是一行，
        # 排序后行间用 \n 拼接；行内因为本身就是单条，无需再插空格）
        sorted_text = _concat_blocks_to_text(regions) if regions else ""

        avg_conf = total_conf / len(words_result) if words_result else 0.0
        return OCRResult(
            text=sorted_text,
            confidence=round(avg_conf, 3),
            engine="baidu_ocr",
            regions=regions,
        )


class PaddleOCREngine:
    """PaddleOCR-VL本地识别引擎（公式+手写增强）"""

    _ocr = None
    _api_version = None  # "v3" (PaddleOCR 3.x) or "v2" (PaddleOCR 2.x)

    def _get_ocr(self):
        if not PADDLEOCR_AVAILABLE:
            return None
        if self._ocr is None:
            # PaddleOCR 3.x: 使用新API（use_textline_orientation + enable_mkldnn=False）
            # PaddleOCR 2.x: 使用旧API（use_angle_cls + show_log + use_gpu）
            try:
                # 尝试新版本API (PaddleOCR 3.x)
                self._ocr = PaddleOCR(
                    use_textline_orientation=True,
                    lang="ch",
                    enable_mkldnn=False,  # 禁用mkldnn避免onednn兼容性问题
                )
                self._api_version = "v3"
                logger.info("[PaddleOCR] 使用PaddleOCR 3.x API")
            except (TypeError, ValueError):
                # 降级到旧版本API (PaddleOCR 2.x)
                try:
                    self._ocr = PaddleOCR(
                        use_angle_cls=True,
                        lang="ch",
                        show_log=False,
                        use_gpu=False,
                    )
                    self._api_version = "v2"
                    logger.info("[PaddleOCR] 使用PaddleOCR 2.x API")
                except Exception as e:
                    logger.error(f"PaddleOCR初始化失败: {e}")
                    return None
        return self._ocr

    async def recognize(self, image_bytes: bytes) -> OCRResult:
        """本地PaddleOCR识别（同步调用包装为异步）"""
        if not PADDLEOCR_AVAILABLE:
            return OCRResult(text="", confidence=0.0, engine="paddleocr_vl")

        import tempfile
        import os

        # 将bytes写入临时文件（PaddleOCR需要文件路径）
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            f.write(image_bytes)
            tmp_path = f.name

        try:
            ocr = self._get_ocr()
            if ocr is None:
                return OCRResult(text="", confidence=0.0, engine="paddleocr_vl")

            # 在线程池中运行同步OCR
            loop = asyncio.get_event_loop()

            regions = []
            total_conf = 0.0

            if self._api_version == "v3":
                # PaddleOCR 3.x: 使用 predict() 方法，返回 OCRResult 对象列表
                results = await loop.run_in_executor(None, ocr.predict, tmp_path)
                for item in results:
                    res = item.get("res", item) if isinstance(item, dict) else (
                        item.json if hasattr(item, "json") else None
                    )
                    if not res:
                        continue
                    # 新版本字段：rec_texts, rec_scores, rec_polys
                    rec_texts = res.get("rec_texts", []) if isinstance(res, dict) else []
                    rec_scores = res.get("rec_scores", []) if isinstance(res, dict) else []
                    rec_polys = res.get("rec_polys", []) if isinstance(res, dict) else []
                    for i, text in enumerate(rec_texts):
                        conf = rec_scores[i] if i < len(rec_scores) else 0.5
                        total_conf += conf
                        # rec_polys 格式: [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
                        if i < len(rec_polys):
                            poly = rec_polys[i]
                            x_coords = [p[0] for p in poly]
                            y_coords = [p[1] for p in poly]
                            regions.append({
                                "bbox": [min(x_coords), min(y_coords),
                                         max(x_coords), max(y_coords)],
                                "text": text,
                                "confidence": round(conf, 3),
                            })
                        else:
                            regions.append({
                                "bbox": [0, 0, 0, 0],
                                "text": text,
                                "confidence": round(conf, 3),
                            })
            else:
                # PaddleOCR 2.x: 使用 ocr() 方法
                result = await loop.run_in_executor(None, ocr.ocr, tmp_path, True)
                for line in result[0] if result[0] else []:
                    box, (text, conf) = line
                    total_conf += conf
                    x_coords = [p[0] for p in box]
                    y_coords = [p[1] for p in box]
                    regions.append({
                        "bbox": [min(x_coords), min(y_coords),
                                 max(x_coords), max(y_coords)],
                        "text": text,
                        "confidence": round(conf, 3),
                    })

            # C 方案：按阅读顺序排序后再拼接
            # 避免把 "x=6" 识别成 "9=x"（多个文字块按位置排序后稳定为 "x=6"）
            sorted_text = _concat_blocks_to_text(regions) if regions else ""

            avg_conf = total_conf / len(regions) if regions else 0.0
            return OCRResult(
                text=sorted_text,
                confidence=round(avg_conf, 3),
                engine="paddleocr_vl",
                regions=regions,
            )
        finally:
            os.unlink(tmp_path)


def fuse_results(baidu: OCRResult, paddle: OCRResult) -> FusedOCRResult:
    """双引擎置信度融合：取置信度较高的引擎结果为主"""
    engines_used = []
    per_engine = {}

    if baidu.confidence > 0:
        engines_used.append("baidu_ocr")
        per_engine["baidu_ocr"] = baidu
    if paddle.confidence > 0:
        engines_used.append("paddleocr_vl")
        per_engine["paddleocr_vl"] = paddle

    # 选择置信度更高的引擎结果作为主结果
    if baidu.confidence >= paddle.confidence and baidu.confidence > 0:
        primary = baidu
    elif paddle.confidence > 0:
        primary = paddle
    else:
        primary = OCRResult(text="", confidence=0.0, engine="none")

    # 融合公式：优先使用PaddleOCR识别到的公式
    formulas = paddle.formulas if paddle.formulas else []

    return FusedOCRResult(
        text=primary.text,
        confidence=primary.confidence,
        formulas=formulas,
        regions=primary.regions,
        engines_used=engines_used,
        per_engine_results=per_engine,
    )


class OCRService:
    """OCR识别服务 - 对外统一接口"""

    def __init__(self):
        self.baidu = BaiduOCREngine()
        self.paddle = PaddleOCREngine() if PADDLEOCR_AVAILABLE else None

    async def recognize(self, image_bytes: bytes) -> FusedOCRResult:
        """双引擎并行识别 + 置信度融合（含多级降级）"""
        baidu_task = self.baidu.recognize(image_bytes)

        if self.paddle is not None:
            # 双引擎模式
            paddle_task = self.paddle.recognize(image_bytes)
            results = await asyncio.gather(
                baidu_task, paddle_task, return_exceptions=True
            )

            baidu_result = results[0] if not isinstance(results[0], Exception) else OCRResult(
                text="", confidence=0.0, engine="baidu_ocr"
            )
            paddle_result = results[1] if not isinstance(results[1], Exception) else OCRResult(
                text="", confidence=0.0, engine="paddleocr_vl"
            )

            both_failed = (baidu_result.confidence == 0.0 and paddle_result.confidence == 0.0)

            if both_failed:
                logger.warning("[OCRService] Level 2降级：双引擎均失败，标记需人工录入")
                return FusedOCRResult(
                    text="",
                    confidence=0.0,
                    formulas=[],
                    regions=[],
                    engines_used=["manual_fallback"],
                    per_engine_results={},
                    needs_manual_input=True,
                )

            return fuse_results(baidu_result, paddle_result)
        else:
            # PaddleOCR 不可用，仅使用百度引擎
            try:
                baidu_result = await baidu_task
            except Exception:
                baidu_result = OCRResult(text="", confidence=0.0, engine="baidu_ocr")

            if baidu_result.confidence == 0.0:
                logger.warning("[OCRService] 降级：百度OCR失败且PaddleOCR不可用，标记需人工录入")
                return FusedOCRResult(
                    text="",
                    confidence=0.0,
                    formulas=[],
                    regions=[],
                    engines_used=["manual_fallback"],
                    per_engine_results={},
                    needs_manual_input=True,
                )

            return FusedOCRResult(
                text=baidu_result.text,
                confidence=baidu_result.confidence,
                formulas=baidu_result.formulas,
                regions=baidu_result.regions,
                engines_used=["baidu_ocr"],
                per_engine_results={"baidu_ocr": baidu_result},
            )

    async def recognize_single(self, image_bytes: bytes, engine: str = "baidu_ocr") -> OCRResult:
        """单引擎识别（调试用）"""
        if engine == "baidu_ocr":
            return await self.baidu.recognize(image_bytes)
        else:
            if self.paddle is not None:
                return await self.paddle.recognize(image_bytes)
            else:
                return OCRResult(text="", confidence=0.0, engine="paddleocr_vl")


# 模块级单例
ocr_service = OCRService()
