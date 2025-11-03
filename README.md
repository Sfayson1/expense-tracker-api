📊 Expense Tracker API

A secure backend API for tracking personal expenses.
Built with FastAPI, PostgreSQL, SQLAlchemy, & JWT authentication.

> 🚧 Active learning project by Sherika Fayson — building skills for a backend → data engineering career path.

## ✅ Features

| Feature                                               |   Status  |
| ----------------------------------------------------- | :-------: |
| User registration & login                             |     ✅     |
| JWT authentication                                    |     ✅     |
| Create / list / update / delete expenses              |     ✅     |
| PostgreSQL + SQLAlchemy ORM                           |     ✅     |
| Argon2 password hashing                               |     ✅     |
| Swagger API docs (`/docs`)                            |     ✅     |
| Filtering expenses (category, search, amounts, dates) |     ✅     |
| Sorting + Pagination with total count                 |     ✅     |
| Stats endpoints (monthly summary & totals by month)   |     ✅     |
| Database migrations (Alembic)                         |     ✅     |
| Composite indexes for performance                     |     ✅     |
| Frontend dashboard                                    | 🔜 Future |


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

### 🔎 Filters on /expenses/:
```bash
/expenses/?category=food&q=grocery&min_amount=5&max_amount=50
/date_from=2025-01-01&date_to=2025-02-01
/month=2025-11&sort=amount&order=asc&limit=20&offset=0
```

### 📈 Stats
Method	Endpoint	Returns
GET	/expenses/stats/summary?month=YYYY-MM	Total, avg, by-category breakdown
GET	/expenses/stats/by-month?year=YYYY	Monthly totals for charting

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
## 📅 Roadmap

✅ Day 4 Complete: Filtering + Pagination + Stats + Indexes
🔜 Day 5: React Dashboard UI
🔜 Day 6: Docker + Deployment
✨ Future: Authentication UI, charts, category icons, budgeting tips


## 🧑‍💻 Author
Sherika Fayson — Aspiring Backend & Data Engineer
