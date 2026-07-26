"""错题本 API - 单元测试

测试覆盖：
1. GET /api/correction/list - 错题列表（角色权限、知识点过滤、分页）
2. GET /api/correction/{grading_id} - 错题详情（权限校验、数据聚合）
3. _parse_kp_list 辅助函数
"""
import json
from unittest.mock import MagicMock, patch

# ============ 辅助函数 ============

def _make_mock_user(role: str = "teacher", uid: int = 1):
    u = MagicMock()
    u.role = role
    u.id = uid
    return u


def _make_mock_grading(grading_id=1, submission_id=10, score=6, max_score=10,
                       error_type="计算粗心", error_cause="符号漏写",
                       knowledge_points=None, created_at="2026-07-19T10:00:00"):
    g = MagicMock()
    g.id = grading_id
    g.submission_id = submission_id
    g.score = score
    g.max_score = max_score
    g.error_type = error_type
    g.error_cause = error_cause
    g.knowledge_points = json.dumps(knowledge_points or ["一元二次方程"])
    g.rubric_json = None
    g.grading_json = None
    g.comment = "解题过程有误"
    g.created_at = created_at
    return g


def _make_mock_submission(submission_id=10, student_id=1, homework_id=5, content="学生答案"):
    s = MagicMock()
    s.id = submission_id
    s.student_id = student_id
    s.homework_id = homework_id
    s.content = content
    return s


def _make_mock_homework(homework_id=5, title="周练卷第3题", description="标准答案内容"):
    h = MagicMock()
    h.id = homework_id
    h.title = title
    h.description = description
    return h


# ============ _parse_kp_list 测试 ============

def test_parse_kp_list_normal():
    from backend.api.correction_routes import _parse_kp_list
    assert _parse_kp_list('["一元二次方程", "因式分解"]') == ["一元二次方程", "因式分解"]


def test_parse_kp_list_empty():
    from backend.api.correction_routes import _parse_kp_list
    assert _parse_kp_list(None) == []
    assert _parse_kp_list("") == []


def test_parse_kp_list_string():
    from backend.api.correction_routes import _parse_kp_list
    assert _parse_kp_list('"单一知识点"') == ["单一知识点"]


def test_parse_kp_list_invalid_json():
    from backend.api.correction_routes import _parse_kp_list
    assert _parse_kp_list("not json") == []


# ============ GET /list 测试 ============

@patch("backend.api.correction_routes.get_current_user")
@patch("backend.api.correction_routes.get_db")
def test_list_mistakes_student_sees_own(db_mock, auth_mock):
    """学生角色：只能看自己的错题，忽略传入的 student_id"""
    from backend.api.correction_routes import list_mistakes

    student = _make_mock_user(role="student", uid=42)
    auth_mock.return_value = student

    # mock db chain
    mock_query = MagicMock()
    mock_join = MagicMock()
    mock_outerjoin = MagicMock()
    mock_filter = MagicMock()
    mock_filter.count.return_value = 1
    mock_filter.order_by.return_value = mock_filter
    mock_filter.offset.return_value = mock_filter
    mock_filter.limit.return_value = mock_filter

    grading = _make_mock_grading()
    submission = _make_mock_submission(student_id=42)
    homework = _make_mock_homework()
    mock_filter.all.return_value = [(grading, submission, homework)]

    # 链式调用
    mock_query.join.return_value = mock_join
    mock_join.outerjoin.return_value = mock_outerjoin
    mock_outerjoin.filter.return_value = mock_filter

    db = MagicMock()
    db.query.return_value = mock_query
    db_mock.return_value = iter([db])

    result = list_mistakes(student_id=99, db=db, current_user=student)
    assert result["total"] == 1
    assert result["items"][0]["grading_id"] == 1


@patch("backend.api.correction_routes.get_current_user")
@patch("backend.api.correction_routes.get_db")
def test_list_mistakes_empty(db_mock, auth_mock):
    """没有错题时返回空列表"""
    from backend.api.correction_routes import list_mistakes

    teacher = _make_mock_user(role="teacher", uid=1)
    auth_mock.return_value = teacher

    mock_query = MagicMock()
    mock_join = MagicMock()
    mock_outerjoin = MagicMock()
    mock_filter = MagicMock()
    mock_filter.count.return_value = 0
    mock_filter.order_by.return_value = mock_filter
    mock_filter.offset.return_value = mock_filter
    mock_filter.limit.return_value = mock_filter
    mock_filter.all.return_value = []

    mock_query.join.return_value = mock_join
    mock_join.outerjoin.return_value = mock_outerjoin
    mock_outerjoin.filter.return_value = mock_filter

    db = MagicMock()
    db.query.return_value = mock_query
    db_mock.return_value = iter([db])

    result = list_mistakes(db=db, current_user=teacher)
    assert result["total"] == 0
    assert result["items"] == []


# ============ GET /{grading_id} 测试 ============

@patch("backend.api.correction_routes.get_current_user")
@patch("backend.api.correction_routes.get_db")
def test_get_mistake_detail_success(db_mock, auth_mock):
    """正常获取错题详情"""
    from backend.api.correction_routes import get_mistake_detail
    from backend.models.tables import CorrectionRecord

    teacher = _make_mock_user(role="teacher", uid=1)
    auth_mock.return_value = teacher

    grading = _make_mock_grading(grading_id=18, score=6, max_score=10,
                                  error_type="计算粗心", error_cause="符号漏写")
    submission = _make_mock_submission(submission_id=207, student_id=1, homework_id=5)
    homework = _make_mock_homework(homework_id=5, title="周练卷第3题", description="标准答案内容")
    homework.teacher_id = 1  # 匹配 teacher.uid，通过 IDOR 权限检查

    # CorrectionRecord
    cr = MagicMock()
    cr.id = 5
    cr.correction_score = 9
    cr.original_score = 6
    cr.improved = True
    cr.created_at = "2026-07-19T12:00:00"

    db = MagicMock()
    # 第一次 query: GradingResult
    q1 = MagicMock()
    q1.filter.return_value.first.return_value = grading
    # 第二次 query: HomeworkSubmission
    q2 = MagicMock()
    q2.filter.return_value.first.return_value = submission
    # 第三次 query: Homework（IDOR 权限检查）
    q3 = MagicMock()
    q3.filter.return_value.first.return_value = homework
    # 第四次 query: Homework（响应数据，复用 q3）
    # 第五次 query: CorrectionRecord
    q4 = MagicMock()
    q4.filter.return_value.order_by.return_value.all.return_value = [cr]

    db.query.side_effect = [q1, q2, q3, q3, q4]
    db_mock.return_value = iter([db])

    result = get_mistake_detail(grading_id=18, db=db, current_user=teacher)
    assert result["grading_id"] == 18
    assert result["score"] == 6
    assert result["max_score"] == 10
    assert result["error_type"] == "计算粗心"
    assert result["homework_title"] == "周练卷第3题"
    assert len(result["correction_records"]) == 1
    assert result["correction_records"][0]["correction_id"] == 5
    assert result["correction_records"][0]["improved"] is True


@patch("backend.api.correction_routes.get_current_user")
@patch("backend.api.correction_routes.get_db")
def test_get_mistake_detail_not_found(db_mock, auth_mock):
    """批改记录不存在返回 404"""
    from backend.api.correction_routes import get_mistake_detail
    from fastapi import HTTPException

    teacher = _make_mock_user(role="teacher", uid=1)
    auth_mock.return_value = teacher

    db = MagicMock()
    q = MagicMock()
    q.filter.return_value.first.return_value = None
    db.query.return_value = q
    db_mock.return_value = iter([db])

    try:
        get_mistake_detail(grading_id=999, db=db, current_user=teacher)
        assert False, "Should have raised HTTPException"
    except HTTPException as e:
        assert e.status_code == 404


@patch("backend.api.correction_routes.get_current_user")
@patch("backend.api.correction_routes.get_db")
def test_get_mistake_detail_student_forbidden(db_mock, auth_mock):
    """学生不能看别人的错题"""
    from backend.api.correction_routes import get_mistake_detail
    from fastapi import HTTPException

    student = _make_mock_user(role="student", uid=42)
    auth_mock.return_value = student

    grading = _make_mock_grading(grading_id=18)
    submission = _make_mock_submission(submission_id=207, student_id=99)  # 不是自己的

    db = MagicMock()
    q1 = MagicMock()
    q1.filter.return_value.first.return_value = grading
    q2 = MagicMock()
    q2.filter.return_value.first.return_value = submission
    db.query.side_effect = [q1, q2]
    db_mock.return_value = iter([db])

    try:
        get_mistake_detail(grading_id=18, db=db, current_user=student)
        assert False, "Should have raised HTTPException"
    except HTTPException as e:
        assert e.status_code == 403
