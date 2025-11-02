from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class ExpenseCreate(BaseModel):
    category: str = Field(min_length=1, max_length=64)
    amount: float = Field(gt=0)
    note: str | None = Field(default=None, max_length=255)

class ExpenseOut(ExpenseCreate):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)  
