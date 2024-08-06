from pydantic import BaseModel
from typing import List
from datetime import datetime
from models.user_model import User

class OrderBase(BaseModel):
    user_id: int
    date: datetime
    delivery_info: str
    pizza_details: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    delivery_info: str
    pizza_details: str

class OrderInDBBase(OrderBase):
    id: int

    class Config:
        orm_mode = True

class Order(OrderInDBBase):
    pass

class OrderWithUser(OrderInDBBase):
    user: User 