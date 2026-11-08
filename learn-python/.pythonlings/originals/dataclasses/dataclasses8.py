# Exercise: Dataclasses 8
# I AM NOT DONE
#
# A dataclass is still a normal class, so you can add methods to it
# as usual. They use `self` to read the fields.
#
# Challenge: fill in the two methods of `Rectangle`:
#     area       returns width * height
#     perimeter  returns 2 * (width + height)

from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        pass  # Bug: return the correct value

    def perimeter(self) -> float:
        pass  # Bug: return the correct value


rect = Rectangle(4.0, 3.0)
square = Rectangle(5.0, 5.0)
