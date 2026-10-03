# Exercise: Type Hints 3
# I AM NOT DONE
#
# Add type hints to the function `total`, including what is INSIDE the collections:
#   - the parameter `scores` is a `list[int]` (a list of whole numbers)
#   - the parameter `labels` is a `dict[str, int]` (a dictionary with string keys and int values)
#   - the function returns an `int`
#
# It should look like:
#   def total(scores: list[int], labels: dict[str, int]) -> int:

def total(scores, labels):
    return sum(scores) + sum(labels.values())
