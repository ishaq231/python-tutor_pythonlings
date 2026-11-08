# Exercise: Enums 4
# I AM NOT DONE
#
# You can loop over an enum to get every member, in the order they were
# written. Use a comprehension to collect each member's value.
#
#     [m.value for m in Light]
#
# Replace the ??? so that `size_codes` is the list of all the Size values:
# ["S", "M", "L"].

from enum import Enum

class Size(Enum):
    SMALL = "S"
    MEDIUM = "M"
    LARGE = "L"

size_codes = ???
