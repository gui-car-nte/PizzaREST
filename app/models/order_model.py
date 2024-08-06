from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    pizza_id: int
    quantity: int
    delivery_address: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    status: Optional[str] = "Pending"

class OrderInDBBase(OrderBase):
    id: int
    user_id: int
    order_date: datetime
    status: str

    class Config:
        orm_mode = True

class Order(OrderInDBBase):
    pass
