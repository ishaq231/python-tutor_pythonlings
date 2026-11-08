# Exercise: Itertools 3
# I AM NOT DONE
#
# `product(a, b)` gives every possible pairing, with one item from each
# sequence. This is like a nested loop turned into a single line.
#
#     list(product([1, 2], "ab"))     gives   [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
#
# Replace the ??? so that `coordinates` holds every (x, y) pair from `xs` and `ys`.

from itertools import product

xs = [0, 1]
ys = ["low", "high"]
coordinates = list(???)
