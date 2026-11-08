# Exercise: Oop Advanced 12
# I AM NOT DONE
#
# Special methods can even make your objects work with maths signs! When Python
# sees `a + b`, it calls `a.__add__(b)`. (Others are __sub__ for -, __mul__ for *.)
#
# For a Vector, adding means adding the x parts and the y parts. Replace the ???
# so that it returns a NEW Vector with the sums. For example Vector(1, 2) +
# Vector(3, 4) should be Vector(4, 6).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return ???
