from datetime import date
from typing import Dict, List, Optional
from fastapi import UploadFile
from pydantic import BaseModel


class TransactionBase(BaseModel):
    id_legacy: str
    date: date
    payment_method: str
    amount: float
    description: str


class TransactionIn(TransactionBase):
    origin: str
    id_category: Optional[int]
    category_name: Optional[str]
    id_title: Optional[int]
    title_name: Optional[str]


class TransactionImport(TransactionBase):
    title: Optional[Dict]
    category: Optional[Dict]
    duplicated: bool


class TransactionDB(TransactionBase):
    id: int
    title: Dict
    category: Dict
