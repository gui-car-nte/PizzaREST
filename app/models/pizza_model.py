from pydantic import BaseModel

class PizzaBase(BaseModel):
    name: str
    ingredients: str
    price: int
    preparation_time: int

class PizzaCreate(PizzaBase):
    pass

class PizzaUpdate(BaseModel):
    ingredients: str
    price: int
    preparation_time: int

class PizzaInDBBase(PizzaBase):
    id: int

    class Config:
        from_attributes = True

class Pizza(PizzaInDBBase):
    pass

