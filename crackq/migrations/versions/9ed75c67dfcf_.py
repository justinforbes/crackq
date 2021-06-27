"""empty message

Revision ID: 9ed75c67dfcf
Revises: 13aa5174ae92
Create Date: 2021-06-14 11:25:50.311026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ed75c67dfcf'
down_revision = '13aa5174ae92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sessions')
    op.alter_column('templates', 'id',
               existing_type=sa.NUMERIC(precision=16),
               type_=sqlalchemy_utils.types.uuid.UUIDType(),
               existing_nullable=False)
    op.alter_column('user', 'id',
               existing_type=sa.NUMERIC(precision=16),
               type_=sqlalchemy_utils.types.uuid.UUIDType(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.NUMERIC(precision=16),
               existing_nullable=False)
    op.alter_column('templates', 'id',
               existing_type=sqlalchemy_utils.types.uuid.UUIDType(),
               type_=sa.NUMERIC(precision=16),
               existing_nullable=False)
    op.create_table('sessions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('session_id', sa.VARCHAR(length=255), nullable=True),
    sa.Column('data', sa.BLOB(), nullable=True),
    sa.Column('expiry', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    # ### end Alembic commands ###