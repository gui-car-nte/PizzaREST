from sqlalchemy.orm import Session
from app.models import user_model, user_schema
from app.services.auth_service import hash_password

async def get_users_all(db: Session):
    with db as data:
        db_user = data.query(user_schema.User).all()
        return db_user


async def get_user_by_id(db: Session, user_id: int):
    with db as session:
        return session.query(user_schema.User).filter(user_schema.User.id == user_id).first()


async def create_user(db: Session, user: user_model.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = user_schema.User(
        username = user.username,
        hashed_password = hashed_password,
        email = user.email,
        phone_number = user.phone_number,
        address = user.address
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def update_user(db: Session, user: user_model.User, update_info: user_model.UserUpdate):
    user = db.merge(user)

    if update_info.email:
        user.email = update_info.email
    if update_info.username:
        user.username = update_info.username
    if update_info.phone_number:
        user.phone_number = update_info.phone_number
    if update_info.address:
        user.address = update_info.address

    db.commit()
    db.refresh(user)
    return user
