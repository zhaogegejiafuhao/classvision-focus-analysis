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


# --- 试卷扫描 ---

class QuestionRegionIn(BaseModel):
    question_index: int
    question_type: str  # "objective" | "subjective"
    x: float
    y: float
    w: float
    h: float
    max_score: float
    standard_answer: str


class PaperTemplateCreate(BaseModel):
    name: str
    classroom_id: int | None = None
    questions: list[QuestionRegionIn]


class QuestionRegionOut(BaseModel):
    question_index: int
    question_type: str
    x: float
    y: float
    w: float
    h: float
    max_score: float
    standard_answer: str


class PaperTemplateOut(BaseModel):
    id: int
    name: str
    classroom_id: int | None = None
    question_count: int
    total_score: float
    regions_config: str
    created_at: datetime

    model_config = {"from_attributes": True}


class PaperTemplateDetail(PaperTemplateOut):
    questions: list[QuestionRegionOut]


class ScanPaperRequest(BaseModel):
    image_data: str
    template_id: int
    person_id: int | None = None
    student_name: str | None = None
    classroom_id: int | None = None
    grade_subjective: bool = True


class PaperAnswerOut(BaseModel):
    id: int
    paper_id: int
    question_index: int
    question_type: str
    ocr_text: str
    standard_answer: str
    max_score: float
    auto_score: float
    final_score: float | None = None
    ai_suggestion: str | None = None
    correct: bool | None = None

    model_config = {"from_attributes": True}


class PaperOut(BaseModel):
    id: int
    template_id: int
    classroom_id: int | None = None
    person_id: int | None = None
    student_name: str | None = None
    image_path: str | None = None
    corrected_image_path: str | None = None
    total_auto_score: float
    final_score: float | None = None
    status: str
    scanned_at: datetime
    graded_at: datetime | None = None

    model_config = {"from_attributes": True}


class PaperDetail(PaperOut):
    answers: list[PaperAnswerOut] = []
    template_name: str | None = None


class ScanPaperResponse(BaseModel):
    paper_id: int
    corrected_image: str | None = None
    corners: list | None = None
    answers: list[PaperAnswerOut]
    total_auto_score: float


class PaperAnswerUpdate(BaseModel):
    final_score: float
    ai_suggestion: str | None = None
    ocr_text: str | None = None


class PaperFinalScoreUpdate(BaseModel):
    final_score: float


class PaperStatistics(BaseModel):
    template_id: int
    template_name: str
    total_papers: int
    avg_score: float
    max_score: float
    min_score: float
    score_distribution: dict[str, int]
    per_question_accuracy: list[dict]
