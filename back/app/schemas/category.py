from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CategoryIn(CategoryBase):
    pass


class CategoryDb(CategoryBase):
    id: int
    descriptions: Optional[List[str]]


class BindCategory(BaseModel):
    id_category: int
    description: str
