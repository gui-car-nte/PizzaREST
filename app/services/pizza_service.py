from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import pizza_model as Pizza
from models import pizza_schema as PizzaSchema

def create_pizza(db: Session, pizza: Pizza.PizzaCreate):
    try:
        db_pizza = PizzaSchema.Pizza(
            name = pizza.name,
            ingredients = pizza.ingredients,
            price = pizza.price,
            preparation_time = pizza.preparation_time,
        )
        db.add(db_pizza)
        db.commit()
        db.refresh(db_pizza)
        return db_pizza
    except SQLAlchemyError as e:
        db.rollback() 
        raise e


async def get_all_pizzas(db: Session):
    try:
        return db.query(PizzaSchema.Pizza).all()
    except SQLAlchemyError as e:
        raise e


async def get_pizza_by_id(db: Session, pizza_id: int):
    try:
        pizza = db.query(PizzaSchema.Pizza).filter(PizzaSchema.Pizza.id == pizza_id).first()
        if not pizza:
            raise ValueError(f"Pizza with ID {pizza_id} not found")
        return pizza
    except SQLAlchemyError as e:
        raise e
