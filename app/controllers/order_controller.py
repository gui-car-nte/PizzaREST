from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.models import order_model as Order
from app.services import order_service as OrderService
from app.database.connection import get_db

router = APIRouter()


@router.post("/", response_model = Order.OrderCreate)
def create_order(order: Order.Order):
    db: Session = get_db()
    try:
        return OrderService.create_order(db = db, order = order)
    finally:
        db.close()


@router.get("/{order_id}", response_model = Order.OrderWithUser)
def get_order(order_id: int):
    db: Session = get_db()
    try:
        return OrderService.get_order_by_id(db = db, order_id = order_id)
    finally:
        db.close()


@router.put("/{order_id}/delivery_info", response_model = Order.Order)
async def update_order_delivery_info(order_id: int, delivery_info: str):
    try:

        db: Session = get_db()
        updated_order = await OrderService.update_order_delivery_info(db, order_id, delivery_info)
        
        return updated_order
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(e))
