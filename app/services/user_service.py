from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from app.services.auth_service import get_password_hash

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = user_model.User(
        username=user.username,
        hashed_password=hashed_password,
        email=user.email,
        phone_number=user.phone_number,
        address=user.address
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

