# Exercise: Decorators 10
# I AM NOT DONE
#
# MEMOIZATION means remembering answers you've already worked out, so you
# don't repeat slow work. A decorator is perfect for this. The cache is a
# dictionary stored on the wrapper (wrapper.cache) with the arguments as the key:
#
#     if args in wrapper.cache:      <- seen before? use the saved answer
#         ...
#     else:
#         ...work it out, then save it in wrapper.cache[args]
#
# Finish the wrapper in `memoize` so that func is only called for arguments it
# hasn't seen before.

import functools


def memoize(func):
    @functools.wraps(func)
    def wrapper(*args):
        # bug: always calls func, never checks or updates the cache
        return func(*args)
    wrapper.cache = {}
    return wrapper


call_count = 0


@memoize
def slow_square(n):
    global call_count
    call_count += 1
    return n * n
