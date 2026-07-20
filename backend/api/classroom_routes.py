import random
import string
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.core.security import get_current_user, assert_teacher_or_admin, assert_owner_or_admin
from backend.models.tables import Classroom, Student, AttentionRecord, ExamRiskRecord, RegisteredPerson, Report, ChatMessage, ClassroomMember
from backend.models.schemas import ClassroomCreate, ClassroomUpdate, ClassroomOut, ClassroomDetail, ClassroomEndOut, PublicClassroomOut, JoinByInviteCode, ClassroomMemberOut, MyClassroomOut

router = APIRouter(prefix="/api/classrooms", tags=["classrooms"])


@router.post("", response_model=ClassroomOut)
def create_classroom(
    data: ClassroomCreate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    assert_teacher_or_admin(current_user)
    teacher_person_id = data.teacher_person_id
    if teacher_person_id is None and current_user.role in ("teacher", "admin"):
        teacher_person_id = current_user.id
    classroom = Classroom(
        name=data.name,
        teacher=data.teacher,
        exam_mode=data.exam_mode,
        teacher_person_id=teacher_person_id,
        course_code=data.course_code,
        is_public=data.is_public,
    )
    db.add(classroom)
    db.commit()
    db.refresh(classroom)
    return classroom


@router.get("", response_model=list[ClassroomOut])
def list_classrooms(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """按角色过滤课堂列表：学生只看参与的，教师只看自己的，admin 看全部"""
    q = db.query(Classroom)
    if current_user.role == "student":
        # 学生：只返回自己参与的课堂
        my_classroom_ids = (
            db.query(Student.classroom_id)
            .filter(Student.person_id == current_user.id)
            .subquery()
        )
        q = q.filter(Classroom.id.in_(my_classroom_ids))
    elif current_user.role == "teacher":
        # 教师：只返回自己创建的课堂
        q = q.filter(Classroom.teacher_person_id == current_user.id)
    # admin: 不加过滤
    return q.order_by(Classroom.started_at.desc()).all()


@router.get("/{classroom_id}", response_model=ClassroomDetail)
def get_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 访问权限：学生只能访问自己参与的课堂
    if current_user.role == "student":
        enrolled = db.query(Student).filter(
            Student.classroom_id == classroom_id,
            Student.person_id == current_user.id,
        ).first()
        if not enrolled:
            raise HTTPException(403, "你未参与该课堂")
    # 教师只能访问自己的课堂
    elif current_user.role == "teacher":
        if classroom.teacher_person_id != current_user.id:
            raise HTTPException(403, "你无权查看该课堂")

    records = db.query(AttentionRecord).filter(
        AttentionRecord.classroom_id == classroom_id
    ).all()

    student_ids = db.query(func.distinct(AttentionRecord.student_id)).filter(
        AttentionRecord.classroom_id == classroom_id
    ).all()

    head_down_count = 0
    head_turn_count = 0
    fatigue_count = 0
    for (sid,) in student_ids:
        student_records = [r for r in records if r.student_id == sid]
        if any(abs(r.pitch) > 15 for r in student_records):
            head_down_count += 1
        if any(abs(r.yaw) > 20 for r in student_records):
            head_turn_count += 1
        if any(r.is_blinking for r in student_records):
            fatigue_count += 1

    high = sum(1 for r in records if r.attention_score >= 60)
    medium = sum(1 for r in records if 30 <= r.attention_score < 60)
    low = sum(1 for r in records if r.attention_score < 30)

    stats = {
        "head_down_count": head_down_count,
        "head_turn_count": head_turn_count,
        "fatigue_count": fatigue_count,
        "attention_distribution": {"high": high, "medium": medium, "low": low},
    }

    if classroom.exam_mode:
        risk_counts = (
            db.query(ExamRiskRecord.risk_level, func.count())
            .filter(ExamRiskRecord.classroom_id == classroom_id)
            .group_by(ExamRiskRecord.risk_level)
            .all()
        )
        stats["risk_distribution"] = {level: count for level, count in risk_counts}

    classroom.stats = stats
    # 获取教师姓名
    teacher_name = classroom.teacher
    if classroom.teacher_person_id:
        person = db.query(RegisteredPerson).filter(RegisteredPerson.id == classroom.teacher_person_id).first()
        if person:
            teacher_name = person.name
    classroom.teacher_person_name = teacher_name
    return classroom


@router.put("/{classroom_id}", response_model=ClassroomOut)
def update_classroom(
    classroom_id: int,
    data: ClassroomUpdate,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """编辑课堂（创建者或管理员）"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_owner_or_admin(classroom.teacher_person_id, current_user)

    if data.name is not None:
        classroom.name = data.name
    if data.teacher is not None:
        classroom.teacher = data.teacher
    if data.exam_mode is not None:
        classroom.exam_mode = data.exam_mode
    if data.teacher_person_id is not None:
        classroom.teacher_person_id = data.teacher_person_id
    if data.course_code is not None:
        classroom.course_code = data.course_code
    if data.is_public is not None:
        classroom.is_public = data.is_public

    db.commit()
    db.refresh(classroom)
    return classroom


@router.delete("/{classroom_id}")
def delete_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """删除课堂（创建者或管理员）级联删除关联数据"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    assert_owner_or_admin(classroom.teacher_person_id, current_user)

    db.query(AttentionRecord).filter(AttentionRecord.classroom_id == classroom_id).delete()
    db.query(ExamRiskRecord).filter(ExamRiskRecord.classroom_id == classroom_id).delete()
    db.query(ChatMessage).filter(ChatMessage.classroom_id == classroom_id).delete()
    db.query(Report).filter(Report.classroom_id == classroom_id).delete()
    db.query(Student).filter(Student.classroom_id == classroom_id).delete()
    db.delete(classroom)
    db.commit()
    return {"message": "课堂已删除"}


@router.put("/{classroom_id}/end", response_model=ClassroomEndOut)
def end_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    if classroom.ended_at:
        raise HTTPException(400, "课堂已结束")

    classroom.ended_at = datetime.now()
    if classroom.started_at:
        classroom.duration = int((classroom.ended_at - classroom.started_at).total_seconds() / 60)

    avg = db.query(func.avg(AttentionRecord.attention_score)).filter(
        AttentionRecord.classroom_id == classroom_id
    ).scalar()
    classroom.avg_attention = round(avg or 0, 1)

    classroom.total_students = db.query(Student).filter(
        Student.classroom_id == classroom_id
    ).count()

    db.commit()
    db.refresh(classroom)
    return classroom


# ===================== 课堂加入相关端点 =====================


@router.get("/my", response_model=list[MyClassroomOut])
def list_my_classrooms(
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """获取当前用户已加入的课堂列表（基于 ClassroomMember 表）"""
    member_rows = (
        db.query(ClassroomMember.classroom_id)
        .filter(ClassroomMember.person_id == current_user.id)
        .subquery()
    )
    classrooms = (
        db.query(Classroom)
        .filter(Classroom.id.in_(member_rows))
        .order_by(Classroom.started_at.desc())
        .all()
    )
    return classrooms


@router.get("/public", response_model=list[PublicClassroomOut])
def list_public_classrooms(
    search: str | None = None,
    db: Session = Depends(get_db),
):
    """搜索公开课堂列表，支持按 name 或 course_code 搜索"""
    q = db.query(Classroom).filter(Classroom.is_public == True)
    if search:
        keyword = f"%{search}%"
        q = q.filter(or_(Classroom.name.ilike(keyword), Classroom.course_code.ilike(keyword)))
    return q.order_by(Classroom.started_at.desc()).all()


@router.post("/join", response_model=ClassroomMemberOut)
def join_by_invite_code(
    data: JoinByInviteCode,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """通过邀请码加入课堂"""
    classroom = db.query(Classroom).filter(Classroom.invite_code == data.invite_code).first()
    if not classroom:
        raise HTTPException(404, "邀请码无效，未找到对应课堂")

    # 检查是否已加入
    existing = db.query(ClassroomMember).filter(
        ClassroomMember.classroom_id == classroom.id,
        ClassroomMember.person_id == current_user.id,
    ).first()
    if existing:
        raise HTTPException(400, "你已加入该课堂")

    member = ClassroomMember(classroom_id=classroom.id, person_id=current_user.id)
    db.add(member)

    # 同步创建 Student 记录，使 CV 检测能跟踪该学生
    existing_student = db.query(Student).filter(
        Student.classroom_id == classroom.id,
        Student.person_id == current_user.id,
    ).first()
    if not existing_student:
        # 分配一个不冲突的 track_id（取当前课堂最大 track_id + 1）
        max_track = db.query(func.max(Student.track_id)).filter(
            Student.classroom_id == classroom.id
        ).scalar() or 0
        student = Student(
            classroom_id=classroom.id,
            track_id=max_track + 1,
            person_id=current_user.id,
            name=current_user.name,
        )
        db.add(student)

    db.commit()
    db.refresh(member)
    return member


@router.post("/join/{classroom_id}", response_model=ClassroomMemberOut)
def join_public_classroom(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """直接加入公开课堂"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")
    if not classroom.is_public:
        raise HTTPException(403, "该课堂不是公开课堂，无法直接加入")

    # 检查是否已加入
    existing = db.query(ClassroomMember).filter(
        ClassroomMember.classroom_id == classroom_id,
        ClassroomMember.person_id == current_user.id,
    ).first()
    if existing:
        raise HTTPException(400, "你已加入该课堂")

    member = ClassroomMember(classroom_id=classroom_id, person_id=current_user.id)
    db.add(member)

    # 同步创建 Student 记录
    existing_student = db.query(Student).filter(
        Student.classroom_id == classroom_id,
        Student.person_id == current_user.id,
    ).first()
    if not existing_student:
        max_track = db.query(func.max(Student.track_id)).filter(
            Student.classroom_id == classroom_id
        ).scalar() or 0
        student = Student(
            classroom_id=classroom_id,
            track_id=max_track + 1,
            person_id=current_user.id,
            name=current_user.name,
        )
        db.add(student)

    db.commit()
    db.refresh(member)
    return member


@router.post("/{classroom_id}/generate-invite")
def generate_invite_code(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """生成邀请码：管理员可生成任何课堂，教师只能生成自己课堂的邀请码"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 权限检查
    if current_user.role == "admin":
        pass
    elif current_user.role == "teacher":
        if classroom.teacher_person_id != current_user.id:
            raise HTTPException(403, "你无权为该课堂生成邀请码")
    else:
        raise HTTPException(403, "仅教师或管理员可生成邀请码")

    if classroom.invite_code:
        raise HTTPException(400, "该课堂已存在邀请码，不可再次生成")

    # 生成13位随机邀请码（数字+小写+大写字母），确保唯一
    chars = string.ascii_letters + string.digits
    for _ in range(100):
        code = "".join(random.choices(chars, k=13))
        if not db.query(Classroom).filter(Classroom.invite_code == code).first():
            break
    else:
        raise HTTPException(500, "邀请码生成失败，请重试")

    classroom.invite_code = code
    db.commit()
    db.refresh(classroom)
    return {"invite_code": classroom.invite_code}


@router.get("/{classroom_id}/invite-code")
def get_invite_code(
    classroom_id: int,
    current_user: RegisteredPerson = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """查看邀请码：管理员可查看所有课堂，教师只能查看自己课堂的邀请码"""
    classroom = db.query(Classroom).filter(Classroom.id == classroom_id).first()
    if not classroom:
        raise HTTPException(404, "课堂不存在")

    # 权限检查
    if current_user.role == "admin":
        pass
    elif current_user.role == "teacher":
        if classroom.teacher_person_id != current_user.id:
            raise HTTPException(403, "你无权查看该课堂邀请码")
    else:
        raise HTTPException(403, "仅教师或管理员可查看邀请码")

    if not classroom.invite_code:
        raise HTTPException(404, "该课堂尚未生成邀请码")

    return {"invite_code": classroom.invite_code}
