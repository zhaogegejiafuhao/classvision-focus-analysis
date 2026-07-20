from datetime import datetime

from pydantic import BaseModel


# --- 课堂 ---
class ClassroomCreate(BaseModel):
    name: str
    teacher: str
    exam_mode: bool = False
    teacher_person_id: int | None = None  # 关联已注册的老师身份
    course_code: str | None = None
    is_public: bool = True


class ClassroomUpdate(BaseModel):
    name: str | None = None
    teacher: str | None = None
    exam_mode: bool | None = None
    teacher_person_id: int | None = None
    course_code: str | None = None
    is_public: bool | None = None


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
    course_code: str | None = None
    is_public: bool = True

    model_config = {"from_attributes": True}


class ClassroomDetail(ClassroomOut):
    stats: dict | None = None
    teacher_person_name: str | None = None


class ClassroomEndOut(ClassroomOut):
    pass


class PublicClassroomOut(BaseModel):
    """公开课堂列表项（课堂加入页面）"""
    id: int
    name: str
    teacher: str
    course_code: str | None = None
    is_public: bool = True
    invite_code: str | None = None
    total_students: int = 0
    teacher_person_id: int | None = None
    teacher_person_name: str | None = None

    model_config = {"from_attributes": True}


class JoinByInviteCode(BaseModel):
    invite_code: str


class MyClassroomOut(BaseModel):
    """已加入课堂列表项"""
    id: int
    name: str
    course_code: str | None = None
    teacher: str = ""
    teacher_person_name: str | None = None

    model_config = {"from_attributes": True}


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
    # mode: "fast"=快速回答（关闭 HyDE/Multi-Query，延迟低）
    #       "deep"=深度思考（启用 HyDE/Multi-Query，检索质量高但延迟大）
    mode: str = "fast"


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


# --- 课堂加入 ---
class JoinByInviteCode(BaseModel):
    invite_code: str


class PublicClassroomOut(BaseModel):
    id: int
    name: str
    teacher: str
    course_code: str | None = None
    started_at: datetime
    teacher_person_id: int | None = None

    model_config = {"from_attributes": True}


class ClassroomMemberOut(BaseModel):
    id: int
    classroom_id: int
    person_id: int
    joined_at: datetime

    model_config = {"from_attributes": True}


# --- AI 智能批改 ---


class AIGradeRequest(BaseModel):
    """AI批改请求"""
    submission_id: int | None = None         # 提交ID（可选，若不传则不持久化）
    question: str                        # 题目文本
    standard_answer: str = ""            # 标准答案/写作要求
    total_score: float = 100.0
    subject_type: str = "math"           # math / essay
    image_base64: str | None = None      # 学生手写图片（可选，用于OCR+几何）
    student_text: str | None = None      # 学生答案文本（可选，优先于submission.content使用）


class AIGradeResponse(BaseModel):
    """AI批改响应"""
    submission_id: int
    suggested_score: float
    max_score: float
    comment: str
    rubric: dict | None = None
    grading: dict | None = None
    model_key: str = "standard"
    confidence: float = 0.85
    grading_method: str = "llm"
    error_type: str | None = None
    error_cause: str | None = None
    knowledge_points: list[str] = []


class GradingResultOut(BaseModel):
    """批改结果输出"""
    id: int
    submission_id: int
    score: float
    max_score: float
    comment: str
    model_key: str
    grading_method: str
    confidence: float
    error_type: str | None = None
    error_cause: str | None = None
    knowledge_points: list[str] = []
    confirmed: bool = False
    confirmed_score: float | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


class GradeConfirmRequest(BaseModel):
    """教师确认/修正AI批改结果"""
    confirmed_score: float | None = None  # 修正分数（None则确认AI分数）


class KnowledgeAnalysisRequest(BaseModel):
    """知识归因分析请求"""
    student_id: int
    analysis_type: str = "math"  # math / writing


class KnowledgeAnalysisResponse(BaseModel):
    """知识归因分析响应"""
    student_id: int
    analysis_type: str
    radar: dict
    weak_points: list[dict]
    correction_status: dict | None = None


class CorrectionSubmitRequest(BaseModel):
    """订正提交请求"""
    submission_id: int
    corrections: list[dict]  # [{"question_id": "q1", "image_base64": "...", "text": "订正文本答案"}]


class CorrectionComparisonOut(BaseModel):
    """订正前后对比"""
    question_id: str
    original_score: float
    correction_score: float
    max_score: float
    improved: bool
    remaining_errors: list[str] = []
    new_comment: str = ""


class SimilarQuestionRequest(BaseModel):
    """相似题生成请求"""
    question: str
    knowledge_points: list[str] = []
    error_type: str = ""
    tier: str = "中等生"  # 优等生/中等生/学困生
    count: int = 3
    standard_answer: str = ""


class SimilarQuestionResponse(BaseModel):
    """相似题生成响应"""
    questions: list[dict]


# --- 错题本 ---


class MistakeListItem(BaseModel):
    """错题本列表项：从 GradingResult 筛选 error_type 非空的记录"""
    grading_id: int
    submission_id: int
    score: float
    max_score: float
    error_type: str | None = None
    error_cause: str | None = None
    knowledge_points: list[str] = []
    created_at: datetime
    homework_id: int | None = None
    homework_title: str = ""

    model_config = {"from_attributes": True}


class MistakeListResponse(BaseModel):
    """错题本列表分页响应"""
    total: int
    page: int
    page_size: int
    items: list[MistakeListItem]


class MistakeCorrectionRecord(BaseModel):
    """错题详情中嵌入的订正历史项"""
    correction_id: int
    correction_score: float
    original_score: float
    improved: bool
    created_at: datetime


class MistakeDetail(BaseModel):
    """错题详情：聚合原题+批改+订正历史"""
    grading_id: int
    submission_id: int
    homework_id: int | None = None
    homework_title: str = ""
    question_text: str = ""
    standard_answer: str = ""
    student_answer_ocr: str = ""
    rubric: dict | None = None
    grading: dict | None = None
    score: float
    max_score: float
    comment: str = ""
    error_type: str | None = None
    error_cause: str | None = None
    knowledge_points: list[str] = []
    created_at: datetime
    correction_records: list[MistakeCorrectionRecord] = []


# --- 相似题持久化 ---


class GenerateSimilarRequest(BaseModel):
    """从错题一键生成相似题请求"""
    count: int = 3
    tier: str = "中等生"  # 优等生/中等生/学困生，可省略后端自动推断


class SimilarQuestionPersisted(BaseModel):
    """已持久化的相似题"""
    similar_id: int
    student_id: int
    source_grading_id: int | None = None
    question_text: str
    standard_answer: str = ""
    difficulty: str = "中等"
    variant_type: str = "同类变式"
    tier: str = "中等生"
    mastery_status: str = "pending"
    created_at: datetime

    model_config = {"from_attributes": True}


class SimilarQuestionListResponse(BaseModel):
    """相似题列表分页响应"""
    total: int
    page: int
    page_size: int
    items: list[SimilarQuestionPersisted]
