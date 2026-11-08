# Exercise: Itertools 1
# I AM NOT DONE
#
# The `itertools` module is a toolbox for working with sequences and loops.
# Most of its tools are lazy: they make items one at a time, so you wrap them in
# list() to see everything.
#
# `chain(a, b)` joins sequences end to end, as if they were one.
#
#     list(chain([1, 2], [3]))     gives   [1, 2, 3]
#
# Replace the ??? so that `combined` is the letters followed by the numbers.

from itertools import chain

letters = ["a", "b"]
numbers = [1, 2, 3]
combined = list(???)
