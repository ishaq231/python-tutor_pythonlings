# Exercise: Oop Advanced 8
# I AM NOT DONE
#
# Remember the @classmethod from the Classes exercises, an alternative way to
# make an object? `cls` is the class itself, so `cls(a, b)` creates a new
# instance.
#
# Here the text "3,4" is split into two pieces. Those pieces are still strings,
# so turn them into whole numbers with int(). Replace the ??? with a
# call that makes a new Coordinate from them.

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_text(cls, text):
        x_text, y_text = text.split(",")
        return ???
