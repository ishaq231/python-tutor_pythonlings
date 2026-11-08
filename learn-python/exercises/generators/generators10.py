# Exercise: Generators 10
# I AM NOT DONE
#
# Generators are great for processing a stream of data one piece at a time.
# A RUNNING TOTAL adds each new number to everything before it:
# the running totals of 1, 2, 3, 4 are 1, 3, 6, 10.
#
# Fix `running_total(numbers)` so that it adds each number to `total` and
# yields the new total (not the raw number).

def running_total(numbers):
    total = 0
    for n in numbers:
        # Bug: yields n instead of the accumulated total.
        yield n
