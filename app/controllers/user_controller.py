from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.services import user_service
from app.database.connection import get_db

router = APIRouter()

@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate):
    db: Session = get_db()
    return user_service.create_user(db=db, user=user)