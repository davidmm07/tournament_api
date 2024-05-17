"""Add battles

Revision ID: 833724243ce0
Revises: 51143d2565aa
Create Date: 2022-12-13

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "833724243ce0"
down_revision = "51143d2565aa"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "battles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("winner", sa.Integer(), nullable=True),
        sa.Column("monsterA", sa.Integer(), nullable=True),
        sa.Column("monsterB", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("battles")