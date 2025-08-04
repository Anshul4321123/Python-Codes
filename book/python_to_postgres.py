import psycopg2
import psycopg2.extras

hostname="localhost"
port=5432
username="postgres"
pwd="Anshul@896"
port_id=5432
database="book_management_test"
conn=None
cur=None
try:
    conn = psycopg2.connect(
        host=hostname,
        port=port_id,
        user=username,
        password=pwd,
        dbname=database
    )
    cur= conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    create_script = '''CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        author VARCHAR(100) NOT NULL,
        published_year INT NOT NULL,
        genre VARCHAR(50) NOT NULL,
        rating FLOAT CHECK (rating >= 0 AND rating <= 5)
        );'''
    
    # cur.execute(create_script)

    # insert_script = '''INSERT INTO books (title, author, published_year, genre, rating)
    #                   VALUES (%s, %s, %s, %s, %s);'''
    # insert_values = ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction', 4.5)

    # cur.execute(insert_script, insert_values)

    cur.execute("SELECT * FROM books;")
    print(cur.fetchall())

    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
  if conn is not None:
    conn.close()
  if cur is not None:
    cur.close()