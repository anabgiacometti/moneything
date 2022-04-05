from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from app.db import metadata, sqlalchemy


title = sqlalchemy.Table(
    "title",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(80), unique=True),
    UniqueConstraint("id", "name", name="title_id_name_ix_1"),
)

title_mapper = sqlalchemy.Table(
    "title_mapper",
    metadata,
    Column("id_title", Integer, ForeignKey("title.id"), primary_key=True),
    Column("description", String(255), primary_key=True, unique=True),
)
