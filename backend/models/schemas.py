from datetime import datetime

from pydantic import BaseModel


# --- 课堂 ---
class ClassroomCreate(BaseModel):
    name: str
    teacher: str
    exam_mode: bool = False
    teacher_person_id: int | None = None  # 关联已注册的老师身份


class ClassroomOut(BaseModel):
    id: int
    name: str
    teacher: str
    started_at: datetime
    ended_at: datetime | None = None
    duration: int = 0
    avg_attention: float = 0
    total_students: int = 0
    exam_mode: bool = False
    teacher_person_id: int | None = None

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
    risk_level: str | None = None

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


# --- 对话 ---
class ChatRequest(BaseModel):
    content: str


class ChatMessageOut(BaseModel):
    id: int
    classroom_id: int
    role: str
    content: str
    timestamp: datetime

    model_config = {"from_attributes": True}


# --- 人员注册 ---
class PersonCreate(BaseModel):
    name: str
    role: str  # "student" or "teacher"


class PersonOut(BaseModel):
    id: int
    name: str
    role: str
    created_at: datetime

    model_config = {"from_attributes": True}


class ClassroomWithTeacher(ClassroomDetail):
    teacher_person: PersonOut | None = None


# --- RAG ---
class RAGQueryRequest(BaseModel):
    question: str
    top_k: int = 5


class RetrievedChunk(BaseModel):
    content: str
    score: float
    source: str
    chunk_id: int


class RAGQueryResponse(BaseModel):
    answer: str
    sources: list[str]
    retrieved_chunks: list[RetrievedChunk]


class KnowledgeDocumentOut(BaseModel):
    id: int
    filename: str
    file_type: str
    total_chunks: int
    indexed: bool
    created_at: datetime

    model_config = {"from_attributes": True}
