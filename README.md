# PizzaREST API
PizzaREST is a RESTful API built with FastAPI for managing users, orders, and pizzas. This API allows you to create, read, update, and delete users, orders, and pizzas, while implementing basic authentication and other features.

## Table of Contents
- Features
- Installation
- Environment Variables
- Running the Application
- API Endpoints
    - User Endpoints
    - Order Endpoints
    - Pizza Endpoints
- Authentication
- Database
- License
## Features
User Management: Create, update, delete, and view users.
Order Management: Create, update, delete, and view pizza orders.
Pizza Management: Create, update, delete, and view pizzas.
Basic Authentication: Implemented with username and password (Base64 hashed).
Database Integration: Uses SQLAlchemy with a SQLite database (by default).
## Installation
### 1. Clone the repository:
```
git clone https://github.com/yourusername/PizzaREST.git
cd PizzaREST
```
### 2. Create and activate a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
On Windows use: .venv\Scripts\activate
```
### 3. Install the dependencies:
```
pip install -r requirements.txt
```
## Environment Variables
Create a .env file in the root directory and add the following variables:
```
DATABASE_URI=sqlite:///./test.db
```
This will the default URI used by the program, you can change it to anything you would like in your .env file
## Running the Application
### 1. Run main.py
```
python3 main.py
```
This automatically runs the server with uvicorn
### 2. Access the API:
- The API will be available at http://127.0.0.1:8000.
- Access the interactive API docs at http://127.0.0.1:8000/docs.
## API Endpoints
### User Endpoints
- Create a User: POST /api/users/
    - Request Body: { "username": "string", "email": "string", "password": "string" }
- Update User Information: PUT /api/users/
    - Request Body: { "phone_number": "string", "address": "string" }
- Get User by ID: GET /api/users/{user_id}
### Order Endpoints
- Create an Order: POST /api/orders/
    - Request Body: { "user_id": int, "delivery_info": "string", "pizza_details": "string" }
- Update Delivery Info: PUT /api/orders/{order_id}/delivery_info
    - Request Body: { "delivery_info": "string" }
- Get Order by ID: GET /api/orders/{order_id}
### Pizza Endpoints
- Create a Pizza: POST /api/pizzas/
    - Request Body: { "name": "string", "ingredients": "string", "price": float, "preparation_time": "string" }
- Get All Pizzas: GET /api/pizzas/
- Get Pizza by ID: GET /api/pizzas/{pizza_id}
## Authentication
Basic authentication is implemented using a username and password, where the password is Base64 hashed.
- Login: Obtain a session cookie by sending the correct credentials.
- Protected Endpoints: Certain endpoints require authentication via the session cookie.
## Database
The application uses SQLAlchemy with a SQLite database by default. You can change the database by modifying the DATABASE_URI in the .env file.
- Database Schemas: Defined in app/models/.
## License
This project is licensed under the MIT License.