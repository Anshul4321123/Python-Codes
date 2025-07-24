from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    username: str
    email: str
    address: Address  # Nested model


@app.post("/users/")
def create_user(user: User):
    return {"user": user}
#  More Complex: Lists and Optional Fields


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Order(BaseModel):
    order_id: int
    items: List[Item]       # List of nested models
    total: float


@app.post("/orders/")
def create_order(order: Order):
    return order
