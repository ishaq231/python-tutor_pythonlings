# Exercise: Functional 7
# I AM NOT DONE
#
# A function can also RETURN another function. An inner function remembers
# the variables of the function that made it (this is called a CLOSURE).
#
#     def make_adder(n):
#         return lambda x: x + n       <- remembers n
#
#     add5 = make_adder(5)
#     add5(10)      gives   15
#
# Finish `make_multiplier(n)` so that it returns a function which multiplies
# its input by n. For example make_multiplier(3)(4) is 12.

def make_multiplier(n):
    pass
