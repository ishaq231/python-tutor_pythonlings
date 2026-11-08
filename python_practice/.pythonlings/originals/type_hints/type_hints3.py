# Exercise: Type Hints 3
# I AM NOT DONE
#
# For collections like lists and dictionaries, you can say what is INSIDE them
# using square brackets:
#     list[int]          a list of whole numbers
#     dict[str, int]     a dictionary with str keys and int values
#
# Add type hints to `total`:
#     scores is a list[int]
#     labels is a dict[str, int]
#     the function returns an int
#
# It should look like:
#     def total(scores: list[int], labels: dict[str, int]) -> int:

def total(scores, labels):
    return sum(scores) + sum(labels.values())
