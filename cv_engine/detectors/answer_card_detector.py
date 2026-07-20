"""答题卡气泡检测器——基于 OpenCV 的客观题答案识别

支持两种检测模式：
1. standard_5x10x4：标准 5列×10题×4选项 答题卡模板（坐标按图像尺寸自动计算）
2. generic：通用 HoughCircles 圆检测（Phase 4 启用，本文件预留接口）

核心算法：
- 预处理：灰度化 → 高斯模糊 → 自适应二值化（Otsu）
- 倾斜校正：基于 minAreaRect 计算主方向 → warpAffine 旋转校正
- 气泡定位（标准模板）：按网格坐标采样，每个位置计算圆区域填充率
- 填充率：圆区域内黑色像素占比 > FILL_THRESHOLD(0.45) 视为填涂

返回结构 AnswerCardResult：
- bubbles: 所有气泡信息列表
- answers: {question_index: [option_indices]}（option_index: 0=A, 1=B, 2=C, 3=D）
- skew_angle: 倾斜角度（度）
- debug_image_b64: 调试可视化图（base64 PNG）

模块级单例：answer_card_detector = AnswerCardDetector()
"""
from __future__ import annotations

import base64
import logging
from dataclasses import dataclass, field
from typing import Optional

import cv2
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class BubbleMark:
    """单个气泡的检测结果"""
    question_index: int          # 题号 (0-based)
    option_index: int            # 选项 (0=A, 1=B, 2=C, 3=D)
    filled: bool                 # 是否填涂
    fill_ratio: float            # 填充率 (0.0-1.0)
    center: tuple[int, int]      # 圆心像素坐标 (x, y)
    radius: int                  # 圆半径


@dataclass
class AnswerCardResult:
    """答题卡检测结果"""
    template_type: str                       # "standard_5x10x4" | "generic"
    bubbles: list[BubbleMark] = field(default_factory=list)
    answers: dict[int, list[int]] = field(default_factory=dict)  # {q_idx: [opt_idx]}
    skew_angle: float = 0.0
    debug_image_b64: str = ""                # 调试可视化图（base64 PNG）
    error: Optional[str] = None              # 检测失败时的错误信息


class AnswerCardDetector:
    """答题卡气泡检测器

    使用方式：
        result = answer_card_detector.detect(image_bytes, template_type="standard_5x10x4")
        # result.answers: {0: [0], 1: [1, 3], ...}  表示第1题选A，第2题选BD
    """

    # 填充率阈值：> 0.45 视为填涂
    FILL_THRESHOLD = 0.45
    # 标准 5×10×4 模板布局：5列 × 10题 × 4选项
    STANDARD_LAYOUT = (5, 10, 4)

    # ============ 主入口 ============

    def detect(self, image_bytes: bytes, template_type: str = "standard_5x10x4") -> AnswerCardResult:
        """主入口：图像字节 → 答题卡检测结果

        Args:
            image_bytes: 图片二进制数据（JPEG/PNG）
            template_type: "standard_5x10x4" 或 "generic"

        Returns:
            AnswerCardResult
        """
        try:
            # 解码图像
            img_array = np.frombuffer(image_bytes, dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            if img is None:
                return AnswerCardResult(template_type=template_type, error="图像解码失败")

            # 预处理 + 倾斜校正
            gray = self._preprocess(img)
            gray, skew_angle = self._correct_skew(gray)

            # 按模板类型分发
            if template_type == "standard_5x10x4":
                bubbles = self._detect_bubbles_standard(gray)
            elif template_type == "generic":
                bubbles = self._detect_bubbles_generic(gray)
            else:
                return AnswerCardResult(template_type=template_type, error=f"未知模板类型: {template_type}")

            # 提取答案字典
            answers = self._bubbles_to_answers(bubbles)

            # 生成调试可视化图
            debug_b64 = self._render_debug_image(img, bubbles, skew_angle)

            logger.info(
                f"[AnswerCardDetector] template={template_type}, "
                f"bubbles={len(bubbles)}, filled={sum(1 for b in bubbles if b.filled)}, "
                f"skew={skew_angle:.2f}°"
            )

            return AnswerCardResult(
                template_type=template_type,
                bubbles=bubbles,
                answers=answers,
                skew_angle=skew_angle,
                debug_image_b64=debug_b64,
            )
        except Exception as e:
            logger.exception(f"[AnswerCardDetector] 检测异常: {e}")
            return AnswerCardResult(template_type=template_type, error=f"{type(e).__name__}: {e}")

    # ============ 图像预处理 ============

    def _preprocess(self, img: np.ndarray) -> np.ndarray:
        """预处理：灰度化 → 高斯模糊 → 自适应二值化

        Args:
            img: BGR 彩色图

        Returns:
            二值化灰度图（黑底白字反转，便于后续检测黑色气泡）
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 高斯模糊去噪
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # 自适应二值化：能适应光照不均
        # cv2.THRESH_BINARY_INV 让气泡（深色）变成白色，便于后续检测
        binary = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV, 15, 10
        )
        return binary

    def _correct_skew(self, binary: np.ndarray) -> tuple[np.ndarray, float]:
        """倾斜校正：基于最小外接矩形计算主方向

        策略：
        1. 找到所有非零像素点（前景）
        2. 用 minAreaRect 拟合最小外接矩形，得到倾斜角度
        3. 用 warpAffine 旋转校正

        Args:
            binary: 二值化图像

        Returns:
            (校正后的二值图, 倾斜角度)
        """
        # 找到所有前景像素坐标
        coords = np.column_stack(np.where(binary > 0))
        if len(coords) < 100:
            # 前景太少，无法计算倾斜，直接返回
            return binary, 0.0

        # minAreaRect 接受 (x, y) 顺序
        rect = cv2.minAreaRect(coords.astype(np.float32))
        angle = rect[-1]

        # minAreaRect 返回的角度范围是 [-90, 0)，需要规范化
        # 如果角度 < -45，说明是竖直方向倾斜，加 90 度
        if angle < -45:
            angle = angle + 90

        # 角度过小则不校正（避免无意义旋转）
        if abs(angle) < 0.5:
            return binary, 0.0

        # 旋转校正
        h, w = binary.shape
        center = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(
            binary, rotation_matrix, (w, h),
            flags=cv2.INTER_NEAREST, borderMode=cv2.BORDER_CONSTANT, borderValue=0
        )
        return rotated, angle

    # ============ 标准模板检测 ============

    def _detect_bubbles_standard(self, binary: np.ndarray) -> list[BubbleMark]:
        """标准 5×10×4 模板检测

        布局假设：
        - 5列 × 10题 × 4选项 = 200 个气泡
        - 题号从上到下递增（每列10题）
        - 选项从左到右为 ABCD
        - 气泡均匀分布在图像主体区域（去掉边距）

        Args:
            binary: 预处理+校正后的二值图

        Returns:
            气泡列表（200 个，按题号-选项顺序）
        """
        h, w = binary.shape
        cols, rows_per_col, opts = self.STANDARD_LAYOUT  # (5, 10, 4)

        # 边距：上下左右各留 5% 的边距，避免边缘气泡被裁切
        margin_x = int(w * 0.05)
        margin_y = int(h * 0.05)
        usable_w = w - 2 * margin_x
        usable_h = h - 2 * margin_y

        # 每列宽度、每行高度
        col_width = usable_w / cols
        row_height = usable_h / rows_per_col

        # 气泡半径：取列宽和行高的较小值的 30%
        radius = int(min(col_width / (opts + 1), row_height) * 0.30)
        radius = max(radius, 8)  # 最小 8 像素

        bubbles: list[BubbleMark] = []
        for col in range(cols):
            for row in range(rows_per_col):
                # 题号：col * rows_per_col + row
                q_idx = col * rows_per_col + row
                # 列中心 x 坐标
                col_center_x = int(margin_x + col_width * (col + 0.5))
                # 行中心 y 坐标
                row_center_y = int(margin_y + row_height * (row + 0.5))

                # 在该位置检测 4 个选项气泡
                # 4 个选项在列内水平排列
                opt_spacing = col_width / (opts + 1)
                for opt in range(opts):
                    cx = int(col_center_x - col_width / 2 + opt_spacing * (opt + 1))
                    cy = row_center_y

                    # 计算填充率
                    fill_ratio = self._compute_fill_ratio(binary, (cx, cy), radius)
                    filled = fill_ratio >= self.FILL_THRESHOLD

                    bubbles.append(BubbleMark(
                        question_index=q_idx,
                        option_index=opt,
                        filled=filled,
                        fill_ratio=fill_ratio,
                        center=(cx, cy),
                        radius=radius,
                    ))

        return bubbles

    # ============ 通用检测（Phase 4）============

    def _detect_bubbles_generic(self, binary: np.ndarray) -> list[BubbleMark]:
        """通用 HoughCircles 圆检测（Phase 4 启用）

        Phase 1 阶段返回空列表，后续实现：
        1. cv2.HoughCircles 检测所有圆
        2. 按位置聚类成题号（同行/同列归为一题）
        3. 每题内按 x 坐标排序为 ABCD
        """
        logger.warning("[AnswerCardDetector] generic 模式暂未实现（Phase 4）")
        return []

    # ============ 工具方法 ============

    def _compute_fill_ratio(self, binary: np.ndarray, center: tuple[int, int], radius: int) -> float:
        """计算圆区域内白色像素占比（前景填充率）

        Args:
            binary: 二值化图像（前景为白色 255，背景为黑色 0）
            center: 圆心 (x, y)
            radius: 圆半径

        Returns:
            填充率 (0.0-1.0)
        """
        h, w = binary.shape
        cx, cy = center

        # 边界检查
        if cx - radius < 0 or cx + radius >= w or cy - radius < 0 or cy + radius >= h:
            return 0.0

        # 创建圆形 mask
        mask = np.zeros((radius * 2 + 1, radius * 2 + 1), dtype=np.uint8)
        cv2.circle(mask, (radius, radius), radius, 255, -1)

        # 提取 ROI
        roi = binary[cy - radius:cy + radius + 1, cx - radius:cx + radius + 1]

        # 计算 mask 区域内的白色像素占比
        if roi.shape != mask.shape:
            return 0.0

        masked = cv2.bitwise_and(roi, mask)
        white_pixels = int(np.count_nonzero(masked))
        total_pixels = int(np.count_nonzero(mask))

        if total_pixels == 0:
            return 0.0

        return white_pixels / total_pixels

    def _bubbles_to_answers(self, bubbles: list[BubbleMark]) -> dict[int, list[int]]:
        """将气泡列表转换为答案字典

        Returns:
            {question_index: [option_indices]}
            例如 {0: [0], 1: [1, 3]} 表示第1题选A，第2题选BD
            未填涂的题不在字典中
        """
        answers: dict[int, list[int]] = {}
        for b in bubbles:
            if b.filled:
                answers.setdefault(b.question_index, []).append(b.option_index)
        # 每题内按选项索引排序
        for q_idx in answers:
            answers[q_idx].sort()
        return answers

    def _render_debug_image(self, img: np.ndarray, bubbles: list[BubbleMark], skew_angle: float) -> str:
        """生成调试可视化图：在原图上绘制气泡检测结果

        - 绿色圆：已填涂
        - 红色圆：未填涂
        - 顶部显示倾斜角度

        Returns:
            base64 编码的 PNG 图片
        """
        debug = img.copy()
        for b in bubbles:
            color = (0, 255, 0) if b.filled else (0, 0, 255)  # BGR
            cv2.circle(debug, b.center, b.radius, color, 2)
            # 在圆心标注填充率
            text = f"{b.fill_ratio:.2f}"
            cv2.putText(debug, text, (b.center[0] - 15, b.center[1] - b.radius - 3),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1)

        # 顶部显示倾斜角度
        cv2.putText(debug, f"Skew: {skew_angle:.2f}°  Filled: {sum(1 for b in bubbles if b.filled)}/{len(bubbles)}",
                    (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # 编码为 PNG → base64
        ok, buffer = cv2.imencode('.png', debug)
        if not ok:
            return ""
        return base64.b64encode(buffer).decode('utf-8')


# 模块级单例
answer_card_detector = AnswerCardDetector()
