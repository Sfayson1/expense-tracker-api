"""add composite indexes for expenses

Revision ID: 4c2fbf924f60
Revises: fe9aa023fe96
Create Date: 2025-11-03 12:48:23.393064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c2fbf924f60'
down_revision: Union[str, Sequence[str], None] = 'fe9aa023fe96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index(
        "ix_expenses_user_created",
        "expenses",
        ["user_id", "created_at"],
        unique=False,
    )

    op.create_index(
        "ix_expenses_user_category_created",
        "expenses",
        ["user_id", "category", "created_at"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_expenses_user_category_created", table_name="expenses")
    op.drop_index("ix_expenses_user_created", table_name="expenses")
