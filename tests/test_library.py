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


