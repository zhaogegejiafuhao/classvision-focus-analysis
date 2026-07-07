from datetime import datetime

from pydantic import BaseModel


# --- 课堂 ---
class ClassroomCreate(BaseModel):
    name: str
    teacher: str


class ClassroomOut(BaseModel):
    id: int
    name: str
    teacher: str
    started_at: datetime
    ended_at: datetime | None = None
    duration: int = 0
    avg_attention: float = 0
    total_students: int = 0

    model_config = {"from_attributes": True}


class ClassroomDetail(ClassroomOut):
    stats: dict | None = None


class ClassroomEndOut(ClassroomOut):
    pass


# --- 学生 ---
class StudentOut(BaseModel):
    id: int
    track_id: int
    name: str | None = None
    avg_attention: float = 0
    head_down_count: int = 0
    blink_count: int = 0

    model_config = {"from_attributes": True}


# --- 注意力时间线 ---
class TimelinePoint(BaseModel):
    timestamp: str
    avg_attention: float
    student_count: int


# --- 报告 ---
class ReportOut(BaseModel):
    id: int
    classroom_id: int
    content: str
    created_at: datetime

    model_config = {"from_attributes": True}
