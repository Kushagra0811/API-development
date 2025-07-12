"""add content column to posts table

Revision ID: 03bad6c41630
Revises: 7a0c0c0ae374
Create Date: 2025-07-10 02:32:50.533906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03bad6c41630'
down_revision: Union[str, Sequence[str], None] = '7a0c0c0ae374'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
