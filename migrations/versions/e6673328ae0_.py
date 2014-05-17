"""Adds movie table

Revision ID: e6673328ae0
Revises: None
Create Date: 2014-05-17 16:32:57.445312

"""

# revision identifiers, used by Alembic.
revision = 'e6673328ae0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'movie',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=True),
        sa.Column('rating', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('movie')
