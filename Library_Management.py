library ={} #{book_id:( title,author, copies)}
def add_book():
    book_id = (input("Enter Book ID: "))
    if book_id in library:
        print("book already exits!!")
        return
    title = input("enter the title of the book: ")
    author = input("enter the name of the author of the book: ")
    copies = input(f"enter the number of copies of the book '{title}'")
    library[book_id] = (title, author, copies)
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
        print("Book copies updated successfully!\n")
    else:
        print("Book not found!\n")

def delete_book():
    key = input("Enter Book ID to delete: ")
    if key in library:
        del library[key]
        print("Book deleted successfully!\n")
    else:
        print("Book not found!\n")

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