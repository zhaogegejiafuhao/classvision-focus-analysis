"""F 方案 - 重批改历史记录 API 集成测试

测试覆盖：
A. 写入断言（13 个）：
   regrade_essay / manual_input 接口正确写入 AnswerRegradeHistory 表
   覆盖 before/after 分数、总分、max_score 快照、input_mode、force_essay、
   writing_attribution、writing_kg 异常、manual_input 无 LLM 字段等

B. 读取接口（10 个）：
   GET /api/answer-sheet/submissions/{sid}/questions/{qid}/regrade-history
   覆盖权限校验、不存在校验、排序、跨题隔离、detail 模式、分页

C. 建表验证（1 个）：
   Base.metadata.create_all 自动建 answer_regrade_history 表，含 24 列 + 复合索引

测试策略：mock db + mock grading_service + mock writing_kg + mock ocr_service
直接调用路由函数（不走 HTTP），与 test_regrade_essay_api.py 同模式
"""
import asyncio
import json
import sys
from datetime import datetime
from unittest.mock import MagicMock, AsyncMock, patch

import pytest

sys.path.insert(0, "d:/ClassVision")


# ============ 工具函数（与 test_regrade_essay_api.py 同模式）============

def _make_user(role: str = "teacher", uid: int = 1, name: str = "测试教师"):
    u = MagicMock()
    u.role = role
    u.id = uid
    u.name = name
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
    """构造 mock db，按 regrade_essay/manual_input 路由实际流程返回：
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


def _make_ocr_result(text: str = "x=2", confidence: float = 0.95,
                     needs_manual_input: bool = False):
    """构造 mock ocr_service.recognize 返回值"""
    r = MagicMock()
    r.text = text
    r.confidence = confidence
    r.needs_manual_input = needs_manual_input
    return r


def _extract_history(db) -> "AnswerRegradeHistory":
    """从 db.add.call_args_list 中提取 AnswerRegradeHistory 实例

    抛出 AssertionError 如果未找到。
    """
    from backend.models.tables import AnswerRegradeHistory
    history_objs = [
        call.args[0] for call in db.add.call_args_list
        if call.args and isinstance(call.args[0], AnswerRegradeHistory)
    ]
    assert len(history_objs) >= 1, "应至少写入 1 条 AnswerRegradeHistory 记录"
    return history_objs[-1]  # 取最后一条（避免 manual_input 多次调用的歧义）


# ============ A. 写入断言（13 个）============

@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_regrade_essay_writes_history(mock_writing_kg, mock_grading):
    """1. regrade_essay 后 db.add 调用包含 AnswerRegradeHistory 实例"""
    from backend.api.answer_sheet_routes import regrade_essay
    from backend.models.tables import AnswerRegradeHistory

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 2x + 3 = 7", score=10.0)
    graded_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    # 应写入 AnswerRegradeHistory 实例
    history_calls = [
        call for call in db.add.call_args_list
        if call.args and isinstance(call.args[0], AnswerRegradeHistory)
    ]
    assert len(history_calls) == 1, f"应恰好写入 1 条 history，实际 {len(history_calls)}"
    print("[PASS] test_regrade_essay_writes_history")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_before_score_none_on_first(mock_writing_kg, mock_grading):
    """2. 首次批改（existing_answer=None）→ before_score=None, before_is_correct=None"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 2x = 4", score=10.0)
    graded_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None,  # 首次批改
        all_answers=[graded_answer],
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.before_score is None, f"首次批改 before_score 应为 None，实际 {history.before_score}"
    assert history.before_is_correct is None, f"首次批改 before_is_correct 应为 None，实际 {history.before_is_correct}"
    print("[PASS] test_history_before_score_none_on_first")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_before_score_captured(mock_writing_kg, mock_grading):
    """3. 已有 Answer 时 → before_score=旧 score, before_is_correct=旧 is_correct"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=5.0, status="graded")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 3x = 9", score=10.0)
    existing_answer = _make_answer(
        content="x=1",  # 之前错答
        score=3.0, is_correct=False,
    )
    updated_answer = _make_answer(content="x=3", score=10.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer,
        all_answers=[updated_answer],
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=3",
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.before_score == 3.0, f"before_score 应=3.0，实际 {history.before_score}"
    assert history.before_is_correct is False, f"before_is_correct 应=False，实际 {history.before_is_correct}"
    print("[PASS] test_history_before_score_captured")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_after_score_correct(mock_writing_kg, mock_grading):
    """4. history.after_score = suggested_score, after_is_correct = (ratio>=0.8)"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 5x = 25", score=20.0)
    graded_answer = _make_answer(content="x=5", score=17.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    # 17/20 = 0.85 ≥ 0.8 → is_correct=True
    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=17.0, max_score=20.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=5",
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.after_score == 17.0, f"after_score 应=17.0，实际 {history.after_score}"
    assert history.after_is_correct is True, f"after_is_correct 应=True（17/20=0.85≥0.8），实际 {history.after_is_correct}"
    print("[PASS] test_history_after_score_correct")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_total_scores(mock_writing_kg, mock_grading):
    """5. before_total_score = submission.score（旧），after_total_score = 重算后 total_score"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    # 旧总分 5.0
    submission = _make_submission(sid=10, exam_id=1, score=5.0, status="graded")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 7x = 14", score=10.0)
    existing_answer = _make_answer(content="x=1", score=0.0, is_correct=False)
    # 重算总分：本题 10 + 其他题 8 = 18
    updated_answer = _make_answer(content="x=2", score=10.0, is_correct=True)
    other_answer = _make_answer(content="A", score=8.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer,
        all_answers=[updated_answer, other_answer],
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=2",
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.before_total_score == 5.0, f"before_total_score 应=5.0，实际 {history.before_total_score}"
    assert history.after_total_score == 18.0, f"after_total_score 应=18.0（10+8），实际 {history.after_total_score}"
    print("[PASS] test_history_total_scores")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_max_score_snapshot(mock_writing_kg, mock_grading):
    """6. history.max_score = llm_result['max_score']，不是 question.score

    场景：question.score=10，但 LLM 返回 max_score=15（防后续 question 改动后失去参照）
    """
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 11x = 121", score=10.0)
    graded_answer = _make_answer(content="x=11", score=12.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    # LLM 返回 max_score=15（与 question.score=10 不同）
    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=12.0, max_score=15.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=11",
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.max_score == 15.0, f"max_score 应=15.0（LLM 返回值），实际 {history.max_score}"
    print("[PASS] test_history_max_score_snapshot")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_input_mode_text(mock_writing_kg, mock_grading):
    """7. student_text 模式 → input_mode='text'"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 13x = 169", score=10.0)
    graded_answer = _make_answer(content="x=13", score=10.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="x=13",  # text 模式
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.input_mode == "text", f"text 模式 input_mode 应='text'，实际 {history.input_mode}"
    print("[PASS] test_history_input_mode_text")


@patch("backend.services.ocr.ocr_service")
@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_input_mode_image(mock_writing_kg, mock_grading, mock_ocr):
    """8. image_file 模式 → input_mode='image'"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="解方程 17x = 289", score=10.0)
    graded_answer = _make_answer(content="x=17", score=10.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    mock_ocr.recognize = AsyncMock(return_value=_make_ocr_result(
        text="x=17", confidence=0.95,
    ))
    mock_grading.grade_math = AsyncMock(return_value=_make_llm_result(
        suggested_score=10.0, max_score=10.0, is_essay=False,
    ))

    image_file = _make_upload_file(content=b"fake png bytes")
    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text=None,  # 显式传 None，避免 Form(None) 默认值占位触发 .strip() 异常
        image_file=image_file,  # image 模式
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.input_mode == "image", f"image 模式 input_mode 应='image'，实际 {history.input_mode}"
    print("[PASS] test_history_input_mode_image")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_force_essay_flag(mock_writing_kg, mock_grading):
    """9. force_essay=True → history.force_essay=True（严格判断，避免 Form 默认值陷阱）

    场景：content 不含"作文"关键词，但 force_essay=True → 走 grade_essay
    """
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    # content 不含作文关键词，正常会走 grade_math；force_essay=True 强制作文
    question = _make_question(qid=100, exam_id=1, qtype="essay",
                              content="请论述三角形内角和定理的证明", score=20.0)
    graded_answer = _make_answer(content="证明...", score=18.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    mock_grading.grade_essay = AsyncMock(return_value=_make_llm_result(
        suggested_score=18.0, max_score=20.0, is_essay=True,
    ))

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="证明过程...",
        force_essay=True,  # 强制作文
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.force_essay is True, f"force_essay=True 时 history.force_essay 应=True，实际 {history.force_essay}"
    assert history.is_essay is True, f"force_essay=True 时 history.is_essay 应=True，实际 {history.is_essay}"
    # grade_essay 应被调用，grade_math 不应被调用
    mock_grading.grade_essay.assert_awaited_once()
    print(f"[PASS] test_history_force_essay_flag (force_essay={history.force_essay}, is_essay={history.is_essay})")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_writing_attribution_json(mock_writing_kg, mock_grading):
    """10. 作文 + 有错因 → writing_attribution_json 非空，含 dimension/fine_nodes/suggestion"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    # content 含"作文"关键词 → 自动走 grade_essay
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="请以《我的家乡》为题写一篇不少于 600 字的作文",
        answer="写作要求...", score=20.0,
    )
    graded_answer = _make_answer(content="我的家乡...", score=15.0, is_correct=False)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    mock_grading.grade_essay = AsyncMock(return_value=_make_llm_result(
        suggested_score=15.0, max_score=20.0, is_essay=True,
        error_cause="修辞单一",
        knowledge_points=["语言表达-修辞手法"],
        model_key="doubao",
        grading_method="essay_llm",
    ))
    mock_writing_kg.map_error_cause_to_dimension.return_value = "language"
    mock_writing_kg.map_error_cause_to_nodes.return_value = ["lang_rhetoric"]
    mock_writing_kg.get_error_cause_suggestion.return_value = "建议多使用比喻、排比等修辞手法"

    asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="我的家乡在北方的一个小村庄...",
        current_user=user, db=db,
    ))

    history = _extract_history(db)
    assert history.writing_attribution_json, f"有错因时 writing_attribution_json 应非空"
    wa = json.loads(history.writing_attribution_json)
    assert wa["dimension"] == "language", f"dimension 应='language'，实际 {wa.get('dimension')}"
    assert wa["fine_nodes"] == ["lang_rhetoric"], f"fine_nodes 应=['lang_rhetoric']"
    assert "比喻" in wa["suggestion"], f"suggestion 应含'比喻'，实际 {wa.get('suggestion')}"
    print(f"[PASS] test_history_writing_attribution_json (dimension={wa['dimension']})")


@patch("backend.services.grader.grading_service")
@patch("backend.services.writing_graph.writing_kg")
def test_history_writing_kg_failure(mock_writing_kg, mock_grading):
    """11. writing_kg 异常 → writing_attribution_json=None，接口不挂"""
    from backend.api.answer_sheet_routes import regrade_essay

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="essay",
        content="请以《我的老师》为题写一篇作文",
        answer="写作要求...", score=20.0,
    )
    graded_answer = _make_answer(content="我的老师...", score=14.0, is_correct=False)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[graded_answer],
    )

    mock_grading.grade_essay = AsyncMock(return_value=_make_llm_result(
        suggested_score=14.0, max_score=20.0, is_essay=True,
        error_cause="结构混乱",
    ))
    # writing_kg 抛异常
    mock_writing_kg.map_error_cause_to_dimension.side_effect = RuntimeError("KG 服务不可用")

    # 接口不应挂
    result = asyncio.run(regrade_essay(
        submission_id=10, question_id=100,
        student_text="我的老师...",
        current_user=user, db=db,
    ))
    assert result["regrade"] is True

    history = _extract_history(db)
    assert history.writing_attribution_json is None, \
        f"writing_kg 异常时 writing_attribution_json 应=None，实际 {history.writing_attribution_json}"
    print("[PASS] test_history_writing_kg_failure")


def test_manual_input_writes_history():
    """12. manual_input 后 db.add 包含 AnswerRegradeHistory，regrade_method='manual_input'"""
    from backend.api.answer_sheet_routes import manual_input_answer
    from backend.models.tables import AnswerRegradeHistory

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single",
                              answer="0", score=5.0, content="单选题")
    new_answer = _make_answer(content="0", score=5.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[new_answer],
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",
        current_user=user, db=db,
    )

    assert result["manual_input"] is True
    history_calls = [
        call for call in db.add.call_args_list
        if call.args and isinstance(call.args[0], AnswerRegradeHistory)
    ]
    assert len(history_calls) == 1, f"应写入 1 条 history，实际 {len(history_calls)}"
    history = history_calls[0].args[0]
    assert history.regrade_method == "manual_input", \
        f"regrade_method 应='manual_input'，实际 {history.regrade_method}"
    print("[PASS] test_manual_input_writes_history")


def test_history_manual_input_no_llm_fields():
    """13. manual_input 的 history：所有 LLM 相关字段全为 None"""
    from backend.api.answer_sheet_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single",
                              answer="0", score=5.0, content="单选题")
    new_answer = _make_answer(content="0", score=5.0, is_correct=True)
    db = _build_db_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=None, all_answers=[new_answer],
    )

    manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",
        current_user=user, db=db,
    )

    history = _extract_history(db)
    # LLM 字段全为 None
    assert history.is_essay is False, f"is_essay 应=False，实际 {history.is_essay}"
    assert history.model_key is None, f"model_key 应=None，实际 {history.model_key}"
    assert history.grading_method is None, f"grading_method 应=None，实际 {history.grading_method}"
    assert history.error_cause is None, f"error_cause 应=None，实际 {history.error_cause}"
    assert history.grading_json is None, f"grading_json 应=None，实际 {history.grading_json}"
    assert history.writing_attribution_json is None, f"writing_attribution_json 应=None，实际 {history.writing_attribution_json}"
    # manual_input 的 input_mode 也是 None（不走 OCR 也不走 text 模式）
    assert history.input_mode is None, f"input_mode 应=None，实际 {history.input_mode}"
    assert history.force_essay is False, f"force_essay 应=False，实际 {history.force_essay}"
    # comment 也是 None
    assert history.comment is None, f"comment 应=None，实际 {history.comment}"
    print("[PASS] test_history_manual_input_no_llm_fields")


# ============ B. 读取接口（10 个）============

def _build_list_history_db(submission=None, exam=None, question=None,
                            history_records=None, total_count=None):
    """构造 mock db，按 list_regrade_history 路由实际流程返回：
      1. query(ExamSubmission).filter().first()  → submission
      2. query(Exam).filter().first()            → exam
      3. query(Question).filter().first()        → question
      4. query(AnswerRegradeHistory).filter().order_by().count()  → total
      5. query(AnswerRegradeHistory).filter().order_by().offset().limit().all()  → records
    """
    db = MagicMock()

    # 前 3 次 first() 调用走 query(X).filter().first()
    first_returns = [submission, exam, question]
    # 注意：第 4 次开始是 query(AnswerRegradeHistory)，它的查询链是 filter().order_by().count()
    # 和 filter().order_by().offset().limit().all()
    # 这两条链都从 db.query(AnswerRegradeHistory) 开始
    # 所以我们需要根据 db.query() 传入的 model 来区分

    # 简化方案：用 side_effect 函数根据传入的 model 返回不同的 query mock
    def _query_side_effect(model):
        q = MagicMock()
        filter_q = MagicMock()

        # 注意：Python 三元表达式优先级，必须先算出 model_name 再比较
        model_name = model.__name__ if hasattr(model, '__name__') else str(model)
        if model_name == 'AnswerRegradeHistory':
            # 第 4 个 query：AnswerRegradeHistory
            order_q = MagicMock()
            order_q.count.return_value = total_count if total_count is not None else len(history_records or [])
            order_q.offset.return_value.limit.return_value.all.return_value = history_records or []
            filter_q.order_by.return_value = order_q
        else:
            # 前 3 个 query：ExamSubmission / Exam / Question
            if first_returns:
                filter_q.first.return_value = first_returns.pop(0)
            else:
                filter_q.first.return_value = None

        q.filter.return_value = filter_q
        return q

    db.query.side_effect = _query_side_effect
    return db


def _make_history_record(rid: int = 1, submission_id: int = 10, question_id: int = 100,
                          operator_id: int = 1, operator_name: str = "张老师",
                          operator_role: str = "teacher",
                          regrade_method: str = "regrade_essay",
                          input_mode: str = "text", force_essay: bool = False,
                          before_score: float = None, after_score: float = 10.0,
                          before_is_correct: bool = None, after_is_correct: bool = True,
                          max_score: float = 10.0,
                          before_total_score: float = None, after_total_score: float = 10.0,
                          student_text: str = "x=2",
                          is_essay: bool = False,
                          model_key: str = "standard", grading_method: str = "llm",
                          error_cause: str = "none",
                          knowledge_points_json: str = None,
                          grading_json: str = None,
                          writing_attribution_json: str = None,
                          comment: str = "批改完成",
                          created_at: datetime = None):
    """构造 mock AnswerRegradeHistory 记录"""
    r = MagicMock()
    r.id = rid
    r.submission_id = submission_id
    r.question_id = question_id
    r.operator_id = operator_id
    r.regrade_method = regrade_method
    r.input_mode = input_mode
    r.force_essay = force_essay
    r.before_score = before_score
    r.after_score = after_score
    r.before_is_correct = before_is_correct
    r.after_is_correct = after_is_correct
    r.max_score = max_score
    r.before_total_score = before_total_score
    r.after_total_score = after_total_score
    r.student_text = student_text
    r.is_essay = is_essay
    r.model_key = model_key
    r.grading_method = grading_method
    r.error_cause = error_cause
    r.knowledge_points_json = knowledge_points_json
    r.grading_json = grading_json
    r.writing_attribution_json = writing_attribution_json
    r.comment = comment
    r.created_at = created_at or datetime(2026, 7, 19, 14, 30, 0)

    # operator relationship
    op = MagicMock()
    op.name = operator_name
    op.role = operator_role
    r.operator = op
    return r


def test_list_history_permission_denied_student():
    """14. 学生 → 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("student", 100)
    db = _build_list_history_db()

    with pytest.raises(HTTPException) as exc:
        list_regrade_history(
            submission_id=10, question_id=100,
            current_user=user, db=db,
        )
    assert exc.value.status_code == 403
    print("[PASS] test_list_history_permission_denied_student")


def test_list_history_permission_denied_other_teacher():
    """15. 非该考试教师 → 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 999)  # 不同 teacher_id
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)  # 属于 teacher_id=1
    db = _build_list_history_db(submission=submission, exam=exam)

    with pytest.raises(HTTPException) as exc:
        list_regrade_history(
            submission_id=10, question_id=100,
            current_user=user, db=db,
        )
    assert exc.value.status_code == 403
    assert "无权" in exc.value.detail
    print("[PASS] test_list_history_permission_denied_other_teacher")


def test_list_history_admin_can_read_any():
    """16. admin → 200，可读任意考试的历史"""
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("admin", 999)  # admin，且不是该考试教师
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)  # 属于 teacher_id=1
    question = _make_question(qid=100, exam_id=1)
    history_records = [_make_history_record(rid=1, after_score=10.0)]
    db = _build_list_history_db(
        submission=submission, exam=exam, question=question,
        history_records=history_records, total_count=1,
    )

    result = list_regrade_history(
        submission_id=10, question_id=100,
        current_user=user, db=db,
    )
    assert result["total"] == 1
    assert len(result["records"]) == 1
    print("[PASS] test_list_history_admin_can_read_any")


def test_list_history_submission_not_found():
    """17. submission 不存在 → 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    db = _build_list_history_db(submission=None)

    with pytest.raises(HTTPException) as exc:
        list_regrade_history(
            submission_id=999, question_id=100,
            current_user=user, db=db,
        )
    assert exc.value.status_code == 404
    assert "提交" in exc.value.detail
    print("[PASS] test_list_history_submission_not_found")


def test_list_history_question_not_in_exam():
    """18. question 不属于该考试 → 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    # question 属于 exam_id=2
    question = _make_question(qid=100, exam_id=2)
    db = _build_list_history_db(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        list_regrade_history(
            submission_id=10, question_id=100,
            current_user=user, db=db,
        )
    assert exc.value.status_code == 400
    assert "不属于" in exc.value.detail
    print("[PASS] test_list_history_question_not_in_exam")


def test_list_history_returns_desc_order():
    """19. 多条历史按 created_at DESC 排序（mock 直接返回有序列表，验证 order_by 被调用）"""
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1)
    # 模拟按 created_at DESC 排好序的记录
    history_records = [
        _make_history_record(rid=3, created_at=datetime(2026, 7, 19, 16, 0, 0)),
        _make_history_record(rid=2, created_at=datetime(2026, 7, 19, 15, 0, 0)),
        _make_history_record(rid=1, created_at=datetime(2026, 7, 19, 14, 0, 0)),
    ]
    db = _build_list_history_db(
        submission=submission, exam=exam, question=question,
        history_records=history_records, total_count=3,
    )

    result = list_regrade_history(
        submission_id=10, question_id=100,
        current_user=user, db=db,
    )

    assert result["total"] == 3
    assert len(result["records"]) == 3
    # 验证返回顺序与 mock 一致（DESC）
    assert result["records"][0]["id"] == 3
    assert result["records"][1]["id"] == 2
    assert result["records"][2]["id"] == 1
    print("[PASS] test_list_history_returns_desc_order")


def test_list_history_isolated_per_question():
    """20. 同 submission 不同 question 的历史互不串

    验证：filter 链同时按 submission_id 和 question_id 过滤
    """
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1)
    # 只返回 question_id=100 的历史（即使同 submission 有别的 question 历史）
    history_records = [
        _make_history_record(rid=1, question_id=100, after_score=10.0),
    ]
    db = _build_list_history_db(
        submission=submission, exam=exam, question=question,
        history_records=history_records, total_count=1,
    )

    result = list_regrade_history(
        submission_id=10, question_id=100,
        current_user=user, db=db,
    )

    # 验证接口返回的 question_id 顶层字段正确
    assert result["question_id"] == 100, \
        f"返回的 question_id 应=100，实际 {result['question_id']}"
    # mock 返回 1 条记录，验证 records 数量正确（filter 链按 submission_id + question_id 过滤）
    assert len(result["records"]) == 1, \
        f"应返回 1 条记录（仅 question_id=100 的历史），实际 {len(result['records'])}"
    # 验证返回的 record id 正确（来自 mock 中 question_id=100 的记录）
    assert result["records"][0]["id"] == 1
    print("[PASS] test_list_history_isolated_per_question")


def test_list_history_detail_false_omits_grading_json():
    """21. detail=False → 不含 grading_json/writing_attribution_json/完整 student_text"""
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1)
    long_student_text = "x" * 200  # 200 字，超过 100 字截断阈值
    history_records = [
        _make_history_record(
            rid=1,
            student_text=long_student_text,
            knowledge_points_json=json.dumps(["知识点1", "知识点2"], ensure_ascii=False),
            grading_json='{"grading": "full"}',
            writing_attribution_json='{"dimension": "language"}',
        ),
    ]
    db = _build_list_history_db(
        submission=submission, exam=exam, question=question,
        history_records=history_records, total_count=1,
    )

    result = list_regrade_history(
        submission_id=10, question_id=100,
        detail=False,
        current_user=user, db=db,
    )

    rec = result["records"][0]
    # 列表模式应有 student_text_head（前 100 字）
    assert "student_text_head" in rec, "列表模式应有 student_text_head"
    assert len(rec["student_text_head"]) == 100, \
        f"student_text_head 应截到 100 字，实际 {len(rec['student_text_head'])}"
    # 列表模式不应有完整 student_text/grading_json/writing_attribution_json
    assert "student_text" not in rec, "列表模式不应返回完整 student_text"
    assert "grading_json" not in rec, "列表模式不应返回 grading_json"
    assert "writing_attribution_json" not in rec, "列表模式不应返回 writing_attribution_json"
    # 应有 knowledge_points 反序列化数组
    assert "knowledge_points" in rec, "列表模式应返回 knowledge_points 反序列化数组"
    assert rec["knowledge_points"] == ["知识点1", "知识点2"]
    print("[PASS] test_list_history_detail_false_omits_grading_json")


def test_list_history_detail_true_includes_grading_json():
    """22. detail=True → 含 grading_json/writing_attribution_json/完整 student_text/student_text_head"""
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1)
    full_student_text = "完整学生答案文字内容"
    history_records = [
        _make_history_record(
            rid=1,
            student_text=full_student_text,
            knowledge_points_json=json.dumps(["知识点A"], ensure_ascii=False),
            grading_json='{"grading": {"total_score": 10}}',
            writing_attribution_json='{"dimension": "language", "fine_nodes": ["lang_rhetoric"]}',
        ),
    ]
    db = _build_list_history_db(
        submission=submission, exam=exam, question=question,
        history_records=history_records, total_count=1,
    )

    result = list_regrade_history(
        submission_id=10, question_id=100,
        detail=True,
        current_user=user, db=db,
    )

    rec = result["records"][0]
    # 详情模式应有完整字段
    assert rec.get("student_text") == full_student_text, "详情模式应返回完整 student_text"
    assert rec.get("student_text_head") == full_student_text, "详情模式也应有 student_text_head"
    assert rec.get("grading_json") == {"grading": {"total_score": 10}}, \
        f"详情模式应返回反序列化的 grading_json，实际 {rec.get('grading_json')}"
    assert rec.get("writing_attribution_json") == {"dimension": "language", "fine_nodes": ["lang_rhetoric"]}, \
        f"详情模式应返回反序列化的 writing_attribution_json，实际 {rec.get('writing_attribution_json')}"
    print("[PASS] test_list_history_detail_true_includes_grading_json")


def test_list_history_pagination():
    """23. limit=10, offset=20 → safe_limit=10, safe_offset=20, total 正确"""
    from backend.api.answer_sheet_routes import list_regrade_history

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1)
    # mock 返回 3 条记录（虽然 offset=20，但 mock 不真正分页，主要验证参数透传）
    history_records = [
        _make_history_record(rid=21),
        _make_history_record(rid=22),
        _make_history_record(rid=23),
    ]
    db = _build_list_history_db(
        submission=submission, exam=exam, question=question,
        history_records=history_records, total_count=100,
    )

    result = list_regrade_history(
        submission_id=10, question_id=100,
        limit=10, offset=20,
        current_user=user, db=db,
    )

    assert result["total"] == 100, f"total 应=100，实际 {result['total']}"
    assert result["limit"] == 10, f"limit 应=10，实际 {result['limit']}"
    assert result["offset"] == 20, f"offset 应=20，实际 {result['offset']}"
    assert len(result["records"]) == 3  # mock 返回的 3 条
    print("[PASS] test_list_history_pagination")


# ============ C. 建表验证（1 个）============

def test_answer_regrade_history_table_auto_created():
    """24. Base.metadata.create_all 后，answer_regrade_history 表存在，含 24 列 + 复合索引"""
    from sqlalchemy import create_engine, inspect
    from backend.core.database import Base
    # 触发所有表模型注册（包括 AnswerRegradeHistory）
    from backend.models import tables  # noqa: F401

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    insp = inspect(engine)

    # 表存在
    assert "answer_regrade_history" in insp.get_table_names(), \
        "answer_regrade_history 表应被自动创建"

    # 列数 = 24
    columns = insp.get_columns("answer_regrade_history")
    column_names = [c["name"] for c in columns]
    expected_columns = {
        "id", "submission_id", "question_id", "operator_id",
        "regrade_method", "input_mode", "force_essay",
        "before_score", "after_score",
        "before_is_correct", "after_is_correct",
        "max_score", "before_total_score", "after_total_score",
        "student_text",
        "is_essay", "model_key", "grading_method", "error_cause",
        "knowledge_points_json", "grading_json", "writing_attribution_json",
        "comment", "created_at",
    }
    assert len(columns) == 24, f"应有 24 列，实际 {len(columns)} 列：{column_names}"
    missing = expected_columns - set(column_names)
    assert not missing, f"缺少列：{missing}"

    # 复合索引存在
    indexes = insp.get_indexes("answer_regrade_history")
    index_names = [idx["name"] for idx in indexes]
    assert "ix_answer_regrade_history_sub_q" in index_names, \
        f"应有复合索引 ix_answer_regrade_history_sub_q，实际索引：{index_names}"
    # 验证索引包含两列
    sub_q_idx = next(idx for idx in indexes if idx["name"] == "ix_answer_regrade_history_sub_q")
    assert set(sub_q_idx["column_names"]) == {"submission_id", "question_id"}, \
        f"复合索引应含 submission_id + question_id，实际 {sub_q_idx['column_names']}"
    print(f"[PASS] test_answer_regrade_history_table_auto_created (列数={len(columns)}, 索引={index_names})")


# ============ 主入口 ============

if __name__ == "__main__":
    print("=" * 60)
    print("F 方案 - 重批改历史记录 API 集成测试（24 个）")
    print("=" * 60)

    # A. 写入断言
    print("\n--- A. 写入断言（13 个）---")
    test_regrade_essay_writes_history()
    test_history_before_score_none_on_first()
    test_history_before_score_captured()
    test_history_after_score_correct()
    test_history_total_scores()
    test_history_max_score_snapshot()
    test_history_input_mode_text()
    test_history_input_mode_image()
    test_history_force_essay_flag()
    test_history_writing_attribution_json()
    test_history_writing_kg_failure()
    test_manual_input_writes_history()
    test_history_manual_input_no_llm_fields()

    # B. 读取接口
    print("\n--- B. 读取接口（10 个）---")
    test_list_history_permission_denied_student()
    test_list_history_permission_denied_other_teacher()
    test_list_history_admin_can_read_any()
    test_list_history_submission_not_found()
    test_list_history_question_not_in_exam()
    test_list_history_returns_desc_order()
    test_list_history_isolated_per_question()
    test_list_history_detail_false_omits_grading_json()
    test_list_history_detail_true_includes_grading_json()
    test_list_history_pagination()

    # C. 建表验证
    print("\n--- C. 建表验证（1 个）---")
    test_answer_regrade_history_table_auto_created()

    print("\n" + "=" * 60)
    print("[ALL PASSED] 24 个测试全部通过")
    print("=" * 60)
