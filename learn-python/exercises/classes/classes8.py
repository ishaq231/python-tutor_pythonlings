# Exercise: Classes 8
# I AM NOT DONE
#
# Printing an object normally shows something unhelpful like
# <Book object at 0x7f...>. You can control this with the special method
# `__str__`, which returns the text that should be shown when the object is
# turned into a string (by str() or print()).
#
#     def __str__(self):
#         return f"..."
#
# Add a `__str__` method to Book so that str(book) gives
# "Book: <title> by <author>". For example "Book: 1984 by Orwell".

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("1984", "Orwell")
