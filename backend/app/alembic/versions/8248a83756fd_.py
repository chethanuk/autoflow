"""empty message

Revision ID: 8248a83756fd
Revises: d9c17a1ed3f7
Create Date: 2024-07-06 15:57:38.913972

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from tidb_vector.sqlalchemy import VectorType


# revision identifiers, used by Alembic.
revision = "8248a83756fd"
down_revision = "d9c17a1ed3f7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "site_settings",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=False),
        sa.Column(
            "data_type", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=False
        ),
        sa.Column("value", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("site_settings")
    # ### end Alembic commands ###
