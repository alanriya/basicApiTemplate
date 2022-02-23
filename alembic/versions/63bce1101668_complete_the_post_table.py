"""complete the post table

Revision ID: 63bce1101668
Revises: 7d5565e14212
Create Date: 2022-02-23 13:20:20.009150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63bce1101668'
down_revision = '7d5565e14212'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
