"""请假 API 集成测试

核心测试点：
- 状态机（pending → approved/rejected）
- 审批副作用：approved 时自动创建/更新 Attendance 记录 + 发通知
- 权限矩阵（学生只能请自己的，教师只能审批自己课堂的）
"""
from datetime import datetime, timedelta
import pytest


# ══════════════════════════════════════════════════════════════
# 辅助 fixture
# ══════════════════════════════════════════════════════════════
@pytest.fixture()
def classroom_with_student(teacher_client, student_client):
    """创建公开课堂并让学生加入"""
    resp = teacher_client.post("/api/classrooms", json={
        "name": "请假测试课堂", "teacher": "张老师", "is_public": True,
    })
    cid = resp.json()["id"]
    student_client.post(f"/api/classrooms/join/{cid}")
    return cid


def _create_leave(client, classroom_id, days_range=7, reason="生病请假"):
    """提交请假申请，默认覆盖前后 7 天"""
    now = datetime.now()
    return client.post("/api/leaves", json={
        "classroom_id": classroom_id,
        "start_date": (now - timedelta(days=days_range)).isoformat(),
        "end_date": (now + timedelta(days=days_range)).isoformat(),
        "leave_type": "sick",
        "reason": reason,
    })


# ══════════════════════════════════════════════════════════════
# 创建请假
# ══════════════════════════════════════════════════════════════
class TestCreateLeave:
    """POST /api/leaves"""

    def test_student_create_success(self, student_client, classroom_with_student):
        """学生为自己课堂请假"""
        resp = _create_leave(student_client, classroom_with_student)
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "pending"
        assert data["reason"] == "生病请假"
        assert data["leave_type"] == "sick"
        assert data["student_name"] == "李同学"
        assert data["classroom_name"] == "请假测试课堂"

    def test_non_member_create_forbidden(self, student_client, teacher_client):
        """不为成员的课堂请假 → 403"""
        # teacher 创建课堂但不让学生加入
        resp = teacher_client.post("/api/classrooms", json={
            "name": "别人的课堂", "teacher": "张老师", "is_public": False,
        })
        cid = resp.json()["id"]
        resp = _create_leave(student_client, cid)
        assert resp.status_code == 403

    def test_teacher_create_forbidden(self, teacher_client, classroom_with_student):
        """教师不能请假（不是学生身份）→ 403"""
        resp = _create_leave(teacher_client, classroom_with_student)
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# 列表
# ══════════════════════════════════════════════════════════════
class TestListLeaves:
    """GET /api/leaves"""

    def test_student_sees_own_only(self, student_client, teacher_client, classroom_with_student):
        """学生只看到自己的请假"""
        _create_leave(student_client, classroom_with_student)
        resp = student_client.get("/api/leaves")
        assert resp.status_code == 200
        leaves = resp.json()
        assert len(leaves) == 1
        assert leaves[0]["student_name"] == "李同学"

    def test_teacher_sees_classroom_leaves(self, teacher_client, student_client, classroom_with_student):
        """教师看到自己课堂的请假"""
        _create_leave(student_client, classroom_with_student)
        resp = teacher_client.get("/api/leaves")
        assert resp.status_code == 200
        assert len(resp.json()) == 1

    def test_filter_by_status(self, student_client, teacher_client, classroom_with_student):
        """按状态过滤"""
        _create_leave(student_client, classroom_with_student)
        # pending 状态
        resp = student_client.get("/api/leaves?status=pending")
        assert len(resp.json()) == 1
        # approved 状态（还没审批）
        resp = student_client.get("/api/leaves?status=approved")
        assert len(resp.json()) == 0


# ══════════════════════════════════════════════════════════════
# 审批（核心：副作用）
# ══════════════════════════════════════════════════════════════
class TestReviewLeave:
    """POST /api/leaves/{id}/review"""

    def test_approve_success(self, teacher_client, student_client, classroom_with_student):
        """教师批准请假"""
        lid = _create_leave(student_client, classroom_with_student).json()["id"]
        resp = teacher_client.post(f"/api/leaves/{lid}/review", json={
            "status": "approved", "feedback": "注意休息",
        })
        assert resp.status_code == 200

        # 验证状态变更
        leaves = teacher_client.get("/api/leaves").json()
        leave = [l for l in leaves if l["id"] == lid][0]
        assert leave["status"] == "approved"
        assert leave["teacher_feedback"] == "注意休息"
        assert leave["reviewed_at"] is not None

    def test_reject_success(self, teacher_client, student_client, classroom_with_student):
        """教师拒绝请假"""
        lid = _create_leave(student_client, classroom_with_student).json()["id"]
        resp = teacher_client.post(f"/api/leaves/{lid}/review", json={
            "status": "rejected", "feedback": "理由不充分",
        })
        assert resp.status_code == 200

        leaves = teacher_client.get("/api/leaves").json()
        leave = [l for l in leaves if l["id"] == lid][0]
        assert leave["status"] == "rejected"

    def test_review_nonexistent(self, teacher_client):
        """审批不存在的请假 → 404"""
        resp = teacher_client.post("/api/leaves/99999/review", json={
            "status": "approved", "feedback": "",
        })
        assert resp.status_code == 404

    def test_student_cannot_review(self, student_client, classroom_with_student):
        """学生不能审批 → 403"""
        lid = _create_leave(student_client, classroom_with_student).json()["id"]
        resp = student_client.post(f"/api/leaves/{lid}/review", json={
            "status": "approved", "feedback": "",
        })
        assert resp.status_code == 403

    def test_approve_creates_notification(self, teacher_client, student_client, classroom_with_student):
        """审批后学生收到通知"""
        lid = _create_leave(student_client, classroom_with_student).json()["id"]
        teacher_client.post(f"/api/leaves/{lid}/review", json={
            "status": "approved", "feedback": "已批准",
        })
        # 学生应该收到通知
        resp = student_client.get("/api/notifications")
        titles = [n["title"] for n in resp.json()]
        assert any("已通过" in t for t in titles)

    def test_reject_creates_notification(self, teacher_client, student_client, classroom_with_student):
        """拒绝后学生收到通知"""
        lid = _create_leave(student_client, classroom_with_student).json()["id"]
        teacher_client.post(f"/api/leaves/{lid}/review", json={
            "status": "rejected", "feedback": "理由不足",
        })
        resp = student_client.get("/api/notifications")
        titles = [n["title"] for n in resp.json()]
        assert any("已拒绝" in t for t in titles)

    def test_approve_creates_leave_attendance(
        self, teacher_client, student_client, classroom_with_student
    ):
        """批准请假后，范围内的签到会话自动创建 leave 状态的考勤记录"""
        # 先创建一个签到会话（start_time = now，在请假范围内）
        session_resp = teacher_client.post("/api/checkin/sessions", json={
            "classroom_id": classroom_with_student, "type": "normal",
        })
        session_id = session_resp.json()["id"]

        # 学生请假（覆盖今天）
        lid = _create_leave(student_client, classroom_with_student).json()["id"]

        # 教师批准
        teacher_client.post(f"/api/leaves/{lid}/review", json={
            "status": "approved", "feedback": "同意",
        })

        # 查看签到记录，应该有 leave 状态的记录
        resp = teacher_client.get(f"/api/checkin/sessions/{session_id}/attendances")
        attendances = resp.json()
        assert len(attendances) == 1
        assert attendances[0]["status"] == "leave"
        assert "请假" in attendances[0]["note"]

    def test_approve_updates_absent_to_leave(
        self, teacher_client, student_client, classroom_with_student
    ):
        """批准请假后，已有的 absent 记录更新为 leave"""
        # 创建签到并关闭（学生未签到 → absent）
        session_resp = teacher_client.post("/api/checkin/sessions", json={
            "classroom_id": classroom_with_student, "type": "normal",
        })
        session_id = session_resp.json()["id"]
        teacher_client.post(f"/api/checkin/sessions/{session_id}/close")

        # 确认有 absent 记录
        resp = teacher_client.get(f"/api/checkin/sessions/{session_id}/attendances")
        assert resp.json()[0]["status"] == "absent"

        # 学生请假并批准
        lid = _create_leave(student_client, classroom_with_student).json()["id"]
        teacher_client.post(f"/api/leaves/{lid}/review", json={
            "status": "approved", "feedback": "同意",
        })

        # absent 应该变成 leave
        resp = teacher_client.get(f"/api/checkin/sessions/{session_id}/attendances")
        assert resp.json()[0]["status"] == "leave"
