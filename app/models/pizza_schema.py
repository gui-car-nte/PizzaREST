from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    ingredients = Column(String)
    price = Column(Integer)
    preparation_time = Column(Integer)

