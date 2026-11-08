# Exercise: Generators 2
# I AM NOT DONE
#
# Calling a generator function does NOT run it. It gives back a GENERATOR
# OBJECT, like a machine that's ready to produce values when asked. It is not a
# list. To collect everything it makes into a list, wrap it with list():
#
#     list(three())      gives   [1, 2, 3]
#
# `squares(n)` is already written and works. Call `squares(5)`, turn the
# result into a list, and save it in `result`.

def squares(n):
    for i in range(1, n + 1):
        yield i * i


# Replace None with the correct expression.
result = None
