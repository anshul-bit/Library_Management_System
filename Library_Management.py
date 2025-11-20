import csv  

FILENAME = "library.csv"  
library = {}  # {book_id:( title,author, copies)}

def load_library():
    """Load existing data from CSV into the library dict."""
    try:
        with open(FILENAME, newline='') as f:
            reader = csv.reader(f)
            next(reader, None) 
            for row in reader:
                if len(row) != 4:
                    continue
                book_id, title, author, copies = row
                library[book_id] = (title, author, copies)
    except FileNotFoundError:
        pass

def save_library():
    """Save current library dict to CSV."""
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['book_id', 'title', 'author', 'copies'])
        for book_id, (title, author, copies) in library.items():
            writer.writerow([book_id, title, author, copies])

def add_book():
    book_id = (input("Enter Book ID: "))
    if book_id in library:
        print("book already exits!!")
        return
    title = input("enter the title of the book: ")
    author = input("enter the name of the author of the book: ")
    copies = input(f"enter the number of copies of the book '{title}'")
    library[book_id] = (title, author, copies)
    save_library() 
    print(f"Book '{title}' is added successfully!!")

def display_books():
    if not library:
        print("No books available in the library!!\n")
        return
    print("\nLibrary Books")
    print("-"*60)
    print(f"{'Book id':<10}{'Title':<20}{'Author':<15}{'Copies':<6}")
    print("-"*60)
    for book_id, details in library.items():
        title, author, copies = details
        print(f"{book_id:<10}{title:<20}{author:<15}{copies:<6}")
    print()

def search_book():
    key = input("Enter Book ID to search: ")
    if key in library:
        title, author, copies = library[key]
        print(f"\nBook Found!\nTitle: {title}\nAuthor: {author}\n Copies: {copies}\n")
    else:
        print("Book not found!\n")

def update_copies():
    key = input("Enter Book ID to update copies: ")
    if key in library:
        title, author, copies = library[key]
        new_copies = int(input("Enter new number of copies: "))
        library[key] = (title, author, new_copies)
        save_library()  
        print("Book copies updated successfully!\n")
    else:
        print("Book not found!\n")

def delete_book():
    key = input("Enter Book ID to delete: ")
    if key in library:
        del library[key]
        save_library()  
        print("Book deleted successfully!\n")
    else:
        print("Book not found!\n")


load_library()

while True:
    print("==== Library Book Management System ====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Update Book Copies")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        update_copies()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice!Tryagain.\n")
