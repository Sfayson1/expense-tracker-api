from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app import models
from app.schemas.user import UserCreate, UserOut
from app.core.security import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/register", response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter_by(email=payload.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    u = models.User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(u); db.commit(); db.refresh(u)
    return u

@router.post("/login")
def login(payload: UserCreate, db: Session = Depends(get_db)):
    u = db.query(models.User).filter_by(email=payload.email).first()
    if not u or not verify_password(payload.password, u.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_token(u.id), "token_type": "bearer"}
