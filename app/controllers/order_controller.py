from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from models import order_model as Order
from services import order_service as OrderService
from database.connection import get_db

router = APIRouter()


@router.post("/", response_model = Order.Order) 
def create_order_endpoint(order: Order.OrderCreate):
    db: Session = get_db()
    return OrderService.create_order(db = db, order = order)


@router.get("/{order_id}", response_model = Order.OrderWithUser)
def get_order(order_id: int):
    db: Session = get_db()
    return OrderService.get_order_by_id(db = db, order_id = order_id)


@router.put("/{order_id}/delivery_info", response_model = Order.Order)
async def update_order_delivery_info(order_id: int, delivery_info: str):
    try:
        db: Session = get_db()
        updated_order = await OrderService.update_order_delivery_info(db, order_id, delivery_info)
        
        return updated_order
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = str(e))
