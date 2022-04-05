from typing import List
from fastapi import APIRouter, HTTPException, UploadFile
from app.api.v1.utils.decorators import login_required
from app.crud.csv_import import CVSImport
from pandas.errors import ParserError
from app.schemas.csv_import import ImportPreview
from app.schemas.msg import Msg

router = APIRouter()


@router.post("/preview", response_model=ImportPreview)
@login_required
async def preview(origin: str, files: List[UploadFile]):
    try:
        return await CVSImport(origin=origin, files=files).get_preview()
    except ParserError:
        raise HTTPException(status_code=400, detail="All files must have the same origin.")
    except AssertionError:
        raise HTTPException(status_code=400, detail="Import only avaible for csv files.")


@router.post("/save", response_model=Msg)
@login_required
async def save(origin: str, on_duplicate: str, files: List[UploadFile]):
    try:
        rows = await CVSImport(origin=origin, files=files).save(on_duplicate)
        return {"message": f"Imported {rows} rows"}
    except ParserError:
        raise HTTPException(status_code=400, detail="All files must have the same origin.")
    except AssertionError:
        raise HTTPException(status_code=400, detail="Import only avaible for csv files.")
