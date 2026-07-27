"""实验报告管理 API 集成测试

核心测试点：
- 实验 CRUD（创建/查询/删除）
- 实验报告提交（文本/附件、重复提交覆盖）
- 报告批改（评分 + 通知副作用）
- 报告打回
- 报告附件下载
- 权限矩阵（教师/学生/管理员/非成员）
"""
import io
import os
from datetime import datetime
from pathlib import Path

import pytest

from backend.api.experiment_routes import UPLOAD_DIR
from backend.models.tables import (
    Classroom, Student, Experiment, ExperimentReport, Notification,
)


# ══════════════════════════════════════════════════════════════
# 辅助 fixtures
# ══════════════════════════════════════════════════════════════
@pytest.fixture()
def classroom_with_student(teacher_client, student_client):
    """创建公开课堂并让学生加入"""
    resp = teacher_client.post("/api/classrooms", json={
        "name": "实验测试课堂", "teacher": "张老师", "is_public": True,
    })
    classroom_id = resp.json()["id"]
    student_client.post(f"/api/classrooms/join/{classroom_id}")
    return classroom_id


def _create_experiment(client, title="实验一", classroom_id=None, **kwargs):
    """创建实验"""
    payload = {"title": title, "description": "实验描述", **kwargs}
    if classroom_id is not None:
        payload["classroom_id"] = classroom_id
    return client.post("/api/experiments", json=payload)


def _submit_report(client, experiment_id, content="我的实验报告", filename=None):
    """提交实验报告"""
    data = {"content": content}
    files = None
    if filename:
        files = [("file", (filename, io.BytesIO(b"report content"), "application/octet-stream"))]
    return client.post(f"/api/experiments/{experiment_id}/submit", data=data, files=files)


# ══════════════════════════════════════════════════════════════
# GET /api/experiments
# ══════════════════════════════════════════════════════════════
class TestListExperiments:
    """实验列表"""

    def test_teacher_sees_own(self, teacher_client, classroom_with_student):
        """教师只看到自己创建的实验"""
        _create_experiment(teacher_client, title="我的实验", classroom_id=classroom_with_student)
        resp = teacher_client.get("/api/experiments")
        assert resp.status_code == 200
        titles = [e["title"] for e in resp.json()]
        assert "我的实验" in titles

    def test_student_sees_joined_classroom(self, teacher_client, student_client, classroom_with_student):
        """学生看到自己课堂的实验"""
        _create_experiment(teacher_client, title="学生可见实验", classroom_id=classroom_with_student)
        resp = student_client.get("/api/experiments")
        assert resp.status_code == 200
        titles = [e["title"] for e in resp.json()]
        assert "学生可见实验" in titles

    def test_student_no_classroom_returns_empty(self, student_client):
        """未加入任何课堂的学生看到空列表"""
        resp = student_client.get("/api/experiments")
        assert resp.status_code == 200
        assert resp.json() == []

    def test_admin_sees_all(self, teacher_client, admin_client, classroom_with_student):
        """管理员能看到所有实验"""
        _create_experiment(teacher_client, title="教师实验", classroom_id=classroom_with_student)
        resp = admin_client.get("/api/experiments")
        assert resp.status_code == 200
        assert len(resp.json()) >= 1


# ══════════════════════════════════════════════════════════════
# POST /api/experiments
# ══════════════════════════════════════════════════════════════
class TestCreateExperiment:
    """创建实验"""

    def test_teacher_create_success(self, teacher_client, classroom_with_student):
        """教师创建实验成功"""
        resp = _create_experiment(teacher_client, title="新实验", classroom_id=classroom_with_student)
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "新实验"
        assert data["classroom_id"] == classroom_with_student
        assert data["status"] == "open"
        assert data["total_score"] == 100.0

    def test_student_create_forbidden(self, student_client, classroom_with_student):
        """学生不能创建 → 403"""
        resp = _create_experiment(student_client, classroom_id=classroom_with_student)
        assert resp.status_code == 403

    def test_teacher_create_for_other_classroom_forbidden(
        self, db_session, teacher_client, admin_user,
    ):
        """教师不能给他人课堂创建实验 → 403"""
        classroom = Classroom(name="他人课堂", teacher="管理员",
                              teacher_person_id=admin_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)
        resp = _create_experiment(teacher_client, classroom_id=classroom.id)
        assert resp.status_code == 403

    def test_admin_create_any_classroom(self, db_session, admin_client, teacher_user):
        """管理员可以给任何课堂创建实验"""
        classroom = Classroom(name="教师课堂", teacher="张老师",
                              teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)
        resp = _create_experiment(admin_client, classroom_id=classroom.id)
        assert resp.status_code == 200

    def test_create_without_classroom(self, teacher_client):
        """不绑定课堂也能创建实验"""
        resp = _create_experiment(teacher_client, title="自由实验")
        assert resp.status_code == 200
        assert resp.json()["classroom_id"] is None


# ══════════════════════════════════════════════════════════════
# GET /api/experiments/{id}
# ══════════════════════════════════════════════════════════════
class TestGetExperiment:
    """实验详情"""

    def test_owner_get_detail(self, teacher_client, classroom_with_student):
        """创建者查看详情"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = teacher_client.get(f"/api/experiments/{eid}")
        assert resp.status_code == 200
        assert resp.json()["id"] == eid

    def test_nonexistent(self, teacher_client):
        """不存在的实验 → 404"""
        resp = teacher_client.get("/api/experiments/99999")
        assert resp.status_code == 404

    def test_other_teacher_forbidden(self, db_session, teacher_client, admin_user):
        """非创建者教师不能查看 → 403"""
        exp = Experiment(teacher_id=admin_user.id, title="admin的实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        resp = teacher_client.get(f"/api/experiments/{exp.id}")
        assert resp.status_code == 403

    def test_student_member_can_view(self, teacher_client, student_client, classroom_with_student):
        """课堂成员学生可以查看"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = student_client.get(f"/api/experiments/{eid}")
        assert resp.status_code == 200


# ══════════════════════════════════════════════════════════════
# DELETE /api/experiments/{id}
# ══════════════════════════════════════════════════════════════
class TestDeleteExperiment:
    """删除实验"""

    def test_owner_delete_success(self, teacher_client, classroom_with_student):
        """创建者删除实验"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = teacher_client.delete(f"/api/experiments/{eid}")
        assert resp.status_code == 200
        # 确认已删除
        assert teacher_client.get(f"/api/experiments/{eid}").status_code == 404

    def test_non_owner_delete_forbidden(self, db_session, teacher_client, admin_user):
        """非创建者教师不能删除 → 403"""
        exp = Experiment(teacher_id=admin_user.id, title="admin实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        resp = teacher_client.delete(f"/api/experiments/{exp.id}")
        assert resp.status_code == 403

    def test_student_delete_forbidden(self, teacher_client, student_client, classroom_with_student):
        """学生不能删除 → 403"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = student_client.delete(f"/api/experiments/{eid}")
        assert resp.status_code == 403

    def test_admin_can_delete_any(self, db_session, admin_client, teacher_user):
        """管理员可以删除任何实验"""
        exp = Experiment(teacher_id=teacher_user.id, title="教师实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        resp = admin_client.delete(f"/api/experiments/{exp.id}")
        assert resp.status_code == 200

    def test_delete_cascades_reports(self, db_session, teacher_client, teacher_user, student_user):
        """删除实验时级联删除报告"""
        exp = Experiment(teacher_id=teacher_user.id, title="级联测试", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        report = ExperimentReport(experiment_id=exp.id, student_id=student_user.id, content="x")
        db_session.add(report)
        db_session.commit()

        resp = teacher_client.delete(f"/api/experiments/{exp.id}")
        assert resp.status_code == 200
        # 报告应被删除
        assert db_session.query(ExperimentReport).filter_by(experiment_id=exp.id).count() == 0


# ══════════════════════════════════════════════════════════════
# POST /api/experiments/{id}/submit
# ══════════════════════════════════════════════════════════════
class TestSubmitReport:
    """提交实验报告"""

    def test_student_submit_text_success(self, teacher_client, student_client, classroom_with_student):
        """学生提交纯文本报告成功"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = _submit_report(student_client, eid, content="实验完成")
        assert resp.status_code == 200
        data = resp.json()
        assert data["content"] == "实验完成"
        assert data["status"] == "submitted"
        assert data["file_name"] is None

    def test_student_submit_with_file(self, teacher_client, student_client, classroom_with_student):
        """学生提交带附件的报告"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        resp = _submit_report(student_client, eid, filename="report.pdf")
        assert resp.status_code == 200
        assert resp.json()["file_name"] == "report.pdf"

    def test_resubmit_overwrites(self, teacher_client, student_client, classroom_with_student):
        """重复提交覆盖原报告"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid, content="第一版")
        resp = _submit_report(student_client, eid, content="第二版")
        assert resp.status_code == 200
        assert resp.json()["content"] == "第二版"
        # 仍是同一条记录
        reports = student_client.get(f"/api/experiments/{eid}/reports").json()
        assert len(reports) == 1

    def test_nonexistent_experiment(self, student_client):
        """不存在的实验 → 404"""
        resp = _submit_report(student_client, 99999)
        assert resp.status_code == 404

    def test_student_non_member_forbidden(self, db_session, student_client, teacher_user):
        """非课堂成员学生不能提交 → 403"""
        exp = Experiment(teacher_id=teacher_user.id, title="他人实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        resp = _submit_report(student_client, exp.id)
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# GET /api/experiments/{id}/reports
# ══════════════════════════════════════════════════════════════
class TestListReports:
    """报告列表"""

    def test_teacher_sees_all_reports(self, teacher_client, student_client, classroom_with_student):
        """教师看到所有提交的报告"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid, content="学生报告")
        resp = teacher_client.get(f"/api/experiments/{eid}/reports")
        assert resp.status_code == 200
        assert len(resp.json()) == 1

    def test_student_sees_only_own(self, teacher_client, student_client, classroom_with_student):
        """学生只看到自己的报告"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid, content="我的报告")
        resp = student_client.get(f"/api/experiments/{eid}/reports")
        assert resp.status_code == 200
        reports = resp.json()
        assert len(reports) == 1
        assert reports[0]["content"] == "我的报告"

    def test_non_owner_teacher_forbidden(self, db_session, teacher_client, admin_user):
        """非创建者教师不能查看报告 → 403"""
        exp = Experiment(teacher_id=admin_user.id, title="admin实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        resp = teacher_client.get(f"/api/experiments/{exp.id}/reports")
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# POST /api/experiments/reports/{report_id}/grade
# ══════════════════════════════════════════════════════════════
class TestGradeReport:
    """批改报告"""

    def test_teacher_grade_success(self, teacher_client, student_client, student_user, classroom_with_student, db_session):
        """教师批改报告成功并发通知"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid, content="待批改")
        report_id = teacher_client.get(f"/api/experiments/{eid}/reports").json()[0]["id"]

        resp = teacher_client.post(f"/api/experiments/reports/{report_id}/grade", json={
            "score": 85, "feedback": "做得不错",
        })
        assert resp.status_code == 200
        assert resp.json()["success"] is True

        # 验证报告状态已更新
        report = db_session.query(ExperimentReport).filter_by(id=report_id).first()
        assert report.score == 85
        assert report.feedback == "做得不错"
        assert report.status == "graded"
        assert report.graded_at is not None

        # 验证通知已发送给学生
        notif = db_session.query(Notification).filter_by(
            receiver_id=student_user.id, type="homework",
        ).first()
        assert notif is not None
        assert "实验报告已批改" in notif.title

    def test_non_owner_grade_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """非创建者教师不能批改 → 403"""
        exp = Experiment(teacher_id=admin_user.id, title="admin实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        report = ExperimentReport(experiment_id=exp.id, student_id=student_user.id, content="x")
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = teacher_client.post(f"/api/experiments/reports/{report.id}/grade", json={
            "score": 90, "feedback": "",
        })
        assert resp.status_code == 403

    def test_grade_nonexistent_report(self, teacher_client):
        """批改不存在的报告 → 404"""
        resp = teacher_client.post("/api/experiments/reports/99999/grade", json={
            "score": 90, "feedback": "",
        })
        assert resp.status_code == 404

    def test_student_grade_forbidden(self, teacher_client, student_client, classroom_with_student):
        """学生不能批改 → 403"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid)
        report_id = student_client.get(f"/api/experiments/{eid}/reports").json()[0]["id"]
        resp = student_client.post(f"/api/experiments/reports/{report_id}/grade", json={
            "score": 100, "feedback": "自评",
        })
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# POST /api/experiments/reports/{report_id}/return
# ══════════════════════════════════════════════════════════════
class TestReturnReport:
    """打回报告"""

    def test_teacher_return_success(self, teacher_client, student_client, classroom_with_student, db_session):
        """教师打回报告成功"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid)
        report_id = teacher_client.get(f"/api/experiments/{eid}/reports").json()[0]["id"]

        resp = teacher_client.post(f"/api/experiments/reports/{report_id}/return", json={
            "feedback": "请重做",
        })
        assert resp.status_code == 200
        report = db_session.query(ExperimentReport).filter_by(id=report_id).first()
        assert report.status == "returned"
        assert report.feedback == "请重做"

    def test_return_default_feedback(self, teacher_client, student_client, classroom_with_student, db_session):
        """不打回时不传 feedback 使用默认"""
        eid = _create_experiment(teacher_client, classroom_id=classroom_with_student).json()["id"]
        _submit_report(student_client, eid)
        report_id = teacher_client.get(f"/api/experiments/{eid}/reports").json()[0]["id"]

        resp = teacher_client.post(f"/api/experiments/reports/{report_id}/return")
        assert resp.status_code == 200
        report = db_session.query(ExperimentReport).filter_by(id=report_id).first()
        assert report.feedback == "请重做"

    def test_non_owner_return_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """非创建者教师不能打回 → 403"""
        exp = Experiment(teacher_id=admin_user.id, title="admin实验", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        report = ExperimentReport(experiment_id=exp.id, student_id=student_user.id, content="x")
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = teacher_client.post(f"/api/experiments/reports/{report.id}/return", json={"feedback": ""})
        assert resp.status_code == 403


# ══════════════════════════════════════════════════════════════
# GET /api/experiments/reports/{report_id}/download
# ══════════════════════════════════════════════════════════════
class TestDownloadReport:
    """下载报告附件"""

    def test_owner_download_success(self, db_session, teacher_client, teacher_user, student_user):
        """教师下载学生提交的报告"""
        exp = Experiment(teacher_id=teacher_user.id, title="下载测试", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)

        # 创建带文件的报告
        file_path = os.path.join(UPLOAD_DIR, "test_download_report.pdf")
        Path(file_path).write_bytes(b"report content")
        report = ExperimentReport(
            experiment_id=exp.id, student_id=student_user.id,
            content="", file_path=file_path, file_name="report.pdf",
        )
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = teacher_client.get(f"/api/experiments/reports/{report.id}/download")
        assert resp.status_code == 200
        assert resp.content == b"report content"

    def test_student_download_own(self, db_session, student_client, teacher_user, student_user):
        """学生下载自己的报告"""
        exp = Experiment(teacher_id=teacher_user.id, title="学生下载", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)

        file_path = os.path.join(UPLOAD_DIR, "student_own.pdf")
        Path(file_path).write_bytes(b"my report")
        report = ExperimentReport(
            experiment_id=exp.id, student_id=student_user.id,
            content="", file_path=file_path, file_name="mine.pdf",
        )
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = student_client.get(f"/api/experiments/reports/{report.id}/download")
        assert resp.status_code == 200

    def test_student_download_others_forbidden(self, db_session, student_client, teacher_user, student_user):
        """学生不能下载他人的报告 → 403"""
        exp = Experiment(teacher_id=teacher_user.id, title="他人报告", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        # 创建另一个学生的报告
        from backend.models.tables import RegisteredPerson
        other = RegisteredPerson(name="王同学", role="student", username="other_exp",
                                  password_hash="x", face_embedding="[]")
        db_session.add(other)
        db_session.commit()
        db_session.refresh(other)

        file_path = os.path.join(UPLOAD_DIR, "other_report.pdf")
        Path(file_path).write_bytes(b"other")
        report = ExperimentReport(
            experiment_id=exp.id, student_id=other.id,
            content="", file_path=file_path, file_name="other.pdf",
        )
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = student_client.get(f"/api/experiments/reports/{report.id}/download")
        assert resp.status_code == 403

    def test_download_missing_file(self, db_session, teacher_client, teacher_user, student_user):
        """文件丢失 → 404"""
        exp = Experiment(teacher_id=teacher_user.id, title="丢失文件", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        report = ExperimentReport(
            experiment_id=exp.id, student_id=student_user.id,
            content="", file_path="uploads/experiments/nonexistent.pdf", file_name="x.pdf",
        )
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = teacher_client.get(f"/api/experiments/reports/{report.id}/download")
        assert resp.status_code == 404

    def test_download_no_attachment(self, db_session, teacher_client, teacher_user, student_user):
        """报告没有附件 → 404"""
        exp = Experiment(teacher_id=teacher_user.id, title="无附件", description="")
        db_session.add(exp)
        db_session.commit()
        db_session.refresh(exp)
        report = ExperimentReport(
            experiment_id=exp.id, student_id=student_user.id,
            content="只有文本", file_path=None, file_name=None,
        )
        db_session.add(report)
        db_session.commit()
        db_session.refresh(report)

        resp = teacher_client.get(f"/api/experiments/reports/{report.id}/download")
        assert resp.status_code == 404
