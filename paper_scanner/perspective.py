"""OpenCV 透视矫正：检测试卷边界、矫正倾斜"""

import cv2
import numpy as np


def detect_paper_corners(image: np.ndarray) -> list[list[int]] | None:
    """检测图像中试卷的四个角点。

    流程：灰度 → 高斯模糊 → Canny边缘 → findContours → 近似多边形 → 找最大4点轮廓
    返回 [[x1,y1],[x2,y2],[x3,y3],[x4,y4]] 或 None
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)

    contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            return approx.reshape(4, 2).tolist()

    # 回退：取最大轮廓的最小外接矩形
    if contours:
        rect = cv2.minAreaRect(contours[0])
        box = cv2.boxPoints(rect)
        return box.astype(int).tolist()

    return None


def order_points(corners: list[list[float]]) -> np.ndarray:
    """将4个点排序为：左上、右上、右下、左下"""
    pts = np.array(corners, dtype="float32")
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]   # 左上：和最小
    rect[2] = pts[np.argmax(s)]   # 右下：和最大

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # 右上：差最小
    rect[3] = pts[np.argmax(diff)]  # 左下：差最大

    return rect


def four_point_transform(image: np.ndarray, corners: list[list[float]]) -> np.ndarray:
    """计算透视变换矩阵并 warp 为俯视图"""
    rect = order_points(corners)
    (tl, tr, br, bl) = rect

    width_top = np.hypot(tr[0] - tl[0], tr[1] - tl[1])
    width_bottom = np.hypot(br[0] - bl[0], br[1] - bl[1])
    max_width = max(int(width_top), int(width_bottom))

    height_left = np.hypot(bl[0] - tl[0], bl[1] - tl[1])
    height_right = np.hypot(br[0] - tr[0], br[1] - tr[1])
    max_height = max(int(height_left), int(height_right))

    dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1],
    ], dtype="float32")

    matrix = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, matrix, (max_width, max_height))
    return warped


def correct_perspective(image: np.ndarray, target_width: int = 1000) -> tuple[np.ndarray | None, list | None]:
    """完整透视矫正流水线。

    返回 (corrected_image, corners) 或 (原图, None) 如果检测失败。
    结果缩放到 target_width 以标准化 OCR 输入尺寸。
    """
    corners = detect_paper_corners(image)
    if corners is None:
        # 回退：直接使用原图
        h, w = image.shape[:2]
        if w > target_width:
            scale = target_width / w
            image = cv2.resize(image, (target_width, int(h * scale)))
        return image, None

    try:
        warped = four_point_transform(image, corners)
    except Exception:
        h, w = image.shape[:2]
        if w > target_width:
            scale = target_width / w
            image = cv2.resize(image, (target_width, int(h * scale)))
        return image, None

    # 缩放到标准宽度
    h, w = warped.shape[:2]
    if w > 0:
        scale = target_width / w
        warped = cv2.resize(warped, (target_width, int(h * scale)))

    return warped, corners
