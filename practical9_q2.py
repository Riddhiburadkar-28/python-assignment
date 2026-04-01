class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        print(f"Book '{title}' added successfully.")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title} - {status}")

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{title}' issued successfully.")
                    return
                else:
                    print("Book already issued.")
                    return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{title}' returned successfully.")
                    return
                else:
                    print("Book was not issued.")
                    return
        print("Book not found.")


# Menu-driven program
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        library.add_book(title)

    elif choice == '2':
        library.display_books()

    elif choice == '3':
        title = input("Enter book title to lend: ")
        library.lend_book(title)

    elif choice == '4':
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")