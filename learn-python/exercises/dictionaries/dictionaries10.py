# Exercise: Dictionaries 10
# I AM NOT DONE
#
# A great use for a dictionary is COUNTING things. A "frequency dictionary"
# has the thing as its key and how many times you've seen it as its value.
#
# For each word in the loop:
#     - if you have already seen it, add 1 to its count
#     - if it's new, its count should start at 0 and go up to 1
# `.get(word, 0)` is perfect for this, because it gives you 0 if the word
# isn't in the dictionary yet.
#
# Count how many times each word appears in `words` and save the dictionary
# in `freq`. Expected: {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1,
# "and": 1, "hat": 1}

words = ["the", "cat", "sat", "on", "the", "mat", "and", "the", "cat", "hat"]

freq = {}
for ???:
    ???
