from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///./test.db")
engine = create_engine(f"{DATABASE_URI}", connect_args = {"check_same_thread": False})
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()


def get_db():
    with SessionLocal() as db:
        return db

