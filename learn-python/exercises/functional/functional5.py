# Exercise: Functional 5
# I AM NOT DONE
#
# `sorted()` can take a `key=` function. Python runs it on every item and
# sorts by the answers (not by the items themselves).
#
#     sorted(["bb", "a", "ccc"], key=lambda w: -len(w))
#     gives   ["ccc", "bb", "a"]
#
# Replace the ??? with a lambda that returns the length of a word, so
# `by_length` is sorted from the shortest word to the longest.

words = ["banana", "fig", "apple", "kiwi", "date"]

by_length = sorted(words, key=???)
