"""课件管理 API 集成测试

核心测试点：
- 课件列表的权限过滤（教师只看自己、学生只看所在课堂）
- 上传课件（教师/admin 权限、文件类型校验、大小校验）
- 下载课件（课堂成员权限校验）
- 删除课件（owner/admin 权限）
- 文件扩展名白名单
"""
import io
import os
import shutil
from pathlib import Path

import pytest

from backend.api.material_routes import UPLOAD_DIR
from backend.models.tables import Classroom, Student, CourseMaterial


# ══════════════════════════════════════════════════════════════
# 辅助 fixtures
# ══════════════════════════════════════════════════════════════
@pytest.fixture()
def classroom_with_student(teacher_client, student_client):
    """创建公开课堂并让学生加入"""
    resp = teacher_client.post("/api/classrooms", json={
        "name": "课件测试课堂", "teacher": "张老师", "is_public": True,
    })
    classroom_id = resp.json()["id"]
    student_client.post(f"/api/classrooms/join/{classroom_id}")
    return classroom_id


def _make_file(content: bytes = b"hello world", filename: str = "test.pdf"):
    """构造上传文件对象"""
    return ("file", (filename, io.BytesIO(content), "application/octet-stream"))


def _upload(client, title="测试课件", classroom_id=None, filename="test.pdf", content=b"hello"):
    """上传课件辅助函数"""
    data = {"title": title}
    if classroom_id is not None:
        data["classroom_id"] = str(classroom_id)
    files = [ _make_file(content, filename) ]
    return client.post("/api/materials/upload", data=data, files=files)


def _create_material_record(db_session, teacher_user, classroom_id=None, file_path=None):
    """直接在 DB 中创建课件记录（绕过文件上传）"""
    # 确保文件存在
    if file_path is None:
        file_path = os.path.join(UPLOAD_DIR, "fake_test_file.pdf")
        Path(file_path).write_bytes(b"fake content")

    material = CourseMaterial(
        teacher_id=teacher_user.id,
        classroom_id=classroom_id,
        title="DB直建课件",
        file_path=file_path,
        file_name="record.pdf",
        file_size=100,
        file_type="pdf",
    )
    db_session.add(material)
    db_session.commit()
    db_session.refresh(material)
    return material


# ══════════════════════════════════════════════════════════════
# GET /api/materials
# ══════════════════════════════════════════════════════════════
class TestListMaterials:
    """课件列表"""

    def test_teacher_sees_own(self, db_session, teacher_client, teacher_user):
        """教师只能看到自己上传的课件"""
        _create_material_record(db_session, teacher_user)
        resp = teacher_client.get("/api/materials")
        assert resp.status_code == 200
        items = resp.json()
        assert len(items) >= 1
        assert all(m["title"] == "DB直建课件" for m in items)

    def test_student_sees_only_joined_classroom(
        self, db_session, teacher_client, teacher_user, student_user, student_client,
    ):
        """学生只能看到自己所在课堂的课件"""
        # 教师创建课堂
        classroom = Classroom(name="学生课件测试", teacher="张老师",
                              teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)

        # 学生加入课堂
        student = Student(classroom_id=classroom.id, person_id=student_user.id, track_id=1, name="李同学")
        db_session.add(student)
        db_session.commit()

        # 教师给该课堂上传课件
        _create_material_record(db_session, teacher_user, classroom_id=classroom.id)
        # 教师给其他课堂上传课件（学生看不到）
        other_classroom = Classroom(name="其他课堂", teacher="张老师",
                                    teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(other_classroom)
        db_session.commit()
        db_session.refresh(other_classroom)
        _create_material_record(db_session, teacher_user, classroom_id=other_classroom.id)

        resp = student_client.get("/api/materials")
        assert resp.status_code == 200
        items = resp.json()
        # 只能看到自己课堂的课件
        assert all(m["classroom_id"] == classroom.id for m in items)
        assert len(items) == 1

    def test_student_filter_by_classroom(self, db_session, teacher_user, student_user, student_client):
        """学生按 classroom_id 过滤且必须是成员"""
        classroom = Classroom(name="课件过滤测试", teacher="张老师",
                              teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)

        student = Student(classroom_id=classroom.id, person_id=student_user.id, track_id=1)
        db_session.add(student)
        db_session.commit()
        _create_material_record(db_session, teacher_user, classroom_id=classroom.id)

        resp = student_client.get(f"/api/materials?classroom_id={classroom.id}")
        assert resp.status_code == 200
        assert len(resp.json()) == 1

    def test_student_filter_non_member_forbidden(self, db_session, teacher_user, student_client):
        """学生过滤非成员课堂 → 403"""
        classroom = Classroom(name="非成员课堂", teacher="张老师",
                              teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        resp = student_client.get(f"/api/materials?classroom_id={classroom.id}")
        assert resp.status_code == 403

    def test_admin_sees_all(self, db_session, admin_client, teacher_user, admin_user):
        """管理员能看到所有课件"""
        _create_material_record(db_session, teacher_user)
        _create_material_record(db_session, admin_user)
        resp = admin_client.get("/api/materials")
        assert resp.status_code == 200
        assert len(resp.json()) >= 2


# ══════════════════════════════════════════════════════════════
# POST /api/materials/upload
# ══════════════════════════════════════════════════════════════
class TestUploadMaterial:
    """上传课件"""

    def test_teacher_upload_success(self, teacher_client, classroom_with_student):
        """教师上传课件成功"""
        resp = _upload(teacher_client, title="第一课", classroom_id=classroom_with_student)
        assert resp.status_code == 200
        data = resp.json()
        assert data["title"] == "第一课"
        assert data["file_name"] == "test.pdf"
        assert data["id"] is not None

    def test_student_upload_forbidden(self, student_client, classroom_with_student):
        """学生不能上传 → 403"""
        resp = _upload(student_client, classroom_id=classroom_with_student)
        assert resp.status_code == 403

    def test_invalid_extension(self, teacher_client):
        """不支持的文件类型 → 400"""
        resp = _upload(teacher_client, filename="malware.exe")
        assert resp.status_code == 400
        assert "不支持的文件类型" in resp.json()["detail"]

    def test_admin_can_upload(self, admin_client):
        """管理员可以上传课件"""
        resp = _upload(admin_client, title="管理员课件")
        assert resp.status_code == 200

    def test_upload_without_classroom(self, teacher_client):
        """不上传到指定课堂也能成功"""
        resp = _upload(teacher_client, title="无课堂课件")
        assert resp.status_code == 200


# ══════════════════════════════════════════════════════════════
# GET /api/materials/{id}/download
# ══════════════════════════════════════════════════════════════
class TestDownloadMaterial:
    """下载课件"""

    def test_owner_download_success(self, db_session, teacher_client, teacher_user):
        """上传者可以下载自己的课件"""
        material = _create_material_record(db_session, teacher_user)
        resp = teacher_client.get(f"/api/materials/{material.id}/download")
        assert resp.status_code == 200
        assert resp.content == b"fake content"

    def test_nonexistent_material(self, teacher_client):
        """不存在的课件 → 404"""
        resp = teacher_client.get("/api/materials/99999/download")
        assert resp.status_code == 404

    def test_student_member_download(self, db_session, teacher_user, student_user, student_client):
        """课堂成员学生可以下载"""
        classroom = Classroom(name="下载测试", teacher="张老师",
                              teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)
        student = Student(classroom_id=classroom.id, person_id=student_user.id, track_id=1)
        db_session.add(student)
        db_session.commit()

        material = _create_material_record(db_session, teacher_user, classroom_id=classroom.id)
        resp = student_client.get(f"/api/materials/{material.id}/download")
        assert resp.status_code == 200

    def test_student_non_member_download_forbidden(self, db_session, teacher_user, student_client):
        """非成员学生不能下载 → 403"""
        classroom = Classroom(name="他人课堂", teacher="张老师",
                              teacher_person_id=teacher_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)
        material = _create_material_record(db_session, teacher_user, classroom_id=classroom.id)
        resp = student_client.get(f"/api/materials/{material.id}/download")
        assert resp.status_code == 403

    def test_other_teacher_download_forbidden(self, db_session, teacher_client, teacher_user, admin_user):
        """非创建者教师不能下载他课堂的课件 → 403"""
        classroom = Classroom(name="admin课堂", teacher="管理员",
                              teacher_person_id=admin_user.id, is_public=True)
        db_session.add(classroom)
        db_session.commit()
        db_session.refresh(classroom)
        material = _create_material_record(db_session, admin_user, classroom_id=classroom.id)
        resp = teacher_client.get(f"/api/materials/{material.id}/download")
        assert resp.status_code == 403

    def test_download_missing_file(self, db_session, teacher_client, teacher_user):
        """文件在磁盘上丢失 → 404"""
        material = _create_material_record(
            db_session, teacher_user, file_path="uploads/materials/nonexistent_file.pdf",
        )
        resp = teacher_client.get(f"/api/materials/{material.id}/download")
        assert resp.status_code == 404
        assert "文件不存在" in resp.json()["detail"]


# ══════════════════════════════════════════════════════════════
# DELETE /api/materials/{id}
# ══════════════════════════════════════════════════════════════
class TestDeleteMaterial:
    """删除课件"""

    def test_owner_delete_success(self, db_session, teacher_client, teacher_user):
        """上传者可以删除自己的课件"""
        material = _create_material_record(db_session, teacher_user)
        resp = teacher_client.delete(f"/api/materials/{material.id}")
        assert resp.status_code == 200
        assert resp.json()["success"] is True
        # 确认 DB 记录已删除
        assert db_session.query(CourseMaterial).filter_by(id=material.id).first() is None

    def test_non_owner_delete_forbidden(self, db_session, teacher_client, admin_user):
        """非上传者教师不能删除 → 403"""
        material = _create_material_record(db_session, admin_user)
        resp = teacher_client.delete(f"/api/materials/{material.id}")
        assert resp.status_code == 403

    def test_student_delete_forbidden(self, db_session, student_client, teacher_user):
        """学生不能删除 → 403"""
        material = _create_material_record(db_session, teacher_user)
        resp = student_client.delete(f"/api/materials/{material.id}")
        assert resp.status_code == 403

    def test_admin_can_delete_any(self, db_session, admin_client, teacher_user):
        """管理员可以删除任何课件"""
        material = _create_material_record(db_session, teacher_user)
        resp = admin_client.delete(f"/api/materials/{material.id}")
        assert resp.status_code == 200

    def test_delete_nonexistent(self, teacher_client):
        """删除不存在的课件 → 404"""
        resp = teacher_client.delete("/api/materials/99999")
        assert resp.status_code == 404

    def test_delete_removes_file(self, db_session, teacher_client, teacher_user, tmp_path):
        """删除课件时同时删除物理文件"""
        # 在临时位置创建文件（但要在 UPLOAD_DIR 内才会被清理）
        file_path = os.path.join(UPLOAD_DIR, "to_delete_test.pdf")
        Path(file_path).write_bytes(b"will be deleted")
        assert os.path.exists(file_path)

        material = _create_material_record(db_session, teacher_user, file_path=file_path)
        resp = teacher_client.delete(f"/api/materials/{material.id}")
        assert resp.status_code == 200
        # 物理文件应被删除
        assert not os.path.exists(file_path)
