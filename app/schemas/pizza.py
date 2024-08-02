from pydantic import BaseModel
from typing import List
from app.schemas.order import Order

class PizzaBase(BaseModel):
    name: str
    ingredients: str
    price: float
    preparation_time: int

class PizzaCreate(PizzaBase):
    pass

class PizzaUpdate(BaseModel):
    ingredients: str
    price: float
    preparation_time: int

class PizzaInDBBase(PizzaBase):
    id: int

    class Config:
        orm_mode = True

class Pizza(PizzaInDBBase):
    pass

class PizzaWithOrders(PizzaInDBBase):
    orders: List[Order]
