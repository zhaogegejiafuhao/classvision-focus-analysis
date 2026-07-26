"""通知 API 集成测试

核心测试点：
- 双重已读机制（个人通知用 is_read 字段，全体通知用 NotificationReadStatus 关联表）
- 权限矩阵（创建/删除的权限分流）
- 级联删除（NotificationReadStatus 随通知一起清理）
"""
import pytest
from backend.models.tables import NotificationReadStatus


# ══════════════════════════════════════════════════════════════
# 创建通知
# ══════════════════════════════════════════════════════════════
class TestCreateNotification:
    """POST /api/notifications"""

    def test_teacher_create_personal(self, teacher_client, student_user):
        """教师创建个人通知"""
        resp = teacher_client.post("/api/notifications", json={
            "title": "作业提醒", "content": "请明天交作业",
            "receiver_id": student_user.id, "type": "homework",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "作业提醒"
        assert data["receiver_id"] == student_user.id
        assert data["is_read"] is False
        assert data["sender_name"] == "张老师"

    def test_teacher_create_broadcast(self, teacher_client):
        """教师创建全体通知（receiver_id=None）"""
        resp = teacher_client.post("/api/notifications", json={
            "title": "系统公告", "content": "明天放假",
        })
        assert resp.status_code == 200
        assert resp.json()["receiver_id"] is None

    def test_student_create_forbidden(self, student_client):
        """学生不能创建通知 → 403"""
        resp = student_client.post("/api/notifications", json={
            "title": "test", "content": "test",
        })
        assert resp.status_code == 403

    def test_admin_create_success(self, admin_client):
        """管理员可以创建通知"""
        resp = admin_client.post("/api/notifications", json={
            "title": "管理员公告", "content": "系统维护",
        })
        assert resp.status_code == 200


# ══════════════════════════════════════════════════════════════
# 列表与可见性
# ══════════════════════════════════════════════════════════════
class TestListNotifications:
    """GET /api/notifications"""

    def test_personal_notification_visibility(self, teacher_client, student_client, admin_client, student_user, teacher_user):
        """个人通知只有接收者能看到"""
        # teacher 给 student 发个人通知
        teacher_client.post("/api/notifications", json={
            "title": "给学生", "content": "私人消息", "receiver_id": student_user.id,
        })
        # admin 给 teacher 发个人通知
        admin_client.post("/api/notifications", json={
            "title": "给老师", "content": "私消息", "receiver_id": teacher_user.id,
        })
        # student 只能看到给自己的，看不到给 teacher 的
        resp = student_client.get("/api/notifications")
        titles = [n["title"] for n in resp.json()]
        assert "给学生" in titles
        assert "给老师" not in titles

    def test_broadcast_visible_to_all(self, teacher_client, student_client, admin_client):
        """全体通知所有人都能看到"""
        # teacher 发全体通知
        teacher_client.post("/api/notifications", json={
            "title": "全体公告", "content": "大家注意",
        })
        # student 应该能看到
        resp = student_client.get("/api/notifications")
        assert resp.status_code == 200
        titles = [n["title"] for n in resp.json()]
        assert "全体公告" in titles

    def test_unread_only_filter(self, teacher_client, student_client):
        """unread_only 过滤只返回未读通知"""
        # 发两条通知给学生
        for title in ["通知A", "通知B"]:
            teacher_client.post("/api/notifications", json={
                "title": title, "content": "内容",
            })
        # 标记第一条已读（需要获取 id）
        resp = student_client.get("/api/notifications")
        first_id = resp.json()[0]["id"]
        student_client.post(f"/api/notifications/{first_id}/read")

        # 过滤未读（通知B 被标记已读，通知A 仍然未读）
        resp = student_client.get("/api/notifications?unread_only=true")
        unread_titles = [n["title"] for n in resp.json()]
        assert "通知A" in unread_titles
        assert "通知B" not in unread_titles


# ══════════════════════════════════════════════════════════════
# 未读计数
# ══════════════════════════════════════════════════════════════
class TestUnreadCount:
    """GET /api/notifications/unread-count"""

    def test_initial_unread_count(self, teacher_client, student_client):
        """刚收到通知时未读数正确"""
        teacher_client.post("/api/notifications", json={
            "title": "全体1", "content": "内容",
        })
        teacher_client.post("/api/notifications", json={
            "title": "全体2", "content": "内容",
        })
        resp = student_client.get("/api/notifications/unread-count")
        assert resp.status_code == 200
        assert resp.json()["unread_count"] == 2

    def test_unread_count_after_read(self, teacher_client, student_client):
        """标记已读后未读数减少"""
        teacher_client.post("/api/notifications", json={"title": "A", "content": "x"})
        teacher_client.post("/api/notifications", json={"title": "B", "content": "x"})

        # 标记一条已读
        nid = student_client.get("/api/notifications").json()[0]["id"]
        student_client.post(f"/api/notifications/{nid}/read")

        resp = student_client.get("/api/notifications/unread-count")
        assert resp.json()["unread_count"] == 1

    def test_unread_count_after_read_all(self, teacher_client, student_client):
        """全部已读后未读数为 0"""
        teacher_client.post("/api/notifications", json={"title": "A", "content": "x"})
        teacher_client.post("/api/notifications", json={"title": "B", "content": "x"})

        student_client.post("/api/notifications/read-all")
        resp = student_client.get("/api/notifications/unread-count")
        assert resp.json()["unread_count"] == 0


# ══════════════════════════════════════════════════════════════
# 标记已读（双重机制）
# ══════════════════════════════════════════════════════════════
class TestMarkAsRead:
    """POST /api/notifications/{id}/read"""

    def test_mark_personal_read(self, teacher_client, student_client, student_user, db_session):
        """个人通知标记已读 → is_read=True"""
        # teacher 给 student 发个人通知
        resp = teacher_client.post("/api/notifications", json={
            "title": "个人", "content": "x", "receiver_id": student_user.id,
        })
        nid = resp.json()["id"]

        # student 标记已读
        resp = student_client.post(f"/api/notifications/{nid}/read")
        assert resp.status_code == 200

        # 验证 is_read=True
        notifs = student_client.get("/api/notifications").json()
        target = [n for n in notifs if n["id"] == nid][0]
        assert target["is_read"] is True

    def test_mark_broadcast_read(self, teacher_client, student_client, db_session):
        """全体通知标记已读 → NotificationReadStatus 创建"""
        # teacher 发全体通知
        resp = teacher_client.post("/api/notifications", json={
            "title": "全体", "content": "x",
        })
        nid = resp.json()["id"]

        # student 标记已读
        student_client.post(f"/api/notifications/{nid}/read")

        # 验证 NotificationReadStatus 记录存在
        count = db_session.query(NotificationReadStatus).filter(
            NotificationReadStatus.notification_id == nid,
        ).count()
        assert count == 1

    def test_mark_broadcast_read_idempotent(self, teacher_client, student_client, db_session):
        """全体通知重复标记已读不会创建多条记录"""
        nid = teacher_client.post("/api/notifications", json={
            "title": "全体", "content": "x",
        }).json()["id"]

        student_client.post(f"/api/notifications/{nid}/read")
        student_client.post(f"/api/notifications/{nid}/read")  # 重复

        count = db_session.query(NotificationReadStatus).filter(
            NotificationReadStatus.notification_id == nid,
        ).count()
        assert count == 1

    def test_non_receiver_cannot_mark_personal(self, teacher_client, admin_client, student_user):
        """非接收者不能标记个人通知已读 → 403"""
        # teacher 给 student 发个人通知
        nid = teacher_client.post("/api/notifications", json={
            "title": "私人", "content": "x", "receiver_id": student_user.id,
        }).json()["id"]

        # admin 尝试标记（admin 应该能标记？看代码：receiver_id != current_user.id 且 role != admin... 
        # 等等，代码只检查 receiver_id != current_user.id，没有 admin 豁免）
        # 实际上 admin 的 receiver_id 不是 student_user.id，所以会 403
        # 但 admin 可能不需要标记别人的通知已读
        resp = admin_client.post(f"/api/notifications/{nid}/read")
        # admin 不是接收者，应该 403
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# 删除通知（权限矩阵 + 级联清理）
# ══════════════════════════════════════════════════════════════
class TestDeleteNotification:
    """DELETE /api/notifications/{id}"""

    def test_delete_personal_by_receiver(self, teacher_client, student_client, student_user):
        """接收者可以删除个人通知"""
        nid = teacher_client.post("/api/notifications", json={
            "title": "给学生的", "content": "x", "receiver_id": student_user.id,
        }).json()["id"]

        resp = student_client.delete(f"/api/notifications/{nid}")
        assert resp.status_code == 200

    def test_delete_personal_by_non_receiver_forbidden(self, teacher_client, student_client, student_user, admin_user):
        """非接收者不能删除个人通知 → 403"""
        # teacher 给 student 发
        nid = teacher_client.post("/api/notifications", json={
            "title": "给学生的", "content": "x", "receiver_id": student_user.id,
        }).json()["id"]

        # 另一个学生想删（这里用 teacher，因为只有一个 student_client）
        resp = teacher_client.delete(f"/api/notifications/{nid}")
        assert resp.status_code == 403

    def test_delete_broadcast_by_sender(self, teacher_client):
        """发送者可以删除自己的全体通知"""
        nid = teacher_client.post("/api/notifications", json={
            "title": "我的公告", "content": "x",
        }).json()["id"]

        resp = teacher_client.delete(f"/api/notifications/{nid}")
        assert resp.status_code == 200

    def test_delete_broadcast_by_admin(self, teacher_client, admin_client):
        """管理员可以删除任何全体通知"""
        nid = teacher_client.post("/api/notifications", json={
            "title": "教师的公告", "content": "x",
        }).json()["id"]

        resp = admin_client.delete(f"/api/notifications/{nid}")
        assert resp.status_code == 200

    def test_delete_broadcast_by_other_forbidden(self, teacher_client, student_client):
        """普通用户不能删除别人的全体通知 → 403"""
        nid = teacher_client.post("/api/notifications", json={
            "title": "教师公告", "content": "x",
        }).json()["id"]

        resp = student_client.delete(f"/api/notifications/{nid}")
        assert resp.status_code == 403

    def test_delete_cascades_read_status(self, teacher_client, student_client, admin_client, db_session):
        """删除通知时级联清理 NotificationReadStatus"""
        # 发全体通知
        nid = teacher_client.post("/api/notifications", json={
            "title": "将删除", "content": "x",
        }).json()["id"]
        # student 标记已读（创建 NotificationReadStatus）
        student_client.post(f"/api/notifications/{nid}/read")
        assert db_session.query(NotificationReadStatus).filter(
            NotificationReadStatus.notification_id == nid,
        ).count() == 1

        # teacher 删除通知
        teacher_client.delete(f"/api/notifications/{nid}")

        # NotificationReadStatus 应该被级联删除
        assert db_session.query(NotificationReadStatus).filter(
            NotificationReadStatus.notification_id == nid,
        ).count() == 0

    def test_delete_nonexistent(self, teacher_client):
        """删除不存在的通知 → 404"""
        resp = teacher_client.delete("/api/notifications/99999")
        assert resp.status_code == 404
