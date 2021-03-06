"""create category, category_mapper, title, title mapper and transactions tables

Revision ID: b3afa1f50966
Revises: 
Create Date: 2022-04-04 02:15:54.225758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3afa1f50966'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id', 'name', name='category_id_name_ix_1')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_table('title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id', 'name', name='title_id_name_ix_1'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_title_id'), 'title', ['id'], unique=False)
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_legacy', sa.String(length=255), nullable=True),
    sa.Column('origin', sa.String(length=80), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('payment_method', sa.String(length=20), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_legacy')
    )
    op.create_index(op.f('ix_transaction_id'), 'transaction', ['id'], unique=False)
    op.create_table('category_mapper',
    sa.Column('id_category', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['id_category'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id_category', 'description'),
    sa.UniqueConstraint('description')
    )
    op.create_table('title_mapper',
    sa.Column('id_title', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['id_title'], ['title.id'], ),
    sa.PrimaryKeyConstraint('id_title', 'description'),
    sa.UniqueConstraint('description')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('title_mapper')
    op.drop_table('category_mapper')
    op.drop_index(op.f('ix_transaction_id'), table_name='transaction')
    op.drop_table('transaction')
    op.drop_index(op.f('ix_title_id'), table_name='title')
    op.drop_table('title')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
