# Exercise: Type Hints 7
# I AM NOT DONE
#
# Add type hints to the function `apply_twice` using `Callable` from `typing`.
# `Callable` is the type hint for a function that you pass in.
#   - the parameter `func` is `Callable[[int], int]`
#     (a function that takes one int and returns an int)
#   - the parameter `value` is an `int`
#   - the function returns an `int`
#
# The import for `Callable` is already there for you.
#
# It should look like:
#   def apply_twice(func: Callable[[int], int], value: int) -> int:

from typing import Callable


def apply_twice(func, value):
    return func(func(value))
