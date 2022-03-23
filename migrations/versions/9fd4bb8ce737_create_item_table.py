"""create item table

Revision ID: 9fd4bb8ce737
Revises: 
Create Date: 2022-03-09 22:54:05.547065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fd4bb8ce737'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('item', 
    sa.Column('id', sa.String(), nullable=False, primary_key=True),
    sa.Column('admin_id', sa.String(), nullable=False)
    )
    pass


def downgrade():
    op.drop_table('item')
    pass
