# Exercise: Collections 1
# I AM NOT DONE
#
# The `collections` module has some extra-clever containers. The first is
# `Counter`, which counts things for you. Give it a list and it gives back a
# dictionary-like object of how many times each item appears:
#
#     Counter(["a", "b", "a"])     gives   Counter({"a": 2, "b": 1})
#
# It does the job of your frequency loop from the Dictionaries exercises in one line!
#
# Make `counts` a Counter of the `words` list.

from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = ???
