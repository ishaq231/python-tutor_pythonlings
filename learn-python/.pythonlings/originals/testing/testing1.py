# Exercise: Testing 1
# I AM NOT DONE
#
# How do you know your code works? You TEST it: run it and check that you
# get the answer you expect. Python's `assert` statement does this checking:
#
#     assert 1 + 1 == 2        <- nothing happens, the test passes
#     assert 1 + 1 == 3        <- raises an AssertionError, the test fails
#
# So silence means success, and an error means something is wrong.
#
# Replace the ??? so the assertion passes, i.e. what should double(2) be?

def double(x):
    return x * 2


result = double(2)
assert result == ???
