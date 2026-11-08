# Exercise: Decorators 8
# I AM NOT DONE
#
# What if you want to give the decorator an option, like @repeat(3)? Then you
# need THREE layers of functions:
#
#     def repeat(n):              <- 1. the factory: takes the option
#         def decorator(func):    <- 2. the real decorator: takes the function
#             def wrapper(*args, **kwargs):   <- 3. the wrapper
#                 ...
#             return wrapper
#         return decorator
#
# `repeat(3)` gives back a decorator, and the `@` then applies it.
#
# Finish `repeat(n)` so the wrapped function is called n times, and the
# LAST result is returned.

import functools


def repeat(n):
    # return a decorator here
    pass


@repeat(3)
def say(word):
    return word


@repeat(1)
def identity(x):
    return x
