from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

class ExpenseCreate(BaseModel):
    category: str
    amount: float = Field(gt=0)
    note: str | None = None

class ExpenseOut(ExpenseCreate):
    id: int
    user_id: int
    model_config = ConfigDict(from_attributes=True)  # Pydantic v2
