from sqlalchemy.orm import Session
from app.models import user_model, user_schema
from app.services.auth_service import hash_password

def create_user(db: Session, user: user_model.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = user_schema.User(
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

