import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "7be94db97e67"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "taxi_fare",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("pickup_datetime", sa.DateTime(), nullable=True),
        sa.Column("pickup_longitude", sa.Float(), nullable=True),
        sa.Column("pickup_latitude", sa.Float(), nullable=True),
        sa.Column("dropoff_longitude", sa.Float(), nullable=True),
        sa.Column("dropoff_latitude", sa.Float(), nullable=True),
        sa.Column("passenger_count", sa.Integer(), nullable=True),
        sa.Column("fare_amount", sa.Float(), nullable=True),
    )

def downgrade() -> None:
    op.drop_table("taxi_fare")

