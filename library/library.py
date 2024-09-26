
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        return f"{self.isbn} - {self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book({self.isbn}, {self.title}, {self.author}, {self.year}, Borrowed: {self.is_borrowed})"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book

    def search_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        return self.books[isbn]

    def borrow_book(self, isbn):
        book = self.search_book(isbn)
        if book.is_borrowed:
            raise ValueError("Book already borrowed.")
        book.is_borrowed = True
        return book

    def return_book(self, isbn):
        book = self.search_book(isbn)
        if not book.is_borrowed:
            raise ValueError("Book is not borrowed.")
        book.is_borrowed = False

    def available_books(self):
        return [book for book in self.books.values() if not book.is_borrowed]

    def list_available_books(self):
        return "\n".join(str(book) for book in self.available_books())
