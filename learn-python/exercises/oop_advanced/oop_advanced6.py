# Exercise: Oop Advanced 6
# I AM NOT DONE
#
# You met __repr__ in the Classes exercises. It should look like the code
# that would create the object. Use an f-string:
#
#     f"Dog(name={self.name})"
#
# Replace the ??? so that repr(Point(2, 5)) is exactly "Point(x=2, y=5)".

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return ???
