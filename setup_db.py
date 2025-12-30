import sqlite3

DB_PATH = "data/bookshelf.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create authors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bio TEXT
)
""")

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    author_id INTEGER,
    genre TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
)
""")

# Insert sample authors
cursor.execute("INSERT INTO authors (name, bio) VALUES ('J.K. Rowling', 'British author'), ('George Orwell', 'British novelist')")

# Insert sample books
cursor.execute("INSERT INTO books (title, year, author_id, genre) VALUES ('Harry Potter and the Sorcerer''s Stone', 1997, 1, 'Fantasy'), ('1984', 1949, 2, 'Dystopian')")

conn.commit()
conn.close()

print("Database created with sample data!")
