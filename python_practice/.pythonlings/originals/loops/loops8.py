# Exercise: Loops 8
# I AM NOT DONE
#
# Sometimes you need the position number as well as the item. `enumerate`
# gives you both at once:
#
#     for position, item in enumerate(["a", "b"]):
#         ...position is 0 then 1, and item is "a" then "b"...
#
# By default it counts from 0. Write enumerate(words, start=1) to count
# from 1 instead.
#
# Use enumerate to loop over `words` and build a list of strings that look
# like "N: word", where N counts from 1. For example ["cat", "dog"] becomes
# ["1: cat", "2: dog"]. Save the list in `labeled`.

words = ["python", "is", "fun"]
labeled = []
# write your for loop (with enumerate) here
