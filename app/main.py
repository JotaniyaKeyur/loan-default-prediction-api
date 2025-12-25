from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas, crud, auth, database, ml_model

# DB
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db_session():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User routes
@app.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user)

@app.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(get_db_session)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

# ML predict route
@app.post("/predict", response_model=schemas.PredictionOut)
def predict(input_data: schemas.PredictionInput, db: Session = Depends(get_db_session)):
    predicted_category = ml_model.predict(input_data)
    crud.create_prediction(db, predicted_category)
    return {"predicted_category": predicted_category}
