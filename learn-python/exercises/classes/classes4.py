# Exercise: Classes 4
# I AM NOT DONE
#
# A function that belongs to a class is called a METHOD. Methods are defined
# with `def` inside the class and get `self` as their first parameter, which
# lets them use the object's attributes (like self.width).
#
# You call a method on an instance with a dot: rect.area()
#
# The `area` method currently returns 0. Make it return the rectangle's width
# times its height.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0


rect = Rectangle(4, 5)
