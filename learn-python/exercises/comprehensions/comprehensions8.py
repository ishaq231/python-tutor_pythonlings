# Exercise: Comprehensions 8
# I AM NOT DONE
#
# Remember the one-line if/else from the Conditionals exercises? You can use it
# in the FIRST part of a comprehension to choose a value for each item.
# Notice that this `if ... else` goes at the START, not the end, so it picks
# what to put in. (An `if` at the END would filter items out instead.)
#
#     ["pos" if x > 0 else "non-pos" for x in [-1, 2, 0]]
#     gives   ["non-pos", "pos", "non-pos"]
#
# Build `labels`: for each number in `values`, "even" if it's even, otherwise "odd".

values = [1, 2, 3, 4, 5, 6]

labels = ???
