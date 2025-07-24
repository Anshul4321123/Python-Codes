from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()

@app.get("/")
def first():
    return {"message":"Hello, world!"}


@app.post("/login")
def login(username:str=(Form(...)),password:str=(Form(...))):
    return {"username":username,"password":password}

@app.post("/uploadfile")
def upload_file(file:UploadFile = (File(...))):
    with open(f"upload/{file.filename}","wb") as f:
        f.write(file.file.read())
        return {"filename":file.filename}
    

@app.post("/savefile")
def save_file(file:List[UploadFile]=File(...)):
    