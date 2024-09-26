import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from library.library import Book, Library

# tests/test_library.py
import pytest
from library.library import Book, Library

# Test for adding books
def test_add_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    assert len(library.books) == 1
    assert library.books["12345"].title == "Test Book"

def test_add_duplicate_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    with pytest.raises(ValueError, match="Book with this ISBN already exists."):
        library.add_book(book)

# Test for borrowing books
def test_borrow_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    borrowed_book = library.borrow_book("12345")
    assert borrowed_book.is_borrowed is True
    assert library.books["12345"].is_borrowed is True

def test_borrow_unavailable_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    library.borrow_book("12345")
    with pytest.raises(ValueError, match="Book already borrowed."):
        library.borrow_book("12345")

def test_borrow_non_existent_book():
    library = Library()
    with pytest.raises(ValueError, match="Book not found."):
        library.borrow_book("99999")

# Test for returning books
def test_return_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    library.borrow_book("12345")
    library.return_book("12345")
    assert book.is_borrowed is False

def test_return_non_borrowed_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    with pytest.raises(ValueError, match="Book is not borrowed."):
        library.return_book("12345")

# Test for viewing available books
def test_available_books():
    library = Library()
    book1 = Book("12345", "Test Book", "Author", 2020)
    book2 = Book("67890", "Another Book", "Author", 2019)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("12345")
    available_books = library.available_books()
    assert len(available_books) == 1
    assert available_books[0].isbn == "67890"

def test_list_available_books():
    library = Library()
    book1 = Book("12345", "Test Book", "Author", 2020)
    book2 = Book("67890", "Another Book", "Author", 2019)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("12345")
    assert library.list_available_books() == "67890 - Another Book by Author (2019)"
