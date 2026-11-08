# Exercise: Exceptions 2
# I AM NOT DONE
#
# Different mistakes give different error types, so you can catch just the one
# you expect. Trying to turn "hello" into a number with int("hello") raises
# a ValueError.
#
# It's best to catch the SPECIFIC error you expect (like `except ValueError:`)
# so other, unexpected bugs aren't hidden.
#
# Finish `parse_number(s)` so it converts the string `s` to an int and returns
# it. If that doesn't work, return -1 instead.

def parse_number(s):
    return int(s)
