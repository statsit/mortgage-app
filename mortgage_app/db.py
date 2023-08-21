import os 
from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    Float,
    Date,
    create_engine, 
    MetaData,
    Table
)

from sqlalchemy.sql import func


DATABASE_URL = os.getenv("DATABASE_URLV2")

engine = create_engine(DATABASE_URL)

metadata = MetaData()


mortgage_tbl = Table(
    "mortgage_tbl",
    metadata,
    Column("created", Date, default=func.now(), nullable=False),
    Column("principal", Float),
    Column("interest", Float),
    Column("principal_interest", Float),
    Column("balance",Float),
    Column("monthly_repayment", Float),
    Column("monthly_repayment_aud", Float),
    Column("exchange_rate", Integer),
    Column("interest_rate", Float),
)

database= Database(DATABASE_URL)