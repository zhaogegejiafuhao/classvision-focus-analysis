from datetime import datetime

from pydantic import BaseModel


# --- 课堂 ---
class ClassroomCreate(BaseModel):
    name: str
    teacher: str
    exam_mode: bool = False
    teacher_person_id: int | None = None  # 关联已注册的老师身份


class ClassroomUpdate(BaseModel):
    name: str | None = None
    teacher: str | None = None
    exam_mode: bool | None = None
    teacher_person_id: int | None = None


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
    teacher_person_name: str | None = None


class ClassroomEndOut(ClassroomOut):
    pass


# --- 学生 ---
class StudentCreate(BaseModel):
    classroom_id: int
    track_id: int
    name: str | None = None
    person_id: int | None = None


class StudentUpdate(BaseModel):
    name: str | None = None
    person_id: int | None = None


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


class PersonUpdate(BaseModel):
    name: str | None = None
    username: str | None = None
    password: str | None = None


class PersonOut(BaseModel):
    id: int
    name: str
    role: str
    username: str | None = None
    employee_id: str | None = None
    phone: str | None = None
    department_id: int | None = None
    department_name: str | None = None
    id_card: str | None = None
    major: str | None = None
    email: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


class DepartmentOut(BaseModel):
    id: int
    name: str
    type: str = "class"
    member_count: int = 0
    created_at: datetime

    model_config = {"from_attributes": True}


class ImportResultRow(BaseModel):
    row: int
    employee_id: str = ""
    name: str = ""
    error: str = ""


class ImportResult(BaseModel):
    total: int
    success: int
    failed: int
    errors: list[ImportResultRow] = []


# --- 认证 ---
class LoginRequest(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    role: str
    username: str | None = None

    model_config = {"from_attributes": True}


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


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
    uploaded_by: int | None = None
    uploader_name: str | None = None
    visibility: str = "private"

    model_config = {"from_attributes": True}


# --- OJ 判题 ---
class OjProblemOut(BaseModel):
    id: int
    title: str
    difficulty: str
    time_limit: int
    memory_limit: int
    submitted_count: int = 0
    accepted_count: int = 0
    created_by: int | None = None

    model_config = {"from_attributes": True}


class OjTestCaseOut(BaseModel):
    id: int
    input: str
    expected_output: str
    is_sample: bool

    model_config = {"from_attributes": True}


class OjTestCaseCreate(BaseModel):
    input: str
    expected_output: str
    is_sample: bool = False


class OjProblemCreate(BaseModel):
    title: str
    description: str
    input_format: str = ""
    output_format: str = ""
    sample_input: str = ""
    sample_output: str = ""
    hint: str = ""
    time_limit: int = 1000
    memory_limit: int = 256 * 1024 * 1024
    difficulty: str = "简单"
    test_cases: list[OjTestCaseCreate] = []


class OjProblemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    input_format: str | None = None
    output_format: str | None = None
    sample_input: str | None = None
    sample_output: str | None = None
    hint: str | None = None
    time_limit: int | None = None
    memory_limit: int | None = None
    difficulty: str | None = None
    test_cases: list[OjTestCaseCreate] | None = None


class OjProblemDetail(BaseModel):
    id: int
    title: str
    description: str
    input_format: str
    output_format: str
    sample_input: str
    sample_output: str
    hint: str
    time_limit: int
    memory_limit: int
    difficulty: str
    created_by: int | None = None
    sample_test_cases: list[OjTestCaseOut] = []

    model_config = {"from_attributes": True}


class OjSubmissionCreate(BaseModel):
    problem_id: int
    language: str = "cpp"
    source_code: str


class OjSubmissionOut(BaseModel):
    id: int
    problem_id: int
    problem_title: str = ""
    language: str
    status: str
    cpu_time: int
    memory: int
    error_message: str = ""
    source_code: str = ""
    submitted_at: datetime

    model_config = {"from_attributes": True}


# --- 考试风险记录 ---
class ExamRiskOut(BaseModel):
    id: int
    student_id: int
    student_name: str = ""
    risk_level: str
    gaze_deviation_duration: float = 0
    head_down_duration: float = 0
    head_turn_events: int = 0
    cheating_object_nearby: bool = False
    attention_score: float = 0
    timestamp: datetime

    model_config = {"from_attributes": True}


# --- 学生个人报告 ---
class StudentClassroomAttention(BaseModel):
    """学生在某课堂的注意力数据"""
    classroom_id: int
    classroom_name: str
    teacher: str
    avg_attention: float
    head_down_count: int
    blink_count: int
    duration: int = 0
    started_at: datetime | None = None
    timeline: list[TimelinePoint] = []


class StudentPersonalReport(BaseModel):
    """学生个人注意力报告"""
    student_name: str
    total_classrooms: int
    overall_avg_attention: float
    best_classroom: str
    worst_classroom: str
    classrooms: list[StudentClassroomAttention]
