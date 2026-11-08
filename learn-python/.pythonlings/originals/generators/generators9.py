# Exercise: Generators 9
# I AM NOT DONE
#
# Behind the scenes, a `for` loop uses the ITERATOR PROTOCOL: it calls
# `__iter__` to get an iterator, then keeps calling `__next__` on it. When
# there is nothing left, __next__ must raise StopIteration to tell the loop
# to stop:
#
#     raise StopIteration
#
# Right now `Counter.__next__` goes on forever. Fix it so Counter(stop) counts
# 0, 1, 2, ... up to stop - 1, just like range(stop), and then raises
# StopIteration.

class Counter:
    def __init__(self, stop):
        self.stop = stop
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Bug: increments forever — add a StopIteration guard.
        value = self.current
        self.current += 1
        return value
