from fastapi import FastAPI
from app.database.connection import engine, Base
from app.controllers import user_controller, order_controller, pizza_controller

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_controller.router, prefix="/api/users", tags=["users"])
app.include_router(order_controller.router, prefix="/api/orders", tags=["orders"])
app.include_router(pizza_controller.router, prefix="/api/pizzas", tags=["pizzas"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pizza API!"}
