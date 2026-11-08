# Exercise: Generators 5
# I AM NOT DONE
#
# `next(gen)` asks a generator for its next value, one at a time. Each call
# carries on from where the last stopped. When there are no more values left,
# Python raises a StopIteration error to say it's finished. (A `for` loop
# handles that quietly for you.)
#
# `letters` yields "a", "b", "c". Replace each `None` with a next(gen) call to
# get the first, second and third values. Don't turn the whole thing into a list.

def letters():
    yield "a"
    yield "b"
    yield "c"


gen = letters()

# Replace each None with a next() call on gen.
first = None
second = None
third = None
