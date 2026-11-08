# Exercise: Decorators 7
# I AM NOT DONE
#
# Functions are objects, so they can carry attributes, just like the
# instances in the Classes exercises. A decorator can use this to remember
# things between calls, like a counter.
#
# Fix the wrapper in `count_calls` so that it adds 1 to wrapper.call_count
# every time it is called, before it calls func.

import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # bug: call_count is never incremented
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


@count_calls
def add(a, b):
    return a + b
