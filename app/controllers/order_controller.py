from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import order_schema, order_model
from app.services import order_service
from app.database.connection import get_db

router = APIRouter()

@router.post("/", response_model=order_schema.Order)
def create_order(order: order_model.OrderCreate):
    db: Session = get_db()
    try:
        return order_service.create_order(db=db, order=order)
    finally:
        db.close()

@router.get("/{order_id}", response_model=order_model.OrderWithUser)
def get_order(order_id: int):
    db: Session = get_db()
    try:
        return order_service.get_order(db=db, order_id=order_id)
    finally:
        db.close()
