from typing import List, Set
from pydantic import BaseModel
from .transaction import TransactionDB, TransactionImport


class ImportBase(BaseModel):
    origin: str


class ImportPreview(ImportBase):
    preview: List[TransactionImport]
    no_category: Set[str]
    no_title: Set[str]
