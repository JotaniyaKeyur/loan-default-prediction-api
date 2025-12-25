# 🚀 Loan Default Prediction API (Production-Ready ML System)

A **full-stack, production-grade Machine Learning API** that predicts whether a borrower is likely to default on a loan, built with real-world engineering practices — not just a trained model.

This project demonstrates how to take an ML solution **from data preprocessing → model training → API → database → authentication → migrations**, exactly how it works in industry.

---

## 📌 Problem Statement

Predict loan default risk using historical financial and behavioral data. This is a **core problem in fintech, credit scoring, and risk analytics**, where accuracy, robustness, and system reliability matter.

---

## 🧠 Machine Learning Pipeline

Built completely from scratch:

- Data Cleaning & **MICE Imputation**
- Advanced **Feature Engineering** (risk-aware derived features)
- **SMOTE** to handle class imbalance
- Hyperparameter tuning using **Optuna + StratifiedKFold**
- **XGBoost Classifier** optimized on **ROC-AUC**
- Model persistence & reusable inference pipeline

The trained model is stored and loaded for real-time inference via the API.

---

## ⚙️ Backend & System Architecture

### 🔧 Tech Stack

- **FastAPI** – High-performance REST API framework
- **Pydantic** – Input validation & computed fields
- **SQLAlchemy ORM** – Database abstraction
- **Alembic** – Database migrations & schema versioning
- **SQLite** – Lightweight relational database
- **JWT Authentication** – Secure auth-ready endpoints
- **Uvicorn** – ASGI server

---

## 🗂️ Project Structure

```
loan-default-prediction-api/
│
├── alembic/              # Alembic migration scripts
├── alembic.ini           # Alembic configuration
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── database.py       # DB connection & session
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # DB operations
│   ├── auth.py           # JWT & password hashing
│   ├── ml_model.py       # ML inference logic
│   └── __init__.py
│
├── model.pkl             # Trained ML model
├── mlapi.db              # SQLite database
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── .env.example          # Environment variables template
```

---

## 🔐 Authentication

- JWT-based authentication
- Secure password hashing with **bcrypt**
- Token-based access ready for role-based extensions

---

## 📡 API Endpoints

### 🔑 Auth

- `POST /signup` – Register a new user
- `POST /login` – Authenticate and receive JWT token

### 🤖 Prediction

- `POST /predict` – Predict loan default category

Swagger UI available at:
```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Prediction Request

```json
{
  "RevolvingUtilizationOfUnsecuredLines": 0.45,
  "age": 45,
  "NumberOfTime30_59DaysPastDueNotWorse": 1,
  "DebtRatio": 0.8,
  "MonthlyIncome": 5000,
  "NumberOfOpenCreditLinesAndLoans": 6,
  "NumberOfTimes90DaysLate": 0,
  "NumberRealEstateLoansOrLines": 1,
  "NumberOfTime60_89DaysPastDueNotWorse": 0,
  "NumberOfDependents": 2
}
```

The API automatically computes derived risk features internally.

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/JotaniyaKeyur/loan-default-prediction-api.git
cd loan-default-prediction-api
```

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
DATABASE_URL=sqlite:///./mlapi.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Run Database Migrations

```bash
alembic upgrade head
```

### 6️⃣ Start the API Server

```bash
uvicorn app.main:app --reload
```

Open browser:
```
http://127.0.0.1:8000/docs
```

---

## 🧩 Debugging & Engineering Lessons

This project involved real-world debugging challenges:

- Python dependency conflicts (NumPy / Pandas / XGBoost)
- Model compatibility across versions
- Alembic + environment variable issues
- Production-safe password hashing
- API failure tracing & logging

➡️ These lessons are documented in a **LinkedIn follow-up post** (see comments).

---

## 🚀 Future Improvements

- Switch SQLite → **PostgreSQL**
- Dockerize the application
- CI/CD pipeline (GitHub Actions)
- Model versioning & monitoring
- Role-based access control

---

## 👤 Author

**Keyur Jotaniya**  
Aspiring AI / ML Engineer | Backend & Production ML Enthusiast

🔗 GitHub: https://github.com/JotaniyaKeyur

---

⭐ If you found this project useful, consider starring the repository!

