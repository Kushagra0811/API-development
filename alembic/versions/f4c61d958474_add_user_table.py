"""add user table

Revision ID: f4c61d958474
Revises: 03bad6c41630
Create Date: 2025-07-10 02:38:50.773438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4c61d958474'
down_revision: Union[str, Sequence[str], None] = '03bad6c41630'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', sa.Column('id', sa.Integer(), nullable = False),sa.Column('email',sa.String(),nullable=False),sa.Column('password',sa.String(),nullable=False),sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default =sa.text('now()'),nullable=False), sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
