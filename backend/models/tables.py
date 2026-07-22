from datetime import datetime

from sqlalchemy import Integer, String, Float, Boolean, Text, DateTime, ForeignKey, Index
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
    teacher_person_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True, index=True)
    course_code: Mapped[str | None] = mapped_column(String(50), nullable=True)  # 课序号
    is_public: Mapped[bool] = mapped_column(Boolean, default=True)  # 是否公开（课堂加入页可见）
    invite_code: Mapped[str | None] = mapped_column(String(13), nullable=True, unique=True)  # 邀请码（13位，生成后不可改）

    students: Mapped[list["Student"]] = relationship(back_populates="classroom")
    records: Mapped[list["AttentionRecord"]] = relationship(back_populates="classroom")
    report: Mapped["Report | None"] = relationship(back_populates="classroom", uselist=False)
    exam_risk_records: Mapped[list["ExamRiskRecord"]] = relationship(back_populates="classroom")
    chat_messages: Mapped[list["ChatMessage"]] = relationship(back_populates="classroom")
    teacher_person: Mapped["RegisteredPerson | None"] = relationship(back_populates="classrooms_as_teacher")
    members: Mapped[list["ClassroomMember"]] = relationship(back_populates="classroom")


class ClassroomMember(Base):
    """课堂成员表：记录学生与课堂的加入关系"""
    __tablename__ = "classroom_member"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    joined_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship(back_populates="members")
    person: Mapped["RegisteredPerson"] = relationship(back_populates="classroom_memberships")


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    track_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    person_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True, index=True)

    classroom: Mapped["Classroom"] = relationship(back_populates="students")
    records: Mapped[list["AttentionRecord"]] = relationship(back_populates="student")
    exam_risk_records: Mapped[list["ExamRiskRecord"]] = relationship(back_populates="student")
    person: Mapped["RegisteredPerson | None"] = relationship(back_populates="students")


class AttentionRecord(Base):
    __tablename__ = "attention_record"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"), index=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
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
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"), index=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
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
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    role: Mapped[str] = mapped_column(String(10))  # "user" or "assistant"
    content: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship(back_populates="chat_messages")


class RegisteredPerson(Base):
    """注册人员表（学生和老师共用）"""
    __tablename__ = "registered_person"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(10))  # "student", "teacher", "admin"
    username: Mapped[str | None] = mapped_column(String(50), unique=True, nullable=True)  # 登录用户名
    password_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)  # 密码哈希
    face_embedding: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON存储512维特征向量
    employee_id: Mapped[str | None] = mapped_column(String(50), nullable=True)  # 学号/工号（唯一索引由迁移创建）
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    department_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("department.id"), nullable=True, index=True)
    id_card: Mapped[str | None] = mapped_column(String(20), nullable=True)
    major: Mapped[str | None] = mapped_column(String(100), nullable=True)
    email: Mapped[str | None] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    students: Mapped[list["Student"]] = relationship(back_populates="person")
    classrooms_as_teacher: Mapped[list["Classroom"]] = relationship(back_populates="teacher_person")
    classroom_memberships: Mapped[list["ClassroomMember"]] = relationship(back_populates="person")
    department: Mapped["Department | None"] = relationship(back_populates="members")


class Department(Base):
    """部门/班级表"""
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    type: Mapped[str] = mapped_column(String(20), default="class")  # class(班级)/department(部门)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    members: Mapped[list["RegisteredPerson"]] = relationship(back_populates="department")


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
    uploaded_by: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True, index=True)
    visibility: Mapped[str] = mapped_column(String(20), default="private")  # public/staff/private

    chunks: Mapped[list["KnowledgeChunk"]] = relationship(back_populates="document")
    uploader: Mapped["RegisteredPerson | None"] = relationship()


class KnowledgeChunk(Base):
    """知识库文本块表（支持父子分块）"""
    __tablename__ = "knowledge_chunk"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("knowledge_document.id"), index=True)
    chunk_index: Mapped[int] = mapped_column(Integer)  # 在文档中的顺序
    content: Mapped[str] = mapped_column(Text)  # 文本内容
    embedding_stored: Mapped[bool] = mapped_column(Boolean, default=False)  # 是否已存储到FAISS
    is_parent: Mapped[bool] = mapped_column(Boolean, default=False)  # 是否为父分块
    parent_chunk_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("knowledge_chunk.id"), nullable=True, index=True)  # 子分块指向父分块

    document: Mapped["KnowledgeDocument"] = relationship(back_populates="chunks")
    parent: Mapped["KnowledgeChunk | None"] = relationship(remote_side=[id], backref="children_chunks")


class OjProblem(Base):
    """OJ 题目表"""
    __tablename__ = "oj_problem"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text)
    input_format: Mapped[str] = mapped_column(Text, default="")
    output_format: Mapped[str] = mapped_column(Text, default="")
    sample_input: Mapped[str] = mapped_column(Text, default="")
    sample_output: Mapped[str] = mapped_column(Text, default="")
    hint: Mapped[str] = mapped_column(Text, default="")
    time_limit: Mapped[int] = mapped_column(Integer, default=1000)
    memory_limit: Mapped[int] = mapped_column(Integer, default=256 * 1024 * 1024)
    difficulty: Mapped[str] = mapped_column(String(10), default="简单")
    created_by: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    test_cases: Mapped[list["OjTestCase"]] = relationship(back_populates="problem", cascade="all, delete-orphan")
    submissions: Mapped[list["OjSubmission"]] = relationship(back_populates="problem")
    creator: Mapped["RegisteredPerson | None"] = relationship()


class OjTestCase(Base):
    """OJ 测试用例表"""
    __tablename__ = "oj_test_case"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    problem_id: Mapped[int] = mapped_column(Integer, ForeignKey("oj_problem.id"), index=True)
    input: Mapped[str] = mapped_column(Text)
    expected_output: Mapped[str] = mapped_column(Text)
    is_sample: Mapped[bool] = mapped_column(Boolean, default=False)

    problem: Mapped["OjProblem"] = relationship(back_populates="test_cases")


class OjSubmission(Base):
    """OJ 提交记录表"""
    __tablename__ = "oj_submission"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    problem_id: Mapped[int] = mapped_column(Integer, ForeignKey("oj_problem.id"), index=True)
    language: Mapped[str] = mapped_column(String(10))
    source_code: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="Pending")
    cpu_time: Mapped[int] = mapped_column(Integer, default=0)
    memory: Mapped[int] = mapped_column(Integer, default=0)
    error_message: Mapped[str] = mapped_column(Text, default="")
    submitted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    problem: Mapped["OjProblem"] = relationship(back_populates="submissions")


class RagConversation(Base):
    """RAG 多轮对话会话表"""
    __tablename__ = "rag_conversation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    title: Mapped[str] = mapped_column(String(200), default="新对话")
    state: Mapped[str] = mapped_column(String(20), default="idle")  # idle/querying/clarifying/answering
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    messages: Mapped[list["RagMessage"]] = relationship(back_populates="conversation", order_by="RagMessage.id")


class RagMessage(Base):
    """RAG 对话消息表"""
    __tablename__ = "rag_message"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    conversation_id: Mapped[int] = mapped_column(Integer, ForeignKey("rag_conversation.id"), index=True)
    role: Mapped[str] = mapped_column(String(10))  # "user" or "assistant"
    content: Mapped[str] = mapped_column(Text)
    retrieved_chunks: Mapped[str | None] = mapped_column(Text, default=None)  # JSON 存储检索到的 chunk
    is_followup: Mapped[bool] = mapped_column(Boolean, default=False)  # 是否为追问（不触发新检索）
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    conversation: Mapped["RagConversation"] = relationship(back_populates="messages")


class Notification(Base):
    """消息通知表"""
    __tablename__ = "notification"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    type: Mapped[str] = mapped_column(String(20), default="system")  # system/homework/exam/attendance
    sender_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True, index=True)
    receiver_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("registered_person.id"), nullable=True, index=True)  # NULL表示全体
    classroom_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("classroom.id"), nullable=True, index=True)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    sender: Mapped["RegisteredPerson | None"] = relationship(foreign_keys=[sender_id])
    receiver: Mapped["RegisteredPerson | None"] = relationship(foreign_keys=[receiver_id])
    classroom: Mapped["Classroom | None"] = relationship()


class Attendance(Base):
    """考勤签到表"""
    __tablename__ = "attendance"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("student.id"), index=True)
    checkin_session_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("checkin_session.id"), nullable=True, index=True)
    status: Mapped[str] = mapped_column(String(20), default="present")  # present/absent/late/leave
    checkin_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    checkin_code: Mapped[str | None] = mapped_column(String(10), nullable=True)  # 学生输入的验证码
    note: Mapped[str | None] = mapped_column(String(200), nullable=True)  # 备注
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship()
    student: Mapped["Student"] = relationship()
    checkin_session: Mapped["CheckinSession | None"] = relationship(back_populates="attendances")


class Homework(Base):
    """作业表"""
    __tablename__ = "homework"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    classroom_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("classroom.id"), nullable=True, index=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    deadline: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    total_score: Mapped[float] = mapped_column(Float, default=100.0)
    status: Mapped[str] = mapped_column(String(20), default="open")  # open/closed/archived
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    classroom: Mapped["Classroom | None"] = relationship()
    teacher: Mapped["RegisteredPerson"] = relationship()
    submissions: Mapped[list["HomeworkSubmission"]] = relationship(back_populates="homework")


class HomeworkAttachment(Base):
    """作业附件表"""
    __tablename__ = "homework_attachment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    homework_id: Mapped[int] = mapped_column(Integer, ForeignKey("homework.id"), index=True)
    filename: Mapped[str] = mapped_column(String(200))
    file_path: Mapped[str] = mapped_column(String(500))
    file_size: Mapped[int] = mapped_column(Integer, default=0)

    homework: Mapped["Homework"] = relationship()


class HomeworkSubmission(Base):
    """作业提交表"""
    __tablename__ = "homework_submission"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    homework_id: Mapped[int] = mapped_column(Integer, ForeignKey("homework.id"), index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    content: Mapped[str] = mapped_column(Text, default="")
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    feedback: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(20), default="submitted")  # submitted/graded/returned
    submitted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    graded_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    homework: Mapped["Homework"] = relationship(back_populates="submissions")
    student: Mapped["RegisteredPerson"] = relationship()
    attachments: Mapped[list["SubmissionAttachment"]] = relationship(back_populates="submission")
    grading_results: Mapped[list["GradingResult"]] = relationship(back_populates="submission")


class SubmissionAttachment(Base):
    """提交附件表"""
    __tablename__ = "submission_attachment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(Integer, ForeignKey("homework_submission.id"), index=True)
    filename: Mapped[str] = mapped_column(String(200))
    file_path: Mapped[str] = mapped_column(String(500))
    file_size: Mapped[int] = mapped_column(Integer, default=0)

    submission: Mapped["HomeworkSubmission"] = relationship(back_populates="attachments")


class CheckinSession(Base):
    """签到会话表"""
    __tablename__ = "checkin_session"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    type: Mapped[str] = mapped_column(String(20), default="normal")  # normal/encrypted
    code: Mapped[str | None] = mapped_column(String(6), nullable=True)  # 加密签到的验证码
    status: Mapped[str] = mapped_column(String(20), default="active")  # active/closed
    start_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    classroom: Mapped["Classroom"] = relationship()
    teacher: Mapped["RegisteredPerson"] = relationship()
    attendances: Mapped[list["Attendance"]] = relationship(back_populates="checkin_session")


class Exam(Base):
    """考试表"""
    __tablename__ = "exam"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    classroom_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("classroom.id"), nullable=True, index=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    duration: Mapped[int] = mapped_column(Integer, default=60)  # 考试时长（分钟）
    total_score: Mapped[float] = mapped_column(Float, default=100.0)
    status: Mapped[str] = mapped_column(String(20), default="draft")  # draft/published/closed
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    classroom: Mapped["Classroom | None"] = relationship()
    teacher: Mapped["RegisteredPerson"] = relationship()
    questions: Mapped[list["Question"]] = relationship(back_populates="exam", order_by="Question.order")
    submissions: Mapped[list["ExamSubmission"]] = relationship(back_populates="exam")


class Question(Base):
    """题目表"""
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(Integer, ForeignKey("exam.id"), index=True)
    type: Mapped[str] = mapped_column(String(20))  # single/multi/judge/fill/essay
    content: Mapped[str] = mapped_column(Text)
    options: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON格式选项
    answer: Mapped[str] = mapped_column(Text)  # 正确答案
    score: Mapped[float] = mapped_column(Float, default=10.0)
    order: Mapped[int] = mapped_column(Integer, default=1)

    exam: Mapped["Exam"] = relationship(back_populates="questions")
    answers: Mapped[list["Answer"]] = relationship(back_populates="question")


class ExamSubmission(Base):
    """考试提交表"""
    __tablename__ = "exam_submission"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(Integer, ForeignKey("exam.id"), index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="in_progress")  # in_progress/submitted/graded
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    submitted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    graded_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    exam: Mapped["Exam"] = relationship(back_populates="submissions")
    student: Mapped["RegisteredPerson"] = relationship()
    answers: Mapped[list["Answer"]] = relationship(back_populates="submission")


class Answer(Base):
    """答案表"""
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(Integer, ForeignKey("exam_submission.id"), index=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("question.id"), index=True)
    content: Mapped[str] = mapped_column(Text, default="")
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)

    submission: Mapped["ExamSubmission"] = relationship(back_populates="answers")
    question: Mapped["Question"] = relationship(back_populates="answers")


class QuestionBank(Base):
    """题库——独立于考试的题目集合"""
    __tablename__ = "question_bank"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    type: Mapped[str] = mapped_column(String(20))  # single/multi/judge/fill/essay
    content: Mapped[str] = mapped_column(Text)
    options: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON
    answer: Mapped[str] = mapped_column(Text)
    score: Mapped[float] = mapped_column(Float, default=10.0)
    category: Mapped[str | None] = mapped_column(String(100), nullable=True)  # 分类
    tags: Mapped[str | None] = mapped_column(String(200), nullable=True)  # 逗号分隔标签
    difficulty: Mapped[int] = mapped_column(Integer, default=1)  # 1-5
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    teacher: Mapped["RegisteredPerson"] = relationship()


class CourseMaterial(Base):
    """课件/教学资源"""
    __tablename__ = "course_material"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    classroom_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("classroom.id"), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    file_path: Mapped[str] = mapped_column(String(500))  # 存储路径
    file_name: Mapped[str] = mapped_column(String(200))  # 原始文件名
    file_size: Mapped[int] = mapped_column(Integer, default=0)  # 字节
    file_type: Mapped[str] = mapped_column(String(50))  # pdf/pptx/docx/mp4等
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    teacher: Mapped["RegisteredPerson"] = relationship()
    classroom: Mapped["Classroom | None"] = relationship()


class GradeConfig(Base):
    """成绩权重配置"""
    __tablename__ = "grade_config"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), unique=True)
    homework_weight: Mapped[float] = mapped_column(Float, default=0.3)
    exam_weight: Mapped[float] = mapped_column(Float, default=0.4)
    attendance_weight: Mapped[float] = mapped_column(Float, default=0.1)
    usual_weight: Mapped[float] = mapped_column(Float, default=0.2)  # 平时分

    classroom: Mapped["Classroom"] = relationship()


class UsualScore(Base):
    """学生平时分（教师手动设置）"""
    __tablename__ = "usual_score"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    person_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    score: Mapped[float] = mapped_column(Float, default=80.0)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        {"sqlite_autoincrement": True},
    )


class AnswerRegradeHistory(Base):
    """答题重批改历史记录（大题 LLM 重批改 + 人工补录统一审计）

    记录每次 regrade-essay / manual-input 接口调用的完整审计信息：
    - before/after 分数与总分，便于追溯评分变化
    - max_score 快照，避免后续 question.score 改动后失去参照
    - LLM 完整结果 (grading_json) + 写作归因 (writing_attribution_json)
    - 操作人、时间、入参模式（text/image）、force_essay 标志
    """
    __tablename__ = "answer_regrade_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(Integer, ForeignKey("exam_submission.id"))
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("question.id"))
    operator_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)

    # 重批改方式与入参
    regrade_method: Mapped[str] = mapped_column(String(20))  # 'regrade_essay' / 'manual_input'
    input_mode: Mapped[str | None] = mapped_column(String(20), nullable=True)  # 'text'/'image'/None
    force_essay: Mapped[bool] = mapped_column(Boolean, default=False)

    # 分数变化前后（含总分，便于审计）
    before_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    after_score: Mapped[float] = mapped_column(Float)
    before_is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    after_is_correct: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    max_score: Mapped[float] = mapped_column(Float)  # 重批改时的题目满分快照
    before_total_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    after_total_score: Mapped[float | None] = mapped_column(Float, nullable=True)

    # 学生答案文字（text 模式 = 教师手输；image 模式 = OCR 识别结果）
    student_text: Mapped[str | None] = mapped_column(Text, nullable=True)

    # LLM 相关（仅 regrade_essay 有值，manual_input 全为 None）
    is_essay: Mapped[bool] = mapped_column(Boolean, default=False)
    model_key: Mapped[str | None] = mapped_column(String(50), nullable=True)
    grading_method: Mapped[str | None] = mapped_column(String(50), nullable=True)
    error_cause: Mapped[str | None] = mapped_column(String(50), nullable=True)
    knowledge_points_json: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON 数组
    grading_json: Mapped[str | None] = mapped_column(Text, nullable=True)  # LLM 完整结果
    writing_attribution_json: Mapped[str | None] = mapped_column(Text, nullable=True)  # 写作归因
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    operator: Mapped["RegisteredPerson"] = relationship()

    __table_args__ = (
        Index("ix_answer_regrade_history_sub_q", "submission_id", "question_id"),
    )


class TeachingPlan(Base):
    """教学计划/备课"""
    __tablename__ = "teaching_plan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    classroom_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("classroom.id"), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    objectives: Mapped[str | None] = mapped_column(Text, nullable=True)  # 教学目标
    chapters: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON: 章节安排
    schedule: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON: 进度安排
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="draft")  # draft/published
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    teacher: Mapped["RegisteredPerson"] = relationship()
    classroom: Mapped["Classroom | None"] = relationship()


class ExtensionRequest(Base):
    """作业延期申请"""
    __tablename__ = "extension_request"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    homework_id: Mapped[int] = mapped_column(Integer, ForeignKey("homework.id"), index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    reason: Mapped[str] = mapped_column(Text)
    original_deadline: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    requested_deadline: Mapped[datetime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20), default="pending")  # pending/approved/rejected
    teacher_feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    homework: Mapped["Homework"] = relationship()
    student: Mapped["RegisteredPerson"] = relationship()


class LeaveRequest(Base):
    """请假申请"""
    __tablename__ = "leave_request"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    classroom_id: Mapped[int] = mapped_column(Integer, ForeignKey("classroom.id"), index=True)
    start_date: Mapped[datetime] = mapped_column(DateTime)
    end_date: Mapped[datetime] = mapped_column(DateTime)
    leave_type: Mapped[str] = mapped_column(String(20), default="sick")  # sick/personal/official/other
    reason: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(20), default="pending")  # pending/approved/rejected
    teacher_feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    student: Mapped["RegisteredPerson"] = relationship()
    classroom: Mapped["Classroom"] = relationship()


class Experiment(Base):
    """实验项目"""
    __tablename__ = "experiment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    classroom_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("classroom.id"), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    requirements: Mapped[str | None] = mapped_column(Text, nullable=True)
    deadline: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    total_score: Mapped[float] = mapped_column(Float, default=100.0)
    status: Mapped[str] = mapped_column(String(20), default="open")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    teacher: Mapped["RegisteredPerson"] = relationship()
    classroom: Mapped["Classroom | None"] = relationship()
    reports: Mapped[list["ExperimentReport"]] = relationship(back_populates="experiment")


class ExperimentReport(Base):
    """实验报告提交"""
    __tablename__ = "experiment_report"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    experiment_id: Mapped[int] = mapped_column(Integer, ForeignKey("experiment.id"), index=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    content: Mapped[str] = mapped_column(Text, default="")
    file_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    file_name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    score: Mapped[float | None] = mapped_column(Float, nullable=True)
    feedback: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(20), default="submitted")  # submitted/graded/returned
    submitted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    graded_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    experiment: Mapped["Experiment"] = relationship(back_populates="reports")
    student: Mapped["RegisteredPerson"] = relationship()


# ===== AI 智能批改相关表 =====


class GradingResult(Base):
    """AI批改结果表"""
    __tablename__ = "grading_result"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(Integer, ForeignKey("homework_submission.id"), index=True)
    rubric_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    grading_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    score: Mapped[float] = mapped_column(Float, default=0.0)
    max_score: Mapped[float] = mapped_column(Float, default=100.0)
    comment: Mapped[str] = mapped_column(Text, default="")
    model_key: Mapped[str] = mapped_column(String(50), default="standard")
    grading_method: Mapped[str] = mapped_column(String(50), default="llm")
    confidence: Mapped[float] = mapped_column(Float, default=0.85)
    error_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    error_cause: Mapped[str | None] = mapped_column(String(50), nullable=True)
    knowledge_points: Mapped[str | None] = mapped_column(Text, nullable=True)
    confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    confirmed_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    submission: Mapped["HomeworkSubmission"] = relationship(back_populates="grading_results")


class KnowledgeAnalysis(Base):
    """知识归因分析结果表"""
    __tablename__ = "knowledge_analysis"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    analysis_type: Mapped[str] = mapped_column(String(20))  # math / writing
    radar_json: Mapped[str] = mapped_column(Text)
    weak_points_json: Mapped[str] = mapped_column(Text)
    correction_status_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    student: Mapped["RegisteredPerson"] = relationship()


class CorrectionRecord(Base):
    """订正记录表"""
    __tablename__ = "correction_record"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    submission_id: Mapped[int] = mapped_column(Integer, ForeignKey("homework_submission.id"), index=True)
    original_score: Mapped[float] = mapped_column(Float)
    correction_score: Mapped[float] = mapped_column(Float)
    improved: Mapped[bool] = mapped_column(Boolean, default=False)
    remaining_errors: Mapped[str | None] = mapped_column(Text, nullable=True)
    knowledge_update: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    submission: Mapped["HomeworkSubmission"] = relationship()


class SimilarQuestion(Base):
    """相似题持久化表——错题一键生成变式题并保存，供学生练习"""
    __tablename__ = "similar_question"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    source_grading_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("grading_result.id"), nullable=True, index=True)
    source_correction_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("correction_record.id"), nullable=True, index=True)
    question_text: Mapped[str] = mapped_column(Text)
    standard_answer: Mapped[str] = mapped_column(Text, default="")
    rubric_suggestion: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON
    difficulty: Mapped[str] = mapped_column(String(20), default="中等")
    variant_type: Mapped[str] = mapped_column(String(30), default="同类变式")
    tier: Mapped[str] = mapped_column(String(20), default="中等生")
    knowledge_point_ids: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON 数组
    mastery_status: Mapped[str] = mapped_column(String(20), default="pending")  # pending/passed/failed
    student_answer: Mapped[str | None] = mapped_column(Text, nullable=True)
    practice_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    practiced_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    student: Mapped["RegisteredPerson"] = relationship()


class PaperTemplate(Base):
    """试卷模板——教师拖框标注的空白卷区域，用于扫描件按题切分

    场景：教师在创建考试后，上传一张空白卷扫描件，
    用 PaperTemplateEditor 在 canvas 上拖框标注每道题的区域 (bbox)。
    学生答卷扫描件上传时，系统按模板切分各题图片，再分题型批改。
    """
    __tablename__ = "paper_template"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    exam_id: Mapped[int] = mapped_column(Integer, ForeignKey("exam.id"), unique=True)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("registered_person.id"), index=True)
    blank_image_path: Mapped[str] = mapped_column(String(500))  # 空白卷图片存储路径
    anchor_points: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON: 4 个角点用于透视校正
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    exam: Mapped["Exam"] = relationship()
    teacher: Mapped["RegisteredPerson"] = relationship()
    regions: Mapped[list["QuestionRegion"]] = relationship(
        back_populates="template", cascade="all, delete-orphan", order_by="QuestionRegion.order"
    )


class QuestionRegion(Base):
    """题目区域——模板中每道题的坐标范围

    bbox 为 JSON 字符串：{"x": int, "y": int, "w": int, "h": int}
    坐标基于空白卷原始像素尺寸，前端按缩放比例换算显示。
    region_type 决定该区域走哪种识别+批改流程：
      - bubble: 答题卡气泡检测（单选/多选/判断）
      - fill:   填空题 OCR + 字符串匹配
      - essay:  大题/作文 OCR + LLM 批改
    """
    __tablename__ = "question_region"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    template_id: Mapped[int] = mapped_column(Integer, ForeignKey("paper_template.id"), index=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey("question.id"), index=True)
    region_type: Mapped[str] = mapped_column(String(20))  # bubble | fill | essay
    bbox: Mapped[str] = mapped_column(Text)  # JSON: {x, y, w, h}
    order: Mapped[int] = mapped_column(Integer, default=1)

    template: Mapped["PaperTemplate"] = relationship(back_populates="regions")
    question: Mapped["Question"] = relationship()
