# Exercise: Decorators 2
# I AM NOT DONE
#
# A DECORATOR is a function that takes a function, wraps it inside a new
# function that adds some extra behaviour, and returns that new function.
#
#     def decorator(func):
#         def wrapper():
#             ...extra stuff before or after...
#             return func()
#         return wrapper
#
# The wrapper is an inner function (a function inside a function) that can use
# `func` from outside it.
#
# Finish the `shout` decorator so the wrapper returns the result of `func()`
# in UPPERCASE. Use the .upper() method. The last line makes the new wrapped
# function by hand: loud_greet = shout(greet).

def shout(func):
    def wrapper():
        result = func()
        # return the result, uppercased
        return result
    return wrapper


def greet():
    return "hello"


loud_greet = shout(greet)
