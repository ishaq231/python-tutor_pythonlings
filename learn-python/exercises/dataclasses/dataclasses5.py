# Exercise: Dataclasses 5
# I AM NOT DONE
#
# A dataclass creates `__init__` for you, so you should NOT write your own. Just
# declare the fields and delete the hand-written __init__.
#
# Fix `Vector3`: remove the __init__ method and declare three float fields
# named x, y and z instead.

from dataclasses import dataclass


@dataclass
class Vector3:
    # Bug: fields are missing; there is a hand-written __init__ below.
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


v = Vector3(1.0, 2.0, 3.0)
