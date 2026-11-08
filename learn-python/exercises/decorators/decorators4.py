# Exercise: Decorators 4
# I AM NOT DONE
#
# A wrapper must hand back the result of the wrapped function with `return`.
# Otherwise the answer is thrown away and the caller gets None (nothing).
#
# The wrapper in `double_result` calls func() but throws the result away. Fix it
# so the wrapper returns double the wrapped function's result.

def double_result(func):
    def wrapper():
        func()   # bug: the return value is thrown away
    return wrapper


@double_result
def get_five():
    return 5


@double_result
def get_ten():
    return 10
