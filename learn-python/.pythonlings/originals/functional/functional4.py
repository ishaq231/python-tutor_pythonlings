# Exercise: Functional 4
# I AM NOT DONE
#
# `filter(function, collection)` keeps only the items for which the function
# gives True. (It's like the `if` at the end of a comprehension.)
#
#     list(filter(lambda x: x > 2, [1, 2, 3, 4]))     gives   [3, 4]
#
# Replace the ??? with a lambda that is True for even numbers, so `evens`
# only keeps the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(???, numbers))
