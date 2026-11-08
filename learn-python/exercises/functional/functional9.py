# Exercise: Functional 9
# I AM NOT DONE
#
# Two handy built-in functions answer yes/no questions about a collection:
#     any(...)   True if AT LEAST ONE item passes the test
#     all(...)   True if EVERY item passes the test
#
# You give them a comprehension-style expression (without the square
# brackets):
#
#     any(n > 10 for n in numbers)
#
# Replace the ??? so that `has_negative` is True if any number in `numbers` is
# negative, and `all_positive` is True if all the numbers in `positives` are
# positive (more than 0).

numbers = [3, -1, 4, 1, 5]
positives = [2, 7, 11, 5]

has_negative = any(???)
all_positive = all(???)
