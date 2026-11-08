# Exercise: Oop Advanced 3
# I AM NOT DONE
#
# POLYMORPHISM (Greek for "many shapes") is a posh word for a simple idea:
# different classes can have a method with the SAME name, and you can call it
# without caring which class the object is. Square and Rectangle both have an
# `area()` method, so a list of mixed shapes can be handled by one loop.
#
# Replace the ??? so total_area(shapes) adds up the area() of every shape.
# (sum() with a generator expression or a comprehension is neat.)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def total_area(shapes):
    return ???
