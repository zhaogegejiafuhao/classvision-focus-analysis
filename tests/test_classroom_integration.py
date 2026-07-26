"""课堂 API 集成测试

使用 TestClient 走真实 HTTP 链路，验证：
- 课堂 CRUD 完整流程
- 权限矩阵（teacher/student/admin）
- 邀请码加入 / 公开课堂直接加入
- IDOR 防护（非创建者不能修改/删除）
"""
import pytest


# ══════════════════════════════════════════════════════════════
# 辅助函数
# ══════════════════════════════════════════════════════════════
def _create_classroom(client, name="测试课堂", teacher="张老师", **kwargs):
    """创建课堂并返回响应"""
    payload = {"name": name, "teacher": teacher, **kwargs}
    return client.post("/api/classrooms", json=payload)


# ══════════════════════════════════════════════════════════════
# 创建课堂
# ══════════════════════════════════════════════════════════════
class TestCreateClassroom:
    """POST /api/classrooms"""

    def test_teacher_create_success(self, teacher_client):
        """教师创建课堂成功"""
        resp = _create_classroom(teacher_client, name="高一数学")
        assert resp.status_code == 200
        data = resp.json()
        assert data["name"] == "高一数学"
        assert data["teacher"] == "张老师"
        assert data["teacher_person_id"] is not None

    def test_student_create_forbidden(self, student_client):
        """学生不能创建课堂 → 403"""
        resp = _create_classroom(student_client)
        assert resp.status_code == 403

    def test_admin_create_success(self, admin_client):
        """管理员可以创建课堂"""
        resp = _create_classroom(admin_client, name="管理员课堂")
        assert resp.status_code == 200

    def test_unauthenticated_create(self, client):
        """未登录不能创建 → 401"""
        resp = _create_classroom(client)
        assert resp.status_code == 401

    def test_create_exam_mode_classroom(self, teacher_client):
        """创建考试模式课堂"""
        resp = _create_classroom(teacher_client, name="期末考试", exam_mode=True)
        assert resp.status_code == 200
        assert resp.json()["exam_mode"] is True

    def test_create_private_classroom(self, teacher_client):
        """创建非公开课堂"""
        resp = _create_classroom(teacher_client, name="私有课堂", is_public=False)
        assert resp.status_code == 200
        assert resp.json()["is_public"] is False


# ══════════════════════════════════════════════════════════════
# 列表与详情
# ══════════════════════════════════════════════════════════════
class TestListClassrooms:
    """GET /api/classrooms"""

    def test_teacher_sees_only_own(self, teacher_client, admin_client):
        """教师只能看到自己创建的课堂"""
        # admin 创建一个课堂
        _create_classroom(admin_client, name="管理员课堂")
        # teacher 创建一个课堂
        _create_classroom(teacher_client, name="教师课堂")

        resp = teacher_client.get("/api/classrooms")
        assert resp.status_code == 200
        names = [c["name"] for c in resp.json()]
        assert "教师课堂" in names
        assert "管理员课堂" not in names

    def test_admin_sees_all(self, teacher_client, admin_client):
        """管理员能看到所有课堂"""
        _create_classroom(teacher_client, name="教师课堂")
        _create_classroom(admin_client, name="管理员课堂")

        resp = admin_client.get("/api/classrooms")
        assert resp.status_code == 200
        names = [c["name"] for c in resp.json()]
        assert "教师课堂" in names
        assert "管理员课堂" in names

    def test_student_sees_only_joined(self, student_client, teacher_client):
        """学生只能看到已加入的课堂"""
        # 教师创建课堂
        resp = _create_classroom(teacher_client, name="已加入课堂", is_public=True)
        classroom_id = resp.json()["id"]
        # 学生加入
        student_client.post(f"/api/classrooms/join/{classroom_id}")
        # 教师再创建一个学生未加入的课堂
        _create_classroom(teacher_client, name="未加入课堂", is_public=True)

        resp = student_client.get("/api/classrooms")
        assert resp.status_code == 200
        names = [c["name"] for c in resp.json()]
        assert "已加入课堂" in names
        assert "未加入课堂" not in names


class TestGetClassroomDetail:
    """GET /api/classrooms/{id}"""

    def test_owner_get_detail(self, teacher_client):
        """创建者可以查看详情"""
        cid = _create_classroom(teacher_client, name="详情测试").json()["id"]
        resp = teacher_client.get(f"/api/classrooms/{cid}")
        assert resp.status_code == 200
        assert resp.json()["name"] == "详情测试"

    def test_nonexistent_classroom(self, teacher_client):
        """不存在的课堂 → 404"""
        resp = teacher_client.get("/api/classrooms/99999")
        assert resp.status_code == 404

    def test_other_teacher_forbidden(self, teacher_client, admin_client):
        """非创建者教师不能查看 → 403"""
        cid = _create_classroom(admin_client, name="admin的课堂").json()["id"]
        resp = teacher_client.get(f"/api/classrooms/{cid}")
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# 更新与删除（IDOR 防护）
# ══════════════════════════════════════════════════════════════
class TestUpdateDeleteClassroom:
    """PUT/DELETE /api/classrooms/{id}"""

    def test_owner_update_success(self, teacher_client):
        """创建者可以修改"""
        cid = _create_classroom(teacher_client, name="原名").json()["id"]
        resp = teacher_client.put(f"/api/classrooms/{cid}", json={"name": "新名"})
        assert resp.status_code == 200
        assert resp.json()["name"] == "新名"

    def test_non_owner_update_forbidden(self, teacher_client, admin_client):
        """非创建者不能修改 → 403（IDOR 防护）"""
        cid = _create_classroom(admin_client, name="admin的课堂").json()["id"]
        resp = teacher_client.put(f"/api/classrooms/{cid}", json={"name": "篡改"})
        assert resp.status_code == 403

    def test_owner_delete_success(self, teacher_client):
        """创建者可以删除"""
        cid = _create_classroom(teacher_client, name="待删除").json()["id"]
        resp = teacher_client.delete(f"/api/classrooms/{cid}")
        assert resp.status_code == 200
        # 确认已删除
        resp = teacher_client.get(f"/api/classrooms/{cid}")
        assert resp.status_code == 404

    def test_non_owner_delete_forbidden(self, teacher_client, admin_client):
        """非创建者不能删除 → 403"""
        cid = _create_classroom(admin_client, name="admin的课堂").json()["id"]
        resp = teacher_client.delete(f"/api/classrooms/{cid}")
        assert resp.status_code == 403

    def test_admin_can_delete_any(self, teacher_client, admin_client):
        """管理员可以删除任何课堂"""
        cid = _create_classroom(teacher_client, name="教师的课堂").json()["id"]
        resp = admin_client.delete(f"/api/classrooms/{cid}")
        assert resp.status_code == 200


# ══════════════════════════════════════════════════════════════
# 邀请码加入
# ══════════════════════════════════════════════════════════════
class TestInviteCode:
    """POST /api/classrooms/{id}/generate-invite + /api/classrooms/join"""

    def test_generate_invite_code(self, teacher_client):
        """教师生成邀请码"""
        cid = _create_classroom(teacher_client, name="邀请码测试").json()["id"]
        resp = teacher_client.post(f"/api/classrooms/{cid}/generate-invite")
        assert resp.status_code == 200
        code = resp.json()["invite_code"]
        assert len(code) == 13

    def test_student_cannot_generate_invite(self, student_client, teacher_client):
        """学生不能生成邀请码 → 403"""
        cid = _create_classroom(teacher_client, name="学生测试").json()["id"]
        resp = student_client.post(f"/api/classrooms/{cid}/generate-invite")
        assert resp.status_code == 403

    def test_join_by_invite_code(self, teacher_client, student_client):
        """学生通过邀请码加入课堂"""
        cid = _create_classroom(teacher_client, name="邀请加入").json()["id"]
        code_resp = teacher_client.post(f"/api/classrooms/{cid}/generate-invite")
        code = code_resp.json()["invite_code"]

        resp = student_client.post("/api/classrooms/join", json={"invite_code": code})
        assert resp.status_code == 200
        assert resp.json()["classroom_id"] == cid

    def test_join_invalid_invite_code(self, student_client):
        """无效邀请码 → 404"""
        resp = student_client.post("/api/classrooms/join", json={"invite_code": "invalid12345"})
        assert resp.status_code == 404

    def test_join_twice_forbidden(self, teacher_client, student_client):
        """重复加入 → 400"""
        cid = _create_classroom(teacher_client, name="重复加入").json()["id"]
        code = teacher_client.post(f"/api/classrooms/{cid}/generate-invite").json()["invite_code"]

        student_client.post("/api/classrooms/join", json={"invite_code": code})
        resp = student_client.post("/api/classrooms/join", json={"invite_code": code})
        assert resp.status_code == 400


# ══════════════════════════════════════════════════════════════
# 公开课堂
# ══════════════════════════════════════════════════════════════
class TestPublicClassroom:
    """GET /api/classrooms/public + POST /api/classrooms/join/{id}"""

    def test_list_public_classrooms(self, teacher_client, client):
        """公开课堂列表不需要认证"""
        _create_classroom(teacher_client, name="公开课A", is_public=True)
        _create_classroom(teacher_client, name="私有课B", is_public=False)

        resp = client.get("/api/classrooms/public")
        assert resp.status_code == 200
        names = [c["name"] for c in resp.json()]
        assert "公开课A" in names
        assert "私有课B" not in names

    def test_join_public_directly(self, teacher_client, student_client):
        """学生直接加入公开课堂"""
        cid = _create_classroom(teacher_client, name="公开课", is_public=True).json()["id"]
        resp = student_client.post(f"/api/classrooms/join/{cid}")
        assert resp.status_code == 200

    def test_join_private_directly_forbidden(self, teacher_client, student_client):
        """不能直接加入非公开课堂 → 403"""
        cid = _create_classroom(teacher_client, name="私有课", is_public=False).json()["id"]
        resp = student_client.post(f"/api/classrooms/join/{cid}")
        assert resp.status_code == 403

    def test_search_public_classrooms(self, teacher_client, client):
        """搜索公开课堂"""
        _create_classroom(teacher_client, name="高等数学", is_public=True, course_code="MATH101")
        _create_classroom(teacher_client, name="大学英语", is_public=True, course_code="ENG101")

        # 按名称搜索
        resp = client.get("/api/classrooms/public?search=数学")
        assert resp.status_code == 200
        names = [c["name"] for c in resp.json()]
        assert "高等数学" in names
        assert "大学英语" not in names

        # 按课程代码搜索
        resp = client.get("/api/classrooms/public?search=ENG")
        assert resp.status_code == 200
        assert "大学英语" in [c["name"] for c in resp.json()]
