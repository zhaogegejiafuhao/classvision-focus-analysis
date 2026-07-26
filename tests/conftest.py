"""pytest 全局配置 + 集成测试基础设施

自动将项目根目录加入 sys.path，并设置内存 SQLite 测试 DB。
集成测试使用 FastAPI TestClient + 真实 JWT 认证，走完整 HTTP 链路。
"""
import sys
from pathlib import Path

# 项目根目录 = conftest.py 所在目录的父目录
_PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

# ──────────────────────────────────────────────────────────────
# 在 import backend.* 之前，先替换 database 模块的 engine 为内存 SQLite
# 确保所有后续 import（包括 backend.main）都使用测试 DB，不污染生产库
# ──────────────────────────────────────────────────────────────
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.core import database as db_module
from backend.core.database import Base

_test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # 保证 :memory: 跨连接共享同一库
)
# 启用外键约束（SQLite 默认关闭）
@event.listens_for(_test_engine, "connect")
def _enable_fk(dbapi_conn, conn_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

db_module.engine = _test_engine
db_module.SessionLocal = sessionmaker(bind=_test_engine, autoflush=False, autocommit=False)
Base.metadata.bind = _test_engine

# 确保所有 ORM 模型已注册，然后建表
from backend.models import tables  # noqa: F401,E402
db_module.init_db()

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from backend.core.database import get_db  # noqa: E402
from backend.core.security import create_access_token, hash_password  # noqa: E402
from backend.models.tables import RegisteredPerson  # noqa: E402


# ──────────────────────────────────────────────────────────────
# DB session fixture（每个测试函数清表，保证隔离）
# ──────────────────────────────────────────────────────────────
@pytest.fixture()
def db_session():
    """每个测试函数独立的 DB session，测试结束后清表"""
    session = db_module.SessionLocal()
    yield session
    session.rollback()
    # 按依赖逆序清表（先子后父）
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()
    session.close()


# ──────────────────────────────────────────────────────────────
# 基础 TestClient（未认证，仅 override get_db 指向内存 DB）
# ──────────────────────────────────────────────────────────────
@pytest.fixture()
def client(db_session):
    """未认证的 TestClient，DB 指向内存 SQLite"""
    from backend.main import app

    def _override_db():
        try:
            yield db_session
        finally:
            pass  # 由 db_session fixture 管理生命周期

    app.dependency_overrides[get_db] = _override_db
    # 清空限流器状态，避免测试间相互影响
    from backend.core.rate_limit import _limiter
    _limiter._hits.clear()

    client = TestClient(app)  # 不进 with，跳过 lifespan
    yield client
    app.dependency_overrides.clear()


# ──────────────────────────────────────────────────────────────
# 用户 fixtures（在测试 DB 中创建真实用户记录）
# ──────────────────────────────────────────────────────────────
def _create_user(db_session, name, role, username):
    """创建测试用户并返回"""
    u = RegisteredPerson(
        name=name,
        role=role,
        username=username,
        password_hash=hash_password("123456"),
        face_embedding="[]",
    )
    db_session.add(u)
    db_session.commit()
    db_session.refresh(u)
    return u


@pytest.fixture()
def teacher_user(db_session):
    return _create_user(db_session, "张老师", "teacher", "teacher_test")


@pytest.fixture()
def student_user(db_session):
    return _create_user(db_session, "李同学", "student", "student_test")


@pytest.fixture()
def admin_user(db_session):
    return _create_user(db_session, "管理员", "admin", "admin_test")


# ──────────────────────────────────────────────────────────────
# 已认证的 TestClient（使用真实 JWT token，不 override get_current_user）
# 关键改进：每个 client 是独立的 TestClient 实例，通过 Authorization 头携带
# 各自的 JWT token，走真实认证链路。多个 auth_client 可在同一测试中并存。
# ──────────────────────────────────────────────────────────────
def _make_auth_client(db_session, user):
    """创建带认证头的独立 TestClient"""
    from backend.main import app

    def _override_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _override_db
    # 清空限流器
    from backend.core.rate_limit import _limiter
    _limiter._hits.clear()

    token = create_access_token({"sub": str(user.id), "role": user.role})
    client = TestClient(app)
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client


@pytest.fixture()
def teacher_client(db_session, teacher_user):
    """以教师身份认证的 TestClient（真实 JWT）"""
    yield _make_auth_client(db_session, teacher_user)
    from backend.main import app
    app.dependency_overrides.clear()


@pytest.fixture()
def student_client(db_session, student_user):
    """以学生身份认证的 TestClient（真实 JWT）"""
    yield _make_auth_client(db_session, student_user)
    from backend.main import app
    app.dependency_overrides.clear()


@pytest.fixture()
def admin_client(db_session, admin_user):
    """以管理员身份认证的 TestClient（真实 JWT）"""
    yield _make_auth_client(db_session, admin_user)
    from backend.main import app
    app.dependency_overrides.clear()
