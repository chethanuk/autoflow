"""empty message

Revision ID: 830fd9c44f39
Revises: dfee070b8abd
Create Date: 2024-09-19 13:04:30.351449

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = "830fd9c44f39"
down_revision = "dfee070b8abd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "chat_engines",
        sa.Column(
            "post_verification_url",
            sqlmodel.sql.sqltypes.AutoString(length=256),
            nullable=True,
        ),
    )
    op.add_column(
        "chats",
        sa.Column(
            "origin", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=True
        ),
    )
    op.add_column(
        "feedbacks",
        sa.Column(
            "origin", sqlmodel.sql.sqltypes.AutoString(length=256), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("feedbacks", "origin")
    op.drop_column("chats", "origin")
    op.drop_column("chat_engines", "post_verification_url")
    # ### end Alembic commands ###