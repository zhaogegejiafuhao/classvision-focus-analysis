"""考勤签到 API 集成测试

核心测试点：
- 状态机（active → closed）
- 副作用：创建签到时批量发通知，关闭签到时批量标记缺勤
- 加密签到验证码机制
- 权限矩阵（教师/学生/管理员）
- 学生视角下 code 字段隐藏
"""
import pytest


# ══════════════════════════════════════════════════════════════
# 辅助：创建带学生的课堂
# ══════════════════════════════════════════════════════════════
@pytest.fixture()
def classroom_with_student(teacher_client, student_client):
    """创建一个公开课堂并让学生加入，返回 (classroom_id, session 创建辅助函数)"""
    # 教师创建公开课堂
    resp = teacher_client.post("/api/classrooms", json={
        "name": "签到测试课堂", "teacher": "张老师", "is_public": True,
    })
    classroom_id = resp.json()["id"]
    # 学生加入课堂
    student_client.post(f"/api/classrooms/join/{classroom_id}")
    return classroom_id


def _create_session(client, classroom_id, session_type="normal"):
    """创建签到会话"""
    return client.post("/api/checkin/sessions", json={
        "classroom_id": classroom_id, "type": session_type,
    })


# ══════════════════════════════════════════════════════════════
# 创建签到会话
# ══════════════════════════════════════════════════════════════
class TestCreateSession:
    """POST /api/checkin/sessions"""

    def test_teacher_create_normal(self, teacher_client, classroom_with_student):
        """教师创建普通签到"""
        resp = _create_session(teacher_client, classroom_with_student)
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "active"
        assert data["type"] == "normal"
        assert data["code"] is None  # 普通签到无验证码
        assert data["total_count"] == 1  # 1 个学生
        assert data["checked_count"] == 0

    def test_teacher_create_encrypted(self, teacher_client, classroom_with_student):
        """教师创建加密签到，自动生成 6 位验证码"""
        resp = _create_session(teacher_client, classroom_with_student, "encrypted")
        assert resp.status_code == 200
        data = resp.json()
        assert data["type"] == "encrypted"
        assert data["code"] is not None
        assert len(data["code"]) == 6

    def test_student_create_forbidden(self, student_client, classroom_with_student):
        """学生不能创建签到 → 403"""
        resp = _create_session(student_client, classroom_with_student)
        assert resp.status_code == 403

    def test_duplicate_active_session(self, teacher_client, classroom_with_student):
        """同一课堂已有进行中的签到时不能重复创建 → 400"""
        _create_session(teacher_client, classroom_with_student)
        resp = _create_session(teacher_client, classroom_with_student)
        assert resp.status_code == 400
        assert "进行中" in resp.json()["detail"]

    def test_nonexistent_classroom(self, teacher_client):
        """不存在的课堂 → 404"""
        resp = _create_session(teacher_client, 99999)
        assert resp.status_code == 404

    def test_create_sends_notification(self, teacher_client, student_client, classroom_with_student):
        """创建签到时给学生发通知"""
        _create_session(teacher_client, classroom_with_student)
        # 学生应该收到通知
        resp = student_client.get("/api/notifications")
        assert resp.status_code == 200
        titles = [n["title"] for n in resp.json()]
        assert any("签到提醒" in t for t in titles)


# ══════════════════════════════════════════════════════════════
# 列表与详情
# ══════════════════════════════════════════════════════════════
class TestListSessions:
    """GET /api/checkin/sessions"""

    def test_teacher_sees_own(self, teacher_client, classroom_with_student):
        """教师只看到自己创建的签到"""
        _create_session(teacher_client, classroom_with_student)
        resp = teacher_client.get("/api/checkin/sessions")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    def test_student_code_hidden(self, teacher_client, student_client, classroom_with_student):
        """学生视角下 code 字段被隐藏"""
        _create_session(teacher_client, classroom_with_student, "encrypted")
        resp = student_client.get("/api/checkin/sessions")
        sessions = resp.json()
        assert len(sessions) > 0
        for s in sessions:
            assert s["code"] is None  # 学生看不到验证码

    def test_teacher_can_see_code(self, teacher_client, classroom_with_student):
        """教师能看到验证码"""
        _create_session(teacher_client, classroom_with_student, "encrypted")
        resp = teacher_client.get("/api/checkin/sessions")
        sessions = resp.json()
        assert any(s["code"] is not None for s in sessions)

    def test_filter_by_classroom(self, teacher_client, classroom_with_student):
        """按课堂过滤"""
        _create_session(teacher_client, classroom_with_student)
        resp = teacher_client.get(f"/api/checkin/sessions?classroom_id={classroom_with_student}")
        assert resp.status_code == 200
        for s in resp.json():
            assert s["classroom_id"] == classroom_with_student


class TestGetSession:
    """GET /api/checkin/sessions/{id}"""

    def test_owner_get_detail(self, teacher_client, classroom_with_student):
        """创建者查看详情"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        resp = teacher_client.get(f"/api/checkin/sessions/{sid}")
        assert resp.status_code == 200
        assert resp.json()["id"] == sid

    def test_nonexistent_session(self, teacher_client):
        """不存在的签到 → 404"""
        resp = teacher_client.get("/api/checkin/sessions/99999")
        assert resp.status_code == 404


# ══════════════════════════════════════════════════════════════
# 学生签到
# ══════════════════════════════════════════════════════════════
class TestSubmitCheckin:
    """POST /api/checkin/submit"""

    def test_normal_checkin_success(self, teacher_client, student_client, classroom_with_student):
        """普通签到成功"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        resp = student_client.post("/api/checkin/submit", json={"session_id": sid})
        assert resp.status_code == 200
        assert "成功" in resp.json()["message"]

    def test_encrypted_wrong_code(self, teacher_client, student_client, classroom_with_student):
        """加密签到验证码错误 → 400"""
        sid = _create_session(teacher_client, classroom_with_student, "encrypted").json()["id"]
        resp = student_client.post("/api/checkin/submit", json={
            "session_id": sid, "code": "000000",
        })
        assert resp.status_code == 400
        assert "验证码错误" in resp.json()["detail"]

    def test_encrypted_correct_code(self, teacher_client, student_client, classroom_with_student):
        """加密签到验证码正确 → 成功"""
        session_resp = _create_session(teacher_client, classroom_with_student, "encrypted")
        sid = session_resp.json()["id"]
        code = session_resp.json()["code"]
        resp = student_client.post("/api/checkin/submit", json={
            "session_id": sid, "code": code,
        })
        assert resp.status_code == 200

    def test_duplicate_checkin(self, teacher_client, student_client, classroom_with_student):
        """重复签到 → 400"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        student_client.post("/api/checkin/submit", json={"session_id": sid})
        resp = student_client.post("/api/checkin/submit", json={"session_id": sid})
        assert resp.status_code == 400
        assert "已签到" in resp.json()["detail"]

    def test_checkin_closed_session(self, teacher_client, student_client, classroom_with_student):
        """签到已结束时提交 → 400"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        teacher_client.post(f"/api/checkin/sessions/{sid}/close")
        resp = student_client.post("/api/checkin/submit", json={"session_id": sid})
        assert resp.status_code == 400
        assert "已结束" in resp.json()["detail"]


# ══════════════════════════════════════════════════════════════
# 关闭签到（副作用：标记缺勤）
# ══════════════════════════════════════════════════════════════
class TestCloseSession:
    """POST /api/checkin/sessions/{id}/close"""

    def test_close_success(self, teacher_client, classroom_with_student):
        """关闭签到成功"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        resp = teacher_client.post(f"/api/checkin/sessions/{sid}/close")
        assert resp.status_code == 200

        # 验证状态已变更
        detail = teacher_client.get(f"/api/checkin/sessions/{sid}").json()
        assert detail["status"] == "closed"

    def test_close_marks_absent(self, teacher_client, student_client, classroom_with_student):
        """关闭签到时未签到的学生被标记为缺勤"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        # 不让学生签到，直接关闭
        teacher_client.post(f"/api/checkin/sessions/{sid}/close")

        # 查看签到记录
        resp = teacher_client.get(f"/api/checkin/sessions/{sid}/attendances")
        attendances = resp.json()
        assert len(attendances) == 1  # 1 个学生
        assert attendances[0]["status"] == "absent"
        assert attendances[0]["note"] == "未签到"

    def test_close_after_partial_checkin(self, teacher_client, student_client, classroom_with_student):
        """部分签到后关闭，已签到学生保持 present"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        # 学生先签到
        student_client.post("/api/checkin/submit", json={"session_id": sid})
        # 关闭签到
        teacher_client.post(f"/api/checkin/sessions/{sid}/close")

        resp = teacher_client.get(f"/api/checkin/sessions/{sid}/attendances")
        attendances = resp.json()
        assert len(attendances) == 1
        assert attendances[0]["status"] == "present"

    def test_nonexistent_close(self, teacher_client):
        """关闭不存在的签到 → 404"""
        resp = teacher_client.post("/api/checkin/sessions/99999/close")
        assert resp.status_code == 404


# ══════════════════════════════════════════════════════════════
# 获取签到记录
# ══════════════════════════════════════════════════════════════
class TestGetAttendances:
    """GET /api/checkin/sessions/{id}/attendances"""

    def test_teacher_get_attendances(self, teacher_client, student_client, classroom_with_student):
        """教师查看签到记录"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        student_client.post("/api/checkin/submit", json={"session_id": sid})
        resp = teacher_client.get(f"/api/checkin/sessions/{sid}/attendances")
        assert resp.status_code == 200
        assert len(resp.json()) == 1
        assert resp.json()[0]["status"] == "present"

    def test_nonexistent_session(self, teacher_client):
        """不存在的签到 → 404"""
        resp = teacher_client.get("/api/checkin/sessions/99999/attendances")
        assert resp.status_code == 404


# ══════════════════════════════════════════════════════════════
# 活跃签到查询
# ══════════════════════════════════════════════════════════════
class TestActiveCheckin:
    """GET /api/checkin/active"""

    def test_no_active_session(self, student_client, classroom_with_student):
        """无进行中的签到"""
        resp = student_client.get(f"/api/checkin/active?classroom_id={classroom_with_student}")
        assert resp.status_code == 200
        assert resp.json()["active"] is False

    def test_has_active_session(self, teacher_client, student_client, classroom_with_student):
        """有进行中的签到"""
        _create_session(teacher_client, classroom_with_student)
        resp = student_client.get(f"/api/checkin/active?classroom_id={classroom_with_student}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["active"] is True
        assert "session_id" in data
        assert data["checked"] is False  # 学生还没签到

    def test_active_after_checkin(self, teacher_client, student_client, classroom_with_student):
        """学生已签到后 checked=True"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        student_client.post("/api/checkin/submit", json={"session_id": sid})
        resp = student_client.get(f"/api/checkin/active?classroom_id={classroom_with_student}")
        assert resp.json()["checked"] is True


# ══════════════════════════════════════════════════════════════
# CSV 导出
# ══════════════════════════════════════════════════════════════
class TestExportAttendance:
    """GET /api/checkin/sessions/{id}/export"""

    def test_export_csv(self, teacher_client, student_client, classroom_with_student):
        """导出 CSV"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        student_client.post("/api/checkin/submit", json={"session_id": sid})

        resp = teacher_client.get(f"/api/checkin/sessions/{sid}/export")
        assert resp.status_code == 200
        assert "text/csv" in resp.headers.get("content-type", "")
        assert "attachment" in resp.headers.get("content-disposition", "")
        # CSV 内容应包含 BOM 头
        content = resp.content
        assert content.startswith(b'\xef\xbb\xbf')

    def test_student_export_forbidden(self, teacher_client, student_client, classroom_with_student):
        """学生不能导出 → 403"""
        sid = _create_session(teacher_client, classroom_with_student).json()["id"]
        resp = student_client.get(f"/api/checkin/sessions/{sid}/export")
        assert resp.status_code == 403
