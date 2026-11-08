# Exercise: Itertools 8
# I AM NOT DONE
#
# `pairwise(items)` gives every pair of neighbours: for [1, 2, 3] you get
# (1, 2) and (2, 3). It's great for comparing each item with the next one.
#
# The first part (flattening the batches) is already done for you, with a
# comprehension like the ones you wrote earlier. Replace the ??? so that
# `adjacent_pairs` holds all the neighbouring pairs of `flattened`.

try:
    from itertools import pairwise
except ImportError:  # Python < 3.10
    from itertools import tee

    def pairwise(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

batches = [[1, 2], [3], [4, 5]]
flattened = [item for batch in batches for item in batch]
adjacent_pairs = list(???)
