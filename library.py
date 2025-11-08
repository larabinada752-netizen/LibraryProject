import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="",     
    database="library_db"
)

cursor = conn.cursor()


def add_book(title, author, year, genre):
    sql = "INSERT INTO books (title, author, year_published, genre) VALUES (%s, %s, %s, %s)"
    values = (title, author, year, genre)
    cursor.execute(sql, values)
    conn.commit()
    print("Book added successfully!")

def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        for book in books:
            print(book)
    else:
        print("No books found.")

def update_book(book_id, title, author, year, genre):
    sql = "UPDATE books SET title=%s, author=%s, year_published=%s, genre=%s WHERE id=%s"
    values = (title, author, year, genre, book_id)
    cursor.execute(sql, values)
    conn.commit()
    print("Book updated successfully!")

def delete_book(book_id):
    sql = "DELETE FROM books WHERE id=%s"
    cursor.execute(sql, (book_id,))
    conn.commit()
    print("Book deleted successfully!")


def menu():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year Published: "))
            genre = input("Genre: ")
            add_book(title, author, year, genre)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = int(input("Book ID to update: "))
            title = input("New Title: ")
            author = input("New Author: ")
            year = int(input("New Year Published: "))
            genre = input("New Genre: ")
            update_book(book_id, title, author, year, genre)
        elif choice == "4":
            book_id = int(input("Book ID to delete: "))
            delete_book(book_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

menu()

cursor.close()
conn.close()

