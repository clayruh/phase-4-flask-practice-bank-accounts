"""empty message

Revision ID: 0a8e89b42a17
Revises: 34bcf5759c4b
Create Date: 2023-09-18 13:59:25.124903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8e89b42a17'
down_revision = '34bcf5759c4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'balance',
               existing_type=sa.INTEGER(),
               nullable=0)
    op.alter_column('accounts', 'account_type',
               existing_type=sa.VARCHAR(),
               nullable=0)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('accounts', 'account_type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('accounts', 'balance',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
