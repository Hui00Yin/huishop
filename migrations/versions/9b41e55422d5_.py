"""empty message

Revision ID: 9b41e55422d5
Revises: e676343c29b7
Create Date: 2018-11-06 22:52:36.938834

"""

# revision identifiers, used by Alembic.
revision = '9b41e55422d5'
down_revision = 'e676343c29b7'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('rcv_name', sa.String(length=80), nullable=False),
    sa.Column('rcv_phone', sa.String(length=20), nullable=False),
    sa.Column('province', sa.String(length=20), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('district', sa.String(length=20), nullable=False),
    sa.Column('rcv_address', sa.String(length=200), nullable=False),
    sa.Column('zip', sa.String(length=6), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('sku', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Numeric(precision=12, scale=2, asdecimal=False), nullable=True),
    sa.Column('weight', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('longth', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('width', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('height', sa.Numeric(precision=8, asdecimal=False), nullable=True),
    sa.Column('main_image', sa.String(length=500), nullable=True),
    sa.Column('sub_images', sa.Text(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('posts2')
    op.drop_table('posts1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts1',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('slug', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='posts1_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='posts1_pkey')
    )
    op.create_table('posts2',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('slug', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='posts2_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='posts2_pkey')
    )
    op.drop_table('product_details')
    op.drop_table('addresses')
    op.drop_table('product')
    op.drop_table('category')
    # ### end Alembic commands ###
