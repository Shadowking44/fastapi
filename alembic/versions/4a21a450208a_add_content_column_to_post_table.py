"""add content column to post table

Revision ID: 4a21a450208a
Revises: 6be86d4a829d
Create Date: 2024-02-28 03:32:05.514272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a21a450208a'
down_revision: Union[str, None] = '6be86d4a829d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
