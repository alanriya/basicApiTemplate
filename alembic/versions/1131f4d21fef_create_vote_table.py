"""create vote table

Revision ID: 1131f4d21fef
Revises: 63bce1101668
Create Date: 2022-02-23 13:21:30.746865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1131f4d21fef'
down_revision = '63bce1101668'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )


def downgrade():
    op.drop_table('votes')