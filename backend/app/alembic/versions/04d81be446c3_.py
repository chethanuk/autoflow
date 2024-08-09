"""empty message

Revision ID: 04d81be446c3
Revises: e32f1e546eec
Create Date: 2024-08-08 17:11:50.178696

"""
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '04d81be446c3'
down_revision = 'e32f1e546eec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('llms', 'provider',
               existing_type=mysql.ENUM('OPENAI', 'GEMINI', 'ANTHROPIC_VERTEX', 'OPENAI_LIKE', 'BEDROCK'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('llms', 'provider',
               existing_type=mysql.ENUM('OPENAI', 'GEMINI', 'ANTHROPIC_VERTEX', 'OPENAI_LIKE'),
               nullable=False)
    # ### end Alembic commands ###