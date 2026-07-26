"""Phase 3 大题/作文 LLM 批改 - 单元测试

测试覆盖：
1. _is_essay_question 作文题识别（关键词 + "以...为题" 模式）
2. _grade_essay_question 路由逻辑（mock OCR + grading_service，不调真实 LLM）
"""
import asyncio
import sys
from unittest.mock import AsyncMock, MagicMock, patch

# 把项目根目录加入 sys.path
def test_is_essay_question_keywords():
    """测试作文题关键词识别"""
    from backend.services.answer_sheet import _is_essay_question

    # 1. 直接含"作文"关键词
    assert _is_essay_question("请写一篇作文，题目自拟") is True, "作文关键词识别失败"
    assert _is_essay_question("命题作文：我的梦想") is True, "命题作文识别失败"
    assert _is_essay_question("材料作文：阅读以下材料...") is True, "材料作文识别失败"

    # 2. 含字数要求
    assert _is_essay_question("请写一段话描述你的家乡，不少于300字") is True, "字数要求识别失败"
    assert _is_essay_question("写一篇不少于800字的文章") is True, "不少于识别失败"

    # 3. 含文体/题材
    assert _is_essay_question("文体不限，诗歌除外") is True, "文体识别失败"
    assert _is_essay_question("题材自选") is True, "题材识别失败"

    # 4. "以...为题" 模式（含各种引号/书名号）
    assert _is_essay_question('以"我的父亲"为题写一篇文章') is True, "双引号模式失败"
    assert _is_essay_question("以'春天'为题写一篇文章") is True, "单引号模式失败"
    assert _is_essay_question("以《母亲》为题写一篇文章") is True, "书名号模式失败"

    print("[PASS] test_is_essay_question_keywords")


def test_is_essay_question_math():
    """测试数学/理科解答题识别（应返回 False）"""
    from backend.services.answer_sheet import _is_essay_question

    # 1. 数学计算题
    assert _is_essay_question("已知函数 f(x) = x^2 + 2x，求 f(3) 的值") is False, "函数题误判"
    assert _is_essay_question("解方程：2x + 5 = 13") is False, "方程题误判"
    assert _is_essay_question("计算：3/4 + 5/6") is False, "计算题误判"

    # 2. 几何证明题
    assert _is_essay_question("如图，在三角形ABC中，D是BC的中点，证明：AD ⊥ BC") is False, "几何证明误判"
    assert _is_essay_question("求证：三角形内角和为180度") is False, "求证题误判"

    # 3. 物理题
    assert _is_essay_question("一物体从高处自由落下，求落地时的速度") is False, "物理题误判"

    # 4. 边界场景
    assert _is_essay_question("") is False, "空字符串应返回False"
    assert _is_essay_question(None) is False, "None应返回False"
    assert _is_essay_question("简短的题目") is False, "无关键词短题应返回False"

    print("[PASS] test_is_essay_question_math")


def test_grade_essay_question_routing_math():
    """测试 _grade_essay_question 路由：数学题 → grade_math

    通过 mock OCR + grading_service.grade_math 验证路由正确
    """
    from backend.services.answer_sheet import AnswerSheetOrchestrator
    from backend.services.paper_template import QuestionRegionImage

    # Mock 题目（数学解答题）
    question = MagicMock()
    question.id = 1001
    question.type = "essay"
    question.content = "已知函数 f(x) = x^2 + 2x，求 f(3) 的值"
    question.answer = "f(3) = 9 + 6 = 15"
    question.score = 10.0

    # Mock region
    region = QuestionRegionImage(
        question_id=1001,
        region_type="essay",
        image_bytes=b"fake_image_bytes",
        bbox=(0, 0, 100, 100),
    )

    # Mock OCR 返回
    mock_ocr_result = MagicMock()
    mock_ocr_result.text = "f(3) = 3^2 + 2*3 = 9 + 6 = 15"
    mock_ocr_result.confidence = 0.92
    mock_ocr_result.needs_manual_input = False

    # Mock grading_service.grade_math 返回
    mock_grading_result = {
        "rubric": {"steps": []},
        "grading": {
            "steps": [{"step_id": "s1", "score": 5, "correct": True}],
            "total_score": 8,
            "max_score": 10,
            "error_type": "calculation_error",
            "error_cause": "计算粗心",
            "knowledge_points": ["函数求值"],
            "grading_method": "llm",
        },
        "comment": "解题思路正确，但最后一步计算错误",
        "suggested_score": 8,
        "max_score": 10,
        "confidence": 0.92,
        "flagged": False,
        "model_key": "standard",
    }

    orchestrator = AnswerSheetOrchestrator()

    with patch("backend.services.ocr.ocr_service.recognize", new=AsyncMock(return_value=mock_ocr_result)):
        with patch("backend.services.grader.grading_service.grade_math", new=AsyncMock(return_value=mock_grading_result)) as mock_grade_math:
            with patch("backend.services.grader.grading_service.grade_essay", new=AsyncMock(return_value={})) as mock_grade_essay:
                result = asyncio.run(orchestrator._grade_essay_question(question, region))

    # 验证：调用了 grade_math，没调用 grade_essay
    assert mock_grade_math.called, "数学题应调用 grade_math"
    assert not mock_grade_essay.called, "数学题不应调用 grade_essay"

    # 验证结果
    assert result.question_id == 1001
    assert result.region_type == "essay"
    assert result.score == 8, f"score 应为8，实际={result.score}"
    assert result.max_score == 10
    # 8/10=0.8 >= 0.8 → True
    assert result.is_correct is True, f"得分率0.8应判正确，实际={result.is_correct}"
    assert result.ocr_text == "f(3) = 3^2 + 2*3 = 9 + 6 = 15"
    assert result.confidence == 0.92
    assert result.grading_detail is not None
    assert result.grading_detail["is_essay"] is False
    assert result.grading_detail["model_key"] == "standard"
    # 数学题不应该有 writing_attribution
    assert "writing_attribution" not in result.grading_detail

    print("[PASS] test_grade_essay_question_routing_math")


def test_grade_essay_question_routing_essay():
    """测试 _grade_essay_question 路由：作文题 → grade_essay + writing_kg 归因"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator
    from backend.services.paper_template import QuestionRegionImage

    # Mock 题目（作文题）
    question = MagicMock()
    question.id = 2002
    question.type = "essay"
    question.content = "请以'我的父亲'为题写一篇作文，不少于600字"
    question.answer = "要求：真情实感，结构完整"
    question.score = 50.0

    # Mock region
    region = QuestionRegionImage(
        question_id=2002,
        region_type="essay",
        image_bytes=b"fake_image_bytes",
        bbox=(0, 0, 100, 100),
    )

    # Mock OCR 返回
    mock_ocr_result = MagicMock()
    mock_ocr_result.text = "我的父亲是一位普通的工人，他每天早出晚归..."  # 假设 ≥50 字
    mock_ocr_result.confidence = 0.88
    mock_ocr_result.needs_manual_input = False

    # Mock grading_service.grade_essay 返回（含"素材匮乏"错因）
    mock_grading_result = {
        "rubric": {"dimensions": []},
        "grading": {
            "dimensions": {"content": {"score": 18, "max_score": 20}},
            "steps": [{"step_id": "dim_content", "score": 18, "correct": False}],
            "total_score": 35,
            "max_score": 50,
            "primary_error_cause": "素材匮乏",
            "error_type": "theme_deviation",
            "error_cause": "素材匮乏",
            "knowledge_points": ["内容"],
            "grading_method": "essay_llm",
            "_model_key": "standard",
        },
        "comment": "主题明确但素材不够丰富",
        "suggested_score": 35,
        "max_score": 50,
        "confidence": 0.88,
        "flagged": False,
        "model_key": "standard",
    }

    orchestrator = AnswerSheetOrchestrator()

    with patch("backend.services.ocr.ocr_service.recognize", new=AsyncMock(return_value=mock_ocr_result)):
        with patch("backend.services.grader.grading_service.grade_math", new=AsyncMock(return_value={})) as mock_grade_math:
            with patch("backend.services.grader.grading_service.grade_essay", new=AsyncMock(return_value=mock_grading_result)) as mock_grade_essay:
                result = asyncio.run(orchestrator._grade_essay_question(question, region))

    # 验证：调用了 grade_essay，没调用 grade_math
    assert mock_grade_essay.called, "作文题应调用 grade_essay"
    assert not mock_grade_math.called, "作文题不应调用 grade_math"

    # 验证结果
    assert result.question_id == 2002
    assert result.score == 35, f"score 应为35，实际={result.score}"
    assert result.max_score == 50
    # 35/50 = 0.7 < 0.8 → False
    assert result.is_correct is False, f"得分率0.7应判错误，实际={result.is_correct}"
    assert result.grading_detail is not None
    assert result.grading_detail["is_essay"] is True

    # 验证写作归因
    assert "writing_attribution" in result.grading_detail, "作文场景应有 writing_attribution"
    wa = result.grading_detail["writing_attribution"]
    assert wa["error_cause"] == "素材匮乏"
    assert wa["dimension"] == "theme", f"素材匮乏 → theme，实际={wa['dimension']}"
    assert "topic_understanding" in wa["fine_nodes"], "素材匮乏应映射到 topic_understanding"
    assert "theme_depth" in wa["fine_nodes"], "素材匮乏应映射到 theme_depth"
    assert "素材积累" in wa["suggestion"], "建议中应包含素材积累"

    # 评语中应追加改进建议
    assert "【改进建议】" in result.comment, f"评语应含【改进建议】，实际={result.comment!r}"

    print("[PASS] test_grade_essay_question_routing_essay")


def test_grade_essay_question_ocr_failure():
    """测试 _grade_essay_question OCR 失败处理"""
    from backend.services.answer_sheet import AnswerSheetOrchestrator
    from backend.services.paper_template import QuestionRegionImage

    question = MagicMock()
    question.id = 3003
    question.type = "essay"
    question.content = "求证：三角形内角和为180度"
    question.answer = "证明：..."
    question.score = 10.0

    region = QuestionRegionImage(
        question_id=3003,
        region_type="essay",
        image_bytes=b"fake_image_bytes",
        bbox=(0, 0, 100, 100),
    )

    orchestrator = AnswerSheetOrchestrator()

    # 场景1：OCR 抛异常
    with patch("backend.services.ocr.ocr_service.recognize", new=AsyncMock(side_effect=Exception("网络错误"))):
        result = asyncio.run(orchestrator._grade_essay_question(question, region))

    assert result.error is not None
    assert "OCR 调用失败" in result.error
    assert result.score == 0
    assert result.is_correct is None
    print("  场景1 OCR 异常处理 ✓")

    # 场景2：OCR 返回空文本 + 低置信度
    mock_ocr_result = MagicMock()
    mock_ocr_result.text = ""
    mock_ocr_result.confidence = 0.2
    mock_ocr_result.needs_manual_input = False

    with patch("backend.services.ocr.ocr_service.recognize", new=AsyncMock(return_value=mock_ocr_result)):
        result = asyncio.run(orchestrator._grade_essay_question(question, region))

    assert result.error == "OCR 低置信度或失败"
    assert result.score == 0
    assert result.is_correct is None
    assert "需人工复核" in result.comment
    print("  场景2 OCR 低置信度处理 ✓")

    # 场景3：needs_manual_input = True
    mock_ocr_result.text = "一些文本"
    mock_ocr_result.confidence = 0.95
    mock_ocr_result.needs_manual_input = True

    with patch("backend.services.ocr.ocr_service.recognize", new=AsyncMock(return_value=mock_ocr_result)):
        result = asyncio.run(orchestrator._grade_essay_question(question, region))

    assert result.error == "OCR 双引擎均失败"
    assert result.is_correct is None
    print("  场景3 needs_manual_input 处理 ✓")

    print("[PASS] test_grade_essay_question_ocr_failure")


def main():
    print("=" * 60)
    print("Phase 3 大题/作文 LLM 批改 - 单元测试")
    print("=" * 60)
    test_is_essay_question_keywords()
    test_is_essay_question_math()
    test_grade_essay_question_routing_math()
    test_grade_essay_question_routing_essay()
    test_grade_essay_question_ocr_failure()
    print("=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
