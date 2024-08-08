from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key = True, index = True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    delivery_info = Column(String)
    pizza_details = Column(String)
    user = relationship("User", back_populates = "orders")

