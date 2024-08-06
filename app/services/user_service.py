from sqlalchemy.orm import Session
from app.models import user_model, user_schema

def create_user(db: Session, user: user_model.UserCreate):
    db_user = user_schema.User(
        username=user.username,
        email=user.email,
        phone_number=user.phone_number,
        address=user.address,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(user_schema.User).filter(user_schema.User.username == username).first()
    if user and user.password == password: # type: ignore # TODO check what is causing this warning
        return user
    return None
