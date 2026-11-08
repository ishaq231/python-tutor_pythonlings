# Exercise: Decorators 3
# I AM NOT DONE
#
# Writing `loud_greet = shout(greet)` is a bit long-winded. Python has a
# short-cut: write @decorator_name on the line directly above the `def`.
#
#     @shout
#     def greet():
#         ...
#
# is exactly the same as writing  greet = shout(greet)  after the function.
#
# Put `@stamp` directly above `def get_message():` so calling get_message()
# returns "[STAMPED] hello". The decorator is already written.

def stamp(func):
    def wrapper():
        return "[STAMPED] " + func()
    return wrapper


def get_message():
    return "hello"
