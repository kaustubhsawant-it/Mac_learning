import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

print("Connected to DB")
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    isbn TEXT
    )
'''
)

def add_books(title,author, year, isbn):
    cursor.execute("insert into books(title, author, year, isbn) values (?,?,?,?)"),(title,author,year,isbn)
    conn.commit()

def view_books():
    cursor.execute("Select * from books")
    return cursor.fetchall()

def search_books(title="", author=""):
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", 
                   ('%' + title + '%', '%' + author + '%'))
    results = cursor.fetchall()
    if results:
        for book in results:
            print(book)
    else:
        print("❌ No books found.")

def update_book(book_id, title, author, year, isbn):
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", 
                   (title, author, year, isbn, book_id))
    conn.commit()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()    

while True:
    print("\n📚 Library Menu")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year: ")
        isbn = input("ISBN: ")
        add_books(title, author, year, isbn)

    elif choice == '2':
        view_books()

    elif choice == '3':
        title = input("Search Title (optional): ")
        author = input("Search Author (optional): ")
        search_books(title, author)

    elif choice == '4':
        book_id = input("Enter Book ID to update: ")
        title = input("New Title: ")
        author = input("New Author: ")
        year = input("New Year: ")
        isbn = input("New ISBN: ")
        update_book(book_id, title, author, year, isbn)

    elif choice == '5':
        book_id = input("Enter Book ID to delete: ")
        delete_book(book_id)

    elif choice == '6':
        print("👋 Exiting. Goodbye!")
        break

    else:
        print("❌ Invalid option. Try again.")