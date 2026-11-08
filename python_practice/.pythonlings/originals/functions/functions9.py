# Exercise: Functions 9
# I AM NOT DONE
#
# A function can return more than one value at once. Python packs them into
# a tuple (a fixed pair or group of values). You can UNPACK them into separate
# variables on the left - just like the one-line trick from the Variables exercises:
#
#     first, second = some_function()
#
# `min_max` returns the smallest and biggest numbers as a pair
# (minimum, maximum). Right now `lo` and `hi` each get the WHOLE pair, which
# is wrong. Fix the code so `lo` is the minimum and `hi` is the maximum,
# using a single line with unpacking.

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def min_max(nums):
    return min(nums), max(nums)

lo = min_max(numbers)
hi = min_max(numbers)
