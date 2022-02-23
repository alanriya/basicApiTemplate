"""create post table 2

Revision ID: 99902032efa5
Revises: b9fa946ffaba
Create Date: 2022-02-23 13:17:45.414085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99902032efa5'
down_revision = 'b9fa946ffaba'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
