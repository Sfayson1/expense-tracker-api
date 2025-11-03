from pydantic import BaseModel
from typing import Generic, TypeVar, List

T = TypeVar("T")

class PageMeta(BaseModel):
    total: int
    limit: int
    offset: int

class Page(BaseModel, Generic[T]):
    items: List[T]
    meta: PageMeta
