from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database.connection import Base
from datetime import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    pizza_id = Column(Integer, ForeignKey('pizzas.id'))
    quantity = Column(Integer)
    status = Column(String, default="Pending")
    order_date = Column(DateTime, default=datetime.now)
    delivery_address = Column(String)
    
    user = relationship("User", back_populates="orders")
    pizza = relationship("Pizza", back_populates="orders")
