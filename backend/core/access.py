"""访问控制工具：课堂权限校验与 RAG 文档可见性过滤。

从 stats_routes / rag_routes 抽取的公共函数，消除 chat_routes 跨文件
import 其他路由模块私有函数（带下划线）的耦合。
"""
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models.tables import Classroom, Student, RegisteredPerson, KnowledgeDocument


def assert_classroom_access(
    classroom: Classroom,
    current_user: RegisteredPerson,
    db: Session,
    teacher_only: bool = False,
) -> None:
    """校验用户是否有权访问该课堂

    - admin: 始终通过
    - teacher: 仅自己创建的课堂
    - student: teacher_only=True 时拒绝；否则需为该课堂成员
    """
    if current_user.role == "admin":
        return
    if current_user.role == "teacher":
        if classroom.teacher_person_id != current_user.id:
            raise HTTPException(403, "无权访问该课堂")
        return
    if teacher_only or current_user.role != "student":
        raise HTTPException(403, "无权访问该课堂")
    # 学生需为该课堂成员
    is_member = db.query(Student).filter(
        Student.classroom_id == classroom.id,
        Student.person_id == current_user.id,
    ).first() is not None
    if not is_member:
        raise HTTPException(403, "无权访问该课堂")


def filter_visible_docs(query, current_user: RegisteredPerson):
    """按当前用户角色和可见性过滤 RAG 文档查询"""
    if current_user.role == "admin":
        return query  # admin 可见所有
    if current_user.role == "teacher":
        # 教师：public + staff + 自己的 private
        return query.filter(
            ((KnowledgeDocument.visibility == "public") |
             (KnowledgeDocument.visibility == "staff") |
             (KnowledgeDocument.uploaded_by == current_user.id))
        )
    # student：public + 自己的 private
    return query.filter(
        ((KnowledgeDocument.visibility == "public") |
         (KnowledgeDocument.uploaded_by == current_user.id))
    )


def visible_doc_ids(db: Session, current_user: RegisteredPerson) -> set[int]:
    """获取当前用户可见的文档ID集合"""
    q = db.query(KnowledgeDocument.id)
    q = filter_visible_docs(q, current_user)
    return {row[0] for row in q.all()}
