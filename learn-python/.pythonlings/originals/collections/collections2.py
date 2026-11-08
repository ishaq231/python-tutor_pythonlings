# Exercise: Collections 2
# I AM NOT DONE
#
# A Counter has a handy method, .most_common(n). It gives back the n items
# with the highest counts as a list of (item, count) tuples, biggest first.
#
#     Counter("aabbbc").most_common(2)     gives   [("b", 3), ("a", 2)]
#
# `tally` is already a Counter of the votes. Set `top2` to the two most common.

from collections import Counter

votes = [
    "Alice", "Bob", "Alice", "Carol", "Bob", "Alice",
    "Carol", "Bob", "Alice", "Carol",
]
tally = Counter(votes)
top2 = ???
