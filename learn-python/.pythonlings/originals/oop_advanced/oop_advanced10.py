# Exercise: Oop Advanced 10
# I AM NOT DONE
#
# An ABSTRACT class is a class that's only meant to be a template for other
# classes, and can't be used itself. `@abstractmethod` marks a method that
# every child MUST write for itself. If a child forgets, Python refuses to make
# an object from it.
#
# Shape says "every shape must have an area()". Replace the ??? so Square's
# area() returns the side times the side.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return ???
