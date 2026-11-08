# Exercise: Generators 6
# I AM NOT DONE
#
# A generator doesn't have to ever finish! An INFINITE generator uses a loop
# that never ends. It's safe because it only does the work when asked.
#
#     while True:
#         yield something
#
# But never call list() on an infinite generator. It would run forever! Instead
# use `itertools.islice(gen, 10)` to take just the first 10 values.
#
# Fix `natural_numbers()` so it yields 1, 2, 3, 4, ... forever. `first_ten`
# is already written and takes the first 10.

import itertools


def natural_numbers():
    # Bug: this yields nothing — make it yield 1, 2, 3, ... forever.
    return


first_ten = list(itertools.islice(natural_numbers(), 10))
