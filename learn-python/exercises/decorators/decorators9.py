# Exercise: Decorators 9
# I AM NOT DONE
#
# Decorators can be stacked. The one closest to the `def` is applied FIRST,
# then the one above wraps the result of that.
#
#     @outer
#     @inner
#     def f(): ...
#
# is the same as  f = outer(inner(f))
#
# Stack both decorators on `get_value` so it returns "[B][A]42". Think about
# which wrapper adds its text first and which one goes on the outside.

def add_a(func):
    def wrapper():
        return "[A]" + func()
    return wrapper


def add_b(func):
    def wrapper():
        return "[B]" + func()
    return wrapper


def get_value():
    return "42"
