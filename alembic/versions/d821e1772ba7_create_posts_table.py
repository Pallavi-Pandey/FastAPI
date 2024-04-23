"""create posts table

Revision ID: d821e1772ba7
Revises: 
Create Date: 2024-04-23 07:31:02.042407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd821e1772ba7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, primary_key=True, nullable=False), 
                    sa.Column('title', sa.String(), nullable=False), 
                    sa.Column('content', sa.Text, nullable=False) 
                    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
