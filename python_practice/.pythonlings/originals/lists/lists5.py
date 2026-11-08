# Exercise: Lists 5
# I AM NOT DONE
#
# Slicing works on lists in exactly the same way as on strings:
#     list[start:stop]    begins AT start and stops just BEFORE stop.
# Leave a number out and it goes to the end: list[:3] is the first three
# items, and list[2:] is everything from position 2 onwards. Negative numbers
# count from the back: list[-2:] is the last two.
#
# From letters = ["a", "b", "c", "d", "e", "f"], use slices to make:
#     first_three -> ["a", "b", "c"]
#     last_two    -> ["e", "f"]
#     middle      -> ["c", "d", "e"]   (positions 2 to 4)
# Don't use loops. Replace each ??? with a slice such as 1:3

letters = ["a", "b", "c", "d", "e", "f"]

first_three = letters[???]
last_two    = letters[???]
middle      = letters[???]
