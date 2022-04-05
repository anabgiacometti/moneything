from email import message
from typing import List
from fastapi import APIRouter, HTTPException, UploadFile
from app.api.v1.utils.decorators import login_required
from app.crud.csv_import import CVSImport
from pandas.errors import ParserError

router = APIRouter()


@router.get("/")
@login_required
async def get_transactions():
    # TODO: get by period
    ...
