#!/usr/bin/env python3

from book import Book

import io
import sys
import pytest
import unittest

class TestBook(unittest.TestCase):
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", 272)
        assert(book.page_count == 272)
        assert(book.title == "And Then There Were None")

    def test_invalid_page_count(self):
        with pytest.raises(ValueError, match="page_count must be an integer"):
            book = Book("Invalid Book", "not_an_integer")
def test_requires_int_page_count(self):
    '''prints "page_count must be an integer" if page_count is not an integer.'''
    book = Book("And Then There Were None", 272)

    try:
        book.page_count = "not an integer"
    except ValueError as e:
        assert str(e) == "page_count must be an integer"
    else:
        assert False, "Expected ValueError was not raised"


    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")
