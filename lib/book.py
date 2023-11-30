# book.py

class Book:
    def __init__(self, title, page_count):
        if not isinstance(page_count, int):
            raise ValueError("page_count must be an integer")

        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
