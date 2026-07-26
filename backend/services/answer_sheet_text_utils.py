"""答题卡文本工具（从 answer_sheet.py 抽取）

包含：
- 填空题文本规范化（全角转半角、去标点等）
- Levenshtein 距离/相似度（模糊匹配二次确认）
- 作文题检测（路由到 grade_essay vs grade_math）
"""
from __future__ import annotations

import re


# ===== 填空题文本规范化 =====

# 全角→半角字符偏移量（除空格外）
_FULLWIDTH_OFFSET = 0xFEE0


def _normalize_fill_text(text: str) -> str:
    """填空题文本规范化

    用于 OCR 识别后与学生标准答案的比对，提高匹配率：
    1. 去除首尾空白和内部换行
    2. 全角字符转半角（数字、字母、标点）
    3. 统一小写
    4. 去除首尾的中英文标点
    5. 合并连续空白为单个空格
    """
    if not text:
        return ""
    # 1. 去换行
    s = text.replace("\r", " ").replace("\n", " ")
    # 2. 全角转半角
    s = _to_halfwidth(s)
    # 3. 小写
    s = s.lower()
    # 4. 去首尾标点（中英文）
    s = s.strip(" \t\"'.,;:!?，。；：！？、…—·（()[]【】「」『』")
    # 5. 合并连续空白
    s = " ".join(s.split())
    return s


def _to_halfwidth(s: str) -> str:
    """全角字符转半角

    全角空格 (U+3000) → 半角空格
    全角字符 (U+FF01..U+FF5E) → 减去 0xFEE0 转为对应半角
    """
    if not s:
        return s
    result = []
    for ch in s:
        code = ord(ch)
        if code == 0x3000:  # 全角空格
            result.append(" ")
        elif 0xFF01 <= code <= 0xFF5E:  # 全角字符范围
            result.append(chr(code - _FULLWIDTH_OFFSET))
        else:
            result.append(ch)
    return "".join(result)


# ===== Levenshtein 距离/相似度 =====

def _levenshtein_distance(s1: str, s2: str) -> int:
    """Levenshtein 编辑距离（DP 实现）"""
    if len(s1) < len(s2):
        return _levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def _levenshtein_similarity(s1: str, s2: str) -> float:
    """基于 Levenshtein 距离的相似度 [0.0, 1.0]

    similarity = 1 - distance / max(len(s1), len(s2))
    空字符串返回 0.0
    """
    if not s1 and not s2:
        return 1.0
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 1.0
    dist = _levenshtein_distance(s1, s2)
    return 1.0 - dist / max_len


# ===== 作文题检测 =====

# 作文题关键词（出现任一即认定为作文，路由到 grade_essay）
_ESSAY_KEYWORDS: tuple[str, ...] = (
    "作文", "写一篇", "题材", "文体",
    "不少于", "字数", "根据要求写作", "阅读下面的文字",
    "命题作文", "材料作文", "话题作文", "半命题作文",
    "写话", "写一段话",
)


def _is_essay_question(content: str) -> bool:
    """检测题目是否为语文作文（vs 数学/理科解答题）

    判定规则：题目内容包含作文相关关键词 → 视为作文
    用于在 _grade_essay_question 中决定路由到 grade_essay 还是 grade_math。

    Args:
        content: 题目内容文本

    Returns:
        True 表示认定为作文题，False 表示数学/理科解答题
    """
    if not content:
        return False
    text = content.lower()
    for kw in _ESSAY_KEYWORDS:
        if kw in text:
            return True
    # 特殊模式："以...为题"（支持全角／半角引号、书名号）
    if re.search(r"以[\"\"''《「『].{1,30}[\"\"''》」』]为题", content):
        return True
    return False
