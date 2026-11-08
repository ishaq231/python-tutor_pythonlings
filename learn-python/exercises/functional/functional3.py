# Exercise: Functional 3
# I AM NOT DONE
#
# `map(function, collection)` applies a function to EVERY item and gives
# the results back. It's like a comprehension, but with a function.
#
#     list(map(lambda x: x + 1, [1, 2, 3]))     gives   [2, 3, 4]
#
# The `list(...)` is needed because map gives back a lazy "map object"
# (not a list yet), and list() turns it into a real list.
#
# Replace the ??? with a lambda that doubles a number, so `doubled` holds
# every number in `numbers` times 2.

numbers = [1, 2, 3, 4, 5]

doubled = list(map(???, numbers))
