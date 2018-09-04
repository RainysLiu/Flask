"""manytomany

Revision ID: c52ba8d001ec
Revises: 
Create Date: 2018-08-30 19:12:13.579778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c52ba8d001ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('children',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hobby',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('children_hobby',
    sa.Column('children_id', sa.Integer(), nullable=False),
    sa.Column('hobby_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['children_id'], ['children.id'], ),
    sa.ForeignKeyConstraint(['hobby_id'], ['hobby.id'], ),
    sa.PrimaryKeyConstraint('children_id', 'hobby_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('children_hobby')
    op.drop_table('hobby')
    op.drop_table('children')
    # ### end Alembic commands ###