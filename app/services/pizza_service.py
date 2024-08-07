from sqlalchemy.orm import Session
from app.models import pizza_model, pizza_schema

def create_pizza(db: Session, pizza: pizza_model.PizzaCreate):
    db_pizza = pizza_schema.Pizza(
        name=pizza.name,
        ingredients=pizza.ingredients,
        price=pizza.price,
        preparation_time=pizza.preparation_time,
    )
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def list_pizzas(db: Session):
    return db.query(pizza_model.Pizza).all()
