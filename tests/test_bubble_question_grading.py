"""Phase 4-3 多选/判断题精细化判分 - 单元测试

测试覆盖：
1. 单选题：正常判分 / 多涂判错 / 未填涂
2. 判断题：正常判分 / 多涂判错
3. 多选题：完全正确 / 少选部分分 / 错选0分 / 未填涂
4. 置信度计算：基于 fill_ratio 的"决策清晰度"
5. 气泡检测失败处理
"""
import asyncio
import sys
from unittest.mock import MagicMock, patch

# 把项目根目录加入 sys.path
sys.path.insert(0, "d:/ClassVision")

from cv_engine.detectors.answer_card_detector import (
    AnswerCardResult, BubbleMark,
)


def _make_bubble(q_idx: int, opt_idx: int, filled: bool, fill_ratio: float) -> BubbleMark:
    """构造 BubbleMark 工具函数"""
    return BubbleMark(
        question_index=q_idx,
        option_index=opt_idx,
        filled=filled,
        fill_ratio=fill_ratio,
        center=(10 + opt_idx * 20, 10 + q_idx * 20),
        radius=8,
    )


def _make_question(qid: int, qtype: str, answer: str, score: float = 2.0):
    """构造 Question mock"""
    q = MagicMock()
    q.id = qid
    q.type = qtype
    q.content = f"测试题目 {qid}"
    q.answer = answer
    q.score = score
    return q


def _make_region(qid: int):
    """构造 QuestionRegionImage"""
    from backend.services.paper_template import QuestionRegionImage
    return QuestionRegionImage(
        question_id=qid,
        region_type="bubble",
        image_bytes=b"fake_image_bytes",
        bbox=(0, 0, 100, 100),
    )


# ============ 单选题测试 ============

def test_single_correct():
    """单选题正常：填涂选项1（B）→ 答案 "1" → 满分"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(1001, "single", "1", score=2.0)
    region = _make_region(1001)

    # 4 个选项，只有选项 1 填涂
    bubbles = [
        _make_bubble(0, 0, False, 0.10),
        _make_bubble(0, 1, True, 0.85),
        _make_bubble(0, 2, False, 0.15),
        _make_bubble(0, 3, False, 0.12),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [1]},
        skew_angle=0.5,
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.question_id == 1001
    assert result.student_answer == "1", f"应填涂1，实际={result.student_answer}"
    assert result.score == 2.0, f"应满分2，实际={result.score}"
    assert result.is_correct is True
    assert result.comment == "", f"正常批改不应有comment，实际={result.comment!r}"
    # 置信度计算：已填涂均值=0.85，未填涂均值=(0.10+0.15+0.12)/3=0.1233
    # (0.85 + (1-0.1233)) / 2 ≈ 0.863
    assert 0.8 < result.confidence < 0.9, f"置信度应在0.8-0.9，实际={result.confidence}"
    assert result.grading_detail["student_options"] == [1]
    assert result.grading_detail["bubbles_filled"] == 1
    assert "avg_fill_ratio" in result.grading_detail
    print("[PASS] test_single_correct")


def test_single_multiple_fills_wrong():
    """单选题多涂：填涂选项1和2 → 判错，0分，comment 含"多涂" """
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(1002, "single", "1", score=2.0)
    region = _make_region(1002)

    # 选项 1 和 2 都填涂（多涂）
    bubbles = [
        _make_bubble(0, 0, False, 0.10),
        _make_bubble(0, 1, True, 0.80),
        _make_bubble(0, 2, True, 0.75),
        _make_bubble(0, 3, False, 0.12),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [1, 2]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "1,2", f"应记录多涂1,2，实际={result.student_answer}"
    assert result.score == 0, f"多涂应0分，实际={result.score}"
    assert result.is_correct is False
    assert "多涂" in result.comment, f"comment 应含'多涂'，实际={result.comment!r}"
    print("[PASS] test_single_multiple_fills_wrong")


def test_single_empty():
    """单选题未填涂 → 0分，comment 含"未填涂" """
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(1003, "single", "1", score=2.0)
    region = _make_region(1003)

    # 所有选项都未填涂
    bubbles = [
        _make_bubble(0, 0, False, 0.08),
        _make_bubble(0, 1, False, 0.10),
        _make_bubble(0, 2, False, 0.09),
        _make_bubble(0, 3, False, 0.12),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={},  # 空答案
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "", f"未填涂应空字符串，实际={result.student_answer!r}"
    assert result.score == 0
    assert result.is_correct is False
    assert "未填涂" in result.comment
    # 全部未填涂：置信度 = 1 - avg(0.08,0.10,0.09,0.12) = 1 - 0.0975 = 0.9025
    assert 0.85 < result.confidence < 0.95, f"未填涂置信度应≈0.90，实际={result.confidence}"
    print("[PASS] test_single_empty")


# ============ 判断题测试 ============

def test_judge_correct_true():
    """判断题正常：填涂选项0（true）→ 答案 "true" → 满分"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(2001, "judge", "true", score=1.0)
    region = _make_region(2001)

    bubbles = [
        _make_bubble(0, 0, True, 0.90),
        _make_bubble(0, 1, False, 0.10),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [0]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "true", f"填涂0应转true，实际={result.student_answer}"
    assert result.score == 1.0
    assert result.is_correct is True
    print("[PASS] test_judge_correct_true")


def test_judge_correct_false():
    """判断题正常：填涂选项1（false）→ 答案 "false" → 满分"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(2002, "judge", "false", score=1.0)
    region = _make_region(2002)

    bubbles = [
        _make_bubble(0, 0, False, 0.10),
        _make_bubble(0, 1, True, 0.88),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [1]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "false"
    assert result.score == 1.0
    assert result.is_correct is True
    print("[PASS] test_judge_correct_false")


def test_judge_multiple_fills_wrong():
    """判断题多涂：选项0和1都填涂 → 判错，0分"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(2003, "judge", "true", score=1.0)
    region = _make_region(2003)

    bubbles = [
        _make_bubble(0, 0, True, 0.70),
        _make_bubble(0, 1, True, 0.65),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [0, 1]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "0,1"
    assert result.score == 0
    assert result.is_correct is False
    assert "多涂" in result.comment
    print("[PASS] test_judge_multiple_fills_wrong")


# ============ 多选题测试 ============

def test_multi_full_correct():
    """多选题完全正确：填涂 0,2,3 → 满分"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(3001, "multi", "0,2,3", score=4.0)
    region = _make_region(3001)

    bubbles = [
        _make_bubble(0, 0, True, 0.88),
        _make_bubble(0, 1, False, 0.12),
        _make_bubble(0, 2, True, 0.90),
        _make_bubble(0, 3, True, 0.85),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [0, 2, 3]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "0,2,3"
    assert result.score == 4.0, f"完全正确应满分4，实际={result.score}"
    assert result.is_correct is True
    assert result.comment == ""
    print("[PASS] test_multi_full_correct")


def test_multi_partial_credit():
    """多选题少选：标准 0,2,3（满分4），学生只填 0,2 → 部分分

    ratio = 2/3 ≈ 0.667
    score = 4 * 0.667 * 0.5 ≈ 1.33
    """
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(3002, "multi", "0,2,3", score=4.0)
    region = _make_region(3002)

    bubbles = [
        _make_bubble(0, 0, True, 0.88),
        _make_bubble(0, 1, False, 0.12),
        _make_bubble(0, 2, True, 0.85),
        _make_bubble(0, 3, False, 0.10),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [0, 2]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "0,2"
    # ratio = 2/3, score = 4 * (2/3) * 0.5 = 4/3 ≈ 1.33
    expected = round(4.0 * (2 / 3) * 0.5, 2)
    assert abs(result.score - expected) < 0.01, f"少选应给{expected}，实际={result.score}"
    assert result.is_correct is False, "少选不应判全对"
    assert "少选" in result.comment
    assert "2/3" in result.comment, f"comment 应显示 2/3，实际={result.comment!r}"
    print(f"[PASS] test_multi_partial_credit (score={result.score})")


def test_multi_wrong_choice_zero():
    """多选题错选：标准 0,2，学生填 0,1 → 0分（错选1）"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(3003, "multi", "0,2", score=4.0)
    region = _make_region(3003)

    bubbles = [
        _make_bubble(0, 0, True, 0.85),
        _make_bubble(0, 1, True, 0.80),
        _make_bubble(0, 2, False, 0.12),
        _make_bubble(0, 3, False, 0.10),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [0, 1]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == "0,1"
    assert result.score == 0, f"错选应0分，实际={result.score}"
    assert result.is_correct is False
    assert "错选" in result.comment or "多选" in result.comment
    print("[PASS] test_multi_wrong_choice_zero")


def test_multi_empty():
    """多选题未填涂 → 0分"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(3004, "multi", "0,2", score=4.0)
    region = _make_region(3004)

    bubbles = [
        _make_bubble(0, 0, False, 0.10),
        _make_bubble(0, 1, False, 0.08),
        _make_bubble(0, 2, False, 0.09),
        _make_bubble(0, 3, False, 0.11),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.student_answer == ""
    assert result.score == 0
    assert result.is_correct is False
    assert "未填涂" in result.comment
    print("[PASS] test_multi_empty")


# ============ 置信度计算测试 ============

def test_confidence_clear_decision():
    """置信度：决策清晰场景（已填涂高、未填涂低）→ 置信度高"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(4001, "single", "1", score=2.0)
    region = _make_region(4001)

    # 已填涂 0.95，未填涂 0.05 → 决策非常清晰
    bubbles = [
        _make_bubble(0, 0, False, 0.05),
        _make_bubble(0, 1, True, 0.95),
        _make_bubble(0, 2, False, 0.04),
        _make_bubble(0, 3, False, 0.06),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [1]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    # (0.95 + (1 - 0.05)) / 2 = 0.95
    assert result.confidence >= 0.90, f"决策清晰应置信度≥0.90，实际={result.confidence}"
    print(f"[PASS] test_confidence_clear_decision (confidence={result.confidence})")


def test_confidence_ambiguous_decision():
    """置信度：决策模糊场景（已填涂低、未填涂接近阈值）→ 置信度低"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(4002, "single", "1", score=2.0)
    region = _make_region(4002)

    # 已填涂 0.50（刚过阈值），未填涂 0.42（接近阈值）→ 决策模糊
    bubbles = [
        _make_bubble(0, 0, False, 0.42),
        _make_bubble(0, 1, True, 0.50),
        _make_bubble(0, 2, False, 0.40),
        _make_bubble(0, 3, False, 0.43),
    ]
    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        bubbles=bubbles,
        answers={0: [1]},
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    # (0.50 + (1-0.4167)) / 2 ≈ 0.54
    assert result.confidence < 0.70, f"决策模糊应置信度<0.70，实际={result.confidence}"
    print(f"[PASS] test_confidence_ambiguous_decision (confidence={result.confidence})")


# ============ 检测失败测试 ============

def test_detect_failure():
    """气泡检测失败：detect_result.error 不为 None → 返回错误结果"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator

    question = _make_question(5001, "single", "1", score=2.0)
    region = _make_region(5001)

    detect_result = AnswerCardResult(
        template_type="standard_5x10x4",
        error="图像解码失败",
    )

    orchestrator = AnswerSheetOrchestrator()
    with patch("backend.services.answer_sheet.answer_card_detector.detect", return_value=detect_result):
        result = asyncio.run(orchestrator._grade_bubble_question(question, region))

    assert result.error is not None
    assert "气泡检测失败" in result.error
    assert result.score == 0
    assert result.is_correct is None, "检测失败应 is_correct=None（未批改）"
    print("[PASS] test_detect_failure")


# ============ 主入口 ============

def main():
    print("=" * 60)
    print("Phase 4-3 多选/判断题精细化判分 - 单元测试")
    print("=" * 60)
    test_single_correct()
    test_single_multiple_fills_wrong()
    test_single_empty()
    test_judge_correct_true()
    test_judge_correct_false()
    test_judge_multiple_fills_wrong()
    test_multi_full_correct()
    test_multi_partial_credit()
    test_multi_wrong_choice_zero()
    test_multi_empty()
    test_confidence_clear_decision()
    test_confidence_ambiguous_decision()
    test_detect_failure()
    print("=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
