
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        return f"{self.isbn} - {self.title} by {self.author} ({self.year})"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book
        
    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if book.is_borrowed:
            raise ValueError("Book already borrowed.")
        book.is_borrowed = True
        return book

    def return_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        book = self.books[isbn]
        if not book.is_borrowed:
            raise ValueError("Book is not borrowed.")
        book.is_borrowed = False

    def available_books(self):
        return [book for book in self.books.values() if not book.is_borrowed]



    