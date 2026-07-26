"""认证 API 集成测试

使用 TestClient 走真实 HTTP 链路，验证：
- 登录/注册/获取用户/改密码 的完整流程
- 错误处理（错误密码、重复用户名、短密码、非法角色）
- 限流保护
- JWT 认证机制
"""
import pytest
from backend.core.security import create_access_token, verify_password
from backend.core.rate_limit import _limiter


# ══════════════════════════════════════════════════════════════
# 登录测试
# ══════════════════════════════════════════════════════════════
class TestLogin:
    """POST /api/auth/login"""

    def test_login_success_teacher(self, client, teacher_user):
        """教师登录成功，返回 JWT token 和用户信息"""
        resp = client.post("/api/auth/login", json={
            "username": "teacher_test",
            "password": "123456",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert data["user"]["username"] == "teacher_test"
        assert data["user"]["role"] == "teacher"

    def test_login_success_student(self, client, student_user):
        """学生登录成功"""
        resp = client.post("/api/auth/login", json={
            "username": "student_test",
            "password": "123456",
        })
        assert resp.status_code == 200
        assert resp.json()["user"]["role"] == "student"

    def test_login_wrong_password(self, client, teacher_user):
        """密码错误返回 401"""
        resp = client.post("/api/auth/login", json={
            "username": "teacher_test",
            "password": "wrong_password",
        })
        assert resp.status_code == 401
        assert "用户名或密码错误" in resp.json()["detail"]

    def test_login_nonexistent_user(self, client):
        """不存在的用户返回 401（不泄露用户是否存在）"""
        resp = client.post("/api/auth/login", json={
            "username": "nobody",
            "password": "123456",
        })
        assert resp.status_code == 401

    def test_login_token_is_usable(self, client, teacher_user):
        """登录获取的 token 可以访问 /api/auth/me"""
        resp = client.post("/api/auth/login", json={
            "username": "teacher_test",
            "password": "123456",
        })
        token = resp.json()["access_token"]
        me_resp = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert me_resp.status_code == 200
        assert me_resp.json()["username"] == "teacher_test"


# ══════════════════════════════════════════════════════════════
# 注册测试
# ══════════════════════════════════════════════════════════════
class TestRegister:
    """POST /api/auth/register"""

    def test_register_student_success(self, client):
        """注册学生成功，返回 token"""
        resp = client.post("/api/auth/register", json={
            "name": "新同学",
            "username": "new_student",
            "password": "123456",
            "role": "student",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert data["user"]["username"] == "new_student"
        assert data["user"]["role"] == "student"

    def test_register_teacher_success(self, client):
        """注册教师成功"""
        resp = client.post("/api/auth/register", json={
            "name": "新老师",
            "username": "new_teacher",
            "password": "123456",
            "role": "teacher",
        })
        assert resp.status_code == 200
        assert resp.json()["user"]["role"] == "teacher"

    def test_register_duplicate_username(self, client, teacher_user):
        """重复用户名返回 400"""
        resp = client.post("/api/auth/register", json={
            "name": "重复",
            "username": "teacher_test",
            "password": "123456",
        })
        assert resp.status_code == 400
        assert "已存在" in resp.json()["detail"]

    def test_register_short_password(self, client):
        """密码 <6 位返回 400"""
        resp = client.post("/api/auth/register", json={
            "name": "短密码",
            "username": "short_pw_user",
            "password": "12345",
        })
        assert resp.status_code == 400
        assert "至少6位" in resp.json()["detail"]

    def test_register_admin_role_forbidden(self, client):
        """不允许自助注册 admin 角色"""
        resp = client.post("/api/auth/register", json={
            "name": "黑客",
            "username": "hacker_admin",
            "password": "123456",
            "role": "admin",
        })
        assert resp.status_code == 400
        assert "只能注册学生或教师" in resp.json()["detail"]

    def test_register_default_role_is_student(self, client):
        """不指定 role 时默认为学生"""
        resp = client.post("/api/auth/register", json={
            "name": "默认",
            "username": "default_role_user",
            "password": "123456",
        })
        assert resp.status_code == 200
        assert resp.json()["user"]["role"] == "student"


# ══════════════════════════════════════════════════════════════
# 获取当前用户测试
# ══════════════════════════════════════════════════════════════
class TestGetCurrentUser:
    """GET /api/auth/me"""

    def test_me_without_token(self, client):
        """无 token 访问返回 401"""
        resp = client.get("/api/auth/me")
        assert resp.status_code == 401

    def test_me_with_invalid_token(self, client):
        """无效 token 返回 401"""
        resp = client.get("/api/auth/me", headers={"Authorization": "Bearer invalid_token"})
        assert resp.status_code == 401

    def test_me_with_valid_token(self, client, teacher_user):
        """有效 token 返回当前用户信息"""
        token = create_access_token({"sub": str(teacher_user.id), "role": "teacher"})
        resp = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["username"] == "teacher_test"
        assert data["role"] == "teacher"
        assert data["id"] == teacher_user.id


# ══════════════════════════════════════════════════════════════
# 修改密码测试
# ══════════════════════════════════════════════════════════════
class TestChangePassword:
    """POST /api/auth/change-password"""

    def test_change_password_success(self, client, teacher_user):
        """正确旧密码 + 合规新密码 → 修改成功"""
        token = create_access_token({"sub": str(teacher_user.id), "role": "teacher"})
        resp = client.post("/api/auth/change-password",
            json={"old_password": "123456", "new_password": "newpass789"},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert resp.status_code == 200
        assert "成功" in resp.json()["message"]

    def test_change_password_wrong_old(self, client, teacher_user):
        """旧密码错误返回 400"""
        token = create_access_token({"sub": str(teacher_user.id), "role": "teacher"})
        resp = client.post("/api/auth/change-password",
            json={"old_password": "wrong_old", "new_password": "newpass789"},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert resp.status_code == 400
        assert "当前密码错误" in resp.json()["detail"]

    def test_change_password_short_new(self, client, teacher_user):
        """新密码 <6 位返回 400"""
        token = create_access_token({"sub": str(teacher_user.id), "role": "teacher"})
        resp = client.post("/api/auth/change-password",
            json={"old_password": "123456", "new_password": "12345"},
            headers={"Authorization": f"Bearer {token}"},
        )
        assert resp.status_code == 400
        assert "至少6位" in resp.json()["detail"]

    def test_login_after_password_change(self, client, teacher_user, db_session):
        """改密码后能用新密码登录，旧密码失败"""
        token = create_access_token({"sub": str(teacher_user.id), "role": "teacher"})
        # 改密码
        client.post("/api/auth/change-password",
            json={"old_password": "123456", "new_password": "newpass789"},
            headers={"Authorization": f"Bearer {token}"},
        )
        # 旧密码登录失败
        resp_old = client.post("/api/auth/login", json={
            "username": "teacher_test", "password": "123456",
        })
        assert resp_old.status_code == 401
        # 新密码登录成功
        resp_new = client.post("/api/auth/login", json={
            "username": "teacher_test", "password": "newpass789",
        })
        assert resp_new.status_code == 200


# ══════════════════════════════════════════════════════════════
# 限流测试
# ══════════════════════════════════════════════════════════════
class TestRateLimit:
    """认证路由限流保护"""

    def test_login_rate_limit(self, client, teacher_user):
        """同 IP 连续 10 次登录后触发限流"""
        for i in range(10):
            resp = client.post("/api/auth/login", json={
                "username": "teacher_test", "password": "wrong",
            })
            assert resp.status_code == 401  # 前 10 次是密码错误
        # 第 11 次应该被限流
        resp = client.post("/api/auth/login", json={
            "username": "teacher_test", "password": "123456",
        })
        assert resp.status_code == 429

    def test_register_rate_limit(self, client):
        """同 IP 连续 5 次注册后触发限流"""
        for i in range(5):
            resp = client.post("/api/auth/register", json={
                "name": f"用户{i}", "username": f"user_{i}", "password": "123456",
            })
            assert resp.status_code == 200
        # 第 6 次应该被限流
        resp = client.post("/api/auth/register", json={
            "name": "用户6", "username": "user_6", "password": "123456",
        })
        assert resp.status_code == 429

    def test_login_and_register_separate_limits(self, client, teacher_user):
        """登录和注册有独立的限流计数器"""
        # 用 9 次登录（接近但未达限）
        for i in range(9):
            client.post("/api/auth/login", json={
                "username": "teacher_test", "password": "wrong",
            })
        # 注册应该不受影响（独立计数器）
        resp = client.post("/api/auth/register", json={
            "name": "新用户", "username": "new_user", "password": "123456",
        })
        assert resp.status_code == 200
