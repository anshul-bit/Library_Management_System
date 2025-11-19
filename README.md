# Library_Management_System
Overview
This program allows you to manage a library's book collection by adding, displaying, searching, updating, and deleting book records. All data is stored in memory during runtime using a Python dictionary.

Features
Add Books: Register new books with ID, title, author, and number of copies
Display All Books: View a formatted table of all books in the library
Search Books: Find a specific book by its ID
Update Copies: Modify the number of copies available for any book
Delete Books: Remove books from the library system
Persistent Menu: Continuous operation until you choose to exit
Requirements
Python 3.x (developed and tested with Python 3.8+)
How to Run
Save the code as library.py
Open a terminal/command prompt
Navigate to the file's directory
Run: python library.py
Menu Options
When you start the program, you'll see:

text

==== Library Book Management System ====
1. Add Book
2. Display All Books
3. Search Book
4. Update Book Copies
5. Delete Book
6. Exit
Option Details
1. Add Book

Enter a unique Book ID (case-sensitive)
Provide title, author, and number of copies
Book ID must be unique; duplicates will be rejected
2. Display All Books

Shows all books in a formatted table with columns: Book ID, Title, Author, Copies
3. Search Book

Enter a Book ID to view its details
Displays title, author, and copies if found
4. Update Book Copies

Enter a Book ID
Provide a new number of copies (must be an integer)
5. Delete Book

Enter a Book ID to permanently remove it from the library
6. Exit

Terminates the program
Example Usage Session
text

==== Library Book Management System ====
1. Add Book
2. Display All Books
3. Search Book
4. Update Book Copies
5. Delete Book
6. Exit
Enter your choice (1-6): 1
Enter Book ID: B001
enter the title of the book: Python Programming
enter the name of the author of the book: John Smith
enter the number of copies of the book 'Python Programming': 5
Book 'Python Programming' is added successfully!!

==== Library Book Management System ====
1. Add Book
2. Display All Books
3. Search Book
4. Update Book Copies
5. Delete Book
6. Exit
Enter your choice (1-6): 2

Library Books
------------------------------------------------------------
Book id   Title               Author          Copies
------------------------------------------------------------
B001      Python Programming  John Smith      5
------------------------------------------------------------

==== Library Book Management System ====
1. Add Book
2. Display All Books
3. Search Book
4. Update Book Copies
5. Delete Book
6. Exit
Enter your choice (1-6): 6
Exiting the system. Goodbye!
Data Structure
Books are stored in a dictionary where:

Key: book_id (string, user-provided)
Value: Tuple of (title, author, copies)
Example: {"B001": ("Python Programming", "John Smith", "5")}

Important Notes
Case Sensitivity: Book IDs are case-sensitive (b001 and B001 are different)
No Persistent Storage: All data is lost when the program exits. For permanent storage, consider adding file I/O or database integration
Input Validation: The program has minimal validation:
Book IDs are not checked for format
Copies are stored as strings in add_book() but require integers in update_copies()
No checks for negative numbers or empty fields
No Edit Function: Book titles and authors cannot be modified after creation (only copies can be updated)
Error Handling: Basic error handling for missing books; invalid menu choices show a warning
Potential Improvements
Add data persistence using JSON or CSV files
Implement input validation for all fields
Store copies as integers consistently
Add ability to edit title and author
Make Book ID case-insensitive
Add borrowing/returning functionality
Include search by title or author
Add confirmation prompts for delete operations
