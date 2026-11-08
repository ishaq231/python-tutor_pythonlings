# Exercise: Dataclasses 1
# I AM NOT DONE
#
# Writing __init__ for a class that just stores data gets boring. A
# DATACLASS writes it for you. Put the `@dataclass` decorator above the class,
# then list the fields with their types (type hints) and Python does the rest:
#
#     @dataclass
#     class Pet:
#         name: str
#         age: int
#
#     p = Pet("Rex", 3)     <- __init__ was made for you
#
# Turn `Point` into a dataclass with two int fields, `x` and `y`.
# Add the @dataclass line and the two field lines (remove the `pass`).

from dataclasses import dataclass


class Point:
    pass


origin = Point(0, 0)
