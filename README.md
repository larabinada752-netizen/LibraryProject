# LibraryProject

This project is a **comprehensive Library Management System** developed using **Python** and **MySQL** (via phpMyAdmin).  
The goal of this project is to create a fully functional system that allows users to manage a collection of books efficiently, including adding new books, viewing existing records, updating book information, and deleting books when necessary.

I dedicated significant time and effort to designing this project, ensuring that it demonstrates a solid understanding of both **programming concepts** and **database management**.  
The system implements all the essential **CRUD operations** (Create, Read, Update, Delete), providing a clear example of how Python can be connected to a MySQL database for real-world applications.

The project was developed with attention to:
- **Data integrity** – all operations are reflected immediately in the database.
- **User interaction** – the menu-driven interface makes the system easy to use.
- **Scalability** – the system can be extended to include a GUI interface or a web-based version in the future.
- **Best practices** – structured code, reusable functions, and clear prompts for the user.

This project not only demonstrates my technical skills but also highlights my **dedication and attention to detail**, as I carefully implemented each feature and tested the system thoroughly to ensure smooth functionality. It is a strong example of my ability to design, develop, and deploy a practical application from scratch.



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

## Running the Program (Screenshot)

Here is an example of the program running in the terminal:
### terminal_run1
![Program Running](https://github.com/larabinada752-netizen/LibraryProject/blob/c1f0d334f47a0e8a353686fd0e6b67a2b3d4439d/terminal_run1.png.png)
### terminal_run2
![Program Running](https://github.com/larabinada752-netizen/LibraryProject/blob/c1f0d334f47a0e8a353686fd0e6b67a2b3d4439d/terminal_run2.png.png)

## Database Preview (phpMyAdmin)

This screenshot shows the `books` table inside phpMyAdmin:

![phpMyAdmin Books Table](https://github.com/larabinada752-netizen/LibraryProject/blob/c27d6e87cf3d14cea5bfd8fe3b4b267eb5654552/phpmyadmin_books.png.png)




## Notes
Use View Books to find the Book ID before updating or deleting.

All changes are reflected immediately in the database in phpMyAdmin.

The project can be extended later with a Tkinter GUI or a web version.

## Author
Nada Larabi
