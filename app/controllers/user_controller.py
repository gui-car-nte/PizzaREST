from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import user_model
from app.services import user_service
from app.database.connection import get_db

router = APIRouter()

@router.post("/", response_model=user_model.User)
def create_user(user: user_model.UserCreate):
    db: Session = get_db()
    return user_service.create_user(db=db, user=user)

@router.post("/login", response_model=user_model.User)
def login(username: str, password: str):
    db: Session = get_db()
    try:
        user = user_service.authenticate_user(db, username, password)
        if not user:
            raise HTTPException(status_code=400, detail="Email or password is incorrect")
        return user
    finally:
        db.close()
