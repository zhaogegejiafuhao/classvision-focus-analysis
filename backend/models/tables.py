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

    students: Mapped[list["Student"]] = relationship(back_populates="classroom")
    records: Mapped[list["AttentionRecord"]] = relationship(back_populates="classroom")
    report: Mapped["Report | None"] = relationship(back_populates="classroom", uselist=False)


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"))
    track_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    classroom: Mapped["Classroom"] = relationship(back_populates="students")
    records: Mapped[list["AttentionRecord"]] = relationship(back_populates="student")


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


class Report(Base):
    __tablename__ = "report"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), unique=True)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship(back_populates="report")
