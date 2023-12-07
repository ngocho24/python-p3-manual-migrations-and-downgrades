"""Renaming students to scholars

Revision ID: 481889859db7
Revises: 
Create Date: 2023-12-08 00:32:19.066716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '481889859db7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'name', new_column_name='new_name')



def downgrade():
    op.alter_column('students', 'new_name', new_column_name='name')
