from pydantic import BaseModel,Field

class BookBase(BaseModel):
    title:str
    author:str
    published_year:int= Field(ge=1900,le=2025)
    genre:str
    rating:int = Field(ge=0,le=5)

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    pass