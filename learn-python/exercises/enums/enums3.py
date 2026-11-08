# Exercise: Enums 3
# I AM NOT DONE
#
# Each enum member has two useful attributes:
#     .name    its name as a string, e.g. "HIGH"
#     .value   the value you gave it, e.g. 5
#
# Replace the ??? so `selected_name` and `selected_value` are the name and
# value of `selected`.

from enum import Enum

class Priority(Enum):
    LOW = 1
    HIGH = 5

selected = Priority.HIGH
selected_name = ???
selected_value = ???
