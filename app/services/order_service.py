from sqlalchemy.orm import Session
from datetime import datetime
from models.order_model import Order, OrderCreate
from models.order_schema import Order as OrderSchema

def create_order(db: Session, order: OrderCreate):
    db_order = OrderSchema(
        user_id = order.user_id,
        date = order.date or datetime.now(),
        delivery_info = order.delivery_info,
        pizza_details = order.pizza_details,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first() # type: ignore # ! Look into what is causing thsi warning


async def update_order_delivery_info(db: Session, order_id: int, delivery_info: str) -> Order:
    order = db.query(Order).filter(Order.id == order_id).first() # type: ignore # ! Look into what is causing thsi warning
    
    if not order:
        raise Exception(f"Order with ID {order_id} not found.")
    
    order.delivery_info = delivery_info
    db.commit()
    db.refresh(order)
    
    return order