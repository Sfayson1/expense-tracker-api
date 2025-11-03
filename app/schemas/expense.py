from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ExpenseBase(BaseModel):
    category: str = Field(min_length=1, max_length=64)
    amount: float = Field(gt=0)
    note: Optional[str] = Field(default=None, max_length=255)


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseOut(ExpenseBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
