class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nAvailability: {'Available' if self.available else 'Not Available'}\n")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print(f"User ID: {self.user_id}\nName: {self.name}\nBooks Borrowed: {', '.join(self.books_borrowed)}\n")

    def borrow_book(self, book):
        if book.available:
            self.books_borrowed.append(book.title)
            book.available = False
            print(f"{self.name} has successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.available = True
            print(f"{self.name} has successfully returned '{book.title}'.")
        else:
            print(f"You haven't borrowed '{book.title}'. Cannot return.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered in the library.")

    def borrow_book(self, user, book):
        user.borrow_book(book)

    def return_book(self, user, book):
        user.return_book(book)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display_details()

    def display_users(self):
        print("Library Users:")
        for user in self.users:
            user.display_details()


# Example usage:
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")

user1 = User(1, "Alice")
user2 = User(2, "Bob")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.register_user(user1)
library.register_user(user2)

library.borrow_book(user1, book1)
library.borrow_book(user2, book2)

library.display_books()
library.display_users()
