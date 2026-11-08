# Exercise: Collections 3
# I AM NOT DONE
#
# A `defaultdict` is a dictionary that never gives a KeyError. If you look up a
# key that doesn't exist yet, it quietly creates it with a starting value.
# You tell it what kind of starting value to use:
#
#     counts = defaultdict(int)     <- int() is 0, so new keys start at 0
#     counts["a"] += 1              <- no need to check if "a" exists first
#
# Make `char_counts` a defaultdict(int), then in the loop add 1 to the count
# for each character `ch`. Don't use Counter this time.

from collections import defaultdict

text = "mississippi"
char_counts = ???
for ch in text:
    ???
