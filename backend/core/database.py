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
