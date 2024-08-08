from fastapi import APIRouter, HTTPException, Request, status
from sqlalchemy.orm import Session
from models import user_model as User
from services import user_service as UserService, auth_service as Auth_Service
from database.connection import get_db

router = APIRouter()

@router.get("/")
async def get_users():
    db = get_db()
    result = await UserService.get_users_all(db = db)
    return result


@router.post("/", response_model = User.User)
def create_user(user: User.UserCreate):
    db: Session = get_db()
    return UserService.create_user(db = db, user = user)


@router.put("/", response_model = User.UserUpdate)
async def update_user_info(user_update: User.UserUpdate, request: Request):
    try:
        db = get_db()
        user_id = Auth_Service.get_user_by_cookie(request)
        user = await UserService.get_user_by_id(db, int(user_id))
        
        if user is None:
            raise HTTPException(status_code = 404, detail = "User not found :^(")
        
        new_info = await UserService.update_user(db, user, user_update)
        
        return new_info

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(e))
