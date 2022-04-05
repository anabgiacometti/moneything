from typing import List
from app.crud import CRUD
from app.models import category, category_mapper
from app.db import db
from app.schemas.category import BindCategory
from sqlalchemy import func, select, case


class CategoryCRUD(CRUD):
    def __init__(self):
        self.base_query = (
            select(
                category.c.id,
                category.c.name,
                case(
                    (
                        func.count(category_mapper.c.description) > 0,
                        func.array_agg(category_mapper.c.description),
                    ),
                    (func.count(category_mapper.c.description) == 0, []),
                ).label("descriptions"),
            )
            .outerjoin(category_mapper, category.c.id == category_mapper.c.id_category)
            .group_by(category.c.id, category.c.name)
        )
        super().__init__(model=category)

    async def get_all(self):
        return await db.fetch_all(self.base_query)

    async def get_one(self, id: int):
        return await db.fetch_one(self.base_query.where(category.c.id == id))

    async def get_many_by_description(self, descriptions: List[str]):
        return await db.fetch_all(self.base_query.where(category_mapper.c.description.in_(descriptions)))

    async def delete(self, id: int):
        await CategoryMapperCRUD().delete_by_parent(id_category=id)
        await db.execute(category.delete().where(category.c.id == id))

    async def bind_to_description(self, obj_in: BindCategory):
        await CategoryMapperCRUD().create(obj_in=obj_in)
        return await self.get_one(obj_in.id_category)

    async def unbind_to_description(self, obj_in: BindCategory):
        await CategoryMapperCRUD().delete(id_category=obj_in.id_category, description=obj_in.description)
        return await self.get_one(obj_in.id_category)


class CategoryMapperCRUD(CRUD):
    def __init__(self):
        super().__init__(model=category_mapper)

    async def get_one(self, description: str):
        return await db.fetch_one(category_mapper.select().where(category_mapper.c.description == description))

    async def delete_by_parent(self, id_category: int):
        return await db.execute(category_mapper.delete().where(category_mapper.c.id_category == id_category))

    async def delete(self, id_category: int, description: str):
        return await db.execute(
            category_mapper.delete().where(
                category_mapper.c.id_category == id_category,
                category_mapper.c.description == description,
            )
        )

    async def create(self, obj_in):
        description = await db.execute(
            category_mapper.insert().values(**obj_in.dict()).returning(category_mapper.c.description)
        )
        return await self.get_one(description=description)


CATEGORY = CategoryCRUD()
