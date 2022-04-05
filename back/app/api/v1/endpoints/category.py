from typing import List
from asyncpg import ForeignKeyViolationError, UniqueViolationError
from fastapi import APIRouter, HTTPException
from app.crud.category import CATEGORY
from app.schemas.msg import Msg

from app.schemas.category import CategoryIn, CategoryDb, BindCategory


router = APIRouter()


async def get_obj(id):
    obj = await CATEGORY.get_one(id)
    if not obj:
        raise HTTPException(status_code=400, detail=f"Category with id {id} not found.")
    return obj


@router.get("/", response_model=List[CategoryDb])
async def list():
    return await CATEGORY.get_all()


@router.post("/", response_model=CategoryDb)
async def create(obj_in: CategoryIn):
    try:
        return await CATEGORY.create(obj_in)
    except UniqueViolationError:
        raise HTTPException(status_code=400, detail=f"Category with name {obj_in.name} already exists.")


@router.put("/bind", response_model=CategoryDb)
async def bind(obj_in: BindCategory):
    try:
        return await CATEGORY.bind_to_description(obj_in)
    except ForeignKeyViolationError:
        raise HTTPException(status_code=400, detail=f"Category with id {obj_in.id_category} not found.")


@router.put("/unbind", response_model=CategoryDb)
async def unbind(obj_in: BindCategory):
    await get_obj(obj_in.id_category)
    try:
        return await CATEGORY.unbind_to_description(obj_in)
    except ForeignKeyViolationError:
        raise HTTPException(status_code=400, detail=f"Category with id {obj_in.id_category} not found.")


@router.get("/{id}", response_model=CategoryDb)
async def get_one(id: int):
    return await get_obj(id)


@router.put("/{id}", response_model=CategoryDb)
async def update(id: int, obj_in: CategoryIn):
    obj = await CATEGORY.update(id, obj_in)
    if not obj:
        raise HTTPException(status_code=400, detail=f"Category with id {id} not found.")
    return obj


@router.delete("/{id}", response_model=Msg)
async def delete(id: int):
    await get_obj(id)
    await CATEGORY.delete(id)
    return {"message": "Category was deleted"}
