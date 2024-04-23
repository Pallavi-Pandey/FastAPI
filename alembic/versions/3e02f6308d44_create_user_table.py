"""create user table

Revision ID: 3e02f6308d44
Revises: d821e1772ba7
Create Date: 2024-04-23 08:03:59.926406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e02f6308d44'
down_revision: Union[str, None] = 'd821e1772ba7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )          
    pass


def downgrade():
    op.drop_table('users')
    pass
