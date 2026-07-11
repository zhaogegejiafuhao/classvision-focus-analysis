"""人员注册API（人脸点名/身份绑定）"""
import base64
import json
import logging
import numpy as np
from io import BytesIO

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from PIL import Image

from backend.core.database import get_db
from backend.core.security import get_current_user, hash_password
from backend.models.tables import RegisteredPerson, Classroom, Student
from backend.models.schemas import PersonCreate, PersonUpdate, PersonOut, ClassroomWithTeacher
from cv_engine.face_recognizer import recognizer, embedding_to_json, json_to_embedding

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/persons", tags=["person"])


@router.post("/register", response_model=PersonOut)
def register_person(
    name: str = Form(...),
    role: str = Form(...),  # "student" or "teacher"
    image_data: str = Form(None),  # Base64编码的图像数据
    file: UploadFile = File(None),  # 上传的图像文件
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    注册人员（上传人脸照片+姓名）

    支持两种上传方式：
    1. Base64编码的图像数据（前端摄像头捕获）
    2. 上传的图像文件
    """
    _assert_register_permission(role, current_user)

    # 校验角色
    if role not in ("student", "teacher"):
        raise HTTPException(400, "角色必须是 student 或 teacher")

    # 获取图像
    frame = None
    if image_data:
        try:
            img_bytes = base64.b64decode(image_data)
            pil_image = Image.open(BytesIO(img_bytes))
            frame = np.array(pil_image)
            # PIL是RGB，转BGR
            frame = frame[:, :, ::-1].copy()
        except Exception as e:
            raise HTTPException(400, f"无效的图像数据: {e}")
    elif file:
        try:
            pil_image = Image.open(BytesIO(file.file.read()))
            frame = np.array(pil_image)
            frame = frame[:, :, ::-1].copy()
        except Exception as e:
            raise HTTPException(400, f"无效的图像文件: {e}")
    else:
        raise HTTPException(400, "请提供图像数据或上传图像文件")

    # 提取人脸特征
    embedding = recognizer.extract_embedding(frame)
    if embedding is None:
        raise HTTPException(400, "未检测到人脸，请确保照片中包含清晰的人脸")

    # 检查是否已注册（相似度阈值0.6，避免重复注册）
    existing_persons = db.query(RegisteredPerson).all()
    for person in existing_persons:
        existing_emb = json_to_embedding(person.face_embedding)
        similarity = recognizer.compute_similarity(embedding, existing_emb)
        if similarity >= 0.6:
            raise HTTPException(400, f"该人脸已注册为 {person.name}，请勿重复注册")

    # 存储到数据库
    new_person = RegisteredPerson(
        name=name,
        role=role,
        face_embedding=embedding_to_json(embedding),
    )
    db.add(new_person)
    db.commit()
    db.refresh(new_person)

    return new_person


def _assert_register_permission(target_role: str, current_user: RegisteredPerson):
    """注册权限：admin 可注册学生和老师，teacher 只能注册学生"""
    if current_user.role == "admin":
        return
    if current_user.role == "teacher" and target_role == "student":
        return
    raise HTTPException(403, "无权注册该角色的人员")


@router.get("", response_model=list[PersonOut])
def list_persons(
    role: str = None,  # 可选过滤
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取已注册人员列表"""
    query = db.query(RegisteredPerson)
    if role:
        query = query.filter(RegisteredPerson.role == role)
    if current_user.role == "teacher":
        query = query.filter(RegisteredPerson.role == "student")
    return query.order_by(RegisteredPerson.created_at.desc()).all()


@router.get("/{person_id}", response_model=PersonOut)
def get_person(
    person_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取单个人员信息"""
    person = db.query(RegisteredPerson).filter(RegisteredPerson.id == person_id).first()
    if not person:
        raise HTTPException(404, "人员不存在")
    return person


@router.put("/{person_id}", response_model=PersonOut)
def update_person(
    person_id: int,
    data: PersonUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """编辑人员信息（admin 可编辑所有，teacher 只能编辑学生）"""
    person = db.query(RegisteredPerson).filter(RegisteredPerson.id == person_id).first()
    if not person:
        raise HTTPException(404, "人员不存在")

    if current_user.role == "admin":
        pass
    elif current_user.role == "teacher" and person.role == "student":
        pass
    else:
        raise HTTPException(403, "无权编辑该人员")

    if data.name is not None:
        person.name = data.name
    if data.username is not None:
        existing = db.query(RegisteredPerson).filter(
            RegisteredPerson.username == data.username,
            RegisteredPerson.id != person_id,
        ).first()
        if existing:
            raise HTTPException(400, "用户名已被占用")
        person.username = data.username
    if data.password is not None:
        person.password_hash = hash_password(data.password)

    db.commit()
    db.refresh(person)
    return person


@router.delete("/{person_id}")
def delete_person(
    person_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除已注册人员（admin 可删除所有，teacher 只能删除学生）"""
    person = db.query(RegisteredPerson).filter(RegisteredPerson.id == person_id).first()
    if not person:
        raise HTTPException(404, "人员不存在")

    if current_user.role == "admin":
        pass
    elif current_user.role == "teacher" and person.role == "student":
        pass
    else:
        raise HTTPException(403, "无权删除该人员")

    # 检查是否关联了课堂或学生
    classrooms = db.query(Classroom).filter(Classroom.teacher_person_id == person_id).all()
    students = db.query(Student).filter(Student.person_id == person_id).all()

    if classrooms or students:
        raise HTTPException(400, "该人员已关联课堂或学生，请先解除关联")

    db.delete(person)
    db.commit()
    return {"message": "删除成功"}


@router.post("/match")
def match_face_in_frame(
    image_data: str,  # Base64编码的图像
    role: str = None,  # 可选，只匹配特定角色
    threshold: float = 0.5,
    db: Session = Depends(get_db),
):
    """
    在图像中识别已注册人员

    返回匹配结果列表：[(person_id, name, similarity), ...]
    """
    # 解码图像
    try:
        img_bytes = base64.b64decode(image_data)
        pil_image = Image.open(BytesIO(img_bytes))
        frame = np.array(pil_image)[:, :, ::-1].copy()
    except Exception as e:
        raise HTTPException(400, f"无效的图像数据: {e}")

    # 提取人脸特征
    embedding = recognizer.extract_embedding(frame)
    if embedding is None:
        return {"matches": [], "message": "未检测到人脸"}

    # 加载已注册人脸库
    query = db.query(RegisteredPerson)
    if role:
        query = query.filter(RegisteredPerson.role == role)

    persons = query.all()
    registered_embeddings = [
        (p.id, p.name, json_to_embedding(p.face_embedding))
        for p in persons
    ]

    # 匹配
    matches = []
    for person_id, name, reg_emb in registered_embeddings:
        similarity = recognizer.compute_similarity(embedding, reg_emb)
        if similarity >= threshold:
            matches.append({
                "person_id": person_id,
                "name": name,
                "similarity": round(similarity, 3),
            })

    # 按相似度排序
    matches.sort(key=lambda m: m["similarity"], reverse=True)

    return {"matches": matches[:3]}  # 返回前3个匹配结果


@router.post("/batch-match")
def batch_match_faces(
    image_data: str,  # Base64编码的图像
    role: str = "student",
    threshold: float = 0.5,
    db: Session = Depends(get_db),
):
    """
    批量识别图像中的多个人员（用于课堂点名）

    返回所有检测到的人脸及其匹配结果
    """
    # 解码图像
    try:
        img_bytes = base64.b64decode(image_data)
        pil_image = Image.open(BytesIO(img_bytes))
        frame = np.array(pil_image)[:, :, ::-1].copy()
    except Exception as e:
        raise HTTPException(400, f"无效的图像数据: {e}")

    # 使用 InsightFace 检测所有人脸
    faces = recognizer.app.get(frame)

    # 加载已注册人脸库
    query = db.query(RegisteredPerson).filter(RegisteredPerson.role == role)
    persons = query.all()
    registered_embeddings = [
        (p.id, p.name, json_to_embedding(p.face_embedding))
        for p in persons
    ]

    results = []
    for face in faces:
        embedding = face.embedding
        bbox = face.bbox.astype(int).tolist()

        # 匹配
        best_match = None
        best_score = 0.0
        for person_id, name, reg_emb in registered_embeddings:
            similarity = recognizer.compute_similarity(embedding, reg_emb)
            if similarity > best_score and similarity >= threshold:
                best_score = similarity
                best_match = {
                    "person_id": person_id,
                    "name": name,
                    "similarity": round(similarity, 3),
                }

        results.append({
            "bbox": bbox,
            "match": best_match,
        })

    return {"faces": results, "total_faces": len(results)}