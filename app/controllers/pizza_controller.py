from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.models import pizza_model as Pizza
from app.services import pizza_service as PizzaService
from app.database.connection import get_db

router = APIRouter()

@router.post("/", response_model = Pizza.Pizza)
def create_pizza(pizza: Pizza.PizzaCreate):
    db: Session = get_db()
    try:
        return PizzaService.create_pizza(db = db, pizza = pizza)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = str(e))


@router.get("/", response_model = list[Pizza.Pizza])
async def list_pizzas():
    db: Session = get_db()
    try:
        return await PizzaService.get_all_pizzas(db = db)
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))

@router.get("/{pizza_id}", response_model = Pizza.Pizza)
async def get_pizza_by_id(pizza_id: int):
    db: Session = get_db()
    try:
        return await PizzaService.get_pizza_by_id(db = db, pizza_id = pizza_id)
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = str(ve))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))
