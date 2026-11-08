# Exercise: Itertools 4
# I AM NOT DONE
#
# `groupby(items, key=function)` collects runs of neighbouring items that share
# the same key. IMPORTANT: it only groups items that are NEXT to each other, so
# the data should already be sorted by that key (here it is).
#
# The `key` is a function that takes an item and returns what to group by. Here
# each row is a tuple like ("fruit", "apple"), and you want to group by the
# FIRST item. Replace the ??? with a lambda that does that.

from itertools import groupby

rows = [("fruit", "apple"), ("fruit", "pear"), ("veg", "carrot")]
grouped = {
    category: [name for _, name in group]
    for category, group in groupby(rows, key=??? )
}
