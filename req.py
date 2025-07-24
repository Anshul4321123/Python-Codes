from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str  

@app.get("/login/{user}")
def login(user: str):
    return {"message": f"Welcome back, {user}!"}

@app.get("/user/{user}")
def get_user(user: str):
    if user == "admin":
        return {"message": "Welcome back, admin!"}
    else:
        raise HTTPException(status_code=403, detail="Access denied for non-admin users.")

@app.post("/user/")
def create_user(user: User):
    return {"message": f"User {user.username} created successfully!"}