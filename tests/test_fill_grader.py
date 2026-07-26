"""A+B+C 方案单元测试

A. 多空填空题拆分匹配 + 部分分
B. 数值/单位容差匹配
C. OCR 识别顺序稳定化（_sort_blocks_by_reading_order / _concat_blocks_to_text）
"""
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# ============================================================
# A. 多空填空题拆分匹配
# ============================================================

def test_single_blank_exact_match():
    """单空：精确匹配"""
    from backend.services.fill_grader import grade_fill_answer

    # 完全相同
    score, is_correct, detail = grade_fill_answer("x=5", "x=5", 10.0)
    assert score == 10.0 and is_correct is True
    assert detail["is_multi_blank"] is False
    assert detail["correct_count"] == 1
    assert detail["per_blank"][0]["method"] == "exact"
    print("[PASS] test_single_blank_exact_match")


def test_single_blank_mismatch():
    """单空：错误答案"""
    from backend.services.fill_grader import grade_fill_answer

    score, is_correct, detail = grade_fill_answer("x=6", "x=5", 10.0)
    assert score == 0.0 and is_correct is False
    assert detail["per_blank"][0]["method"] == "none"
    print("[PASS] test_single_blank_mismatch")


def test_multi_blank_all_correct():
    """多空：全对（; 分隔）"""
    from backend.services.fill_grader import grade_fill_answer

    score, is_correct, detail = grade_fill_answer("x=5;y=3", "x=5;y=3", 10.0)
    assert score == 10.0 and is_correct is True
    assert detail["is_multi_blank"] is True
    assert detail["separator"] == ";"
    assert detail["blank_count"] == 2
    assert detail["correct_count"] == 2
    print("[PASS] test_multi_blank_all_correct")


def test_multi_blank_partial_correct():
    """多空：部分对（一半对，得半分）"""
    from backend.services.fill_grader import grade_fill_answer

    # 标准答案 2 空，学生只对 1 空
    score, is_correct, detail = grade_fill_answer("x=5;y=4", "x=5;y=3", 10.0)
    assert score == 5.0, f"应得半分 5.0，实际 {score}"
    assert is_correct is False
    assert detail["correct_count"] == 1
    assert detail["blank_count"] == 2
    assert detail["per_blank"][0]["matched"] is True  # x=5
    assert detail["per_blank"][1]["matched"] is False  # y=4 vs y=3
    print(f"[PASS] test_multi_blank_partial_correct (score={score})")


def test_multi_blank_all_wrong():
    """多空：全错"""
    from backend.services.fill_grader import grade_fill_answer

    score, is_correct, detail = grade_fill_answer("x=6;y=4", "x=5;y=3", 10.0)
    assert score == 0.0 and is_correct is False
    assert detail["correct_count"] == 0
    print("[PASS] test_multi_blank_all_wrong")


def test_multi_blank_student_fewer():
    """多空：学生少填一空"""
    from backend.services.fill_grader import grade_fill_answer

    # 标准 2 空，学生只填 1 空（且对）
    score, is_correct, detail = grade_fill_answer("x=5", "x=5;y=3", 10.0)
    assert score == 5.0, f"少填一空但答对一空，应得 5.0，实际 {score}"
    assert is_correct is False
    assert detail["correct_count"] == 1
    print(f"[PASS] test_multi_blank_student_fewer (score={score})")


def test_multi_blank_three_blanks():
    """多空：3 空场景，按 1/3 比例给分"""
    from backend.services.fill_grader import grade_fill_answer

    # 标准 3 空，学生对 2 空
    score, is_correct, detail = grade_fill_answer("a;b;c", "a;X;c", 9.0)
    assert score == 6.0, f"3 空对 2 空，9×(2/3)=6.0，实际 {score}"
    assert is_correct is False
    assert detail["correct_count"] == 2
    assert detail["blank_count"] == 3
    print(f"[PASS] test_multi_blank_three_blanks (score={score})")


def test_separator_detection():
    """分隔符检测：中英文逗号/分号/顿号"""
    from backend.services.fill_grader import detect_fill_separator

    assert detect_fill_separator("a;b") == ";"
    assert detect_fill_separator("a；b") == "；"
    assert detect_fill_separator("a,b") == ","
    assert detect_fill_separator("a，b") == "，"
    assert detect_fill_separator("a、b") == "、"
    assert detect_fill_separator("ab") is None
    # 优先级：先 ; 后 ，（标准答案里 ; 出现就用 ;）
    assert detect_fill_separator("a;b,c") == ";"
    print("[PASS] test_separator_detection")


def test_multi_blank_chinese_separator():
    """多空：中文逗号分隔"""
    from backend.services.fill_grader import grade_fill_answer

    score, is_correct, detail = grade_fill_answer("北京，上海", "北京，上海", 10.0)
    assert score == 10.0 and is_correct is True
    assert detail["separator"] == "，"
    print("[PASS] test_multi_blank_chinese_separator")


# ============================================================
# B. 数值/单位容差
# ============================================================

def test_numeric_tolerance_equal():
    """数值容差：3.14 ≈ 3.140"""
    from backend.services.fill_grader import grade_fill_answer, _match_single_blank

    matched, method = _match_single_blank("3.14", "3.140")
    assert matched and method == "numeric"

    matched, method = _match_single_blank("3.14", "3.1400000")
    assert matched and method == "numeric"

    # 整数 vs 小数
    matched, method = _match_single_blank("5", "5.0")
    assert matched and method == "numeric"

    # 学生答案 5.0 vs 标准 5
    score, is_correct, _ = grade_fill_answer("5.0", "5", 10.0)
    assert score == 10.0 and is_correct is True
    print("[PASS] test_numeric_tolerance_equal")


def test_numeric_tolerance_different():
    """数值容差：3.14 vs 3.14159 应不等"""
    from backend.services.fill_grader import _match_single_blank

    matched, method = _match_single_blank("3.14", "3.14159")
    assert not matched, "3.14 和 3.14159 差值过大应判不等"
    print("[PASS] test_numeric_tolerance_different")


def test_unit_equivalence_mass():
    """单位等价：质量（kg = 千克 = 公斤）"""
    from backend.services.fill_grader import _match_single_blank

    # kg = 千克
    matched, method = _match_single_blank("5kg", "5千克")
    assert matched and method == "unit", f"5kg vs 5千克 应等价，实际 method={method}"

    # kg = 公斤
    matched, method = _match_single_blank("5kg", "5公斤")
    assert matched and method == "unit"

    # kg ≠ g（单位不等价）
    matched, _ = _match_single_blank("5kg", "5g")
    assert not matched, "5kg vs 5g 单位不等价应判不等"

    # 5kg ≠ 5（一个有单位一个没有）
    matched, _ = _match_single_blank("5kg", "5")
    assert not matched, "5kg vs 5 一个有单位一个没有应判不等"
    print("[PASS] test_unit_equivalence_mass")


def test_unit_equivalence_length():
    """单位等价：长度（m = 米，cm = 厘米 = 公分）"""
    from backend.services.fill_grader import _match_single_blank

    matched, _ = _match_single_blank("1.5m", "1.5米")
    assert matched

    matched, _ = _match_single_blank("100cm", "100厘米")
    assert matched

    matched, _ = _match_single_blank("100cm", "100公分")
    assert matched

    # m ≠ cm（单位不等价，即使数值相同）
    matched, _ = _match_single_blank("1m", "1cm")
    assert not matched
    print("[PASS] test_unit_equivalence_length")


def test_unit_no_actual_conversion():
    """单位等价：不做实际换算（100cm ≠ 1m，虽然物理上等价）"""
    from backend.services.fill_grader import _match_single_blank

    matched, _ = _match_single_blank("100cm", "1m")
    assert not matched, "100cm 和 1m 物理等价但本系统不做换算，应判不等"
    print("[PASS] test_unit_no_actual_conversion")


def test_unit_with_multi_blank():
    """多空场景下，每空独立做单位等价判断"""
    from backend.services.fill_grader import grade_fill_answer

    # 标准：5kg,3m  学生：5千克,3米  → 全对
    score, is_correct, detail = grade_fill_answer("5千克,3米", "5kg,3m", 10.0)
    assert score == 10.0 and is_correct is True
    assert detail["per_blank"][0]["method"] == "unit"
    assert detail["per_blank"][1]["method"] == "unit"
    print("[PASS] test_unit_with_multi_blank")


def test_negative_and_scientific():
    """负数和科学计数法"""
    from backend.services.fill_grader import _match_single_blank

    # 负数
    matched, method = _match_single_blank("-2.5", "-2.5")
    assert matched and method == "exact"

    # 科学计数法
    matched, method = _match_single_blank("1e3", "1000")
    assert matched and method == "numeric", f"1e3 vs 1000 应数值相等，实际 method={method}"

    # 负数 + 单位
    matched, method = _match_single_blank("-2.5m", "-2.5米")
    assert matched and method == "unit"
    print("[PASS] test_negative_and_scientific")


# ============================================================
# C. OCR 识别顺序稳定化
# ============================================================

def test_sort_blocks_single_line():
    """C: 单行多块按 x 排序"""
    from backend.services.ocr import _sort_blocks_by_reading_order

    # 3 个块在同一行（y 相近），x 乱序
    blocks = [
        {"bbox": [50, 10, 70, 50], "text": "="},   # 中间
        {"bbox": [10, 10, 30, 50], "text": "x"},   # 最左
        {"bbox": [80, 10, 100, 50], "text": "5"},  # 最右
    ]
    lines = _sort_blocks_by_reading_order(blocks)
    assert len(lines) == 1, f"应在同一行，实际 {len(lines)} 行"
    assert [b["text"] for b in lines[0]] == ["x", "=", "5"], \
        f"行内应按 x 升序排列，实际 {[b['text'] for b in lines[0]]}"
    print("[PASS] test_sort_blocks_single_line")


def test_sort_blocks_multi_line():
    """C: 多行按 y 分组"""
    from backend.services.ocr import _sort_blocks_by_reading_order

    # 2 行，每行 2 块，y 差距明显
    blocks = [
        {"bbox": [10, 100, 30, 140], "text": "b"},   # 第2行最左
        {"bbox": [10, 10, 30, 50], "text": "a"},     # 第1行最左
        {"bbox": [50, 100, 70, 140], "text": "d"},   # 第2行最右
        {"bbox": [50, 10, 70, 50], "text": "c"},     # 第1行最右
    ]
    lines = _sort_blocks_by_reading_order(blocks)
    assert len(lines) == 2, f"应分 2 行，实际 {len(lines)} 行"
    # 第1行：a, c
    assert [b["text"] for b in lines[0]] == ["a", "c"]
    # 第2行：b, d
    assert [b["text"] for b in lines[1]] == ["b", "d"]
    print("[PASS] test_sort_blocks_multi_line")


def test_sort_blocks_y_jitter():
    """C: y 抖动小于行高一半时归为同一行"""
    from backend.services.ocr import _sort_blocks_by_reading_order

    # 2 块 y 抖动 10（行高 40，抖动 < 20 应同行）
    blocks = [
        {"bbox": [10, 10, 30, 50], "text": "a"},
        {"bbox": [50, 20, 70, 60], "text": "b"},  # y 抖动 10，行高 40，< 20 同行
    ]
    lines = _sort_blocks_by_reading_order(blocks)
    assert len(lines) == 1, f"y 抖动小于行高一半应同行，实际 {len(lines)} 行"
    print("[PASS] test_sort_blocks_y_jitter")


def test_concat_blocks_no_gap():
    """C: 紧邻块拼接无空格（'x' '=' '5' → 'x=5'）"""
    from backend.services.ocr import _concat_blocks_to_text

    # 3 块紧邻（间距 0），拼成 'x=5'
    blocks = [
        {"bbox": [10, 10, 30, 50], "text": "x"},   # x 占 10-30
        {"bbox": [30, 10, 50, 50], "text": "="},   # = 占 30-50（紧邻 x）
        {"bbox": [50, 10, 70, 50], "text": "5"},   # 5 占 50-70（紧邻 =）
    ]
    text = _concat_blocks_to_text(blocks)
    assert text == "x=5", f"紧邻块应拼成 'x=5'，实际 {text!r}"
    print(f"[PASS] test_concat_blocks_no_gap (text={text!r})")


def test_concat_blocks_with_gap():
    """C: 有间距块插空格（'hello' 'world' → 'hello world'）"""
    from backend.services.ocr import _concat_blocks_to_text

    # 2 块有明显间距，应插入空格
    blocks = [
        {"bbox": [10, 10, 60, 50], "text": "hello"},   # 占 10-60（宽 50）
        {"bbox": [80, 10, 130, 50], "text": "world"},  # 占 80-130，间距 20
    ]
    text = _concat_blocks_to_text(blocks)
    assert text == "hello world", f"有间距块应拼成 'hello world'，实际 {text!r}"
    print(f"[PASS] test_concat_blocks_with_gap (text={text!r})")


def test_concat_blocks_multi_line():
    """C: 多行用 \\n 分隔"""
    from backend.services.ocr import _concat_blocks_to_text

    blocks = [
        {"bbox": [10, 10, 60, 50], "text": "line1"},
        {"bbox": [10, 100, 60, 140], "text": "line2"},
    ]
    text = _concat_blocks_to_text(blocks)
    assert text == "line1\nline2", f"多行应用 \\n 分隔，实际 {text!r}"
    print(f"[PASS] test_concat_blocks_multi_line (text={text!r})")


def test_concat_blocks_empty():
    """C: 空列表返回空字符串"""
    from backend.services.ocr import _concat_blocks_to_text

    assert _concat_blocks_to_text([]) == ""
    print("[PASS] test_concat_blocks_empty")


def test_concat_blocks_unordered_input():
    """C: 输入顺序乱（=, 5, x）也能拼成 'x=5'"""
    from backend.services.ocr import _concat_blocks_to_text

    # 故意按乱序输入
    blocks = [
        {"bbox": [50, 10, 70, 50], "text": "5"},
        {"bbox": [10, 10, 30, 50], "text": "x"},
        {"bbox": [30, 10, 50, 50], "text": "="},
    ]
    text = _concat_blocks_to_text(blocks)
    assert text == "x=5", f"乱序输入应排序后拼成 'x=5'，实际 {text!r}"
    print(f"[PASS] test_concat_blocks_unordered_input (text={text!r})")


# ============================================================
# 集成：A+B 联动（auto_grade fill 分支）
# ============================================================

def test_auto_grade_fill_single():
    """auto_grade fill 分支：单空场景"""
    from backend.services.exam_service import auto_grade
    from unittest.mock import MagicMock

    q = MagicMock()
    q.type = "fill"
    q.answer = "x=5"
    q.score = 5.0

    # 完美匹配
    score, is_correct = auto_grade(q, "x=5")
    assert score == 5.0 and is_correct is True

    # 数值容差
    q.answer = "3.14"
    score, is_correct = auto_grade(q, "3.140")
    assert score == 5.0 and is_correct is True

    # 单位等价
    q.answer = "5kg"
    score, is_correct = auto_grade(q, "5千克")
    assert score == 5.0 and is_correct is True
    print("[PASS] test_auto_grade_fill_single")


def test_auto_grade_fill_multi():
    """auto_grade fill 分支：多空场景，按比例给部分分"""
    from backend.services.exam_service import auto_grade
    from unittest.mock import MagicMock

    q = MagicMock()
    q.type = "fill"
    q.answer = "x=5;y=3"
    q.score = 10.0

    # 全对
    score, is_correct = auto_grade(q, "x=5;y=3")
    assert score == 10.0 and is_correct is True

    # 部分对（1/2 对，得 5 分）
    score, is_correct = auto_grade(q, "x=5;y=4")
    assert score == 5.0, f"应得半分 5.0，实际 {score}"
    assert is_correct is False
    print(f"[PASS] test_auto_grade_fill_multi (partial score={score})")


def main():
    print("=" * 60)
    print("A+B+C 方案单元测试")
    print("=" * 60)

    print("\n--- A. 多空填空题拆分匹配 ---")
    test_single_blank_exact_match()
    test_single_blank_mismatch()
    test_multi_blank_all_correct()
    test_multi_blank_partial_correct()
    test_multi_blank_all_wrong()
    test_multi_blank_student_fewer()
    test_multi_blank_three_blanks()
    test_separator_detection()
    test_multi_blank_chinese_separator()

    print("\n--- B. 数值/单位容差 ---")
    test_numeric_tolerance_equal()
    test_numeric_tolerance_different()
    test_unit_equivalence_mass()
    test_unit_equivalence_length()
    test_unit_no_actual_conversion()
    test_unit_with_multi_blank()
    test_negative_and_scientific()

    print("\n--- C. OCR 识别顺序稳定化 ---")
    test_sort_blocks_single_line()
    test_sort_blocks_multi_line()
    test_sort_blocks_y_jitter()
    test_concat_blocks_no_gap()
    test_concat_blocks_with_gap()
    test_concat_blocks_multi_line()
    test_concat_blocks_empty()
    test_concat_blocks_unordered_input()

    print("\n--- 集成：auto_grade fill 分支 ---")
    test_auto_grade_fill_single()
    test_auto_grade_fill_multi()

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
