from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str
    author: str
    published_year: int
    genre: str
    rating: float = Field(ge=0, le=5)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookOut(BookBase):
    id: int

    class Config:
        form_mode = True
    