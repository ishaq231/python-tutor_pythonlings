# Exercise: Functional 8
# I AM NOT DONE
#
# `reduce(function, collection)` squashes a whole collection down to ONE
# value by combining items two at a time, from left to right:
#
#     reduce(f, [a, b, c])   is   f(f(a, b), c)
#
# You need to import it first (it's already done for you). For example
# reduce(lambda a, b: a + b, [1, 2, 3]) works out (1 + 2) + 3 = 6.
#
# Replace the ??? with a lambda that takes two numbers and multiplies them,
# so that `product` is all of `numbers` multiplied together.

from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(???, numbers)
