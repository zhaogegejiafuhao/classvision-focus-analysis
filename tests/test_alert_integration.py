"""教学预警 API 集成测试

核心测试点：
- 三类预警触发条件：出勤率低、作业未交、考试不及格
- 预警级别判定（high/medium）
- 权限校验（教师只看自己课堂、学生只看所在课堂、admin 看所有）
- 空 DB / 无预警场景
- 按 classroom_id 过滤
"""
from datetime import datetime, timedelta

import pytest

from backend.models.tables import (
    Classroom, Student, RegisteredPerson, ClassroomMember,
    CheckinSession, Attendance,
    Homework, HomeworkSubmission,
    Exam, ExamSubmission,
)


# ══════════════════════════════════════════════════════════════
# 辅助函数
# ══════════════════════════════════════════════════════════════
def _set_up_classroom_with_student(db_session, teacher_user, student_user):
    """创建课堂 + 学生 + 课堂成员记录"""
    classroom = Classroom(
        name="预警测试课堂", teacher="张老师",
        teacher_person_id=teacher_user.id, is_public=True,
    )
    db_session.add(classroom)
    db_session.commit()
    db_session.refresh(classroom)

    student = Student(
        classroom_id=classroom.id, person_id=student_user.id,
        track_id=1, name=student_user.name,
    )
    db_session.add(student)
    # 同时加入 ClassroomMember（预警接口用这个判断成员关系）
    member = ClassroomMember(classroom_id=classroom.id, person_id=student_user.id)
    db_session.add(member)
    db_session.commit()
    db_session.refresh(student)
    return classroom, student


# ══════════════════════════════════════════════════════════════
# 基础场景
# ══════════════════════════════════════════════════════════════
class TestGetAlertsBasic:
    """基础查询"""

    def test_empty_alerts(self, db_session, teacher_client, teacher_user, student_user):
        """无任何数据时返回空预警"""
        _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.get("/api/alerts")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total"] == 0
        assert data["high"] == 0
        assert data["alerts"] == []

    def test_teacher_sees_own_classroom(self, db_session, teacher_client, teacher_user, student_user):
        """教师只看到自己课堂的预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.get("/api/alerts")
        assert resp.status_code == 200
        # 教师能看到自己课堂（即使无预警也算成功）
        assert resp.json()["total"] == 0

    def test_student_sees_joined_classroom(self, db_session, student_client, teacher_user, student_user):
        """学生看到自己所在课堂的预警"""
        _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = student_client.get("/api/alerts")
        assert resp.status_code == 200

    def test_student_no_classroom_empty(self, student_client):
        """未加入任何课堂的学生看到空预警"""
        resp = student_client.get("/api/alerts")
        assert resp.status_code == 200
        assert resp.json()["total"] == 0

    def test_admin_sees_all_classrooms(self, db_session, admin_client, teacher_user, admin_user, student_user):
        """管理员看到所有课堂的预警"""
        _set_up_classroom_with_student(db_session, teacher_user, student_user)
        _set_up_classroom_with_student(db_session, admin_user, student_user)
        resp = admin_client.get("/api/alerts")
        assert resp.status_code == 200


# ══════════════════════════════════════════════════════════════
# 按 classroom_id 过滤 + 权限
# ══════════════════════════════════════════════════════════════
class TestAlertFilterByClassroom:
    """按课堂过滤"""

    def test_teacher_filter_own_classroom(self, db_session, teacher_client, teacher_user, student_user):
        """教师按 classroom_id 过滤自己课堂"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = teacher_client.get(f"/api/alerts?classroom_id={classroom.id}")
        assert resp.status_code == 200

    def test_teacher_filter_others_classroom_forbidden(self, db_session, teacher_client, admin_user, student_user):
        """教师不能查看他人课堂的预警 → 403"""
        classroom, _ = _set_up_classroom_with_student(db_session, admin_user, student_user)
        resp = teacher_client.get(f"/api/alerts?classroom_id={classroom.id}")
        assert resp.status_code == 403

    def test_student_filter_non_member_forbidden(self, db_session, student_client, teacher_user, student_user):
        """学生过滤非成员课堂 → 403"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 用另一个学生（非成员）查询
        other = RegisteredPerson(name="王同学", role="student", username="other_alert",
                                 password_hash="x", face_embedding="[]")
        db_session.add(other)
        db_session.commit()
        db_session.refresh(other)
        # student_client 是李同学，不是该课堂成员（_set_up 只让 student_user 加入）
        # 但 student_user 就是李同学…需要创建另一个课堂让 student_client 不是成员
        other_classroom = Classroom(name="非成员课堂", teacher="张老师",
                                    teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(other_classroom)
        db_session.commit()
        db_session.refresh(other_classroom)
        resp = student_client.get(f"/api/alerts?classroom_id={other_classroom.id}")
        assert resp.status_code == 403

    def test_admin_filter_any_classroom(self, db_session, admin_client, teacher_user, student_user):
        """管理员可以查看任何课堂的预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        resp = admin_client.get(f"/api/alerts?classroom_id={classroom.id}")
        assert resp.status_code == 200


# ══════════════════════════════════════════════════════════════
# 出勤率预警
# ══════════════════════════════════════════════════════════════
class TestAttendanceAlert:
    """出勤率预警"""

    def test_low_attendance_triggers_alert(self, db_session, teacher_client, teacher_user, student_user):
        """出勤率 < 60% 触发预警（3次签到只出勤1次）"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 创建 3 次签到
        for i in range(3):
            session = CheckinSession(classroom_id=classroom.id, teacher_id=teacher_user.id,
                                     type="normal", status="closed")
            db_session.add(session)
            db_session.commit()
            db_session.refresh(session)
            # 只第一次出勤，后两次缺勤
            status = "present" if i == 0 else "absent"
            att = Attendance(
                classroom_id=classroom.id, student_id=student_user.id,
                student_record_id=student.id, checkin_session_id=session.id,
                status=status,
            )
            db_session.add(att)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        data = resp.json()
        assert data["total"] >= 1
        att_alerts = [a for a in data["alerts"] if a["type"] == "attendance"]
        assert len(att_alerts) == 1
        assert att_alerts[0]["student_name"] == "李同学"
        # 1/3 ≈ 33% < 40% → high 级别
        assert att_alerts[0]["level"] == "high"
        assert att_alerts[0]["value"] == 33.3

    def test_medium_attendance_alert(self, db_session, teacher_client, teacher_user, student_user):
        """出勤率 40%-60% 之间 → medium 级别（5次签到出勤2次=40%）"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        for i in range(5):
            session = CheckinSession(classroom_id=classroom.id, teacher_id=teacher_user.id,
                                     type="normal", status="closed")
            db_session.add(session)
            db_session.commit()
            db_session.refresh(session)
            status = "present" if i < 2 else "absent"
            att = Attendance(
                classroom_id=classroom.id, student_id=student_user.id,
                student_record_id=student.id, checkin_session_id=session.id,
                status=status,
            )
            db_session.add(att)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        att_alerts = [a for a in resp.json()["alerts"] if a["type"] == "attendance"]
        assert len(att_alerts) == 1
        # 2/5 = 40% → 40% < 60% 触发，但 40% 不 < 40%，所以是 medium
        assert att_alerts[0]["level"] == "medium"

    def test_good_attendance_no_alert(self, db_session, teacher_client, teacher_user, student_user):
        """出勤率 >= 60% 不触发预警"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        for i in range(5):
            session = CheckinSession(classroom_id=classroom.id, teacher_id=teacher_user.id,
                                     type="normal", status="closed")
            db_session.add(session)
            db_session.commit()
            db_session.refresh(session)
            # 4/5 = 80% >= 60%
            status = "present" if i < 4 else "absent"
            att = Attendance(
                classroom_id=classroom.id, student_id=student_user.id,
                student_record_id=student.id, checkin_session_id=session.id,
                status=status,
            )
            db_session.add(att)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        att_alerts = [a for a in resp.json()["alerts"] if a["type"] == "attendance"]
        assert len(att_alerts) == 0

    def test_less_than_three_sessions_no_alert(self, db_session, teacher_client, teacher_user, student_user):
        """签到次数 < 3 时不触发出勤预警"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 只创建 2 次签到（即使全缺勤）
        for i in range(2):
            session = CheckinSession(classroom_id=classroom.id, teacher_id=teacher_user.id,
                                     type="normal", status="closed")
            db_session.add(session)
            db_session.commit()
            db_session.refresh(session)
            att = Attendance(
                classroom_id=classroom.id, student_id=student_user.id,
                student_record_id=student.id, checkin_session_id=session.id,
                status="absent",
            )
            db_session.add(att)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        att_alerts = [a for a in resp.json()["alerts"] if a["type"] == "attendance"]
        assert len(att_alerts) == 0


# ══════════════════════════════════════════════════════════════
# 作业未交预警
# ══════════════════════════════════════════════════════════════
class TestHomeworkAlert:
    """作业未交预警"""

    def test_unsubmitted_homework_triggers_alert(self, db_session, teacher_client, teacher_user, student_user):
        """3次作业未交触发预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 创建 3 个已过截止时间的作业，学生都未提交
        for i in range(3):
            hw = Homework(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"作业{i}", total_score=100,
                deadline=datetime.now() - timedelta(days=1),
            )
            db_session.add(hw)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        hw_alerts = [a for a in resp.json()["alerts"] if a["type"] == "homework"]
        assert len(hw_alerts) == 1
        assert hw_alerts[0]["value"] == 3
        assert hw_alerts[0]["level"] == "medium"  # 3 < 5 → medium

    def test_high_level_homework_alert(self, db_session, teacher_client, teacher_user, student_user):
        """5次以上作业未交 → high 级别"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        for i in range(5):
            hw = Homework(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"作业{i}", total_score=100,
                deadline=datetime.now() - timedelta(days=1),
            )
            db_session.add(hw)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        hw_alerts = [a for a in resp.json()["alerts"] if a["type"] == "homework"]
        assert len(hw_alerts) == 1
        assert hw_alerts[0]["level"] == "high"
        assert hw_alerts[0]["value"] == 5

    def test_submitted_homework_no_alert(self, db_session, teacher_client, teacher_user, student_user):
        """已提交的作业不计入未交"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        hw = Homework(
            classroom_id=classroom.id, teacher_id=teacher_user.id,
            title="已交作业", total_score=100,
            deadline=datetime.now() - timedelta(days=1),
        )
        db_session.add(hw)
        db_session.commit()
        db_session.refresh(hw)
        # 提交作业
        sub = HomeworkSubmission(homework_id=hw.id, student_id=student_user.id, content="已交")
        db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        hw_alerts = [a for a in resp.json()["alerts"] if a["type"] == "homework"]
        assert len(hw_alerts) == 0

    def test_future_deadline_no_alert(self, db_session, teacher_client, teacher_user, student_user):
        """未过截止时间的作业不触发预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        hw = Homework(
            classroom_id=classroom.id, teacher_id=teacher_user.id,
            title="未到期作业", total_score=100,
            deadline=datetime.now() + timedelta(days=7),
        )
        db_session.add(hw)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        hw_alerts = [a for a in resp.json()["alerts"] if a["type"] == "homework"]
        assert len(hw_alerts) == 0


# ══════════════════════════════════════════════════════════════
# 考试不及格预警
# ══════════════════════════════════════════════════════════════
class TestExamAlert:
    """考试不及格预警"""

    def test_failed_exams_triggers_alert(self, db_session, teacher_client, teacher_user, student_user):
        """2次考试不及格触发预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        # 创建 2 场已发布的考试
        for i in range(2):
            exam = Exam(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"考试{i}", total_score=100, status="published",
            )
            db_session.add(exam)
            db_session.commit()
            db_session.refresh(exam)
            # 不及格（< 60 分）
            sub = ExamSubmission(
                exam_id=exam.id, student_id=student_user.id,
                score=40, status="graded",
            )
            db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        exam_alerts = [a for a in resp.json()["alerts"] if a["type"] == "exam"]
        assert len(exam_alerts) == 1
        assert exam_alerts[0]["value"] == 2
        assert exam_alerts[0]["level"] == "medium"

    def test_high_level_exam_alert(self, db_session, teacher_client, teacher_user, student_user):
        """3次以上考试不及格 → high 级别"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        for i in range(3):
            exam = Exam(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"考试{i}", total_score=100, status="published",
            )
            db_session.add(exam)
            db_session.commit()
            db_session.refresh(exam)
            sub = ExamSubmission(
                exam_id=exam.id, student_id=student_user.id,
                score=30, status="graded",
            )
            db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        exam_alerts = [a for a in resp.json()["alerts"] if a["type"] == "exam"]
        assert len(exam_alerts) == 1
        assert exam_alerts[0]["level"] == "high"

    def test_passing_score_no_alert(self, db_session, teacher_client, teacher_user, student_user):
        """及格分数不触发预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        exam = Exam(
            classroom_id=classroom.id, teacher_id=teacher_user.id,
            title="及格考试", total_score=100, status="published",
        )
        db_session.add(exam)
        db_session.commit()
        db_session.refresh(exam)
        sub = ExamSubmission(
            exam_id=exam.id, student_id=student_user.id,
            score=70, status="graded",
        )
        db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        exam_alerts = [a for a in resp.json()["alerts"] if a["type"] == "exam"]
        assert len(exam_alerts) == 0

    def test_draft_exam_no_alert(self, db_session, teacher_client, teacher_user, student_user):
        """未发布的考试（draft）不计入预警"""
        classroom, _ = _set_up_classroom_with_student(db_session, teacher_user, student_user)
        exam = Exam(
            classroom_id=classroom.id, teacher_id=teacher_user.id,
            title="草稿考试", total_score=100, status="draft",
        )
        db_session.add(exam)
        db_session.commit()
        db_session.refresh(exam)
        sub = ExamSubmission(
            exam_id=exam.id, student_id=student_user.id,
            score=10, status="graded",
        )
        db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        exam_alerts = [a for a in resp.json()["alerts"] if a["type"] == "exam"]
        assert len(exam_alerts) == 0


# ══════════════════════════════════════════════════════════════
# 多类型预警混合 + 排序
# ══════════════════════════════════════════════════════════════
class TestMultipleAlerts:
    """多类型预警"""

    def test_multiple_alert_types(self, db_session, teacher_client, teacher_user, student_user):
        """一个学生同时触发多种预警"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)

        # 出勤预警：3次签到全缺勤
        for i in range(3):
            session = CheckinSession(classroom_id=classroom.id, teacher_id=teacher_user.id,
                                     type="normal", status="closed")
            db_session.add(session)
            db_session.commit()
            db_session.refresh(session)
            att = Attendance(
                classroom_id=classroom.id, student_id=student_user.id,
                student_record_id=student.id, checkin_session_id=session.id,
                status="absent",
            )
            db_session.add(att)

        # 作业未交预警：3次作业未交
        for i in range(3):
            hw = Homework(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"作业{i}", total_score=100,
                deadline=datetime.now() - timedelta(days=1),
            )
            db_session.add(hw)

        # 考试不及格预警：2次考试不及格
        for i in range(2):
            exam = Exam(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"考试{i}", total_score=100, status="published",
            )
            db_session.add(exam)
            db_session.commit()
            db_session.refresh(exam)
            sub = ExamSubmission(
                exam_id=exam.id, student_id=student_user.id,
                score=40, status="graded",
            )
            db_session.add(sub)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        data = resp.json()
        # 应有 3 种预警
        types = {a["type"] for a in data["alerts"]}
        assert types == {"attendance", "homework", "exam"}
        assert data["total"] == 3
        # high 级别：出勤 0% < 40% → high
        assert data["high"] >= 1

    def test_alerts_sorted_by_level(self, db_session, teacher_client, teacher_user, student_user):
        """预警按级别排序（high 在前）"""
        classroom, student = _set_up_classroom_with_student(db_session, teacher_user, student_user)

        # high: 出勤 0%（3次全缺勤）
        for i in range(3):
            session = CheckinSession(classroom_id=classroom.id, teacher_id=teacher_user.id,
                                     type="normal", status="closed")
            db_session.add(session)
            db_session.commit()
            db_session.refresh(session)
            att = Attendance(
                classroom_id=classroom.id, student_id=student_user.id,
                student_record_id=student.id, checkin_session_id=session.id,
                status="absent",
            )
            db_session.add(att)

        # medium: 作业未交 3 次
        for i in range(3):
            hw = Homework(
                classroom_id=classroom.id, teacher_id=teacher_user.id,
                title=f"作业{i}", total_score=100,
                deadline=datetime.now() - timedelta(days=1),
            )
            db_session.add(hw)
        db_session.commit()

        resp = teacher_client.get("/api/alerts")
        alerts = resp.json()["alerts"]
        # high 应排在 medium 之前
        levels = [a["level"] for a in alerts]
        if "high" in levels and "medium" in levels:
            assert levels.index("high") < levels.index("medium")
