"""填空题判分引擎（A+B 方案）

支持三种等价匹配策略：
1. 精确匹配（含规范化后）
2. 数值容差（"3.14" ≈ "3.140" ≈ "3.14000"）
3. 单位等价（"5kg" = "5千克" = "5公斤"）

支持多空填空题：
- 自动检测分隔符（; ； , ， 、）
- 按分隔符拆分学生答案和标准答案
- 每空独立匹配，按空数比例给部分分

被以下模块复用：
- backend.api.exam_routes.auto_grade (fill 分支，只取 score/is_correct)
- backend.services.answer_sheet._grade_fill_question (取完整 detail)
"""
import re
from typing import Optional


# ============ 单位等价表 ============
# 归一化到等价类标识符（不关心实际换算关系，只判等价）

_UNIT_EQUIV = {
    # 质量
    "kg": "mass_kg", "千克": "mass_kg", "公斤": "mass_kg",
    "g": "mass_g", "克": "mass_g",
    "mg": "mass_mg", "毫克": "mass_mg",
    "t": "mass_t", "吨": "mass_t",
    # 长度
    "m": "len_m", "米": "len_m",
    "cm": "len_cm", "厘米": "len_cm", "公分": "len_cm",
    "mm": "len_mm", "毫米": "len_mm",
    "km": "len_km", "千米": "len_km", "公里": "len_km",
    "dm": "len_dm", "分米": "len_dm",
    # 时间
    "s": "time_s", "sec": "time_s", "秒": "time_s",
    "min": "time_min", "minute": "time_min", "分钟": "time_min", "分": "time_min",
    "h": "time_h", "hr": "time_h", "hour": "time_h", "小时": "time_h", "时": "time_h",
    # 体积/容积
    "l": "vol_l", "升": "vol_l",
    "ml": "vol_ml", "毫升": "vol_ml",
    # 温度
    "c": "temp_c", "℃": "temp_c", "摄氏度": "temp_c", "度": "temp_c",
    # 百分比
    "%": "pct", "百分号": "pct",
}

# 多空分隔符优先级（中英文）
_FILL_SEPARATORS = [";", "；", ",", "，", "、"]


# ============ 辅助函数 ============

# 数值 + 单位正则：可选符号 + 数字（可含小数/科学计数法）+ 可选单位
_NUM_UNIT_RE = re.compile(
    r'^([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\s*([a-zA-Z\u4e00-\u9fff%℃]*)$'
)


def _split_number_and_unit(text: str) -> tuple[Optional[float], str]:
    """从字符串中拆分出数值和单位

    例：
        "3.14" → (3.14, "")
        "5kg" → (5.0, "kg")
        "1.5米" → (1.5, "米")
        "-2.5e3cm" → (-2500.0, "cm")
        "abc" → (None, "")
    """
    if not text:
        return None, ""
    m = _NUM_UNIT_RE.match(text.strip())
    if not m:
        return None, ""
    try:
        return float(m.group(1)), m.group(2)
    except (ValueError, TypeError):
        return None, ""


def _units_equivalent(u1: str, u2: str) -> bool:
    """判断两个单位是否等价

    规则：
    1. 都为空 → 等价（都是纯数值）
    2. 一个为空另一个非空 → 不等价（一个有单位一个没有）
    3. 直接相等 → 等价
    4. 归一化到等价类后相等 → 等价
    """
    if not u1 and not u2:
        return True
    if not u1 or not u2:
        return False
    if u1 == u2:
        return True
    n1 = _UNIT_EQUIV.get(u1.lower(), u1)
    n2 = _UNIT_EQUIV.get(u2.lower(), u2)
    return n1 == n2


def _match_single_blank(student: str, standard: str) -> tuple[bool, str]:
    """单空匹配：精确 → 数值容差 → 单位等价

    返回 (matched, match_method)
    match_method ∈ {"exact", "numeric", "unit", "none"}
    """
    if not student and not standard:
        return True, "exact"
    if not student or not standard:
        return False, "none"

    # 1. 精确匹配
    if student == standard:
        return True, "exact"

    # 2. 数值容差（纯数字比较，容差 1e-6）
    try:
        s_num = float(student)
        t_num = float(standard)
        if abs(s_num - t_num) < 1e-6:
            return True, "numeric"
    except (ValueError, TypeError):
        pass

    # 3. 单位等价（拆分数值+单位后分别比较）
    s_num, s_unit = _split_number_and_unit(student)
    t_num, t_unit = _split_number_and_unit(standard)
    if s_num is not None and t_num is not None:
        if abs(s_num - t_num) < 1e-6 and _units_equivalent(s_unit, t_unit):
            return True, "unit"

    return False, "none"


def detect_fill_separator(standard_answer: str) -> Optional[str]:
    """检测标准答案中使用的分隔符（用于多空填空题）

    优先级：; ； , ， 、
    返回第一个出现的分隔符，无则返回 None
    """
    if not standard_answer:
        return None
    for sep in _FILL_SEPARATORS:
        if sep in standard_answer:
            return sep
    return None


def grade_fill_answer(
    student_answer: str,
    standard_answer: str,
    max_score: float,
) -> tuple[float, bool, dict]:
    """填空题判分主入口

    返回 (score, is_correct, detail)
    - score: 实际得分（多空按比例给部分分）
    - is_correct: 是否完全正确（所有空都对）
    - detail: {
        "is_multi_blank": bool,
        "separator": str | None,
        "blank_count": int,         # 总空数
        "correct_count": int,       # 答对空数
        "per_blank": [              # 每空详情
            {"student": str, "standard": str, "matched": bool, "method": str},
            ...
        ],
      }
    """
    student = (student_answer or "").strip()
    standard = (standard_answer or "").strip()
    max_score = float(max_score)

    sep = detect_fill_separator(standard)

    if sep:
        # 多空填空题：按分隔符拆分，逐空匹配，按比例给部分分
        standard_parts = [p.strip() for p in standard.split(sep) if p.strip()]
        student_parts = [p.strip() for p in student.split(sep) if p.strip()]

        per_blank = []
        correct_count = 0
        for i, std in enumerate(standard_parts):
            stu = student_parts[i] if i < len(student_parts) else ""
            matched, method = _match_single_blank(stu, std)
            per_blank.append({
                "student": stu,
                "standard": std,
                "matched": matched,
                "method": method,
            })
            if matched:
                correct_count += 1

        blank_count = len(standard_parts)
        ratio = correct_count / blank_count if blank_count > 0 else 0.0
        score = round(max_score * ratio, 2)
        is_correct = (correct_count == blank_count)

        return score, is_correct, {
            "is_multi_blank": True,
            "separator": sep,
            "blank_count": blank_count,
            "correct_count": correct_count,
            "per_blank": per_blank,
        }

    # 单空填空题
    matched, method = _match_single_blank(student, standard)
    if matched:
        return max_score, True, {
            "is_multi_blank": False,
            "separator": None,
            "blank_count": 1,
            "correct_count": 1,
            "per_blank": [{
                "student": student,
                "standard": standard,
                "matched": True,
                "method": method,
            }],
        }
    return 0.0, False, {
        "is_multi_blank": False,
        "separator": None,
        "blank_count": 1,
        "correct_count": 0,
        "per_blank": [{
            "student": student,
            "standard": standard,
            "matched": False,
            "method": method,
        }],
    }
