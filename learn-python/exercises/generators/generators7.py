# Exercise: Generators 7
# I AM NOT DONE
#
# The Fibonacci sequence goes 0, 1, 1, 2, 3, 5, 8, 13, ... Each number is the
# sum of the two before it. You can keep the last two numbers in `a` and `b` and
# update both at once using the one-line trick from the Variables exercises:
#
#     a, b = b, a + b
#
# Fix `fibonacci()` so it yields a, then updates a and b, again and again
# forever. It currently only yields once.

def fibonacci():
    a, b = 0, 1
    # Bug: yields only once instead of looping forever.
    yield a
