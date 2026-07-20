from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
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
