from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Pizza(Base):
    __tablename__ = 'pizzas'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ingredients = Column(String)
    price = Column(Float)
    preparation_time = Column(Integer)
    
    orders = relationship("Order", back_populates="pizza")
