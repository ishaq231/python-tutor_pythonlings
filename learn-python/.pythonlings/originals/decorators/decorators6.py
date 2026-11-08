# Exercise: Decorators 6
# I AM NOT DONE
#
# A problem with decorators: the wrapper replaces your function, so the
# function's name and its description (its docstring, the text in triple quotes)
# get replaced by the wrapper's. The fix is another decorator that is built in:
#
#     import functools
#
#     @functools.wraps(func)      <- put this on the line above `def wrapper`
#     def wrapper(...):
#
# It copies the original name and docstring onto the wrapper.
#
# Add the missing import and the @functools.wraps(func) line inside `preserve`.

def preserve(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@preserve
def compute(x, y):
    """Return the sum of x and y."""
    return x + y
