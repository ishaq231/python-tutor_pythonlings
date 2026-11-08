# Exercise: Recursion 5
# I AM NOT DONE
#
# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ... Each number is the sum of
# the two before it. Here the recursive case calls the function TWICE. It has
# two base cases: fibonacci(0) is 0, and fibonacci(1) is... what? Look at the
# start of the sequence above.
#
# Replace the ??? with the right answer for fibonacci(1).

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return ???
    return fibonacci(n - 1) + fibonacci(n - 2)
