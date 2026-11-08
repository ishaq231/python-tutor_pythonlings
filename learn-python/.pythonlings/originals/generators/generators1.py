# Exercise: Generators 1
# I AM NOT DONE
#
# A normal function runs, hits `return`, and is finished. A GENERATOR function
# uses `yield` instead. It hands back one value, then PAUSES, remembering
# exactly where it was. When you ask for the next value it carries on from that
# spot. Think of it like a bookmark in a book.
#
#     def three():
#         yield 1
#         yield 2
#         yield 3
#
# Any function with a `yield` inside it is a generator function.
#
# Finish `count_up_to(n)` so that it yields the whole numbers 1, 2, ... up to n
# one at a time. Replace the `pass` with a `yield` of the loop variable.

def count_up_to(n):
    for i in range(1, n + 1):
        # yield the value here
        pass
