"""作业系统 API 集成测试

核心测试点：
- 作业 CRUD（创建/查询/修改/删除 + 级联清理）
- 学生提交作业（含重复提交覆盖、截止时间校验）
- 教师批改（评分 + 通知副作用 + GradingResult 同步）
- 作业打回（状态变更 + 通知）
- 延期申请（提交/审批/自动延长截止时间）
- 权限矩阵（教师/学生/管理员/非创建者）
"""
from datetime import datetime, timedelta

import pytest

from backend.models.tables import (
    Homework, HomeworkSubmission, ExtensionRequest, Notification, GradingResult,
)


# ══════════════════════════════════════════════════════════════
# 辅助 fixtures
# ══════════════════════════════════════════════════════════════
@pytest.fixture()
def classroom_with_student(teacher_client, student_client):
    """创建公开课堂并让学生加入"""
    resp = teacher_client.post("/api/classrooms", json={
        "name": "作业测试课堂", "teacher": "张老师", "is_public": True,
    })
    classroom_id = resp.json()["id"]
    student_client.post(f"/api/classrooms/join/{classroom_id}")
    return classroom_id


def _create_homework(client, title="测试作业", classroom_id=None, **kwargs):
    """创建作业"""
    payload = {"title": title, "description": "作业描述", "total_score": 100.0, **kwargs}
    if classroom_id is not None:
        payload["classroom_id"] = classroom_id
    return client.post("/api/homework", json=payload)


# ══════════════════════════════════════════════════════════════
# 作业 CRUD
# ══════════════════════════════════════════════════════════════
class TestHomeworkCRUD:
    """作业增删改查"""

    def test_teacher_create_success(self, teacher_client, classroom_with_student):
        """教师创建作业成功"""
        resp = _create_homework(teacher_client, title="第一次作业", classroom_id=classroom_with_student)
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "第一次作业"
        assert data["status"] == "open"
        assert data["total_score"] == 100.0
        assert data["submission_count"] == 0

    def test_student_create_forbidden(self, student_client, classroom_with_student):
        """学生不能创建作业 → 403"""
        resp = _create_homework(student_client, classroom_id=classroom_with_student)
        assert resp.status_code == 403

    def test_create_with_deadline(self, teacher_client, classroom_with_student):
        """创建带截止时间的作业"""
        deadline = (datetime.now() + timedelta(days=7)).isoformat()
        resp = _create_homework(teacher_client, classroom_id=classroom_with_student,
                                deadline=deadline)
        assert resp.status_code == 200
        assert resp.json()["deadline"] is not None

    def test_create_sends_notification(self, teacher_client, student_client, classroom_with_student):
        """创建作业时给学生发通知"""
        _create_homework(teacher_client, title="通知测试", classroom_id=classroom_with_student)
        resp = student_client.get("/api/notifications")
        titles = [n["title"] for n in resp.json()]
        assert any("新作业" in t for t in titles)

    def test_list_homework(self, teacher_client, classroom_with_student):
        """教师查看作业列表"""
        _create_homework(teacher_client, title="作业A", classroom_id=classroom_with_student)
        _create_homework(teacher_client, title="作业B", classroom_id=classroom_with_student)
        resp = teacher_client.get("/api/homework")
        assert resp.status_code == 200
        titles = [h["title"] for h in resp.json()]
        assert "作业A" in titles
        assert "作业B" in titles

    def test_student_list_forbidden(self, student_client):
        """学生不能查看教师作业列表 → 403"""
        resp = student_client.get("/api/homework")
        assert resp.status_code == 403

    def test_list_assigned_for_student(self, teacher_client, student_client, classroom_with_student):
        """学生查看分配给自己的作业"""
        _create_homework(teacher_client, title="学生作业", classroom_id=classroom_with_student)
        resp = student_client.get("/api/homework/assigned")
        assert resp.status_code == 200
        titles = [h["title"] for h in resp.json()]
        assert "学生作业" in titles

    def test_get_homework_detail(self, teacher_client, classroom_with_student):
        """获取作业详情"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = teacher_client.get(f"/api/homework/{hid}")
        assert resp.status_code == 200
        assert resp.json()["id"] == hid

    def test_nonexistent_homework(self, teacher_client):
        """不存在的作业 → 404"""
        resp = teacher_client.get("/api/homework/99999")
        assert resp.status_code == 404

    def test_update_homework(self, teacher_client, classroom_with_student):
        """更新作业"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = teacher_client.put(f"/api/homework/{hid}", json={"title": "更新标题", "status": "closed"})
        assert resp.status_code == 200
        assert resp.json()["title"] == "更新标题"
        assert resp.json()["status"] == "closed"

    def test_non_owner_update_forbidden(self, db_session, teacher_client, admin_user):
        """非创建者教师不能更新 → 403"""
        hw = Homework(title="admin作业", description="", teacher_id=admin_user.id, total_score=100)
        db_session.add(hw)
        db_session.commit()
        db_session.refresh(hw)
        resp = teacher_client.put(f"/api/homework/{hw.id}", json={"title": "篡改"})
        assert resp.status_code == 403

    def test_delete_homework(self, teacher_client, classroom_with_student):
        """删除作业"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = teacher_client.delete(f"/api/homework/{hid}")
        assert resp.status_code == 200
        # 确认已删除
        assert teacher_client.get(f"/api/homework/{hid}").status_code == 404

    def test_delete_cascades(self, db_session, teacher_client, teacher_user, student_user):
        """删除作业时级联清理提交和延期申请"""
        hw = Homework(title="级联测试", description="", teacher_id=teacher_user.id, total_score=100)
        db_session.add(hw)
        db_session.commit()
        db_session.refresh(hw)
        sub = HomeworkSubmission(homework_id=hw.id, student_id=student_user.id, content="x")
        ext = ExtensionRequest(homework_id=hw.id, student_id=student_user.id,
                               reason="延期", requested_deadline=datetime.now() + timedelta(days=1))
        db_session.add_all([sub, ext])
        db_session.commit()

        resp = teacher_client.delete(f"/api/homework/{hw.id}")
        assert resp.status_code == 200
        assert db_session.query(HomeworkSubmission).filter_by(homework_id=hw.id).count() == 0
        assert db_session.query(ExtensionRequest).filter_by(homework_id=hw.id).count() == 0


# ══════════════════════════════════════════════════════════════
# 作业提交
# ══════════════════════════════════════════════════════════════
class TestHomeworkSubmission:
    """学生提交作业"""

    def test_student_submit_success(self, teacher_client, student_client, classroom_with_student):
        """学生提交作业成功"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = student_client.post(f"/api/homework/{hid}/submit", json={"content": "我的答案"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["content"] == "我的答案"
        assert data["status"] == "submitted"

    def test_resubmit_overwrites(self, teacher_client, student_client, classroom_with_student):
        """重复提交覆盖原内容"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        student_client.post(f"/api/homework/{hid}/submit", json={"content": "第一版"})
        resp = student_client.post(f"/api/homework/{hid}/submit", json={"content": "第二版"})
        assert resp.status_code == 200
        assert resp.json()["content"] == "第二版"

    def test_submit_after_deadline(self, teacher_client, student_client, classroom_with_student):
        """截止后提交 → 400"""
        deadline = (datetime.now() - timedelta(days=1)).isoformat()
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student,
                               deadline=deadline).json()["id"]
        resp = student_client.post(f"/api/homework/{hid}/submit", json={"content": "迟交"})
        assert resp.status_code == 400
        assert "已截止" in resp.json()["detail"]

    def test_submit_nonexistent_homework(self, student_client):
        """不存在的作业 → 404"""
        resp = student_client.post("/api/homework/99999/submit", json={"content": "x"})
        assert resp.status_code == 404

    def test_my_submission_status(self, teacher_client, student_client, classroom_with_student):
        """查看自己是否已提交"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        # 未提交时
        resp = student_client.get(f"/api/homework/my-submissions/{hid}")
        assert resp.status_code == 200
        assert resp.json()["submitted"] is False
        # 提交后
        student_client.post(f"/api/homework/{hid}/submit", json={"content": "已交"})
        resp = student_client.get(f"/api/homework/my-submissions/{hid}")
        assert resp.json()["submitted"] is True


# ══════════════════════════════════════════════════════════════
# 批改与打回
# ══════════════════════════════════════════════════════════════
class TestHomeworkGrading:
    """教师批改与打回"""

    def test_teacher_grade_success(self, db_session, teacher_client, student_client, student_user,
                                    classroom_with_student):
        """教师批改作业并发通知"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        student_client.post(f"/api/homework/{hid}/submit", json={"content": "待批改"})
        sid = teacher_client.get(f"/api/homework/{hid}/submissions").json()[0]["id"]

        resp = teacher_client.post(f"/api/homework/submissions/{sid}/grade", json={
            "score": 85, "feedback": "做得不错",
        })
        assert resp.status_code == 200

        # 验证提交状态
        sub = db_session.query(HomeworkSubmission).filter_by(id=sid).first()
        assert sub.score == 85
        assert sub.feedback == "做得不错"
        assert sub.status == "graded"

        # 验证 GradingResult 已创建
        gr = db_session.query(GradingResult).filter_by(submission_id=sid).first()
        assert gr is not None
        assert gr.score == 85
        assert gr.grading_method == "manual"

        # 验证通知已发送（过滤出批改通知，排除"新作业"通知）
        notif = db_session.query(Notification).filter(
            Notification.receiver_id == student_user.id,
            Notification.type == "homework",
            Notification.title.contains("已批改"),
        ).first()
        assert notif is not None
        assert "已批改" in notif.title

    def test_non_owner_grade_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """非创建者教师不能批改 → 403"""
        hw = Homework(title="admin作业", description="", teacher_id=admin_user.id, total_score=100)
        db_session.add(hw)
        db_session.commit()
        db_session.refresh(hw)
        sub = HomeworkSubmission(homework_id=hw.id, student_id=student_user.id, content="x")
        db_session.add(sub)
        db_session.commit()
        db_session.refresh(sub)

        resp = teacher_client.post(f"/api/homework/submissions/{sub.id}/grade", json={
            "score": 90, "feedback": "",
        })
        assert resp.status_code == 403

    def test_return_submission(self, db_session, teacher_client, student_client, student_user,
                                classroom_with_student):
        """教师打回作业"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        student_client.post(f"/api/homework/{hid}/submit", json={"content": "需重做"})
        sid = teacher_client.get(f"/api/homework/{hid}/submissions").json()[0]["id"]

        resp = teacher_client.post(f"/api/homework/submissions/{sid}/return", json={
            "feedback": "请重新完成",
        })
        assert resp.status_code == 200
        sub = db_session.query(HomeworkSubmission).filter_by(id=sid).first()
        assert sub.status == "returned"
        assert sub.feedback == "请重新完成"

        # 验证通知（过滤出打回通知）
        notif = db_session.query(Notification).filter(
            Notification.receiver_id == student_user.id,
            Notification.type == "homework",
            Notification.title.contains("被打回"),
        ).first()
        assert notif is not None
        assert "被打回" in notif.title

    def test_list_submissions(self, teacher_client, student_client, classroom_with_student):
        """教师查看提交列表"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        student_client.post(f"/api/homework/{hid}/submit", json={"content": "提交"})
        resp = teacher_client.get(f"/api/homework/{hid}/submissions")
        assert resp.status_code == 200
        assert len(resp.json()) == 1


# ══════════════════════════════════════════════════════════════
# 延期申请
# ══════════════════════════════════════════════════════════════
class TestExtensionRequest:
    """延期申请"""

    def test_student_create_extension(self, teacher_client, student_client, classroom_with_student):
        """学生提交延期申请"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = student_client.post("/api/homework/extensions", json={
            "homework_id": hid,
            "reason": "生病",
            "requested_deadline": (datetime.now() + timedelta(days=3)).isoformat(),
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["reason"] == "生病"
        assert data["status"] == "pending"

    def test_teacher_list_extensions(self, teacher_client, student_client, classroom_with_student):
        """教师查看延期申请列表"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        student_client.post("/api/homework/extensions", json={
            "homework_id": hid,
            "reason": "请假",
            "requested_deadline": (datetime.now() + timedelta(days=3)).isoformat(),
        })
        resp = teacher_client.get("/api/homework/extensions")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1

    def test_approve_extension_extends_deadline(self, db_session, teacher_client, student_client,
                                                  classroom_with_student):
        """通过延期申请后自动延长截止时间"""
        original_deadline = datetime.now() + timedelta(days=1)
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student,
                               deadline=original_deadline.isoformat()).json()["id"]
        new_deadline = (datetime.now() + timedelta(days=7)).isoformat()
        ext_resp = student_client.post("/api/homework/extensions", json={
            "homework_id": hid,
            "reason": "需要更多时间",
            "requested_deadline": new_deadline,
        })
        ext_id = ext_resp.json()["id"]

        resp = teacher_client.post(f"/api/homework/extensions/{ext_id}/review", json={
            "status": "approved", "feedback": "同意延期",
        })
        assert resp.status_code == 200

        # 验证截止时间已延长
        hw = db_session.query(Homework).filter_by(id=hid).first()
        assert hw.deadline.strftime("%Y-%m-%d") == datetime.fromisoformat(new_deadline).strftime("%Y-%m-%d")

    def test_reject_extension(self, teacher_client, student_client, classroom_with_student):
        """拒绝延期申请"""
        hid = _create_homework(teacher_client, classroom_id=classroom_with_student).json()["id"]
        ext_resp = student_client.post("/api/homework/extensions", json={
            "homework_id": hid,
            "reason": "理由",
            "requested_deadline": (datetime.now() + timedelta(days=3)).isoformat(),
        })
        ext_id = ext_resp.json()["id"]

        resp = teacher_client.post(f"/api/homework/extensions/{ext_id}/review", json={
            "status": "rejected", "feedback": "不同意",
        })
        assert resp.status_code == 200
        # 验证状态
        exts = teacher_client.get("/api/homework/extensions?status=rejected").json()
        assert any(e["id"] == ext_id for e in exts)

    def test_non_owner_review_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """非创建者教师不能审批 → 403"""
        hw = Homework(title="admin作业", description="", teacher_id=admin_user.id, total_score=100)
        db_session.add(hw)
        db_session.commit()
        db_session.refresh(hw)
        ext = ExtensionRequest(
            homework_id=hw.id, student_id=student_user.id, reason="延期",
            requested_deadline=datetime.now() + timedelta(days=3),
        )
        db_session.add(ext)
        db_session.commit()
        db_session.refresh(ext)

        resp = teacher_client.post(f"/api/homework/extensions/{ext.id}/review", json={
            "status": "approved", "feedback": "",
        })
        assert resp.status_code == 403
