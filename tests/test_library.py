import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from library.library import Book, Library


import pytest
from library.library import Book, Library

# Test for adding books
def test_add_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    assert len(library.books) == 1

# Test for borrowing books
def test_borrow_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    borrowed_book = library.borrow_book("12345")
    assert borrowed_book.is_borrowed == True

# Test for returning books
def test_return_book():
    library = Library()
    book = Book("12345", "Test Book", "Author", 2020)
    library.add_book(book)
    library.borrow_book("12345")
    library.return_book("12345")
    assert book.is_borrowed == False



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




