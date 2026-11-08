# Exercise: Enums 5
# I AM NOT DONE
#
# Members of an enum are compared with `==` or `is`, or checked with `in`. A
# tidy way to test several at once:
#
#     state in (Light.RED, Light.GREEN)
#
# A ticket is "terminal" when it's finished: CLOSED or CANCELLED (but not
# OPEN). Replace the ??? so is_terminal(state) is True for those two and False
# for OPEN.

from enum import Enum, auto

class TicketState(Enum):
    OPEN = auto()
    CLOSED = auto()
    CANCELLED = auto()

def is_terminal(state):
    return ???
