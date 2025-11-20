📚 Library Management System (CSV)
A lightweight, command-line interface (CLI) application written in Python to manage library books. This system uses a CSV file for data persistence, ensuring that book records are saved and reloaded automatically every time you run the program.

🚀 Features
Add Books: Input details like Book ID, Title, Author, and Copy count.
Persistent Storage: Automatically saves data to library.csv immediately after any change.
View Library: Displays all books in a clean, formatted table.
Search: Quickly find book details using the Book ID.
Update Inventory: Modify the number of copies for existing books.
Delete Records: Remove books permanently from the database.
Auto-Initialization: Automatically handles missing CSV files by creating a new one on the first run.
📋 Prerequisites
Python 3.x installed on your system.
No external libraries are required (uses Python's built-in csv module).
🛠️ Installation & Setup
Download the Code:
Save the provided Python script into a file named main.py (or any name you prefer).

Run the Application:
Open your terminal or command prompt, navigate to the folder containing the file, and run:

Bash

python main.py
First Run:
If library.csv does not exist, the program will create it automatically when you add your first book.

📖 Usage Guide
Upon running the script, you will see the following interactive menu:

text

==== Library Book Management System ====
1. Add Book
2. Display All Books
3. Search Book
4. Update Book Copies
5. Delete Book
6. Exit
Operation Details:
Option	Function	Description
1	Add Book	Prompts for ID, Title, Author, and Copies. Prevents duplicate IDs.
2	Display	Shows a formatted list of all books currently in the database.
3	Search	Asks for a Book ID and displays the specific details if found.
4	Update	Asks for a Book ID and the new total number of copies.
5	Delete	Removes a book entry entirely based on the Book ID.
6	Exit	Closes the application safely.
📂 Data Storage
The data is stored in a file named library.csv located in the same directory as the script.

Format:

csv

book_id,title,author,copies
101,Python 101,Mike Smith,5
102,Data Science,Jane Doe,3
Note: You can open library.csv in Excel, Google Sheets, or any text editor to view your data manually, but it is recommended to use the application to make edits to ensure data integrity.

📝 Code Structure
load_library(): Reads the CSV file at startup and populates the internal dictionary.
save_library(): Writes the current state of the dictionary back to the CSV file.
library Dictionary: The in-memory data structure used for fast lookups: { book_id : (title, author, copies) }.
⚠️ Error Handling
Duplicate IDs: The system checks if an ID exists before adding a book to prevent overwriting.
File Not Found: If the CSV file is missing (e.g., first run), the program handles this gracefully without crashing.
