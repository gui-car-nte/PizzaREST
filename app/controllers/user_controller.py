from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.models import user_model
from app.services import user_service
from app.database.connection import get_db

router = APIRouter()

@router.post("/", response_model=user_model.User)
def create_user(user: user_model.UserCreate):
    db: Session = get_db()
    return user_service.create_user(db=db, user=user)

