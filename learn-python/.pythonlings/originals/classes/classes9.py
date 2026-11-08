# Exercise: Classes 9
# I AM NOT DONE
#
# `__repr__` is a cousin of `__str__`. Where __str__ is a friendly message for
# users, __repr__ is for programmers. It should show the object clearly,
# ideally looking like the code that would make it. It's what you see when
# debugging.
#
# Add a `__repr__` method to Color so that repr(c) gives
# "Color(r=255, g=128, b=0)" (using the real values). The __str__ is already written.

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"rgb({self.r}, {self.g}, {self.b})"


c = Color(255, 128, 0)
