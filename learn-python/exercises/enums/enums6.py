# Exercise: Enums 6
# I AM NOT DONE
#
# Enums are classes, so they can have methods! Inside a method, `self` is the
# member itself, and `self.value` is its value. Here every direction's value is
# a tuple of (x change, y change).
#
# Replace the ??? so that delta() returns the member's value.

from enum import Enum

class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)

    def delta(self):
        return ???
