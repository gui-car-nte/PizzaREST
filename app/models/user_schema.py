from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True)
    email = Column(String, unique = True, index = True)
    hashed_password = Column(String)
    phone_number = Column(String)
    address = Column(String)
    is_active = Column(Boolean, default = True)
    is_admin = Column(Boolean, default = False)
    orders = relationship("Order", back_populates = "user")
