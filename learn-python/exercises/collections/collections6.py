# Exercise: Collections 6
# I AM NOT DONE
#
# A namedtuple's fields can be read by name (card.rank) or by index
# (card[0]), because it's still a tuple. And tuples can't be changed, but
# `._replace(field=new_value)` gives you a modified COPY.
#
# 1. Make `card` the King of Spades (rank "K", suit "spades").
# 2. Make `upgraded` a copy of `card` with the rank replaced by "A".

from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])

card = ???
upgraded = ???
