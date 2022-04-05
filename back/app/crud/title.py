from typing import List
from app.crud import CRUD
from app.models import title, title_mapper
from app.db import db
from app.schemas.title import BindTitle
from sqlalchemy import func, select, case


class TitleCRUD(CRUD):
    def __init__(self):
        self.base_query = (
            select(
                title.c.id,
                title.c.name,
                case(
                    (
                        func.count(title_mapper.c.description) > 0,
                        func.array_agg(title_mapper.c.description),
                    ),
                    (func.count(title_mapper.c.description) == 0, []),
                ).label("descriptions"),
            )
            .outerjoin(title_mapper, title.c.id == title_mapper.c.id_title)
            .group_by(title.c.id, title.c.name)
        )
        super().__init__(model=title)

    async def get_all(self):
        return await db.fetch_all(self.base_query)

    async def get_one(self, id: int):
        return await db.fetch_one(self.base_query.where(title.c.id == id))

    async def get_many_by_description(self, descriptions: List[str]):
        return await db.fetch_all(self.base_query.where(title_mapper.c.description.in_(descriptions)))

    async def delete(self, id: int):
        await TitleMapperCRUD().delete_by_parent(id_title=id)
        await db.execute(title.delete().where(title.c.id == id))

    async def bind_to_description(self, obj_in: BindTitle):
        await TitleMapperCRUD().create(obj_in=obj_in)
        return await self.get_one(obj_in.id_title)

    async def unbind_to_description(self, obj_in: BindTitle):
        await TitleMapperCRUD().delete(id_title=obj_in.id_title, description=obj_in.description)
        return await self.get_one(obj_in.id_title)


class TitleMapperCRUD(CRUD):
    def __init__(self):
        super().__init__(model=title_mapper)

    async def get_one(self, description: str):
        return await db.fetch_one(title_mapper.select().where(title_mapper.c.description == description))

    async def delete_by_parent(self, id_title: int):
        return await db.execute(title_mapper.delete().where(title_mapper.c.id_title == id_title))

    async def delete(self, id_title: int, description: str):
        return await db.execute(
            title_mapper.delete().where(
                title_mapper.c.id_title == id_title,
                title_mapper.c.description == description,
            )
        )

    async def create(self, obj_in):
        description = await db.execute(
            title_mapper.insert().values(**obj_in.dict()).returning(title_mapper.c.description)
        )
        return await self.get_one(description=description)


TITLE = TitleCRUD()
