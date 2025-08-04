from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def connect_db():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="",
        dbname="book_management_test"
    )

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
            published_year INT,
            genre VARCHAR(50),
            rating FLOAT CHECK (rating >= 0 AND rating <= 5)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

create_table()

@app.get("/books")
def get_books(author: str = "", genre: str = "", published_year: int = 0):
    conn = connect_db()
    cur = conn.cursor()
    query = "SELECT * FROM books WHERE TRUE"
    params = []

    if author:
        query += " AND author = %s"
        params.append(author)
    if genre:
        query += " AND genre = %s"
        params.append(genre)
    if published_year:
        query += " AND published_year = %s"
        params.append(published_year)

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    books = []
    for row in rows:
        books.append({
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "published_year": row[3],
            "genre": row[4],
            "rating": row[5],
        })

    cur.close()
    conn.close()
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {
            "id": row[0],
            "title": row[1],
            "author": row[2],
            "published_year": row[3],
            "genre": row[4],
            "rating": row[5],
        }
    return JSONResponse(status_code=404, content={"message": "Book not found"})

@app.post("/books")
async def add_book(request: Request):
    data = await request.json()
    title = data.get("title")
    author = data.get("author")
    year = data.get("published_year")
    genre = data.get("genre")
    rating = data.get("rating")

    if not title or not author or not year or not genre or rating is None:
        return JSONResponse(status_code=400, content={"message": "Missing fields"})

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO books (title, author, published_year, genre, rating)
        VALUES (%s, %s, %s, %s, %s) RETURNING id;
    """, (title, author, year, genre, rating))
    book_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return {"id": book_id, "message": "Book added"}

@app.put("/books/{book_id}")
async def update_book(book_id: int, request: Request):
    data = await request.json()
    title = data.get("title")
    author = data.get("author")
    year = data.get("published_year")
    genre = data.get("genre")
    rating = data.get("rating")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM books WHERE id = %s", (book_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        return JSONResponse(status_code=404, content={"message": "Book not found"})

    cur.execute("""
        UPDATE books SET title=%s, author=%s, published_year=%s, genre=%s, rating=%s
        WHERE id=%s;
    """, (title, author, year, genre, rating, book_id))
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Book updated"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM books WHERE id = %s", (book_id,))
    if cur.fetchone() is None:
        cur.close()
        conn.close()
        return JSONResponse(status_code=404, content={"message": "Book not found"})

    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book deleted"}
