# LibraryProject


This project is a **simple Library Management System** built using **Python** and **MySQL** (phpMyAdmin).  
It allows you to add books, view them, update book details, and delete books easily.

---

## **Features**
- Add a new book with details: Title, Author, Year Published, Genre.  
- View all books in the database.  
- Update any book's details using its **Book ID**.  
- Delete a book using its **Book ID**.  
- Connect to MySQL using the `mysql-connector-python` library.  

---

## **Requirements**
- Python 3.x  
- MySQL (recommended via XAMPP)  
- Python library: `mysql-connector-python`  

Install the library via:

pip install mysql-connector-python
## Database Setup
Open phpMyAdmin.

Create a database named library_db.

Run the following SQL code to create the books table:


CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year_published INT,
    genre VARCHAR(100)
);
## Running the Program
1 Make sure MySQL is running in XAMPP.

2 Open VS Code in the project folder.

3 Run the Python file:


python library.py
4 You will see the menu:


1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Exit
5 Follow the instructions to manage books in the library.

## Notes
Use View Books to find the Book ID before updating or deleting.

All changes are reflected immediately in the database in phpMyAdmin.

The project can be extended later with a Tkinter GUI or a web version.

## Author
Nada Larabi
