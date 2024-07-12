"""Add content column to posts table

Revision ID: 5e04ba20b095
Revises: 5f1804009948
Create Date: 2024-06-14 10:51:00.742821

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e04ba20b095'
down_revision: Union[str, None] = '5f1804009948'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
