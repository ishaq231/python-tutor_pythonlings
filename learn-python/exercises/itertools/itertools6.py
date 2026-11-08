# Exercise: Itertools 6
# I AM NOT DONE
#
# `cycle(items)` goes round and round the items forever. Again, combine it with
# islice to take a limited number.
#
#     islice(cycle("ab"), 5)     gives   a, b, a, b, a
#
# Replace the ??? so that `repeated` is six colours: red, blue, red, blue, red, blue.

from itertools import cycle, islice

colors = ["red", "blue"]
repeated = list(???)
