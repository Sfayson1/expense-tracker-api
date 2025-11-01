from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=256)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config: orm_mode = True
