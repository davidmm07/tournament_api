"""Add monsters

Revision ID: 51143d2565aa
Revises: 
Create Date: 2022-12-13

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "51143d2565aa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    monsters_table = op.create_table(
        "monsters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("imageUrl", sa.String(), nullable=False),
        sa.Column("attack", sa.Integer(), nullable=False),
        sa.Column("defense", sa.Integer(), nullable=False),
        sa.Column("hp", sa.Integer(), nullable=False),
        sa.Column("speed", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.bulk_insert(
        monsters_table,
        [
            {"id": 1, "name": "Dead Unicorn", "imageUrl": "https://fakeurl-tournament-public-files.s3.amazonaws.com/tournament-cc-01/dead-unicorn.png", "attack": 60, "defense": 40, "hp": 10, "speed": 80},
            {"id": 2, "name": "Old Shark", "imageUrl": "https://fakeurl-tournament-public-files.s3.amazonaws.com/tournament-cc-01/old-shark.png", "attack": 50, "defense": 20, "hp": 80, "speed": 90},
            {"id": 3, "name": "Red Dragon", "imageUrl": "https://fakeurl-tournament-public-files.s3.amazonaws.com/tournament-cc-01/red-dragon.png", "attack": 90, "defense": 80, "hp": 90, "speed": 70},
            {"id": 4, "name": "Robot Bear", "imageUrl": "https://fakeurl-tournament-public-files.s3.amazonaws.com/tournament-cc-01/robot-bear.png", "attack": 50, "defense": 40, "hp": 80, "speed": 60},
            {"id": 5, "name": "Angry Snake", "imageUrl": "https://fakeurl-tournament-public-files.s3.amazonaws.com/tournament-cc-01/angry-snake.png", "attack": 80, "defense": 20, "hp": 70, "speed": 80},
        ],
    )


def downgrade():
    op.drop_table("monsters")