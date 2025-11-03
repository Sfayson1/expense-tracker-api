from alembic import op
import sqlalchemy as sa

def upgrade():
    op.alter_column(
        "expenses",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        server_default=sa.text("now()"),   # ✅ add default
        existing_nullable=False,
    )

def downgrade():
    op.alter_column(
        "expenses",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        server_default=None,               # remove default
        existing_nullable=False,
    )
