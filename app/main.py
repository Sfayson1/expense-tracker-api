from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, expenses

app = FastAPI(
    title="Expense Tracker API",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
