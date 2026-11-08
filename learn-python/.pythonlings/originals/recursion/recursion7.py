# Exercise: Recursion 7
# I AM NOT DONE
#
# Lists can be nested: a list can contain other lists, like
# [1, [2, 3], [4, [5]]]. A loop is awkward for this because you don't know
# how deep it goes, but recursion copes easily. If an item is itself a list,
# call deep_sum on it, which handles whatever it contains.
#
# `isinstance(first, list)` checks if something is a list. Most of the work is
# done. Replace the ??? with the sum of the REST of the list.

def deep_sum(nested):
    if not nested:
        return 0
    first = nested[0]
    rest = nested[1:]
    if isinstance(first, list):
        return deep_sum(first) + ???
    return first + deep_sum(rest)
