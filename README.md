📊 Expense Tracker API

A secure backend API for tracking personal expenses.
Built with FastAPI, PostgreSQL, SQLAlchemy, & JWT authentication.

> 🚧 Active learning project by Sherika Fayson — building skills for a backend → data engineering career path.

## ✅ Features

| Feature | Status |
|--------|:-----:|
| User registration & login | ✅ |
| JWT Authentication | ✅ |
| Create, Read, Update, Delete (CRUD) expenses | ✅ |
| Filtering by category + month | ✅ |
| Pagination support | ✅ |
| Secure password hashing (Argon2) | ✅ |
| PostgreSQL with Alembic migrations | ✅ |
| Swagger Docs | ✅ |
| Cascade delete when user is removed | ✅ |
| Sorting (newest first) | ✅ |
| Analytics endpoints | 🔜 |
| Frontend dashboard | 🔜 Future |

---

## 🏗 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Auth | JWT + OAuth2 scheme |
| Password Security | Argon2 hashing |
| Serialization | Pydantic v2 |
| Docs | OpenAPI / Swagger UI |

---

## 🧪 API Endpoints

### 🔐 Auth

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|:---:|
| `POST` | `/auth/register` | Create new user | ❌ |
| `POST` | `/auth/login` | Get a JWT token | ❌ |

### 💸 Expenses

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|:---:|
| `GET` | `/expenses/` | List user expenses (filter + paginate) | ✅ |
| `POST` | `/expenses/` | Create expense | ✅ |
| `PUT` | `/expenses/{id}` | Update expense | ✅ |
| `DELETE` | `/expenses/{id}` | Delete expense | ✅ |

✅ Filters available:
- `?category=grocery`
- `?month=2025-11`
- `?limit=50&offset=0`

---

## 🚀 Local Setup

### Clone
```bash
git clone https://github.com/Sfayson1/expense-tracker-api.git
cd expense-tracker-api
```

### Create Virtual Env & Install Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables
Create `.env`:
```
DATABASE_URL=postgresql://localhost/expenses_dev
JWT_SECRET=change-me
JWT_ALG=HS256
JWT_EXPIRE_MIN=1440
```

### Initialize the DB
```bash
python3 - <<EOF2
from app.db.session import Base, engine
import app.models
Base.metadata.create_all(bind=engine)
EOF2
```
### Alembic Migrations
```bash
# Create migration after schema changes
alembic revision --autogenerate -m "describe change"

# Apply migration
alembic upgrade head
```

### Run the Server
```bash
uvicorn app.main:app --reload
```

Docs: http://127.0.0.1:8000/docs

---
## 📅 Roadmap Progress

| Day    | Milestone                           | Status |
| ------ | ----------------------------------- | :----: |
| Day 1  | Setup + Register/Login              |    ✅   |
| Day 2  | CRUD + Auth everywhere              |    ✅   |
| Day 3  | Migrations + Filtering + Pagination |    ✅   |
| Day 4  | Analytics endpoints + tests         |   🔜   |
| Future | Dashboard UI + Deployment           |   🔜   |


## 🧑‍💻 Author
Sherika Fayson — Aspiring Backend & Data Engineer
