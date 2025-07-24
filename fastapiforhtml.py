from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = [
    {"username": "john", "password": "1234"},
    {"username": "jane", "password": "abcd"},
    {"username": "doraemon", "password": "nobita"}
]

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return JSONResponse(content={"message": "Login successful!"}, status_code=200)
    return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)
