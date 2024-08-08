from fastapi import APIRouter
from sqlalchemy.orm import Session
from models import user_model
from services import user_service
from database.connection import SessionLocal, get_db

router = APIRouter()

@router.get("/")
async def get_users():
    db = SessionLocal()
    result = user_service.get_user(db=db)
    return result

@router.post("/", response_model=user_model.User)
def create_user(user: user_model.UserCreate):
    db: Session = get_db()
    return user_service.create_user(db=db, user=user)

