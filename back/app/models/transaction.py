from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from app.db import metadata, sqlalchemy


transaction = sqlalchemy.Table(
    "transaction",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("id_legacy", String(255), unique=True),
    Column("origin", String(80)),
    Column("date", Date),
    Column("payment_method", String(20)),
    Column("amount", Float),
    Column("description", String(255)),
)
