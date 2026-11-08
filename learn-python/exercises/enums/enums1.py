# Exercise: Enums 1
# I AM NOT DONE
#
# An ENUM (short for "enumeration") is a fixed set of named choices. Use
# one when a value can only be one of a few options, such as the days of the
# week, traffic light colours, or the suit of a card. It stops typos like
# "gren".
#
#     class Light(Enum):
#         GREEN = "green"
#         RED = "red"
#
# The names are written in CAPITALS, like constants. Each has a value.
#
# Give `Color.RED` the value "red" and `Color.BLUE` the value "blue".
# (The last line, favorite = Color.RED, shows how you pick a member.)

from enum import Enum

class Color(Enum):
    RED = ???
    BLUE = ???

favorite = Color.RED
