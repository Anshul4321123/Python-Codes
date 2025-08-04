from sqlalchemy import Column, Integer, String, Float
from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    published_year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False)
    rating = Column(Float, nullable=False)
    