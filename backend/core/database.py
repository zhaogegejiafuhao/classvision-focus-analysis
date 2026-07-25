from sqlalchemy import create_engine, inspect, text, event
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

from backend.core.config import settings

_logger = logging.getLogger("exam")

engine = create_engine(settings.DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

# 启用 SQLite WAL 模式 + 外键约束 + 合理的 busy_timeout（解决并发写入锁冲突）
@event.listens_for(engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.execute("PRAGMA journal_mode=WAL")          # WAL 模式：读写不互斥
    cursor.execute("PRAGMA busy_timeout=5000")          # 写冲突时等5秒而非立即报错
    cursor.execute("PRAGMA synchronous=NORMAL")         # 平衡安全性与性能
    cursor.close()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    Base.metadata.create_all(bind=engine)
    _migrate_student_last_seen()
    _migrate_classroom_exam_mode()
    _migrate_registered_person_auth_fields()
    _migrate_oj_problem_created_by()
    _migrate_knowledge_document_visibility()
    _migrate_person_extra_fields()
    _migrate_knowledge_chunk_parent_child()
    _migrate_classroom_join_fields()
    _migrate_homework_exam_updated_at()
    _migrate_attachment_file_fields()
    _migrate_student_id_to_person_id()
    _migrate_question_knowledge_points()
    _migrate_attendance_checkin_session_id()
    _migrate_add_missing_indexes()
    _migrate_exam_type_and_answer_images()
    _migrate_answer_ai_grading_fields()
    _migrate_recover_stuck_ai_grading()


def _migrate_person_extra_fields():
    """为 registered_person 表添加花名册相关字段，并创建 department 表"""
    insp = inspect(engine)
    tables = insp.get_table_names()

    # 创建 department 表
    if "department" not in tables:
        with engine.connect() as conn:
            conn.execute(text("""
                CREATE TABLE department (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) UNIQUE NOT NULL,
                    type VARCHAR(20) DEFAULT 'class',
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """))
            conn.commit()

    # 添加 registered_person 新字段
    if "registered_person" in tables:
        columns = {col["name"] for col in insp.get_columns("registered_person")}
        new_cols = {
            "employee_id": "ALTER TABLE registered_person ADD COLUMN employee_id VARCHAR(50)",
            "phone": "ALTER TABLE registered_person ADD COLUMN phone VARCHAR(20)",
            "department_id": "ALTER TABLE registered_person ADD COLUMN department_id INTEGER REFERENCES department(id)",
            "id_card": "ALTER TABLE registered_person ADD COLUMN id_card VARCHAR(20)",
            "major": "ALTER TABLE registered_person ADD COLUMN major VARCHAR(100)",
            "email": "ALTER TABLE registered_person ADD COLUMN email VARCHAR(100)",
        }
        for col_name, sql in new_cols.items():
            if col_name not in columns:
                with engine.connect() as conn:
                    conn.execute(text(sql))
                    conn.commit()

        # 创建唯一索引（SQLite 不支持 ALTER TABLE ADD UNIQUE COLUMN）
        indexes = {idx["name"] for idx in insp.get_indexes("registered_person")} if "registered_person" in tables else set()
        if "ix_person_employee_id" not in indexes:
            try:
                with engine.connect() as conn:
                    conn.execute(text("CREATE UNIQUE INDEX ix_person_employee_id ON registered_person(employee_id) WHERE employee_id IS NOT NULL"))
                    conn.commit()
            except Exception:
                pass  # 索引可能已存在


def _migrate_knowledge_document_visibility():
    """为 knowledge_document 表添加 uploaded_by 和 visibility 字段"""
    insp = inspect(engine)
    if "knowledge_document" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("knowledge_document")}
        if "uploaded_by" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE knowledge_document ADD COLUMN uploaded_by INTEGER"))
                conn.commit()
        if "visibility" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE knowledge_document ADD COLUMN visibility VARCHAR(20) DEFAULT 'private'"))
                conn.commit()


def _migrate_oj_problem_created_by():
    """为 oj_problem 表添加 created_by 字段"""
    insp = inspect(engine)
    if "oj_problem" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("oj_problem")}
        if "created_by" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE oj_problem ADD COLUMN created_by INTEGER"))
                conn.commit()


def _migrate_registered_person_auth_fields():
    """为 registered_person 表添加 username 和 password_hash 字段"""
    insp = inspect(engine)
    if "registered_person" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("registered_person")}
        if "username" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE registered_person ADD COLUMN username VARCHAR(50)"))
                conn.commit()
        if "password_hash" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE registered_person ADD COLUMN password_hash VARCHAR(255)"))
                conn.commit()


def _migrate_student_last_seen():
    insp = inspect(engine)
    if "student" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("student")}
        if "last_seen_at" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE student ADD COLUMN last_seen_at DATETIME"))
                conn.commit()


def _migrate_classroom_exam_mode():
    insp = inspect(engine)
    if "classroom" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("classroom")}
        if "exam_mode" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE classroom ADD COLUMN exam_mode BOOLEAN DEFAULT 0"))
                conn.commit()


def _migrate_knowledge_chunk_parent_child():
    """为 knowledge_chunk 表添加父子分块字段：is_parent 和 parent_chunk_id"""
    insp = inspect(engine)
    if "knowledge_chunk" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("knowledge_chunk")}
        if "is_parent" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE knowledge_chunk ADD COLUMN is_parent BOOLEAN DEFAULT 0"))
                conn.commit()
        if "parent_chunk_id" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE knowledge_chunk ADD COLUMN parent_chunk_id INTEGER REFERENCES knowledge_chunk(id)"))
                conn.commit()


def _migrate_classroom_join_fields():
    """为 classroom 表添加课堂加入相关字段，并创建 classroom_member 表"""
    insp = inspect(engine)
    tables = insp.get_table_names()

    # 创建 classroom_member 表
    if "classroom_member" not in tables:
        with engine.connect() as conn:
            conn.execute(text("""
                CREATE TABLE classroom_member (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    classroom_id INTEGER NOT NULL REFERENCES classroom(id),
                    person_id INTEGER NOT NULL REFERENCES registered_person(id),
                    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """))
            conn.commit()

    # 为 classroom 表添加新字段
    if "classroom" in tables:
        columns = {col["name"] for col in insp.get_columns("classroom")}
        if "course_code" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE classroom ADD COLUMN course_code VARCHAR(50)"))
                conn.commit()
        if "is_public" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE classroom ADD COLUMN is_public BOOLEAN DEFAULT 1"))
                conn.commit()
        if "invite_code" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE classroom ADD COLUMN invite_code VARCHAR(13)"))
                conn.commit()
            # 创建 invite_code 唯一索引
            indexes = {idx["name"] for idx in insp.get_indexes("classroom")}
            if "ix_classroom_invite_code" not in indexes:
                try:
                    with engine.connect() as conn:
                        conn.execute(text("CREATE UNIQUE INDEX ix_classroom_invite_code ON classroom(invite_code) WHERE invite_code IS NOT NULL"))
                        conn.commit()
                except Exception:
                    pass


def _migrate_homework_exam_updated_at():
    """为 homework 和 exam 表添加 updated_at 字段"""
    insp = inspect(engine)
    for table_name in ("homework", "exam"):
        if table_name in insp.get_table_names():
            columns = {col["name"] for col in insp.get_columns(table_name)}
            if "updated_at" not in columns:
                with engine.connect() as conn:
                    conn.execute(text(f"ALTER TABLE {table_name} ADD COLUMN updated_at DATETIME"))
                    conn.commit()


def _migrate_attachment_file_fields():
    """为 homework_attachment 和 submission_attachment 表添加 file_size 字段"""
    insp = inspect(engine)
    for table_name in ("homework_attachment", "submission_attachment"):
        if table_name in insp.get_table_names():
            columns = {col["name"] for col in insp.get_columns(table_name)}
            if "file_size" not in columns:
                with engine.connect() as conn:
                    conn.execute(text(f"ALTER TABLE {table_name} ADD COLUMN file_size INTEGER DEFAULT 0"))
                    conn.commit()


def _migrate_student_id_to_person_id():
    """统一 student_id 含义：AttentionRecord/ExamRiskRecord/Attendance 的 student_id
    从引用 student.id 改为引用 registered_person.id，
    同时添加 student_record_id 字段保留与 Student 记录的关联。
    
    迁移步骤：
    1. 为三张表添加 student_record_id 列
    2. 将原 student_id 值复制到 student_record_id
    3. 将原 student_id 值通过 Student.person_id 转换为 person_id
    """
    insp = inspect(engine)
    
    for table_name in ("attention_record", "exam_risk_record", "attendance"):
        if table_name not in insp.get_table_names():
            continue
        
        columns = {col["name"] for col in insp.get_columns(table_name)}
        
        # 第1步：添加 student_record_id 列
        if "student_record_id" not in columns:
            with engine.connect() as conn:
                conn.execute(text(
                    f"ALTER TABLE {table_name} ADD COLUMN student_record_id INTEGER REFERENCES student(id)"
                ))
                conn.commit()
            
            # 第2步：将原 student_id 复制到 student_record_id
            with engine.connect() as conn:
                conn.execute(text(
                    f"UPDATE {table_name} SET student_record_id = student_id"
                ))
                conn.commit()
            
            # 第3步：将 student_id 从 Student.id 转换为 Student.person_id (registered_person.id)
            # 对于没有 person_id 的 Student 记录，保留原 student_id 值（设为0表示无效）
            with engine.connect() as conn:
                conn.execute(text(
                    f"UPDATE {table_name} SET student_id = "
                    f"COALESCE("
                    f"  (SELECT person_id FROM student WHERE student.id = {table_name}.student_record_id), "
                    f"  0"
                    f") "
                    f"WHERE student_record_id IS NOT NULL"
                ))
                conn.commit()
            
            # 处理 student_record_id 为 NULL 的情况（旧数据没有关联 Student 记录）
            with engine.connect() as conn:
                conn.execute(text(
                    f"UPDATE {table_name} SET student_id = 0 WHERE student_id IS NULL"
                ))
                conn.commit()


def _migrate_question_knowledge_points():
    """为 question 表添加 knowledge_points 字段（JSON 格式存储知识点列表）"""
    insp = inspect(engine)
    if "question" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("question")}
        if "knowledge_points" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE question ADD COLUMN knowledge_points TEXT"))
                conn.commit()


def _migrate_attendance_checkin_session_id():
    """为 attendance 表添加 checkin_session_id 字段，关联签到场次"""
    insp = inspect(engine)
    if "attendance" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("attendance")}
        if "checkin_session_id" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE attendance ADD COLUMN checkin_session_id INTEGER REFERENCES checkin_session(id)"))
                conn.commit()


def _migrate_add_missing_indexes():
    """为频繁查询的列添加数据库索引（SQLite 不支持 CREATE INDEX IF NOT EXISTS 直接用）"""
    insp = inspect(engine)
    existing_indexes = {}
    for table_name in insp.get_table_names():
        existing_indexes[table_name] = {idx["name"] for idx in insp.get_indexes(table_name)}

    indexes_to_create = [
        # (索引名, 表名, 列SQL)
        ("ix_knowledge_analysis_student_id_type", "knowledge_analysis", "student_id, analysis_type"),
        ("ix_registered_person_role", "registered_person", "role"),
        ("ix_homework_status", "homework", "status"),
        ("ix_exam_status", "exam", "status"),
        ("ix_checkin_session_status", "checkin_session", "status"),
        ("ix_oj_submission_status", "oj_submission", "status"),
        ("ix_similar_question_mastery", "similar_question", "mastery_status"),
    ]

    for idx_name, table_name, columns in indexes_to_create:
        if table_name not in insp.get_table_names():
            continue
        if idx_name not in existing_indexes.get(table_name, set()):
            try:
                with engine.connect() as conn:
                    conn.execute(text(f"CREATE INDEX {idx_name} ON {table_name}({columns})"))
                    conn.commit()
            except Exception:
                pass  # 索引可能已存在（并发情况）


def _migrate_exam_type_and_answer_images():
    """为 exam 表添加 exam_type 字段，为 answer 表添加 image_urls 字段"""
    insp = inspect(engine)
    if "exam" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("exam")}
        if "exam_type" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE exam ADD COLUMN exam_type VARCHAR(20) DEFAULT 'computer'"))
                conn.commit()
    if "answer" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("answer")}
        if "image_urls" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE answer ADD COLUMN image_urls TEXT"))
                conn.commit()


def _migrate_answer_ai_grading_fields():
    """为 answer 表添加 AI 批改 + OCR + 教师审核字段（17 个）"""
    insp = inspect(engine)
    if "answer" not in insp.get_table_names():
        return
    columns = {col["name"] for col in insp.get_columns("answer")}
    new_cols = {
        # AI 批改结果
        "ai_status": "ALTER TABLE answer ADD COLUMN ai_status VARCHAR(20)",
        "ai_score": "ALTER TABLE answer ADD COLUMN ai_score FLOAT",
        "ai_comment": "ALTER TABLE answer ADD COLUMN ai_comment TEXT",
        "ai_confidence": "ALTER TABLE answer ADD COLUMN ai_confidence FLOAT",
        "ai_grading_json": "ALTER TABLE answer ADD COLUMN ai_grading_json TEXT",
        "ai_rubric_json": "ALTER TABLE answer ADD COLUMN ai_rubric_json TEXT",
        "ai_model_key": "ALTER TABLE answer ADD COLUMN ai_model_key VARCHAR(50)",
        "ai_graded_at": "ALTER TABLE answer ADD COLUMN ai_graded_at DATETIME",
        "ai_error": "ALTER TABLE answer ADD COLUMN ai_error TEXT",
        # OCR 结果
        "ocr_text": "ALTER TABLE answer ADD COLUMN ocr_text TEXT",
        "ocr_confidence": "ALTER TABLE answer ADD COLUMN ocr_confidence FLOAT",
        "ocr_engines": "ALTER TABLE answer ADD COLUMN ocr_engines VARCHAR(100)",
        # 教师审核
        "needs_review": "ALTER TABLE answer ADD COLUMN needs_review BOOLEAN DEFAULT 0",
        "teacher_confirmed": "ALTER TABLE answer ADD COLUMN teacher_confirmed BOOLEAN DEFAULT 0",
        "teacher_score": "ALTER TABLE answer ADD COLUMN teacher_score FLOAT",
        "teacher_comment": "ALTER TABLE answer ADD COLUMN teacher_comment TEXT",
        "confirmed_at": "ALTER TABLE answer ADD COLUMN confirmed_at DATETIME",
    }
    for col_name, sql in new_cols.items():
        if col_name not in columns:
            with engine.connect() as conn:
                conn.execute(text(sql))
                conn.commit()
                _logger.info(f"[migration] answer.{col_name} added")


def _migrate_recover_stuck_ai_grading():
    """服务重启后恢复卡在 ai_grading 状态的提交

    将 exam_submission.status='ai_grading' 重置为 'submitted'，
    并将 answer.ai_status='processing' 重置为 'pending'，
    使教师可在审核页手动触发重新批改。
    """
    insp = inspect(engine)
    if "exam_submission" not in insp.get_table_names():
        return
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT id FROM exam_submission WHERE status = 'ai_grading'"
        ))
        stuck_ids = [row[0] for row in result]
        if stuck_ids:
            conn.execute(text(
                "UPDATE exam_submission SET status = 'submitted' WHERE status = 'ai_grading'"
            ))
            if "answer" in insp.get_table_names():
                conn.execute(text(
                    "UPDATE answer SET ai_status = 'pending' WHERE ai_status = 'processing'"
                ))
            conn.commit()
            _logger.warning(
                f"[startup] recovered {len(stuck_ids)} stuck ai_grading submissions: {stuck_ids}"
            )
