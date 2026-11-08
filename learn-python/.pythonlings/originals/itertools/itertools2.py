# Exercise: Itertools 2
# I AM NOT DONE
#
# `count(start)` is an infinite counter: start, start + 1, start + 2 ... forever!
# You met infinite generators in the Generators topic, so remember it's unsafe
# to put one inside list(). Use `islice(thing, n)` to take only the first n
# items from it.
#
# Replace the ??? so that `first_four` is the first four numbers counting up
# from 10: [10, 11, 12, 13].

from itertools import count, islice

first_four = list(???)
