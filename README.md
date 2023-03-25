# Book Management System
This Python code is a Book Management System that allows you to perform CRUD (Create, Read, Update, Delete) operations on books in a JSON file called "books.json".

## Requirements
Python 3.x is required to run this code.

## How to use
1. Clone the repository or download the code files.
2. Open a terminal or command prompt in the directory where the code files are located.
3. Run the code using the command **`python book_management_system.py`**.
4. Follow the prompts to perform CRUD operations on books.

## Features
- Add a book: You can add a book by providing its ID, title, author, and year of publication. The book will be added to the "books.json" file.
- Get titles of books: You can get the titles of all the books stored in the "books.json" file. The titles will be displayed with pagination, 10 titles per page.
- Update a book: You can update the details of an existing book by providing its ID. You can update the title, author, and year of publication.
- Delete a book: You can delete a book by providing its ID. The book will be deleted from the "books.json" file.
- Get author names: You can get the names of all the authors of the books stored in the "books.json" file.

## Code Structure
The code is structured as follows:

- The **`BookDetails`** class defines the attributes of a book (id, title, author, year).
- The **`getBooksId`** function returns a list of all the book IDs stored in the "books.json" file.
- The **`addBook`** function prompts the user to enter the details of a new book, creates a BookDetails object, adds it to the "books.json" file, and saves the file.
- The **`getTitleOfBooks`** function displays the titles of all the books stored in the "books.json" file with pagination.
- The **`updateBook`** function prompts the user to enter the ID of the book to be updated, retrieves the book details from the "books.json" file, prompts the user to enter the updated details, updates the book object, saves it to the "books.json" file, and saves the file.
- The **`deleteBook`** function prompts the user to enter the ID of the book to be deleted, retrieves the book details from the "books.json" file, deletes the book object, saves the updated book list to the "books.json" file, and saves the file.
- The **`getAuthorsName`** function retrieves the names of all the authors of the books stored in the "books.json" file and displays them.
- The **`mapToFunctionality`** dictionary maps the user's choice to the corresponding function. The user is prompted to choose an operation, and the corresponding function is executed.
