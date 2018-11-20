"""博客表

Revision ID: 486cc0b38cf6
Revises: d5485de2f703
Create Date: 2018-09-07 17:10:32.699798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '486cc0b38cf6'
down_revision = 'd5485de2f703'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('b_title', sa.String(length=50), nullable=True),
    sa.Column('b_subject', sa.String(length=20), nullable=True),
    sa.Column('b_content', sa.Text(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('b_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['b_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    # ### end Alembic commands ###
