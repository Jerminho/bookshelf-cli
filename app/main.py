from database import Database

def main():
    db = Database()
    cursor = db.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    print("Authors in database:")
    for author in authors:
        print(author)

if __name__ == "__main__":
    main()
