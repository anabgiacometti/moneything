"""
Defining data models
We work with alembic, to make changes to the database use the alembic commands
E.g.: alembic revision -m "description the change" --autogenerate
More information at https://alembic.sqlalchemy.org/en/latest/
"""
from .category import *
from .title import *
from .transaction import *
