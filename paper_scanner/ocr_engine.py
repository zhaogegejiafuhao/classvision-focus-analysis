"""PaddleOCR 懒加载单例。

PaddleOCR 较重（~1-2s 初始化），仅在首次使用时导入。
未安装 paddleocr 时不影响后端启动。
"""

import logging

import numpy as np

logger = logging.getLogger(__name__)


class OCREngine:
    """PaddleOCR 包装器 - 懒加载单例。"""

    _instance = None
    _ocr = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def ocr(self):
        """首次访问时懒加载 PaddleOCR 实例。"""
        if self._ocr is None:
            logger.info("正在加载 PaddleOCR 模型...")
            from paddleocr import PaddleOCR
            self._ocr = PaddleOCR(
                use_angle_cls=True,
                lang="ch",
                show_log=False,
                use_gpu=False,
            )
            logger.info("PaddleOCR 模型加载完成")
        return self._ocr

    def recognize(self, image: np.ndarray) -> list[dict]:
        """对图像区域执行 OCR 识别。

        返回 [{"text": str, "confidence": float, "bbox": [[x1,y1],...]}]
        """
        result = self.ocr.ocr(image, cls=True)
        if not result or not result[0]:
            return []
        items = []
        for line in result[0]:
            bbox, (text, conf) = line
            items.append({
                "text": text.strip(),
                "confidence": round(float(conf), 3),
                "bbox": bbox,
            })
        return items

    def recognize_text(self, image: np.ndarray) -> str:
        """识别图像区域，返回拼接后的纯文本。"""
        items = self.recognize(image)
        return " ".join(item["text"] for item in items)


ocr_engine = OCREngine()
