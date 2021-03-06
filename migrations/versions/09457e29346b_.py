"""empty message

Revision ID: 09457e29346b
Revises: 
Create Date: 2022-06-29 14:44:03.301789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09457e29346b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reptiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('common_name', sa.String(length=250), nullable=True),
    sa.Column('scientific_name', sa.String(length=250), nullable=True),
    sa.Column('conservation_status', sa.String(length=250), nullable=True),
    sa.Column('native_habitat', sa.Text(), nullable=True),
    sa.Column('fun_fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reptiles')
    # ### end Alembic commands ###
