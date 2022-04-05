"""Database communication layer"""
from app.db import db


class CRUD:
    def __init__(self, model):
        self.model = model

    async def get_all(self):
        return await db.fetch_all(self.model.select())

    async def get_one(self, id: int):
        return await db.fetch_one(self.model.select().where(self.model.c.id == id))

    async def create(self, obj_in):
        id = await db.execute(self.model.insert().values(**obj_in.dict()))
        return await self.get_one(id=id)

    async def update(self, obj_id: int, obj_in):
        await db.execute(
            self.model.update().values(**obj_in.dict()).where(self.model.c.id == obj_id)
        )
        return await self.get_one(id=obj_id)
