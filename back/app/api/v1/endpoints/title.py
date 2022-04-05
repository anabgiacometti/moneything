from typing import List
from asyncpg import ForeignKeyViolationError, UniqueViolationError
from fastapi import APIRouter, HTTPException
from app.crud.title import TITLE
from app.schemas.msg import Msg

from app.schemas.title import TitleIn, TitleDb, BindTitle


router = APIRouter()


async def get_obj(id):
    obj = await TITLE.get_one(id)
    if not obj:
        raise HTTPException(status_code=400, detail=f"Title with id {id} not found.")
    return obj


@router.get("/", response_model=List[TitleDb])
async def list():
    return await TITLE.get_all()


@router.post("/", response_model=TitleDb)
async def create(obj_in: TitleIn):
    try:
        return await TITLE.create(obj_in)
    except UniqueViolationError:
        raise HTTPException(status_code=400, detail=f"Title with name {obj_in.name} already exists.")


@router.put("/bind", response_model=TitleDb)
async def bind(obj_in: BindTitle):
    try:
        return await TITLE.bind_to_description(obj_in)
    except ForeignKeyViolationError:
        raise HTTPException(status_code=400, detail=f"Title with id {obj_in.id_title} not found.")


@router.put("/unbind", response_model=TitleDb)
async def unbind(obj_in: BindTitle):
    await get_obj(obj_in.id_title)
    try:
        return await TITLE.unbind_to_description(obj_in)
    except ForeignKeyViolationError:
        raise HTTPException(status_code=400, detail=f"Title with id {obj_in.id_title} not found.")


@router.get("/{id}", response_model=TitleDb)
async def get_one(id: int):
    return await get_obj(id)


@router.put("/{id}", response_model=TitleDb)
async def update(id: int, obj_in: TitleIn):
    obj = await TITLE.update(id, obj_in)
    if not obj:
        raise HTTPException(status_code=400, detail=f"Title with id {id} not found.")
    return obj


@router.delete("/{id}", response_model=Msg)
async def delete(id: int):
    await get_obj(id)
    await TITLE.delete(id)
    return {"message": "Title was deleted"}
