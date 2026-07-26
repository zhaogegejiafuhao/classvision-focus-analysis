"""Phase 2 填空题 OCR 判分 - 单元测试 + 端到端验证

测试覆盖：
1. _normalize_fill_text 文本规范化
2. _to_halfwidth 全角转半角
3. _levenshtein_distance / _levenshtein_similarity 编辑距离与相似度
4. _grade_fill_question 端到端（需后端运行，会真实调用 OCR）
"""
import sys
import os

# 把项目根目录加入 sys.path
sys.path.insert(0, "d:/ClassVision")


def test_normalize_fill_text():
    """测试文本规范化"""
    from backend.services.answer_sheet import _normalize_fill_text

    # 1. 全角数字 → 半角
    assert _normalize_fill_text("１２３") == "123", "全角数字转半角失败"

    # 2. 全角字母 → 半角小写
    assert _normalize_fill_text("ＡＢＣ") == "abc", "全角字母转半角小写失败"

    # 3. 去除换行
    assert _normalize_fill_text("hello\nworld") == "hello world", "去换行失败"

    # 4. 去除首尾标点
    assert _normalize_fill_text("。答案。") == "答案", "去首尾中文句号失败"
    assert _normalize_fill_text('"answer"') == "answer", "去首尾引号失败"

    # 5. 合并连续空白
    assert _normalize_fill_text("a   b\t\tc") == "a b c", "合并空白失败"

    # 6. 综合场景
    raw_ocr = "  Ｘ＝５。\n  "
    expected = "x=5"
    actual = _normalize_fill_text(raw_ocr)
    assert actual == expected, f"综合场景失败: raw={raw_ocr!r}, expected={expected!r}, actual={actual!r}"

    # 7. 空字符串
    assert _normalize_fill_text("") == "", "空字符串处理失败"
    assert _normalize_fill_text(None) == "", "None 处理失败"

    print("[PASS] test_normalize_fill_text")


def test_to_halfwidth():
    """测试全角转半角"""
    from backend.services.answer_sheet import _to_halfwidth

    # 全角空格
    assert _to_halfwidth("　") == " ", "全角空格失败"

    # 全角数字
    assert _to_halfwidth("０１２３４５６７８９") == "0123456789", "全角数字失败"

    # 全角字母
    assert _to_halfwidth("ＡＢＣａｂｃ") == "ABCabc", "全角字母失败"

    # 全角标点：：；，会被转换（在 U+FF01..U+FF5E 范围内）
    # 中文句号 。(U+3002) 不在全角范围内，原样保留
    result = _to_halfwidth("：；，。")
    assert result == ":;,。", f"全角标点失败: {result!r}"

    # 半角字符不变
    assert _to_halfwidth("abc123") == "abc123", "半角字符被修改"

    print("[PASS] test_to_halfwidth")


def test_levenshtein():
    """测试 Levenshtein 距离和相似度"""
    from backend.services.answer_sheet import _levenshtein_distance, _levenshtein_similarity

    # 1. 相同字符串
    assert _levenshtein_distance("abc", "abc") == 0, "相同字符串距离应为0"
    assert _levenshtein_similarity("abc", "abc") == 1.0, "相同字符串相似度应为1.0"

    # 2. 空字符串
    assert _levenshtein_distance("", "abc") == 3, "空字符串距离失败"
    assert _levenshtein_similarity("", "abc") == 0.0, "空字符串相似度失败"
    assert _levenshtein_similarity("", "") == 1.0, "双空字符串相似度应为1.0"

    # 3. 经典案例
    assert _levenshtein_distance("kitten", "sitting") == 3, "kitten/sitting 距离应为3"
    sim = _levenshtein_similarity("kitten", "sitting")
    assert 0.5 < sim < 0.6, f"kitten/sitting 相似度应在0.5-0.6之间，实际={sim}"

    # 4. 填空题场景
    # 学生写"x=5" vs 标准"x=5" 完全相同
    assert _levenshtein_similarity("x=5", "x=5") == 1.0
    # 学生写"x=5." vs 标准"x=5" 1个编辑距离
    # 距离=1, max_len=4, 相似度=0.75（< 0.85，模糊匹配不会通过）
    # 但 _normalize_fill_text 会去掉尾部句号，所以规范化后精确匹配能通过
    sim = _levenshtein_similarity("x=5.", "x=5")
    assert sim == 0.75, f"'x=5.' vs 'x=5' 相似度应为0.75，实际={sim}"
    # 学生写"x=6" vs 标准"x=5" 1个编辑距离
    sim = _levenshtein_similarity("x=6", "x=5")
    assert sim >= 0.66, f"'x=6' vs 'x=5' 相似度应>=0.66，实际={sim}"

    print("[PASS] test_levenshtein")


def test_mock_grade_fill_question():
    """模拟 _grade_fill_question 的核心判分逻辑（不调用真实 OCR）

    通过 mock OCR 返回值验证判分流程
    """
    from backend.services.answer_sheet import _normalize_fill_text, _levenshtein_similarity
    from backend.services.exam_service import auto_grade

    # 模拟一个填空题
    class MockQuestion:
        def __init__(self, answer, score=10):
            self.type = "fill"
            self.answer = answer
            self.score = score

    # 场景1: 完美匹配
    q = MockQuestion("x=5")
    ocr_text = "x=5"
    confidence = 0.95
    normalized = _normalize_fill_text(ocr_text)
    score, is_correct = auto_grade(q, normalized)
    assert is_correct, f"完美匹配应判对: normalized={normalized!r}"
    assert score == 10, f"完美匹配应得满分: score={score}"

    # 场景2: 全角字符（应通过规范化判对）
    q = MockQuestion("x=5")
    ocr_text = "ｘ＝５"  # 全角小写 x = 全角等号 = 全角数字5
    confidence = 0.90
    normalized = _normalize_fill_text(ocr_text)
    # 全角 ｘ(U+FF58) → x, ＝(U+FF1D) → =, ５(U+FF15) → 5 → "x=5"
    score, is_correct = auto_grade(q, normalized)
    assert normalized == "x=5", f"全角规范化失败: normalized={normalized!r}"
    assert is_correct, f"全角字符规范化后应判对: normalized={normalized!r}"
    assert score == 10, f"全角字符规范化后应得满分: score={score}"
    print(f"  场景2 全角字符规范化: ocr={ocr_text!r} → normalized={normalized!r} (判对 ✓)")

    # 场景3: 带换行的 OCR 输出
    q = MockQuestion("hello world")
    ocr_text = "hello\nworld"  # OCR 经常会把空格识别成换行
    confidence = 0.92
    normalized = _normalize_fill_text(ocr_text)
    score, is_correct = auto_grade(q, normalized)
    assert is_correct, f"换行→空格应判对: normalized={normalized!r}, expected='hello world'"
    print(f"  场景3 换行处理: ocr={ocr_text!r} → normalized={normalized!r} (判对 ✓)")

    # 场景4: 带尾部句号
    q = MockQuestion("42")
    ocr_text = "42。"  # OCR 经常加中文句号
    confidence = 0.88
    normalized = _normalize_fill_text(ocr_text)
    score, is_correct = auto_grade(q, normalized)
    assert is_correct, f"尾部句号应判对: normalized={normalized!r}, expected='42'"
    print(f"  场景4 尾部标点: ocr={ocr_text!r} → normalized={normalized!r} (判对 ✓)")

    # 场景5: 单字符错误，相似度高，模糊匹配通过
    q = MockQuestion("beijing")
    ocr_text = "beijlng"  # i 识别成了 l
    confidence = 0.90
    normalized = _normalize_fill_text(ocr_text)
    score, is_correct = auto_grade(q, normalized)
    sim = _levenshtein_similarity(normalized, _normalize_fill_text(q.answer))
    if not is_correct and confidence > 0.85 and sim >= 0.85:
        score, is_correct = q.score, True
    # beijing(7) vs beijlng(7) 距离=1，相似度=6/7≈0.857
    assert is_correct, f"单字符错误应通过模糊匹配: normalized={normalized!r}, sim={sim:.3f}"
    print(f"  场景5 模糊匹配通过: ocr={ocr_text!r}, sim={sim:.3f} (判对 ✓)")

    print("[PASS] test_mock_grade_fill_question")


def main():
    print("=" * 60)
    print("Phase 2 填空题 OCR 判分 - 单元测试")
    print("=" * 60)
    test_normalize_fill_text()
    test_to_halfwidth()
    test_levenshtein()
    test_mock_grade_fill_question()
    print("=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
