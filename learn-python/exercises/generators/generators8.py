# Exercise: Generators 8
# I AM NOT DONE
#
# An ITERABLE is anything you can loop over with `for`. To make your own class
# iterable, give it an `__iter__` method. A very easy way to write one is to
# make `__iter__` itself a generator by using `yield` in it.
#
# Add an `__iter__` method to `Countdown` that yields the numbers from
# self.start down to 1. For example list(Countdown(3)) is [3, 2, 1].
# Don't write a `__next__` method.

class Countdown:
    def __init__(self, start):
        self.start = start

    # Bug: __iter__ is missing — add it so the class is iterable.
