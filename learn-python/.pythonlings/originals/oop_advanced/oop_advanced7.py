# Exercise: Oop Advanced 7
# I AM NOT DONE
#
# By default, two objects are only `==` if they're literally the same object.
# `__eq__` lets you decide what "equal" means for your class. It receives the
# object on the right (`other`) and returns True or False.
#
# Here the first lines check that `other` really is a Book. Replace the ??? so
# that two books are equal when their `isbn` is equal (ignoring the title).

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return ???
