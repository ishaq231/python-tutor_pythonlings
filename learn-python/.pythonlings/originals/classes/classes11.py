# Exercise: Classes 11
# I AM NOT DONE
#
# A CLASS METHOD belongs to the class itself rather than to one instance. It
# gets `cls` (the class) instead of `self`. Its decorator is written on the line
# above with an @ sign. (You will learn more about @ decorators in a later topic.)
#
# A classic use is an "alternative way to make an object":
#
#     @classmethod
#     def from_string(cls, s):
#         return cls(...)       <- cls(...) makes a new instance
#
# Add a `from_string` class method to Temperature. It reads text like "36.6C"
# and returns a new Temperature with the number. Hint: s[:-1] is the text
# without its last character, and float() makes it a decimal number.

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    # Add from_string here


t = Temperature.from_string("36.6C")
boiling = Temperature.from_string("100C")
