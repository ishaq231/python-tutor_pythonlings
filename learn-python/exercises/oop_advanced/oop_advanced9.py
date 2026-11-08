# Exercise: Oop Advanced 9
# I AM NOT DONE
#
# A `@staticmethod` is a function that lives inside a class for tidiness but
# doesn't need `self` or `cls`, because it doesn't use any particular object.
# It's often a handy helper.
#
# Replace the ??? so is_valid(percent) is True when the percentage is from 0 to
# 100 inclusive, and False otherwise. (Python lets you chain comparisons:
# 0 <= x <= 100.)

class Grade:
    @staticmethod
    def is_valid(percent):
        return ???
