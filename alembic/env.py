"""Alembic 迁移环境配置

从 backend.core.config 读取 DATABASE_URL，从 backend.core.database 读取 Base.metadata，
保证迁移与项目代码使用同一套模型定义。
"""

import sys
from logging.config import fileConfig
from pathlib import Path

# 把项目根目录加入 sys.path，让 alembic 能 import backend.*
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from alembic import context
from sqlalchemy import engine_from_config, pool

# 项目配置 & 模型
from backend.core.config import settings
from backend.core.database import Base
# 导入所有表模型，确保 Base.metadata 包含全部表定义
from backend.models import tables  # noqa: F401

config = context.config

# 从项目配置读取数据库 URL（覆盖 alembic.ini 中的设置）
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 目标 metadata：所有表模型的集合
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """离线模式：生成 SQL 脚本而不连接数据库"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        # SQLite 不支持 ALTER，需要 batch 模式
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """在线模式：直接连接数据库执行迁移"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # SQLite batch 模式：用临时表替代 ALTER
            render_as_batch=True,
            # 比较类型与服务器默认值（更精确的 diff）
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
