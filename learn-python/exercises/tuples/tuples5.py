# Exercise: Tuples 5
# I AM NOT DONE
#
# Tuples are IMMUTABLE, which is a long word for "can't be changed". So
# `original[1] = 99` would give an error. Instead you build a NEW tuple.
#
# Handy: you can slice tuples (like lists) and join them with `+`, as long as
# both sides are tuples. A one-item tuple needs its comma: (99,)
#
# Build a new tuple called `updated` which is the same as `original` except
# that the second item (index 1) is 99. It should be (10, 99, 30).

original = (10, 20, 30)

updated = original  # fix this — do not modify original, build a new tuple
