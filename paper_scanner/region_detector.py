"""答题区域自动检测：使用 OpenCV 检测试卷上的文本区域。"""

import cv2
import numpy as np


def detect_answer_regions(image: np.ndarray) -> list[dict]:
    """检测图像中的答题文本区域。

    使用形态学操作合并相邻文字为文本块，再通过轮廓提取区域。
    返回 [{"x": float, "y": float, "w": float, "h": float}, ...]（百分比坐标）
    """
    if image is None or image.size == 0:
        return []

    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 自适应阈值（二值化反转，文字变白）
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 21, 15
    )

    # 形态学操作：水平膨胀合并同行文字，垂直膨胀合并多行为块
    kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (w // 20, 1))
    kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (1, h // 40))
    dilated = cv2.dilate(binary, kernel_h, iterations=1)
    dilated = cv2.dilate(dilated, kernel_v, iterations=1)

    # 查找轮廓
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regions = []
    min_area = w * h * 0.002  # 最小面积阈值（0.2%）
    max_area = w * h * 0.5     # 最大面积阈值（50%）

    for c in contours:
        area = cv2.contourArea(c)
        if area < min_area or area > max_area:
            continue
        x, y, rw, rh = cv2.boundingRect(c)
        # 过滤过窄的区域
        if rh < h * 0.01 or rw < w * 0.02:
            continue
        regions.append({
            "x": round(x / w, 4),
            "y": round(y / h, 4),
            "w": round(rw / w, 4),
            "h": round(rh / h, 4),
        })

    # 按从上到下、从左到右排序
    regions.sort(key=lambda r: (r["y"], r["x"]))
    return regions
