# Exercise: Loops 9
# I AM NOT DONE
#
# A DICTIONARY stores pairs of information: a KEY and its VALUE, like a real
# dictionary links a word to its meaning. It is written with curly brackets:
#
#     ages = {"Zoe": 12, "Max": 13}      <- keys are the names
#
# Looping over `.items()` gives you the key and value together:
#
#     for name, age in ages.items():
#         ...
#
# Use this to find the person with the highest score in `scores`. Save their
# name in `top_name` and their score in `top_score`. The scores are all
# whole numbers that are 0 or more, and only one person has the highest score.
# Hint: compare each score with the best one you have seen so far.

scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95 - 1}
top_name = None
top_score = -1
# write your for loop here
