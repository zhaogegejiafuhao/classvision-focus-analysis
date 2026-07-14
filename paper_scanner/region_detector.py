"""答题区域自动检测：检测答题卡上的网格结构，定位各题答题区域。"""

import cv2
import numpy as np


def detect_answer_regions(image: np.ndarray) -> list[dict]:
    """检测答题卡中的答题区域。

    答题卡通常由水平线和垂直线构成网格结构，每个格子是一道题的答题区。
    本函数通过检测线条来构建网格，然后输出每个格子的百分比坐标。

    返回 [{"x": float, "y": float, "w": float, "h": float}, ...]（百分比坐标）
    """
    if image is None or image.size == 0:
        return []

    h, w = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 尝试基于线条网格检测（适用于标准答题卡）
    regions = _detect_grid_regions(gray, w, h)
    if regions:
        return regions

    # 回退：基于文本块检测（适用于非标准答题卡）
    return _detect_text_regions(gray, w, h)


def _detect_grid_regions(gray: np.ndarray, w: int, h: int) -> list[dict]:
    """通过检测水平线和垂直线构建答题网格。"""
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)[1]

    # 检测水平线
    h_kernel_len = max(w // 20, 50)
    h_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (h_kernel_len, 1))
    h_lines_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, h_kernel)
    h_contours, _ = cv2.findContours(h_lines_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 收集有效水平线的 y 坐标和 x 范围
    h_lines = []
    for c in h_contours:
        x, y, rw, rh = cv2.boundingRect(c)
        if rw < w * 0.15:  # 水平线至少占宽度 15%
            continue
        h_lines.append((y, x, x + rw))
    h_lines.sort(key=lambda l: l[0])

    if len(h_lines) < 3:
        return []

    # 合并相近的水平线（同一行可能检测出多条）
    merged_h = []
    for y, x1, x2 in h_lines:
        if merged_h and abs(y - merged_h[-1][0]) < h * 0.008:
            # 合并到上一条
            merged_h[-1] = (y, min(merged_h[-1][1], x1), max(merged_h[-1][2], x2))
        else:
            merged_h.append((y, x1, x2))

    if len(merged_h) < 3:
        return []

    # 检测垂直线
    v_kernel_len = max(h // 20, 50)
    v_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, v_kernel_len))
    v_lines_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, v_kernel)
    v_contours, _ = cv2.findContours(v_lines_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    v_lines = []
    for c in v_contours:
        x, y, rw, rh = cv2.boundingRect(c)
        if rh < h * 0.15:
            continue
        v_lines.append((x, y, y + rh))
    v_lines.sort(key=lambda l: l[0])

    # 合并相近的垂直线
    merged_v = []
    for x, y1, y2 in v_lines:
        if merged_v and abs(x - merged_v[-1][0]) < w * 0.008:
            merged_v[-1] = (x, min(merged_v[-1][1], y1), max(merged_v[-1][2], y2))
        else:
            merged_v.append((x, y1, y2))

    # 按列分组水平线（答题卡可能有多个列区域）
    # 根据 x 范围将水平线聚类为列
    column_groups = _group_lines_into_columns(merged_h, w)

    regions = []
    for col_lines in column_groups:
        if len(col_lines) < 3:
            continue
        col_x_min = min(l[1] for l in col_lines)
        col_x_max = max(l[2] for l in col_lines)

        # 每对相邻水平线形成一个答题行
        for i in range(len(col_lines) - 1):
            y_top = col_lines[i][0]
            y_bot = col_lines[i + 1][0]
            row_h = y_bot - y_top
            if row_h < h * 0.01:  # 太窄，跳过
                continue
            # 行内可能有多列（用垂直线分割），这里先用整行
            regions.append({
                "x": round(col_x_min / w, 4),
                "y": round(y_top / h, 4),
                "w": round((col_x_max - col_x_min) / w, 4),
                "h": round(row_h / h, 4),
            })

    # 用垂直线进一步分割每个行区域为多个子区域
    if merged_v and len(merged_v) >= 2:
        regions = _split_regions_by_verticals(regions, merged_v, w, h)

    regions.sort(key=lambda r: (r["y"], r["x"]))

    # 限制最大数量，避免过多小区域
    if len(regions) > 60:
        # 按面积排序，保留较大的区域
        regions.sort(key=lambda r: r["w"] * r["h"], reverse=True)
        regions = regions[:60]
        regions.sort(key=lambda r: (r["y"], r["x"]))

    return regions


def _group_lines_into_columns(h_lines: list, w: int) -> list[list]:
    """将水平线按 x 范围聚类为列组。"""
    if not h_lines:
        return []

    # 按 x 起始位置排序
    sorted_lines = sorted(h_lines, key=lambda l: l[1])

    columns = []
    current_col = [sorted_lines[0]]
    col_x_threshold = w * 0.1

    for line in sorted_lines[1:]:
        # 如果 x 范围与当前列重叠或接近，加入当前列
        if abs(line[1] - current_col[-1][1]) < col_x_threshold:
            current_col.append(line)
        else:
            columns.append(current_col)
            current_col = [line]
    columns.append(current_col)

    # 每列内按 y 排序
    for col in columns:
        col.sort(key=lambda l: l[0])

    return columns


def _split_regions_by_verticals(regions: list[dict], v_lines: list, w: int, h: int) -> list[dict]:
    """用垂直线将宽行区域分割为多个子区域。"""
    # 只保留贯穿大部分高度的垂直线
    tall_v = [v for v in v_lines if (v[2] - v[1]) > h * 0.3]
    if len(tall_v) < 2:
        return regions

    split_regions = []
    for r in regions:
        r_x_start = r["x"] * w
        r_x_end = (r["x"] + r["w"]) * w
        # 找到落在此区域内的垂直线
        internal_v = [v[0] for v in tall_v if r_x_start < v[0] < r_x_end]
        if not internal_v:
            split_regions.append(r)
            continue
        # 用垂直线分割
        boundaries = [r_x_start] + sorted(internal_v) + [r_x_end]
        for i in range(len(boundaries) - 1):
            sub_w = boundaries[i + 1] - boundaries[i]
            if sub_w < w * 0.03:  # 子区域太窄，跳过
                continue
            split_regions.append({
                "x": round(boundaries[i] / w, 4),
                "y": r["y"],
                "w": round(sub_w / w, 4),
                "h": r["h"],
            })
    return split_regions


def _detect_text_regions(gray: np.ndarray, w: int, h: int) -> list[dict]:
    """回退方法：基于文本块检测区域（适用于非标准答题卡）。"""
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 21, 15
    )

    kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (w // 20, 1))
    kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (1, h // 40))
    dilated = cv2.dilate(binary, kernel_h, iterations=1)
    dilated = cv2.dilate(dilated, kernel_v, iterations=1)

    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    regions = []
    min_area = w * h * 0.002
    max_area = w * h * 0.3

    for c in contours:
        area = cv2.contourArea(c)
        if area < min_area or area > max_area:
            continue
        x, y, rw, rh = cv2.boundingRect(c)
        if rh < h * 0.01 or rw < w * 0.02:
            continue
        regions.append({
            "x": round(x / w, 4),
            "y": round(y / h, 4),
            "w": round(rw / w, 4),
            "h": round(rh / h, 4),
        })

    regions.sort(key=lambda r: (r["y"], r["x"]))
    return regions
