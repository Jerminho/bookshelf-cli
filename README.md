BookShelf CLI 

What is this?
BookShelf CLI is a small command-line tool to keep track of your books and authors.
It uses a simple SQLite database, and you can do things like:
- See which authors you have
- See which books are in the database
- Add new authors or books later on
- Export your data if you want

Basically, it’s a little bookshelf in your terminal!

What’s in the project so far
- A SQLite database with two tables: authors and books
- Some sample data (2 authors and 2 books) so you can test right away
- A Database class (app/database.py) that handles all connections
- A config file (settings.ini) where the database path is stored
- A small CLI test that prints out authors from the database



You should see the authors printed out — that means everything is working!


