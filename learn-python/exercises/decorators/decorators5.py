# Exercise: Decorators 5
# I AM NOT DONE
#
# So far the wrapped functions took no arguments. To make a decorator work for
# ANY function, the wrapper should accept anything and pass it all on. Remember
# *args and **kwargs from the Functions exercises? They are made for this:
#
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
# Fix the wrapper in `log_call` so that it accepts *args and **kwargs and
# forwards them to func.

def log_call(func):
    def wrapper():   # bug: accepts no arguments
        print(f"calling {func.__name__}")
        return func()  # bug: forwards no arguments
    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
