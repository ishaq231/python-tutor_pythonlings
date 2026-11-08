# Exercise: Recursion 1
# I AM NOT DONE
#
# RECURSION is when a function calls ITSELF. It sounds mad, but think of
# standing between two mirrors, or of Russian dolls with a smaller doll inside
# each one. Every recursive function needs two parts:
#
#     1. a BASE CASE: the simplest situation, answered straight away, which
#        stops the recursion
#     2. a RECURSIVE CASE: solve a slightly smaller version of the
#        problem by calling itself
#
# Forget the base case and the function calls itself forever until Python
# crashes with a RecursionError.
#
# Finish `countdown(n)`: the base case (n is 0) is already done. For the
# recursive case, return n in a list followed by the countdown of n - 1.
# Lists can be joined with +, e.g. [3] + [2, 1].

def countdown(n):
    if n == 0:
        return [0]
    return ???
