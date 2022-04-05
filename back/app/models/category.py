from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from app.db import metadata, sqlalchemy


category = sqlalchemy.Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(80)),
    UniqueConstraint("id", "name", name="category_id_name_ix_1"),
)

category_mapper = sqlalchemy.Table(
    "category_mapper",
    metadata,
    Column("id_category", Integer, ForeignKey("category.id"), primary_key=True),
    Column("description", String(255), primary_key=True, unique=True),
)
