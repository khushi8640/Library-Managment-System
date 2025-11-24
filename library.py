import os

library_file = "library.txt"

# Load books from file
def load_data():
    books = []
    if os.path.exists(library_file):
        with open(library_file, "r") as f:
            for line in f:
                title, author, status = line.strip().split("|")
                books.append({"title": title, "author": author, "status": status})
    return books

# Save books to file
def save_data(books):
    with open(library_file, "w") as f:
        for book in books:
            f.write(f"{book['title']}|{book['author']}|{book['status']}\n")

# Add a book
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books.append({"title": title, "author": author, "status": "available"})
    print("Book added successfully!")

# Display all books
def display_books(books):
    if not books:
        print("No books in the library.")
        return
    print("\n--- Library Books ---")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} by {book['author']} ({book['status']})")

# Search for a book
def search_book(books):
    keyword = input("Enter title or author to search: ").lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"Found: {book['title']} by {book['author']} ({book['status']})")
            found = True
    if not found:
        print("No matching book found.")

# Borrow a book
def borrow_book(books):
    title = input("Enter the book title to borrow: ").lower()
    for book in books:
        if book["title"].lower() == title:
            if book["status"] == "available":
                book["status"] = "issued"
                print("Book issued successfully!")
            else:
                print("Sorry, the book is already issued.")
            return
    print("Book not found.")

# Return a book
def return_book(books):
    title = input("Enter the book title to return: ").lower()
    for book in books:
        if book["title"].lower() == title:
            if book["status"] == "issued":
                book["status"] = "available"
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return
    print("Book not found.")

# Main menu
def main():
    books = load_data()

    while True:
        print("\n--- Library Management Menu ---")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            display_books(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            save_data(books)
            print("Library saved. Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()