# Exercise: Dataclasses 6
# I AM NOT DONE
#
# A dataclass also writes two more special methods for you:
#     __repr__   shows the field values in a readable way, e.g. Book(title='Dune', pages=412)
#     __eq__     lets `==` compare two objects by comparing their fields
#
# A plain class would say two Books with the same title are different objects.
# A dataclass says they're equal.
#
# Turn `Book` into a dataclass with a `title: str` and a `pages: int` field.

# Bug: missing @dataclass decorator and field declarations.
class Book:
    pass


novel = Book("Dune", 412)
copy = Book("Dune", 412)
other = Book("Foundation", 255)
