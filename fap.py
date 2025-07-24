from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()


@app.post("/login/add")
def login(user: str = Form(...), pas: str = Form(...), email: str = None, file: UploadFile = File(...), username: str = "", password: str = ""):
    return {"user": user, "password": pas, "email": email, "file_size": len(file.file.read()), "username": username, "password": password}
