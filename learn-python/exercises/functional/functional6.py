# Exercise: Functional 6
# I AM NOT DONE
#
# Because functions are values, you can pass one function INTO another. A
# function that takes a function as a parameter is called a HIGHER-ORDER
# function. (Hold on to this idea. Decorators are built on it.)
#
#     def run(func, x):
#         return func(x)
#
# Fill in `apply_twice` so it applies `func` to `value` and then applies `func`
# again to that result: f(f(x)). The two lambdas below are for testing it.

def apply_twice(func, value):
    pass


triple = lambda x: x * 3
add_ten = lambda x: x + 10
