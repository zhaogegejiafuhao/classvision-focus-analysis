"""E 方案 - 大题/作文 LLM 重批改 API 集成测试

测试 POST /api/answer-sheet/submissions/{sid}/questions/{qid}/regrade-essay

覆盖场景：
1. 权限校验（学生 403、非该考试教师 403、admin 任意操作）
2. 参数校验（student_text/image_file 都没传 400、student_text 空 400、image_file 空 400）
3. 不存在校验（submission/question/exam 404）
4. 业务校验（题目不属于考试 400、非大题 400）
5. 正常场景（mock LLM）：
   - 数学题 student_text 模式（grade_math）
   - 作文题 student_text 模式（grade_essay，含"作文"关键词触发自动路由）
   - force_essay=True 强制按作文批改（content 不含关键词）
   - 已存在 Answer → 更新；不存在 Answer → 新建
   - 总分重算 + submission.status='graded'
   - 返回完整字段（regrade/is_essay/model_key/grading/error_cause/...）
   - 作文 + 有错因 → 触发 writing_kg 归因
6. image_file 模式：OCR 失败 → 400 提示改用 student_text

测试策略：mock db + mock grading_service + mock writing_kg + mock UploadFile
"""
import asyncio
import sys
from unittest.mock import MagicMock, AsyncMock, patch

import pytest

sys.path.insert(0, "d:/ClassVision")


# ============ 工具函数 ============

def _make_user(role: str = "teacher", uid: int = 1):
    u = MagicMock()
    u.role = role
    u.id = uid
    return u


def _make_exam(exam_id: int = 1, teacher_id: int = 1):
    e = MagicMock()
    e.id = exam_id
    e.teacher_id = teacher_id
    e.title = "测试考试"
    return e


def _make_question(qid: int = 100, exam_id: int = 1, qtype: str = "essay",
                   answer: str = "标准答案", score: float = 10.0,
                   content: str = "解方程 x + 1 = 2"):
    q = MagicMock()
    q.id = qid
    q.exam_id = exam_id
    q.type = qtype
    q.answer = answer
    q.score = score
    q.content = content
    q.order = 1
    return q


def _make_submission(sid: int = 10, exam_id: int = 1, student_id: int = 99,
                     score: float = 0.0, status: str = "pending"):
    s = MagicMock()
    s.id = sid
    s.exam_id = exam_id
    s.student_id = student_id
    s.score = score
    s.status = status
    s.graded_at = None
    return s


def _make_answer(aid: int = 200, submission_id: int = 10, question_id: int = 100,
                 content: str = "", score: float = 0.0, is_correct: bool = False):
    a = MagicMock()
    a.id = aid
    a.submission_id = submission_id
    a.question_id = question_id
    a.content = content
    a.score = score
    a.is_correct = is_correct
    return a


def _build_db_chain(submission=None, exam=None, question=None,
                    existing_answer=None, all_answers=None):
    """构造 mock db，按 regrade_essay 路由实际流程返回：
      1. query(ExamSubmission).filter().first()  → submission
      2. query(Exam).filter().first()            → exam
      3. query(Question).filter().first()        → question
      4. query(Answer).filter().first()          → existing_answer
      5. query(Answer).filter().all()            → all_answers（重算总分）
    """
    db = MagicMock()
    first_returns = [submission, exam, question, existing_answer]
    all_returns = [all_answers or []]

    filter_q = MagicMock()
    filter_q.first.side_effect = first_returns
    filter_q.all.side_effect = all_returns

    query = MagicMock()
    query.filter.return_value = filter_q
    db.query.return_value = query
    return db


def _make_llm_result(suggested_score: float, max_score: float,
                     is_essay: bool, error_cause: str = "none",
                     knowledge_points: list = None,
                     model_key: str = "standard",
                     grading_method: str = "llm",
                     comment: str = "批改完成") -> dict:
    """构造 mock LLM 返回值（与 grading_service.grade_essay/grade_math 返回结构一致）"""
    return {
        "suggested_score": suggested_score,
        "max_score": max_score,
        "comment": comment,
        "model_key": model_key,
        "grading": {
            "total_score": suggested_score,
            "max_score": max_score,
            "error_type": "none" if error_cause == "none" else "concept_error",
            "error_cause": error_cause,
            "knowledge_points": knowledge_points or [],
            "grading_method": grading_method,
            "steps": [],
            "dimensions": {} if is_essay else None,
        },
        "confidence": 0.9,
        "flagged": False,
    }


def _make_upload_file(content: bytes = b"fake image bytes",
                      filename: str = "answer.png"):
    """构造 mock UploadFile"""
    f = MagicMock()
    f.filename = filename
    f.read = AsyncMock(return_value=content)
    return f


# ============ 1. 权限校验 ============

def test_regrade_permission_denied_student():
    """学生角色应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("student", 100)
    db = _build_db_chain()

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text="x=1",
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 403
    print("[PASS] test_regrade_permission_denied_student")


def test_regrade_permission_denied_other_teacher():
    """非该考试教师应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 999)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    db = _build_db_chain(submission=submission, exam=exam)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text="x=1",
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 403
    assert "无权" in exc.value.detail
    print("[PASS] test_regrade_permission_denied_other_teacher")


# ============ 2. 参数校验 ============

def test_regrade_no_text_no_image():
    """student_text 和 image_file 都没传应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    db = _build_db_chain()

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text=None, image_file=None,
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 400
    assert "student_text" in exc.value.detail and "image_file" in exc.value.detail
    print("[PASS] test_regrade_no_text_no_image")


def test_regrade_empty_text():
    """student_text 为空白应返回 400（视为未提供）"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay")
    db = _build_db_chain(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text="   ",  # 全空白
            image_file=None,  # 显式传 None，避免 FastAPI File(None) 默认值占位
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 400
    # 空白 student_text 视为未提供，应返回"必须提供"
    assert "student_text" in exc.value.detail or "image_file" in exc.value.detail
    print("[PASS] test_regrade_empty_text")


# ============ 3. 不存在校验 ============

def test_regrade_submission_not_found():
    """submission 不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    db = _build_db_chain(submission=None)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=999, question_id=100,
            student_text="x=1",
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 404
    assert "提交" in exc.value.detail
    print("[PASS] test_regrade_submission_not_found")


def test_regrade_question_not_found():
    """question 不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    db = _build_db_chain(submission=submission, exam=exam, question=None)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=999,
            student_text="x=1",
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 404
    assert "题目" in exc.value.detail
    print("[PASS] test_regrade_question_not_found")


# ============ 4. 业务校验 ============

def test_regrade_question_not_in_exam():
    """题目不属于该考试应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=2, qtype="essay")  # 属于另一考试
    db = _build_db_chain(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text="x=1",
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 400
    assert "不属于" in exc.value.detail
    print("[PASS] test_regrade_question_not_in_exam")


def test_regrade_non_essay_question():
    """非大题（如单选题）应返回 400，提示用 manual-input"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single")  # 单选题
    db = _build_db_chain(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text="A",
            current_user=user, db=db,
        ))
    assert exc.value.status_code == 400
    assert "大题" in exc.value.detail or "manual-input" in exc.value.detail
    print("[PASS] test_regrade_non_essay_question")


# ============ 5. 正常场景 ============

@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_math_success(mock_writing_kg, mock_grading):
    """数学大题 student_text 模式 → grade_math → 满分场景"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    # content 不含作文关键词 → 走 grade_math
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    # mock grade_math 返回满分
    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
        model_key="standard", comment="解答完整正确",
    ))
    mock_grading.grade_essay = AsyncMock()  # 不应被调用

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    assert result["regrade"] is True
    assert result["is_essay"] is False  # 走数学路由
    assert result["score"] == 10.0
    assert result["is_correct"] is True  # 10/10 >= 0.8
    assert result["model_key"] == "standard"
    assert result["total_score"] == 10.0
    assert result["student_answer"] == "x=2"
    # grade_math 应被调用，grade_essay 不应被调用
    mock_grading.grade_math.assert_awaited_once()
    mock_grading.grade_essay.assert_not_awaited()
    # 数学题不触发写作归因
    mock_writing_kg.map_error_cause_to_dimension.assert_not_called()
    # 应新建 Answer + 写入历史（db.add 被调用 2 次：Answer + AnswerRegradeHistory）
    assert db.add.called
    # F 方案：验证 history 被写入
    assert any(
        call.args[0].__class__.__name__ == "AnswerRegradeHistory"
        for call in db.add.call_args_list
    ), "应写入 AnswerRegradeHistory 历史记录"
    assert db.commit.called
    print(f"[PASS] test_regrade_math_success (score={result['score']}, is_essay={result['is_essay']})")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_essay_auto_route_by_keyword(mock_writing_kg, mock_grading):
    """作文题 student_text 模式 → content 含"作文"关键词 → 自动路由 grade_essay"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    # content 含"作文"关键词 → 走 grade_essay
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="请以《我的家乡》为题写一篇不少于 600 字的作文",
        answer="写作要求：1. 立意明确...", score=20.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="我的家乡在...", score=16.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    # mock grade_essay 返回 16/20，带错因
    mock_grading.grade_essay = AsyncMock(return_value=_make_llm_result(
        suggested_score=16.0, max_score=20.0, is_essay=True,
        error_cause="修辞单一",
        knowledge_points=["语言表达-修辞手法"],
        model_key="doubao",
        grading_method="essay_llm",
        comment="内容充实但语言平淡",
    ))
    mock_grading.grade_math = AsyncMock()  # 不应被调用

    # mock writing_kg 归因
    mock_writing_kg.map_error_cause_to_dimension.return_value = "language"
    mock_writing_kg.map_error_cause_to_nodes.return_value = ["lang_rhetoric"]
    mock_writing_kg.get_error_cause_suggestion.return_value = "建议多使用比喻、排比等修辞手法"

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="我的家乡在北方的一个小村庄...",
        current_user=user, db=db,
    ))

    assert result["is_essay"] is True  # 走作文路由
    assert result["score"] == 16.0
    assert result["is_correct"] is True  # 16/20 = 0.8 >= 0.8
    assert result["model_key"] == "doubao"
    assert result["error_cause"] == "修辞单一"
    assert result["knowledge_points"] == ["语言表达-修辞手法"]
    # 应触发写作归因
    mock_writing_kg.map_error_cause_to_dimension.assert_called_once_with("修辞单一")
    mock_writing_kg.map_error_cause_to_nodes.assert_called_once_with("修辞单一")
    mock_writing_kg.get_error_cause_suggestion.assert_called_once_with("修辞单一")
    # writing_attribution 应有值
    assert result["writing_attribution"] is not None
    assert result["writing_attribution"]["dimension"] == "language"
    assert result["writing_attribution"]["suggestion"] == "建议多使用比喻、排比等修辞手法"
    # comment 应被追加改进建议
    assert "【改进建议】" in result["comment"]
    # grade_essay 被调用，grade_math 不被调用
    mock_grading.grade_essay.assert_awaited_once()
    mock_grading.grade_math.assert_not_awaited()
    print(f"[PASS] test_regrade_essay_auto_route_by_keyword (is_essay={result['is_essay']}, score={result['score']})")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_force_essay_overrides_route(mock_writing_kg, mock_grading):
    """force_essay=True 时即使 content 不含作文关键词也走 grade_essay"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    # content 是数学题，但 force_essay=True 会强制走 grade_essay
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="证明三角形内角和为 180 度",
        answer="证明过程...", score=10.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="证明...", score=8.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    mock_grading.grade_essay = AsyncMock(return_value=_make_llm_result(
        suggested_score=8.0, max_score=10.0, is_essay=True,
        model_key="doubao",
    ))
    mock_grading.grade_math = AsyncMock()  # 不应被调用

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="证明...",
        force_essay=True,  # 强制作文路由
        current_user=user, db=db,
    ))

    assert result["is_essay"] is True  # force_essay 生效
    mock_grading.grade_essay.assert_awaited_once()
    mock_grading.grade_math.assert_not_awaited()
    print(f"[PASS] test_regrade_force_essay_overrides_route (is_essay={result['is_essay']})")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_update_existing_answer(mock_writing_kg, mock_grading):
    """已存在 Answer → 应更新而非新建（不调用 db.add）"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=5.0, status="graded")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    existing_answer = _make_answer(
        aid=200, submission_id=10, question_id=100,
        content="x=1",  # 之前错答
        score=0.0, is_correct=False,
    )
    # 重新批改后总分变为 10
    updated_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    all_answers = [updated_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    assert result["score"] == 10.0
    assert result["is_correct"] is True
    # 已存在 Answer 时不应再 db.add Answer，但仍会 db.add history（F 方案）
    # 即 db.add 应被调用恰好 1 次，且传入的是 AnswerRegradeHistory 而非 Answer
    assert db.add.call_count == 1, f"已存在 Answer 时应只 db.add history 1 次，实际 {db.add.call_count} 次"
    added_obj = db.add.call_args_list[0].args[0]
    assert added_obj.__class__.__name__ == "AnswerRegradeHistory", "应只 add 历史记录而非 Answer"
    assert db.commit.called
    # 应直接修改 existing_answer 的字段
    assert existing_answer.content == "x=2"
    assert existing_answer.score == 10.0
    assert existing_answer.is_correct is True
    print("[PASS] test_regrade_update_existing_answer")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_total_score_recalc(mock_writing_kg, mock_grading):
    """总分重算：多题场景下重批改后总分 = 所有 answer 分数之和"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=5.0, status="graded")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    existing_answer = _make_answer(
        content="x=1", score=0.0, is_correct=False,
    )
    # 5 道题：本题 10 分（重批改后），其他 4 题 8+6+5+2=21 分 → 总分 31
    updated_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    other_answers = [
        _make_answer(content="A", score=8.0, is_correct=True),
        _make_answer(content="B", score=6.0, is_correct=True),
        _make_answer(content="C", score=5.0, is_correct=True),
        _make_answer(content="D", score=2.0, is_correct=False),
    ]
    all_answers = [updated_answer] + other_answers
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    expected_total = 10 + 8 + 6 + 5 + 2  # = 31
    assert result["total_score"] == expected_total, \
        f"总分应={expected_total}，实际={result['total_score']}"
    assert submission.score == expected_total
    print(f"[PASS] test_regrade_total_score_recalc (total={result['total_score']})")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_submission_status_to_graded(mock_writing_kg, mock_grading):
    """submission.status 应更新为 'graded'"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="x=2", score=8.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=8.0, max_score=10.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    assert submission.status == "graded"
    assert submission.graded_at is not None
    print("[PASS] test_regrade_submission_status_to_graded")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_admin_can_operate_any_exam(mock_writing_kg, mock_grading):
    """admin 角色可以操作任意考试"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("admin", 999)  # admin，且不是该考试教师
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)  # 考试属于 teacher_id=1
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    # admin 应能成功
    assert result["score"] == 10.0
    assert result["is_correct"] is True
    print("[PASS] test_regrade_admin_can_operate_any_exam")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_return_complete_fields(mock_writing_kg, mock_grading):
    """返回值应包含所有承诺字段"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="请以《我的老师》为题写一篇作文",
        answer="写作要求...", score=20.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="...", score=14.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    mock_grading.grade_essay = AsyncMock(return_value=_make_llm_result(
        suggested_score=14.0, max_score=20.0, is_essay=True,
        error_cause="逻辑断层",
        knowledge_points=["结构组织-段落衔接"],
        model_key="doubao",
        grading_method="essay_llm",
        comment="结构需要加强",
    ))
    mock_writing_kg.map_error_cause_to_dimension.return_value = "structure"
    mock_writing_kg.map_error_cause_to_nodes.return_value = ["struct_transition"]
    mock_writing_kg.get_error_cause_suggestion.return_value = "建议加强段落间过渡"

    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="我的老师...",
        current_user=user, db=db,
    ))

    # 检查所有承诺返回的字段
    expected_keys = {
        "submission_id", "question_id", "student_answer", "standard_answer",
        "score", "max_score", "is_correct", "total_score", "regrade",
        "is_essay", "model_key", "grading_method", "comment", "grading",
        "error_cause", "knowledge_points", "writing_attribution", "graded_at",
    }
    missing = expected_keys - set(result.keys())
    assert not missing, f"返回值缺少字段: {missing}"
    # 关键值校验
    assert result["regrade"] is True
    assert result["is_essay"] is True
    assert result["model_key"] == "doubao"
    assert result["grading_method"] == "essay_llm"
    assert result["error_cause"] == "逻辑断层"
    assert result["knowledge_points"] == ["结构组织-段落衔接"]
    assert result["writing_attribution"]["dimension"] == "structure"
    print(f"[PASS] test_regrade_return_complete_fields (keys={len(result)})")


# ============ 6. image_file 模式 ============

@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_image_mode_ocr_failed(mock_writing_kg, mock_grading):
    """image_file 模式：OCR 失败（needs_manual_input=True）应返回 400 提示用 student_text"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import regrade_essay

    # 显式设置 AsyncMock，避免 MagicMock 不能 await 或缺少 assert_not_awaited
    mock_grading.grade_math = AsyncMock()
    mock_grading.grade_essay = AsyncMock()

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    db = _build_db_chain(submission=submission, exam=exam, question=question)

    # mock OCR 返回 needs_manual_input=True
    ocr_result = MagicMock()
    ocr_result.text = ""
    ocr_result.confidence = 0.2
    ocr_result.needs_manual_input = True

    with patch("backend.services.ocr.ocr_service.recognize",
               new=AsyncMock(return_value=ocr_result)):
        with pytest.raises(HTTPException) as exc:
            asyncio.run(regrade_essay(
                submission_id=10, question_id=100,
                student_text=None,
                image_file=_make_upload_file(b"fake image"),
                current_user=user, db=db,
            ))

    assert exc.value.status_code == 400
    assert "student_text" in exc.value.detail
    # LLM 不应被调用
    mock_grading.grade_math.assert_not_awaited()
    mock_grading.grade_essay.assert_not_awaited()
    print("[PASS] test_regrade_image_mode_ocr_failed")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_image_mode_success(mock_writing_kg, mock_grading):
    """image_file 模式：OCR 成功 → 走 LLM"""
    from backend.api.answer_sheet_grading_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="解方程 2x + 3 = 7", answer="x=2", score=10.0,
    )
    existing_answer = None
    graded_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    all_answers = [graded_answer]
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    # mock OCR 返回成功
    ocr_result = MagicMock()
    ocr_result.text = "x=2"
    ocr_result.confidence = 0.95
    ocr_result.needs_manual_input = False

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    with patch("backend.services.ocr.ocr_service.recognize",
               new=AsyncMock(return_value=ocr_result)):
        result = asyncio.run(regrade_essay(
            submission_id=10, question_id=100,
            student_text=None,
            image_file=_make_upload_file(b"fake image bytes"),
            current_user=user, db=db,
        ))

    assert result["score"] == 10.0
    assert result["is_correct"] is True
    assert result["student_answer"] == "x=2"  # 来自 OCR
    mock_grading.grade_math.assert_awaited_once()
    print(f"[PASS] test_regrade_image_mode_success (score={result['score']})")


# ============ 入口 ============

if __name__ == "__main__":
    test_regrade_permission_denied_student()
    test_regrade_permission_denied_other_teacher()
    test_regrade_no_text_no_image()
    test_regrade_empty_text()
    test_regrade_submission_not_found()
    test_regrade_question_not_found()
    test_regrade_question_not_in_exam()
    test_regrade_non_essay_question()
    test_regrade_math_success()
    test_regrade_essay_auto_route_by_keyword()
    test_regrade_force_essay_overrides_route()
    test_regrade_update_existing_answer()
    test_regrade_total_score_recalc()
    test_regrade_submission_status_to_graded()
    test_regrade_admin_can_operate_any_exam()
    test_regrade_return_complete_fields()
    test_regrade_image_mode_ocr_failed()
    test_regrade_image_mode_success()
    print("\n🎉 全部 18 个 E 方案集成测试通过！")
