# from fastapi import FastAPI
# from sqlalchemy.orm import Session
# from fastapi.middleware.cors import CORSMiddleware

# import model
# import schema
# import dataset
# from dataset import SessionLocal, engine, Base

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=["*"],
#     allow_credentials=True,
#     allow_method=["*"],
#     allow_headers=["*"]
# )


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/books",response_model=schema.BookOut)
# def create_books(book: schema.BookCreate, db: Session = Depends(get_db)):
#     db_book = model.Book(**book.dict())
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book

# @app.get("/books",response_model=list[schema.BookOut])
# def get_books(author:str="",genre:str="",published_year:int=0,db:Session=Depends(get_db)):
#     query=db.query(model.Book)
#     if author:
#         query=query.filter(model.Book.author==author)
#     if genre:
#         query=query.filter(model.Book.genre==genre)
#     if published_year:
#         quer=query.filter(model.Book.published_year==published_year)
#     return query.all()


from fastapi import FastApi
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from dataset import SessionLocal
import schema
import model

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


app=FastApi()

app.add_middleware(
CORSMiddleware,
allow_origin=["*"],
allow_credentials=True,
allow_method=["*"],
allow_headers=["*"]
)


app.post("/create",response_model=schema.BookOut)
def create_book(book:schema.BookCreate,db.Session=Depends(get_db)):
    db_book=model.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
