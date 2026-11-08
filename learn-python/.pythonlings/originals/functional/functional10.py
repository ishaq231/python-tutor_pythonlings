# Exercise: Functional 10
# I AM NOT DONE
#
# Now chain them together into a pipeline: the output of one step becomes
# the input of the next.
#
#     Step 1, map:     double every score
#     Step 2, filter:  keep only the doubled scores that are bigger than 10
#     Step 3, reduce:  add up what is left
#
# Replace each ??? with the right lambda. Remember reduce's lambda takes TWO
# values (a running total and the next item).

from functools import reduce

scores = [1, 3, 6, 2, 8, 4]

doubled = list(map(???, scores))
above_ten = list(filter(???, doubled))
result = reduce(???, above_ten)
