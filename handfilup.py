from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/login")
def login(username: str = (Form(...)), password: str = (Form(...))):
    return {"username": username, "password": password}


@app.post("/uploadfile")
def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.post("/savefile")
def save_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as f:
        f.write(file.file.read())
    return {"filename": file.filename, "content_type": file.content_type}


app.post("/savefiles")


def save_files(files: list[UploadFile] = File(...)):
    file_details = []
    for file in files:
        with open(f"uploads/{file.filename}", "wb") as f:
            f.write(file.file.read())
        file_details.append({
            "filename": file.filename,
            "content_type": file.content_type
        })
    return {"files": file_details}


@app.post("/upload/")
async def handle_form_and_file(
    username: str = Form(...),
    age: int = Form(...),
    file: UploadFile = File(...)
):
    content = await file.read()

    return JSONResponse({
        "username": username,
        "age": age,
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size": len(content)
    })
