📊 Expense Tracker API

A secure backend API for tracking personal expenses.
Built with FastAPI, PostgreSQL, SQLAlchemy, & JWT authentication.

> 🚧 Active learning project by Sherika Fayson — building skills for a backend → data engineering career path.

## ✅ Features
| Feature | Status |
|--------|:-----:|
| User registration + login | ✅ |
| JWT Authentication | ✅ |
| Create & list expenses | ✅ |
| Secure password hashing (Argon2) | ✅ |
| PostgreSQL database | ✅ |
| Swagger API docs (/docs) | ✅ |
| Update/Delete expenses | 🔜 |
| Migrations via Alembic | 🔜 |
| Filtering + sorting expenses | 🔜 |
| Frontend dashboard | 🔜 Future |

## 🏗️ Tech Stack
| Layer | Technology |
|------|------------|
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic v2 |
| Auth | JWT + Argon2 hashing |
| Docs | Swagger (OpenAPI) |


## 🧪 API Endpoints

### Auth
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:------------:|
| POST | /auth/register | Create a new user | ❌ |
| POST | /auth/login | Get access token | ❌ |

### Expenses
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|:------------:|
| GET | /expenses/ | List user’s expenses | ✅ |
| POST | /expenses/ | Create an expense | ✅ |

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

### 📌 API Endpoints
#### 🔑 Authentication (/auth)
Method	Endpoint	Description
POST	/auth/register	Create user
POST	/auth/login	Login → returns JWT

#### 💰 Expenses (/expenses)
Method	Endpoint	Description
GET	/expenses/	List user expenses (with filters + pagination)
POST	/expenses/	Create new expense
PUT	/expenses/{id}	Update user’s expense
DELETE	/expenses/{id}	Delete user’s expense

### 🔍 Filters
Query Param	Example	Meaning
category	?category=food	Filter by category
month	?month=2025-11	Only expenses from November 2025
limit	?limit=25	Pagination size
offset	?offset=25	Skip records

### ✅ Day 4 Preview

Next step in your backend mastery:

#### 🚀 Add Budget Goals:

* POST /goals/
* GET /goals/summary
* Automatically calculate month spend vs. goal

#### 👤 Add Users API scope:

* GET /auth/me for profile
* Ability to update email/password

#### 📊 Data Visualization API:

* Spend by category chart
* Monthly trend chart

### ⭐️ Future Plans

✅ Deploy to the cloud (Railway, Render, Vercel)
✅ Add testing (pytest)
✅ Add receipts with file uploads
✅ Full frontend UI (React)

---

## 🧑‍💻 Author
Sherika Fayson — Aspiring Backend & Data Engineer
