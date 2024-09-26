# library/library.py

class Book:
    def __init__(self, isbn, title, author, year):
        """Initialize a new book instance.

        Args:
            isbn (str): The ISBN number of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # Indicates if the book is currently borrowed

    def __str__(self):
        """Return a string representation of the book for easy reading."""
        return f"{self.isbn} - {self.title} by {self.author} ({self.year})"

    def __repr__(self):
        """Return a detailed string representation of the book for debugging purposes."""
        return f"Book({self.isbn}, {self.title}, {self.author}, {self.year}, Borrowed: {self.is_borrowed})"


class Library:
    def __init__(self):
        """Initialize a new library instance.

        The library holds a collection of books.
        """
        self.books = {}  # Dictionary to hold books with their ISBN as the key

    def add_book(self, book):
        """Add a new book to the library.

        Args:
            book (Book): The book to be added.

        Raises:
            ValueError: If a book with the same ISBN already exists.
        """
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        self.books[book.isbn] = book  # Store the book using its ISBN as the key

    def search_book(self, isbn):
        """Search for a book by its ISBN.

        Args:
            isbn (str): The ISBN number of the book.

        Returns:
            Book: The book object if found.

        Raises:
            ValueError: If the book is not found.
        """
        if isbn not in self.books:
            raise ValueError("Book not found.")
        return self.books[isbn]  # Return the found book

    def borrow_book(self, isbn):
        """Borrow a book from the library.

        Args:
            isbn (str): The ISBN number of the book to borrow.

        Returns:
            Book: The borrowed book object.

        Raises:
            ValueError: If the book is already borrowed.
        """
        book = self.search_book(isbn)  # Find the book first
        if book.is_borrowed:
            raise ValueError("Book already borrowed.")  # Check if it's already borrowed
        book.is_borrowed = True  # Mark the book as borrowed
        return book  # Return the borrowed book

    def return_book(self, isbn):
        """Return a borrowed book to the library.

        Args:
            isbn (str): The ISBN number of the book to return.

        Raises:
            ValueError: If the book is not currently borrowed.
        """
        book = self.search_book(isbn)  # Find the book
        if not book.is_borrowed:
            raise ValueError("Book is not borrowed.")  # Check if it was borrowed
        book.is_borrowed = False  # Mark the book as available again

    def available_books(self):
        """Get a list of all available books in the library.

        Returns:
            list: A list of available book objects.
        """
        return [book for book in self.books.values() if not book.is_borrowed]  # Filter available books

    def list_available_books(self):
        """Get a string listing of all available books.

        Returns:
            str: A string representation of available books.
        """
        return "\n".join(str(book) for book in self.available_books())  # Join available books into a single string
