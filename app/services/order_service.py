from sqlalchemy.orm import Session
from app.models import order_model, order_schema

def create_order(db: Session, order: order_model.OrderCreate):
    db_order = order_schema.Order(
        user_id=order.user_id,
        date=order.date,
        delivery_info=order.delivery_info,
        pizza_details=order.pizza_details,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(order_model.Order).filter(order_schema.Order.id == order_id).first()

