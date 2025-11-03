from typing import Optional
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from pydantic import BaseModel

from app.db.session import get_db
from app.core.security import get_current_user_id
import app.models as models
from app.schemas.expense import ExpenseCreate, ExpenseOut

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/", response_model=list[ExpenseOut])
def list_expenses(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
    category: Optional[str] = Query(None, description="Exact match"),
    month: Optional[str] = Query(None, description="YYYY-MM (e.g. 2025-11)"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
):
    q = db.query(models.Expense).filter(models.Expense.user_id == user_id)

    if category:
        q = q.filter(models.Expense.category == category)

    if month:
        try:
            start = datetime.strptime(month, "%Y-%m")
            next_month = (start.replace(day=28) + timedelta(days=4)).replace(day=1)
        except ValueError:
            raise HTTPException(status_code=400, detail="month must be YYYY-MM")
        q = q.filter(
            models.Expense.created_at >= start,
            models.Expense.created_at < next_month,
        )

    items = (
        q.order_by(models.Expense.created_at.desc())
         .limit(limit)
         .offset(offset)
         .all()
    )
    return items


@router.post("/", response_model=ExpenseOut, status_code=status.HTTP_201_CREATED)
def create_expense(
    payload: ExpenseCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    expense = models.Expense(**payload.model_dump(), user_id=user_id)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

@router.put("/{expense_id}", response_model=ExpenseOut)
def update_expense(
    expense_id: int,
    payload: ExpenseCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    exp = (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id, models.Expense.user_id == user_id)
        .first()
    )
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    for k, v in payload.model_dump().items():
        setattr(exp, k, v)

    db.commit()
    db.refresh(exp)
    return exp


@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
):
    exp = (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id, models.Expense.user_id == user_id)
        .first()
    )
    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(exp)
    db.commit()
    return

class SummaryOut(BaseModel):
    month: str | None
    total_spent: float
    count: int
    by_category: dict[str, float]

@router.get("/summary", response_model=SummaryOut, tags=["expenses"])
def get_expense_summary(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
    month: str | None = Query(None, description="YYYY-MM (optional)"),
):
    q = db.query(
        models.Expense.category,
        func.sum(models.Expense.amount).label("total_amount")
    ).filter(models.Expense.user_id == user_id)

    if month:
        period = month
        try:
            start = datetime.strptime(period, "%Y-%m")
            next_month = (start.replace(day=28) + timedelta(days=4)).replace(day=1)
        except ValueError:
            raise HTTPException(status_code=400, detail="month must be YYYY-MM")
        q = q.filter(
            models.Expense.created_at >= start,
            models.Expense.created_at < next_month)

    total, cnt = db.query(
        func.coalesce(func.sum(models.Expense.amount), 0),
        func.count(models.Expense.id)
    ).filter(models.Expense.user_id == user_id) \
    .filter(*q._criterion if getattr(q, '_criterion', None) else []) \
    .one()

    rows = db.query(
        models.Expense.category,
        func.coalesce(func.sum(models.Expense.amount), 0.0)
    ).filter(models.Expense.user_id == user_id) \
    .filter(*q._criterion if getattr(q, '_criterion', None) else []) \
    .group_by(models.Expense.category).all()

    by_cat = {c: float(a) for c, a in rows}

    return SummaryOut(
        month=period,
        total_spent=float(total),
        count=int(cnt),
        by_category=by_cat)

class DayPoint(BaseModel):
    date: str
    total: float
@router.get("/trend", response_model=list[DayPoint], tags=["expenses"])
def expenses__trend(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
    days: int = Query(30, ge=1, le=365),
):
    end = datetime.now()
    start = end - timedelta(days=days)
    rows = (
        db.query(
            func.date_trunc("day", models.Expense.created_at).label("d"),
            func.coalesce(func.sum(models.Expense.amount), 0.0).label("total")
        )
        .filter(
            models.Expense.user_id == user_id,
            models.Expense.created_at >= start,
            models.Expense.created_at <= end
        )
        .group_by(func.date_trunc("day", models.Expense.created_at))
        .order_by(func.date_trunc("day", models.Expense.created_at))
        .all()
    )

    return [DayPoint(date=r.d.date().isoformat(), total=float(r.total)) for r in rows]
