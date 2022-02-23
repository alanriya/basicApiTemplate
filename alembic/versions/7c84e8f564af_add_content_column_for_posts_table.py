"""add content column for posts table

Revision ID: 7c84e8f564af
Revises: 1131f4d21fef
Create Date: 2022-02-23 13:22:47.144807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c84e8f564af'
down_revision = '1131f4d21fef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
