from typing import List, Optional
from pydantic import BaseModel


class TitleBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class TitleIn(TitleBase):
    pass


class TitleDb(TitleBase):
    id: int
    descriptions: Optional[List[str]]


class BindTitle(BaseModel):
    id_title: int
    description: str
