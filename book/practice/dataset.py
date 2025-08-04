from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="postgresql://postgres:Anshul%40896@localhost:5432/book_management_test"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine, autoflush=False,autocommit=False)
Base=declarative_base( )

