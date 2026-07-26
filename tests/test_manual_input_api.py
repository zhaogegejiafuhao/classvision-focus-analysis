"""D 方案 - 教师人工补录学生答案 API 集成测试

测试 POST /api/answer-sheet/submissions/{sid}/questions/{qid}/manual-input

覆盖场景：
1. 权限校验（学生 403、非该考试教师 403）
2. 不存在校验（submission/question 404）
3. 业务校验（题目不属于考试 400、大题 400、空答案 400）
4. 正常场景：
   - 单选题精确匹配（对/错）
   - 填空题多空拆分 + 部分分（A 方案集成）
   - 填空题数值/单位容差（B 方案集成）
   - 已存在 Answer → 更新而非新建
   - 总分重算 + submission.status 更新为 graded

测试策略：mock db + mock current_user，直接调用路由函数（不走 HTTP）
"""
import sys
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, "d:/ClassVision")


# ============ 工具函数 ============

def _make_user(role: str = "teacher", uid: int = 1):
    """构造 mock current_user"""
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


def _make_question(qid: int = 100, exam_id: int = 1, qtype: str = "single",
                   answer: str = "0", score: float = 5.0, content: str = "题目"):
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


def _build_db_with_chain(submission=None, exam=None, question=None,
                         existing_answer=None, all_answers=None):
    """构造 mock db，支持多次连续 query().filter().first()/all() 调用

    调用顺序按 manual_input_answer 路由实际流程：
      1. query(ExamSubmission).filter().first()  → submission
      2. query(Exam).filter().first()            → exam
      3. query(Question).filter().first()        → question
      4. query(Answer).filter().first()          → existing_answer
      5. query(Answer).filter().all()            → all_answers（重算总分）

    用 side_effect 列表按顺序返回。
    """
    db = MagicMock()

    # 构造每次 query().filter().first() 的返回值序列
    first_returns = [submission, exam, question, existing_answer]
    # 构造 query().filter().all() 的返回值序列（只调一次：重算总分）
    all_returns = [all_answers or []]

    filter_q = MagicMock()
    filter_q.first.side_effect = first_returns
    filter_q.all.side_effect = all_returns

    query = MagicMock()
    query.filter.return_value = filter_q
    db.query.return_value = query

    return db


# ============ 1. 权限校验 ============

def test_manual_input_permission_denied_student():
    """学生角色应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("student", 100)
    db = _build_db_with_chain()

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=10, question_id=100,
            student_answer="0",
            current_user=user, db=db,
        )
    assert exc.value.status_code == 403
    assert "教师" in exc.value.detail
    print("[PASS] test_manual_input_permission_denied_student")


def test_manual_input_permission_denied_other_teacher():
    """非该考试教师应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 999)  # 不同 teacher_id
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)  # 考试属于 teacher_id=1
    db = _build_db_with_chain(submission=submission, exam=exam)

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=10, question_id=100,
            student_answer="0",
            current_user=user, db=db,
        )
    assert exc.value.status_code == 403
    assert "无权" in exc.value.detail
    print("[PASS] test_manual_input_permission_denied_other_teacher")


# ============ 2. 不存在校验 ============

def test_manual_input_submission_not_found():
    """submission 不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    db = _build_db_with_chain(submission=None)  # submission 不存在

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=999, question_id=100,
            student_answer="0",
            current_user=user, db=db,
        )
    assert exc.value.status_code == 404
    assert "提交" in exc.value.detail
    print("[PASS] test_manual_input_submission_not_found")


def test_manual_input_question_not_found():
    """question 不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    # 第 3 个 first() 返回 None → question 不存在
    db = _build_db_with_chain(submission=submission, exam=exam, question=None)

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=10, question_id=999,
            student_answer="0",
            current_user=user, db=db,
        )
    assert exc.value.status_code == 404
    assert "题目" in exc.value.detail
    print("[PASS] test_manual_input_question_not_found")


# ============ 3. 业务校验 ============

def test_manual_input_question_not_in_exam():
    """题目不属于该考试应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    # question 属于 exam_id=2，与 submission.exam_id=1 不符
    question = _make_question(qid=100, exam_id=2, qtype="single")
    db = _build_db_with_chain(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=10, question_id=100,
            student_answer="0",
            current_user=user, db=db,
        )
    assert exc.value.status_code == 400
    assert "不属于" in exc.value.detail
    print("[PASS] test_manual_input_question_not_in_exam")


def test_manual_input_essay_not_allowed():
    """大题不支持人工补录应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="essay")
    db = _build_db_with_chain(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=10, question_id=100,
            student_answer="essay answer",
            current_user=user, db=db,
        )
    assert exc.value.status_code == 400
    assert "大题" in exc.value.detail or "LLM" in exc.value.detail
    print("[PASS] test_manual_input_essay_not_allowed")


def test_manual_input_empty_answer():
    """学生答案为空应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single")
    db = _build_db_with_chain(submission=submission, exam=exam, question=question)

    with pytest.raises(HTTPException) as exc:
        manual_input_answer(
            submission_id=10, question_id=100,
            student_answer="   ",  # 全空白
            current_user=user, db=db,
        )
    assert exc.value.status_code == 400
    assert "空" in exc.value.detail
    print("[PASS] test_manual_input_empty_answer")


# ============ 4. 正常场景 ============

def test_manual_input_single_correct():
    """单选题正确答案 → 满分"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single", answer="0", score=5.0)
    existing_answer = None  # 不存在 Answer，应新建
    # 重算总分时返回的 answers 列表（包含本次新建的 answer，但 mock 里我们手动构造）
    # 注意：路由内会调 db.add(answer)，但 mock 的 add 不会真的把 answer 加进 all_answers
    # 所以 all_answers 我们直接构造好（模拟已 commit 后的状态）
    new_answer_mock = _make_answer(aid=1, submission_id=10, question_id=100,
                                    content="0", score=5.0, is_correct=True)
    all_answers = [new_answer_mock]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",  # 学生答 A（索引 0），标准答案也是 0
        current_user=user, db=db,
    )

    assert result["submission_id"] == 10
    assert result["question_id"] == 100
    assert result["student_answer"] == "0"
    assert result["score"] == 5.0
    assert result["max_score"] == 5.0
    assert result["is_correct"] is True
    assert result["total_score"] == 5.0  # 只有一题，满分
    assert result["manual_input"] is True
    # 应该调用 db.add（新建 Answer + 写入历史）
    assert db.add.called, "应调用 db.add 新建 Answer 和历史记录"
    # F 方案：验证 history 被写入
    assert any(
        call.args[0].__class__.__name__ == "AnswerRegradeHistory"
        for call in db.add.call_args_list
    ), "应写入 AnswerRegradeHistory 历史记录"
    assert db.commit.called, "应调用 db.commit"
    print("[PASS] test_manual_input_single_correct")


def test_manual_input_single_wrong():
    """单选题错误答案 → 0 分"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single", answer="0", score=5.0)
    existing_answer = None
    wrong_answer = _make_answer(content="1", score=0.0, is_correct=False)
    all_answers = [wrong_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="1",  # 学生答 B，标准答案 A
        current_user=user, db=db,
    )

    assert result["score"] == 0.0
    assert result["is_correct"] is False
    assert result["total_score"] == 0.0
    print("[PASS] test_manual_input_single_wrong")


def test_manual_input_fill_multi_blank_partial():
    """填空题多空拆分 → 部分分（A 方案集成）

    标准答案 "0;1;2"（3 空，每空 2 分），学生答 "0;1;5"（前两空对，第三空错）
    期望：score=4.0（2/3 * 6 ≈ 4.0），is_correct=False
    """
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="fill",
        answer="0;1;2", score=6.0,
    )
    existing_answer = None
    partial_answer = _make_answer(content="0;1;5", score=4.0, is_correct=False)
    all_answers = [partial_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0;1;5",
        current_user=user, db=db,
    )

    # 3 空，2 空对 → 6 * 2/3 = 4.0
    assert result["score"] == pytest.approx(4.0, abs=1e-6), \
        f"多空部分分应=4.0，实际={result['score']}"
    assert result["is_correct"] is False  # 没全对
    assert result["total_score"] == pytest.approx(4.0, abs=1e-6)
    print(f"[PASS] test_manual_input_fill_multi_blank_partial (score={result['score']})")


def test_manual_input_fill_unit_equivalence():
    """填空题单位等价容差 → 满分（B 方案集成）

    标准答案 "5kg"，学生答 "5千克" → 数值相同 + 单位等价 → 满分
    """
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="fill",
        answer="5kg", score=3.0,
    )
    existing_answer = None
    correct_answer = _make_answer(content="5千克", score=3.0, is_correct=True)
    all_answers = [correct_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="5千克",
        current_user=user, db=db,
    )

    assert result["score"] == pytest.approx(3.0, abs=1e-6), \
        f"单位等价应得满分 3.0，实际={result['score']}"
    assert result["is_correct"] is True
    print(f"[PASS] test_manual_input_fill_unit_equivalence (score={result['score']})")


def test_manual_input_numeric_tolerance():
    """填空题数值容差 → 满分（B 方案集成）

    标准答案 "3.14"，学生答 "3.140" → 数值等价 → 满分
    """
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="fill",
        answer="3.14", score=2.0,
    )
    existing_answer = None
    correct_answer = _make_answer(content="3.140", score=2.0, is_correct=True)
    all_answers = [correct_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="3.140",
        current_user=user, db=db,
    )

    assert result["score"] == pytest.approx(2.0, abs=1e-6), \
        f"数值容差应得满分 2.0，实际={result['score']}"
    assert result["is_correct"] is True
    print(f"[PASS] test_manual_input_numeric_tolerance (score={result['score']})")


def test_manual_input_update_existing_answer():
    """已存在 Answer → 应更新而非新建（不调用 db.add）"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single", answer="0", score=5.0)
    # 已存在 Answer（之前错答）
    existing_answer = _make_answer(
        aid=200, submission_id=10, question_id=100,
        content="1", score=0.0, is_correct=False,
    )
    # 重新批改后答案变正确
    updated_answer = _make_answer(
        aid=200, submission_id=10, question_id=100,
        content="0", score=5.0, is_correct=True,
    )
    all_answers = [updated_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",
        current_user=user, db=db,
    )

    assert result["score"] == 5.0
    assert result["is_correct"] is True
    # 关键：已存在 Answer 时不应再 db.add Answer，但仍会 db.add history（F 方案）
    # 即 db.add 应被调用恰好 1 次，且传入的是 AnswerRegradeHistory 而非 Answer
    assert db.add.call_count == 1, f"已存在 Answer 时应只 db.add history 1 次，实际 {db.add.call_count} 次"
    added_obj = db.add.call_args_list[0].args[0]
    assert added_obj.__class__.__name__ == "AnswerRegradeHistory", "应只 add 历史记录而非 Answer"
    assert db.commit.called, "应调用 db.commit"
    # 应直接修改 existing_answer 的字段
    assert existing_answer.content == "0"
    assert existing_answer.score == 5.0
    assert existing_answer.is_correct is True
    print("[PASS] test_manual_input_update_existing_answer")


def test_manual_input_total_score_recalc():
    """总分重算：多题场景下人工补录后总分 = 所有 answer 分数之和"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=7.0, status="graded")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single", answer="0", score=5.0)
    existing_answer = _make_answer(
        aid=200, submission_id=10, question_id=100,
        content="1", score=0.0, is_correct=False,  # 之前错答
    )
    # 模拟重算总分时的 answers 列表：本题从 0 改为 5，加上其他题已有 7 分
    other_answer_1 = _make_answer(content="0", score=3.0, is_correct=True)
    other_answer_2 = _make_answer(content="0", score=4.0, is_correct=True)
    updated_answer = _make_answer(content="0", score=5.0, is_correct=True)
    all_answers = [updated_answer, other_answer_1, other_answer_2]  # 5 + 3 + 4 = 12
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",
        current_user=user, db=db,
    )

    assert result["total_score"] == 12.0, \
        f"总分应=12.0（5+3+4），实际={result['total_score']}"
    # submission.score 应被更新为 12.0
    assert submission.score == 12.0
    print(f"[PASS] test_manual_input_total_score_recalc (total={result['total_score']})")


def test_manual_input_submission_status_to_graded():
    """submission.status 应更新为 'graded'（即使原来是 pending）"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(qid=100, exam_id=1, qtype="single", answer="0", score=5.0)
    existing_answer = None
    correct_answer = _make_answer(content="0", score=5.0, is_correct=True)
    all_answers = [correct_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",
        current_user=user, db=db,
    )

    assert submission.status == "graded", \
        f"submission.status 应更新为 'graded'，实际={submission.status}"
    assert submission.graded_at is not None, "submission.graded_at 应被设置"
    print("[PASS] test_manual_input_submission_status_to_graded")


def test_manual_input_judge_question():
    """判断题人工补录"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("teacher", 1)
    submission = _make_submission(sid=10, exam_id=1, score=0.0, status="pending")
    exam = _make_exam(exam_id=1, teacher_id=1)
    question = _make_question(
        qid=100, exam_id=1, qtype="judge",
        answer="true", score=2.0,
    )
    existing_answer = None
    correct_answer = _make_answer(content="true", score=2.0, is_correct=True)
    all_answers = [correct_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="true",
        current_user=user, db=db,
    )

    assert result["score"] == 2.0
    assert result["is_correct"] is True
    print("[PASS] test_manual_input_judge_question")


def test_manual_input_admin_can_operate_any_exam():
    """admin 角色可以操作任意考试（即使不是该考试的教师）"""
    from backend.api.answer_sheet_grading_routes import manual_input_answer

    user = _make_user("admin", 999)  # admin，且不是该考试教师
    submission = _make_submission(sid=10, exam_id=1)
    exam = _make_exam(exam_id=1, teacher_id=1)  # 考试属于 teacher_id=1
    question = _make_question(qid=100, exam_id=1, qtype="single", answer="0", score=5.0)
    existing_answer = None
    correct_answer = _make_answer(content="0", score=5.0, is_correct=True)
    all_answers = [correct_answer]
    db = _build_db_with_chain(
        submission=submission, exam=exam, question=question,
        existing_answer=existing_answer, all_answers=all_answers,
    )

    result = manual_input_answer(
        submission_id=10, question_id=100,
        student_answer="0",
        current_user=user, db=db,
    )

    # admin 应能成功
    assert result["score"] == 5.0
    assert result["is_correct"] is True
    print("[PASS] test_manual_input_admin_can_operate_any_exam")


# ============ 入口 ============

if __name__ == "__main__":
    test_manual_input_permission_denied_student()
    test_manual_input_permission_denied_other_teacher()
    test_manual_input_submission_not_found()
    test_manual_input_question_not_found()
    test_manual_input_question_not_in_exam()
    test_manual_input_essay_not_allowed()
    test_manual_input_empty_answer()
    test_manual_input_single_correct()
    test_manual_input_single_wrong()
    test_manual_input_fill_multi_blank_partial()
    test_manual_input_fill_unit_equivalence()
    test_manual_input_numeric_tolerance()
    test_manual_input_update_existing_answer()
    test_manual_input_total_score_recalc()
    test_manual_input_submission_status_to_graded()
    test_manual_input_judge_question()
    test_manual_input_admin_can_operate_any_exam()
    print("\n🎉 全部 17 个 D 方案集成测试通过！")
