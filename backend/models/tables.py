from datetime import datetime

from sqlalchemy import Integer, String, Float, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.database import Base


class Classroom(Base):
    __tablename__ = "classroom"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    teacher: Mapped[str] = mapped_column(String(50))
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    duration: Mapped[int] = mapped_column(Integer, default=0)
    avg_attention: Mapped[float] = mapped_column(Float, default=0)
    total_students: Mapped[int] = mapped_column(Integer, default=0)
    exam_mode: Mapped[bool] = mapped_column(Boolean, default=False)
    teacher_person_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True)

    students: Mapped[list["Student"]] = relationship(back_populates="classroom")
    records: Mapped[list["AttentionRecord"]] = relationship(back_populates="classroom")
    report: Mapped["Report | None"] = relationship(back_populates="classroom", uselist=False)
    exam_risk_records: Mapped[list["ExamRiskRecord"]] = relationship(back_populates="classroom")
    chat_messages: Mapped[list["ChatMessage"]] = relationship(back_populates="classroom")
    teacher_person: Mapped["RegisteredPerson | None"] = relationship(back_populates="classrooms_as_teacher")


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"))
    track_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    person_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True)

    classroom: Mapped["Classroom"] = relationship(back_populates="students")
    records: Mapped[list["AttentionRecord"]] = relationship(back_populates="student")
    exam_risk_records: Mapped[list["ExamRiskRecord"]] = relationship(back_populates="student")
    person: Mapped["RegisteredPerson | None"] = relationship(back_populates="students")


class AttentionRecord(Base):
    __tablename__ = "attention_record"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"))
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    attention_score: Mapped[float] = mapped_column(Float)
    pitch: Mapped[float] = mapped_column(Float, default=0)
    yaw: Mapped[float] = mapped_column(Float, default=0)
    roll: Mapped[float] = mapped_column(Float, default=0)
    ear: Mapped[float] = mapped_column(Float, default=0)
    is_blinking: Mapped[bool] = mapped_column(Boolean, default=False)
    blink_count: Mapped[int] = mapped_column(Integer, default=0)
    gaze_score: Mapped[float] = mapped_column(Float, default=0)
    pose_score: Mapped[float] = mapped_column(Float, default=0)
    fatigue_score: Mapped[float] = mapped_column(Float, default=0)

    student: Mapped["Student"] = relationship(back_populates="records")
    classroom: Mapped["Classroom"] = relationship(back_populates="records")


class ExamRiskRecord(Base):
    __tablename__ = "exam_risk_record"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"))
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    risk_level: Mapped[str] = mapped_column(String(10))
    gaze_deviation_duration: Mapped[float] = mapped_column(Float, default=0)
    head_down_duration: Mapped[float] = mapped_column(Float, default=0)
    head_turn_events: Mapped[int] = mapped_column(Integer, default=0)
    cheating_object_nearby: Mapped[bool] = mapped_column(Boolean, default=False)
    attention_score: Mapped[float] = mapped_column(Float, default=0)

    student: Mapped["Student"] = relationship(back_populates="exam_risk_records")
    classroom: Mapped["Classroom"] = relationship(back_populates="exam_risk_records")


class Report(Base):
    __tablename__ = "report"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), unique=True)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship(back_populates="report")


class ChatMessage(Base):
    __tablename__ = "chat_message"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"))
    role: Mapped[str] = mapped_column(String(10))  # "user" or "assistant"
    content: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship(back_populates="chat_messages")


class RegisteredPerson(Base):
    """注册人员表（学生和老师共用）"""
    __tablename__ = "registered_person"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(10))  # "student" or "teacher"
    face_embedding: Mapped[str] = mapped_column(Text)  # JSON存储512维特征向量
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    students: Mapped[list["Student"]] = relationship(back_populates="person")
    classrooms_as_teacher: Mapped[list["Classroom"]] = relationship(back_populates="teacher_person")


class KnowledgeDocument(Base):
    """知识库文档表"""
    __tablename__ = "knowledge_document"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(String(500))  # 存储路径
    file_type: Mapped[str] = mapped_column(String(20))  # "pdf", "txt", "md"
    total_chunks: Mapped[int] = mapped_column(Integer, default=0)
    indexed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    chunks: Mapped[list["KnowledgeChunk"]] = relationship(back_populates="document")


class KnowledgeChunk(Base):
    """知识库文本块表"""
    __tablename__ = "knowledge_chunk"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("knowledge_document.id"))
    chunk_index: Mapped[int] = mapped_column(Integer)  # 在文档中的顺序
    content: Mapped[str] = mapped_column(Text)  # 文本内容
    embedding_stored: Mapped[bool] = mapped_column(Boolean, default=False)  # 是否已存储到FAISS

    document: Mapped["KnowledgeDocument"] = relationship(back_populates="chunks")
