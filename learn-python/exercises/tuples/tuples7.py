# Exercise: Tuples 7
# I AM NOT DONE
#
# Remember swapping from the Variables exercises? It is the same trick with tuples:
#
#     a, b = b, a
#
# The code below tries to swap with two separate lines, but it doesn't
# work. After `a = b`, a has already lost its old value, so both end up
# as 99! Replace those two lines with one line so that a is 99 and b is 7.

a = 7
b = 99

# swap a and b in one line using tuple unpacking
a = b
b = a
