"""initial schema baseline

Baseline revision: marks the database state as of 2026-07-25.
All tables are created by backend.core.database.init_db() (SQLAlchemy create_all).
Future schema changes should be managed via Alembic migrations.

For existing deployments: run `alembic stamp head` to mark this baseline.
For new deployments: init_db() creates all tables; then run `alembic stamp head`.

Revision ID: 7043c2c1d575
Revises:
Create Date: 2026-07-25 22:47:16.301209+08:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7043c2c1d575'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Baseline: no-op.

    Tables are created by init_db() via Base.metadata.create_all().
    This migration exists only to establish the Alembic revision chain.
    Future migrations will build on this baseline.
    """
    pass


def downgrade() -> None:
    """Cannot downgrade past baseline."""
    pass
