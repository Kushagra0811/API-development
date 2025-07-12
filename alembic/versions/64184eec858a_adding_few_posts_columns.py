"""adding few posts columns

Revision ID: 64184eec858a
Revises: 7ca1d13a8404
Create Date: 2025-07-10 02:51:23.605163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '64184eec858a'
down_revision: Union[str, Sequence[str], None] = '7ca1d13a8404'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published',sa.Boolean(),nullable=False, server_default = 'True'))
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text('NOW()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
