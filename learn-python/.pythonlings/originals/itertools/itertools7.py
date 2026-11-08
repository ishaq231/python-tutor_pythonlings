# Exercise: Itertools 7
# I AM NOT DONE
#
# The built-in `zip(a, b)` pairs up items from two lists, but it stops as soon as
# the SHORTER list runs out. `zip_longest` carries on until the longest is
# finished, filling the gaps with a value you choose:
#
#     zip_longest(a, b, fillvalue="?")
#
# Replace the ??? so that `pairs` pairs up `left` and `right`, with "?" for
# anything missing.

from itertools import zip_longest

left = ["a", "b", "c"]
right = [1]
pairs = list(???)
