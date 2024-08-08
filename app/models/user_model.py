from pydantic import BaseModel, EmailStr
from typing import Optional, List
# from .order_model import Order  

class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: Optional[str]
    address: Optional[str]

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    phone_number: Optional[str]
    address: Optional[str]

class UserInDBBase(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True # ! obsolete, from_atribute=True

class User(UserInDBBase):
    pass

# class UserWithOrders(UserInDBBase):
#     orders: List[Order]

class UserInDB(UserInDBBase):
    hashed_password: str

