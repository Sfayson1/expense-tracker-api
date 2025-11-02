from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app import models
from app.core.security import decode_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.expense import ExpenseCreate, ExpenseOut

auth_scheme = HTTPBearer()

router = APIRouter()


def get_current_user_id(creds: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> int:
    token = creds.credentials
    try:
     return decode_token(token)
    except Exception:
       raise HTTPException(
           status_code=401,
           detail="Invalid or expired token",
           headers={"WWW-Authenticate": "Bearer"},
       )

@router.get("/")
def list_expenses(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return db.query(models.Expense).filter(models.Expense.user_id == user_id).all()

@router.post("/", response_model=ExpenseOut, status_code=status.HTTP_201_CREATED)
def create_expense(payload: ExpenseCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    expense = models.Expense(**payload.model_dump(), user_id=user_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense
