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


def _migrate_student_last_seen():
    insp = inspect(engine)
    if "student" in insp.get_table_names():
        columns = {col["name"] for col in insp.get_columns("student")}
        if "last_seen_at" not in columns:
            with engine.connect() as conn:
                conn.execute(text("ALTER TABLE student ADD COLUMN last_seen_at DATETIME"))
                conn.commit()
