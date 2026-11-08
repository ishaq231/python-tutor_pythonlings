# Exercise: Type Hints 7
# I AM NOT DONE
#
# In Python, a function can be passed into another function, just like a
# number or a string! The type hint for "a function" is `Callable`, and it
# says what goes in and what comes out:
#
#     Callable[[int], int]     a function that takes one int and returns an int
#
# (The inner square brackets hold the list of inputs, then comes the output.)
#
# Add type hints to `apply_twice`:
#     func is a Callable[[int], int],  value is an int,  and it returns an int
#
# It should look like:
#     def apply_twice(func: Callable[[int], int], value: int) -> int:
#
# The import for `Callable` is already written for you.

from typing import Callable


def apply_twice(func, value):
    return func(func(value))
