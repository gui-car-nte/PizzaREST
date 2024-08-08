from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import pizza_schema, pizza_model
from app.services import pizza_service
from app.database.connection import get_db

router = APIRouter()

@router.post("/", response_model = pizza_model.Pizza)
def create_pizza(pizza: pizza_model.PizzaCreate):
    db: Session = get_db()
    try:
        return pizza_service.create_pizza(db=db, pizza=pizza)
    finally:
        db.close()

@router.get("/", response_model = list[pizza_model.Pizza])
def list_pizzas():
    db: Session = get_db()
    try:
        return pizza_service.list_pizzas(db=db)
    finally:
        db.close()

