# Exercise: Generators 3
# I AM NOT DONE
#
# A generator can decide what to hand out. Put the `yield` inside an `if` and
# only the values that pass the test come out. Also, a `for` loop can run over a
# generator directly, taking each value one by one.
#
# Finish `evens_up_to(n)` so it yields only the even numbers from 2 up to n.

def evens_up_to(n):
    for i in range(1, n + 1):
        # yield only when i is even
        pass


collected = []
for value in evens_up_to(8):
    collected.append(value)
