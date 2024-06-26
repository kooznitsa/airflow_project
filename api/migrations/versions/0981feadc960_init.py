"""init

Revision ID: 0981feadc960
Revises: 
Create Date: 2024-05-11 11:25:28.817584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0981feadc960'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('retrieved_at', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('to_usd', sa.Float(), nullable=False),
    sa.Column('to_eur', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather',
    sa.Column('retrieved_at', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('wind_speed', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather')
    op.drop_table('currencies')
    # ### end Alembic commands ###
