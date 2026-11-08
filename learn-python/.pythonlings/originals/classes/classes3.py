# Exercise: Classes 3
# I AM NOT DONE
#
# An object can have as many attributes as you like, each one stored with
# `self.something = ...` inside __init__.
#
# The Point class should store both `x` and `y`. At the moment only `x` is
# stored. Add the line that stores `y`.

class Point:
    def __init__(self, x, y):
        self.x = x
        # also store y on the instance


p = Point(3, 7)
