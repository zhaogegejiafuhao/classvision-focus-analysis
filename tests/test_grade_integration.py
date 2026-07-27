"""综合成绩管理 API 集成测试

核心测试点：
- 成绩权重配置 CRUD（默认值返回 / 持久化 / 权重和校验）
- 综合成绩报告计算（作业/考试/考勤/平时分加权）
- 平时分更新（教师权限 + 范围校验）
- 成绩趋势查询（学生只能看自己）
- 权限矩阵（教师/学生/管理员/非成员）
"""
from datetime import datetime

import pytest

from backend.models.tables import (
    Classroom, Student, RegisteredPerson, GradeConfig, UsualScore,
    Homework, HomeworkSubmission, Exam, ExamSubmission,
    CheckinSession, Attendance,
)


# ══════════════════════════════════════════════════════════════
# 辅助 fixtures
# ══════════════════════════════════════════════════════════════
@pytest.fixture()
def classroom_with_student(teacher_client, student_client):
    """创建公开课堂并让学生加入，返回 classroom_id"""
    resp = teacher_client.post("/api/classrooms", json={
        "name": "成绩测试课堂", "teacher": "张老师", "is_public": True,
    })
    classroom_id = resp.json()["id"]
    student_client.post(f"/api/classrooms/join/{classroom_id}")
    return classroom_id


def _set_up_classroom_with_student(db_session, teacher_user, student_user):
    """直接在 DB 中创建课堂 + 学生记录（用于绕过 HTTP 创建链路）"""
    classroom = Classroom(
        name="成绩测试课堂", teacher="张老师",
        teacher_person_id=teacher_user.id, is_public=True,
    )
    db_session.add(classroom)
    db_session.commit()
    db_session.refresh(classroom)

    student = Student(
        classroom_id=classroom.id,
        person_id=student_user.id,
        track_id=1,
        name=student_user.name if student_user else None,
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    return classroom, student


# ══════════════════════════════════════════════════════════════
# GET /api/grades/config/{classroom_id}
# ══════════════════════════════════════════════════════════════
class TestGetGradeConfig:
    """获取成绩权重配置"""

    def test_default_config(self, teacher_client, classroom_with_student):
        """未配置时返回默认权重"""
        resp = teacher_client.get(f"/api/grades/config/{classroom_with_student}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["classroom_id"] == classroom_with_student
        assert data["homework_weight"] == 0.3
        assert data["exam_weight"] == 0.4
        assert data["attendance_weight"] == 0.1
        assert data["usual_weight"] == 0.2

    def test_student_member_can_view(self, student_client, classroom_with_student):
        """课堂成员学生可以查看"""
        resp = student_client.get(f"/api/grades/config/{classroom_with_student}")
        assert resp.status_code == 200

    def test_student_non_member_forbidden(self, student_client, teacher_client):
        """非课堂成员学生不能查看 → 403"""
        # 教师创建一个课堂，学生不加入
        cid = teacher_client.post("/api/classrooms", json={
            "name": "他人课堂", "teacher": "张老师", "is_public": True,
        }).json()["id"]
        resp = student_client.get(f"/api/grades/config/{cid}")
        assert resp.status_code == 403

    def test_other_teacher_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """非创建者教师不能查看 → 403"""
        # 用 admin 创建课堂，teacher 不是创建者
        classroom, _ = _set_up_classroom_with_student(db_session, admin_user, student_user)
        resp = teacher_client.get(f"/api/grades/config/{classroom.id}")
        assert resp.status_code == 403

    def test_admin_can_view_any(self, db_session, admin_client, teacher_user, student_user):
        """管理员可以查看任何课堂"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = admin_client.get(f"/api/grades/config/{classroom.id}")
        assert resp.status_code == 200

    def test_nonexistent_classroom(self, teacher_client):
        """不存在的课堂 → 404"""
        resp = teacher_client.get("/api/grades/config/99999")
        assert resp.status_code == 404


# ══════════════════════════════════════════════════════════════
# POST /api/grades/config/{classroom_id}
# ══════════════════════════════════════════════════════════════
class TestSaveGradeConfig:
    """保存成绩权重配置"""

    def test_teacher_save_success(self, teacher_client, classroom_with_student):
        """教师保存配置成功"""
        resp = teacher_client.post(f"/api/grades/config/{classroom_with_student}", json={
            "homework_weight": 0.4,
            "exam_weight": 0.3,
            "attendance_weight": 0.2,
            "usual_weight": 0.1,
        })
        assert resp.status_code == 200
        assert resp.json()["success"] is True

        # 验证持久化
        resp = teacher_client.get(f"/api/grades/config/{classroom_with_student}")
        assert resp.json()["homework_weight"] == 0.4
        assert resp.json()["exam_weight"] == 0.3

    def test_student_save_forbidden(self, student_client, classroom_with_student):
        """学生不能保存配置 → 403"""
        resp = student_client.post(f"/api/grades/config/{classroom_with_student}", json={
            "homework_weight": 0.4, "exam_weight": 0.3,
            "attendance_weight": 0.2, "usual_weight": 0.1,
        })
        assert resp.status_code == 403

    def test_invalid_weight_sum(self, teacher_client, classroom_with_student):
        """权重之和不为 1 → 400"""
        resp = teacher_client.post(f"/api/grades/config/{classroom_with_student}", json={
            "homework_weight": 0.5, "exam_weight": 0.5,
            "attendance_weight": 0.5, "usual_weight": 0.5,
        })
        assert resp.status_code == 400
        assert "权重之和" in resp.json()["detail"]

    def test_non_owner_teacher_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """非创建者教师不能保存 → 403"""
        classroom, _ = _set_up_classroom_with_student(db_session, admin_user, student_user)
        resp = teacher_client.post(f"/api/grades/config/{classroom.id}", json={
            "homework_weight": 0.4, "exam_weight": 0.3,
            "attendance_weight": 0.2, "usual_weight": 0.1,
        })
        assert resp.status_code == 403

    def test_admin_can_save_any(self, db_session, admin_client, teacher_user, student_user):
        """管理员可以保存任何课堂配置"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = admin_client.post(f"/api/grades/config/{classroom.id}", json={
            "homework_weight": 0.5, "exam_weight": 0.3,
            "attendance_weight": 0.1, "usual_weight": 0.1,
        })
        assert resp.status_code == 200

    def test_update_existing_config(self, db_session, teacher_client, teacher_user, student_user):
        """更新已存在的配置（覆盖而非新增）"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 第一次保存
        teacher_client.post(f"/api/grades/config/{classroom.id}", json={
            "homework_weight": 0.4, "exam_weight": 0.3,
            "attendance_weight": 0.2, "usual_weight": 0.1,
        })
        # 第二次更新
        resp = teacher_client.post(f"/api/grades/config/{classroom.id}", json={
            "homework_weight": 0.2, "exam_weight": 0.5,
            "attendance_weight": 0.2, "usual_weight": 0.1,
        })
        assert resp.status_code == 200
        # 验证更新后的值
        data = teacher_client.get(f"/api/grades/config/{classroom.id}").json()
        assert data["homework_weight"] == 0.2
        assert data["exam_weight"] == 0.5
        # 确保只有一条配置记录
        configs = db_session.query(GradeConfig).filter_by(classroom_id=classroom.id).all()
        assert len(configs) == 1


# ══════════════════════════════════════════════════════════════
# PUT /api/grades/usual-score/{classroom_id}/{person_id}
# ══════════════════════════════════════════════════════════════
class TestUpdateUsualScore:
    """更新学生平时分"""

    def test_teacher_update_success(self, db_session, teacher_client, teacher_user, student_user):
        """教师更新平时分成功"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.put(
            f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=95",
        )
        assert resp.status_code == 200
        assert resp.json()["usual_score"] == 95

        # 验证持久化
        usual = db_session.query(UsualScore).filter_by(
            classroom_id=classroom.id, person_id=student_user.id,
        ).first()
        assert usual is not None
        assert usual.score == 95

    def test_student_update_forbidden(self, db_session, student_client, teacher_user, student_user):
        """学生不能更新平时分 → 403"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = student_client.put(
            f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=95",
        )
        assert resp.status_code == 403

    def test_score_out_of_range_high(self, db_session, teacher_client, teacher_user, student_user):
        """平时分超过 100 → 400"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.put(
            f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=150",
        )
        assert resp.status_code == 400

    def test_score_out_of_range_low(self, db_session, teacher_client, teacher_user, student_user):
        """平时分小于 0 → 400"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.put(
            f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=-5",
        )
        assert resp.status_code == 400

    def test_update_existing_usual_score(self, db_session, teacher_client, teacher_user, student_user):
        """更新已存在的平时分（覆盖而非新增）"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 第一次设置
        teacher_client.put(f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=80")
        # 第二次更新
        resp = teacher_client.put(f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=90")
        assert resp.status_code == 200

        records = db_session.query(UsualScore).filter_by(
            classroom_id=classroom.id, person_id=student_user.id,
        ).all()
        assert len(records) == 1
        assert records[0].score == 90


# ══════════════════════════════════════════════════════════════
# GET /api/grades/report/{classroom_id}
# ══════════════════════════════════════════════════════════════
class TestGradeReport:
    """综合成绩报告"""

    def test_empty_classroom_report(self, db_session, teacher_client, teacher_user, student_user):
        """空课堂（无作业/考试/签到）的报告，平时分默认 80"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.get(f"/api/grades/report/{classroom.id}")
        assert resp.status_code == 200
        data = resp.json()
        assert "config" in data
        assert "students" in data
        assert len(data["students"]) == 1
        s = data["students"][0]
        assert s["name"] == "李同学"
        assert s["homework_avg"] == 0
        assert s["exam_avg"] == 0
        # 无签到时出勤率默认 100
        assert s["attendance_rate"] == 100
        assert s["usual_score"] == 80
        # 综合分 = 0*0.3 + 0*0.4 + 100*0.1 + 80*0.2 = 26
        assert s["total_grade"] == 26.0

    def test_report_with_usual_score(self, db_session, teacher_client, teacher_user, student_user):
        """设置平时分后报告反映新分数"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        teacher_client.put(f"/api/grades/usual-score/{classroom.id}/{student_user.id}?score=95")

        resp = teacher_client.get(f"/api/grades/report/{classroom.id}")
        s = resp.json()["students"][0]
        assert s["usual_score"] == 95
        # 综合分 = 0*0.3 + 0*0.4 + 100*0.1 + 95*0.2 = 29
        assert s["total_grade"] == 29.0

    def test_student_member_can_view_report(self, student_client, classroom_with_student):
        """课堂成员学生可以查看报告"""
        resp = student_client.get(f"/api/grades/report/{classroom_with_student}")
        assert resp.status_code == 200

    def test_student_non_member_report_forbidden(self, student_client, teacher_client):
        """非成员学生不能查看报告 → 403"""
        cid = teacher_client.post("/api/classrooms", json={
            "name": "他人课堂", "teacher": "张老师", "is_public": True,
        }).json()["id"]
        resp = student_client.get(f"/api/grades/report/{cid}")
        assert resp.status_code == 403

    def test_report_sorted_by_total_desc(self, db_session, teacher_client, teacher_user, student_user):
        """报告按综合成绩降序排列"""
        classroom, student1 = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 创建第二个学生
        s2 = RegisteredPerson(name="王同学", role="student", username="wang_test",
                              password_hash="x", face_embedding="[]")
        db_session.add(s2)
        db_session.commit()
        db_session.refresh(s2)
        student2 = Student(classroom_id=classroom.id, person_id=s2.id, track_id=2, name="王同学")
        db_session.add(student2)
        db_session.commit()

        # 给两个学生设置不同平时分：student1=90, s2=60
        db_session.add(UsualScore(classroom_id=classroom.id, person_id=student1.person_id, score=90))
        db_session.add(UsualScore(classroom_id=classroom.id, person_id=s2.id, score=60))
        db_session.commit()

        resp = teacher_client.get(f"/api/grades/report/{classroom.id}")
        students = resp.json()["students"]
        assert len(students) == 2
        # 降序：高分在前
        assert students[0]["total_grade"] >= students[1]["total_grade"]
        assert students[0]["usual_score"] == 90
        assert students[1]["usual_score"] == 60


# ══════════════════════════════════════════════════════════════
# GET /api/grades/trend/{student_id}
# ══════════════════════════════════════════════════════════════
class TestGradeTrend:
    """学生成绩趋势"""

    def test_empty_trend(self, student_client, student_user):
        """无任何成绩记录时返回空趋势"""
        resp = student_client.get(f"/api/grades/trend/{student_user.id}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["trend"] == []
        assert data["avg_homework"] == 0
        assert data["avg_exam"] == 0

    def test_student_cannot_view_others(self, student_client, db_session, teacher_user, student_user):
        """学生不能查看他人成绩趋势 → 403"""
        # 创建另一个学生
        other = RegisteredPerson(name="王同学", role="student", username="other_test",
                                 password_hash="x", face_embedding="[]")
        db_session.add(other)
        db_session.commit()
        db_session.refresh(other)

        resp = student_client.get(f"/api/grades/trend/{other.id}")
        assert resp.status_code == 403

    def test_teacher_can_view_student_trend(self, db_session, teacher_client, teacher_user, student_user):
        """教师可以查看学生成绩趋势"""
        resp = teacher_client.get(f"/api/grades/trend/{student_user.id}")
        assert resp.status_code == 200

    def test_trend_with_homework(self, db_session, teacher_client, teacher_user, student_user):
        """有作业成绩时趋势包含作业记录"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 创建作业和提交记录
        hw = Homework(
            classroom_id=classroom.id, title="作业1", total_score=100,
            teacher_id=teacher_user.id,
        )
        db_session.add(hw)
        db_session.commit()
        db_session.refresh(hw)

        sub = HomeworkSubmission(
            homework_id=hw.id, student_id=student_user.id,
            score=85, status="graded", submitted_at=datetime.now(),
        )
        db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get(f"/api/grades/trend/{student_user.id}")
        data = resp.json()
        assert len(data["trend"]) == 1
        item = data["trend"][0]
        assert item["type"] == "homework"
        assert item["title"] == "作业1"
        assert item["score"] == 85
        assert item["percentage"] == 85.0
        assert item["index"] == 1
        assert data["avg_homework"] == 85.0
