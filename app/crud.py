from sqlalchemy.orm import Session
from . import models, schemas, auth

# Users
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Predictions
def create_prediction(db: Session, predicted_category: int, user_id: int = None):
    db_pred = models.Prediction(predicted_category=predicted_category, user_id=user_id)
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)
    return db_pred

