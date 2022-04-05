from sqlalchemy import select
from typing import Dict, List
from app.crud import CRUD
from app.models import transaction
from app.db import db

from sqlalchemy.sql.expression import bindparam


class TransactionCRUD(CRUD):
    def __init__(self):
        super().__init__(model=transaction)

    async def create_from_csv(self, objs_in: List[Dict]):
        await db.execute(self.model.insert().values(objs_in))

    async def update_from_csv(self, objs_in: List[Dict]):
        query = (
            transaction.update()
            .where(transaction.c.id_legacy == bindparam("_id_legacy"))
            .values(
                date=bindparam("date"),
                payment_method=bindparam("payment_method"),
                amount=bindparam("amount"),
                description=bindparam("description"),
            )
        )
        await db.execute_many(query, objs_in)

    async def get_many_by_id_legacy(self, ids: List[str]):
        return await db.fetch_all(select(transaction.c.id_legacy).where(transaction.c.id_legacy.in_(ids)))


TRANSACTION = TransactionCRUD()
