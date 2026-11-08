# Exercise: Classes 6
# I AM NOT DONE
#
# Default values work in __init__ just like in normal functions (remember
# Functions 5?): put `=` and the default after the parameter name.
#
# At the moment `Car("Tesla")` gives an error because no speed is given. Give
# the `speed` parameter a default value of 0 so that it works.

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


slow = Car("Tesla")
fast = Car("Ferrari", 200)
