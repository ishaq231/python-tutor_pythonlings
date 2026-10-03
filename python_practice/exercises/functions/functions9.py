# Exercise: Functions 9
# I AM NOT DONE
#
# The function `min_max` takes a list of numbers and returns
# the smallest and biggest as a pair, (minimum, maximum).
# Example: min_max([3, 1, 4, 1, 5, 9]) gives (1, 9)
#
# Your job: unpack the pair into two separate variables `lo` and `hi`.
# (Hint: lo, hi = ...)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def min_max(nums):
    return min(nums), max(nums)

lo = min_max(numbers)
hi = min_max(numbers)
