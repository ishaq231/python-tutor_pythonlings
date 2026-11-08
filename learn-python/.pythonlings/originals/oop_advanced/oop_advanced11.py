# Exercise: Oop Advanced 11
# I AM NOT DONE
#
# A MIXIN is a small class that gives extra abilities to other classes that
# inherit from it. It's not meant to be used alone. Here the mixin has a method
# which can work on any object.
#
# Every object stores its attributes in a dictionary called `__dict__`, so
# vars(self) or self.__dict__ gives them to you. Replace the ??? so
# to_dict() returns the object's attributes as a dictionary (a plain copy is
# safest: dict(self.__dict__)).

class DictMixin:
    def to_dict(self):
        return ???

class Product(DictMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
