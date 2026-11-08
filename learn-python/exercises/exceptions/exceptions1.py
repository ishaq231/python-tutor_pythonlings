# Exercise: Exceptions 1
# I AM NOT DONE
#
# Sometimes things go wrong while a program runs, and Python raises an
# EXCEPTION, which is another word for an error. For example, 5 / 0 raises a
# ZeroDivisionError and the program crashes.
#
# You can catch errors and handle them with try / except:
#
#     try:
#         ...code that might go wrong...
#     except ZeroDivisionError:
#         ...what to do instead...
#
# Python runs the `try` part. If the named error happens, it jumps to the
# `except` part instead of crashing.
#
# Finish `safe_divide(a, b)` so that dividing by zero returns the string
# "error". A normal division should return the answer as usual.

def safe_divide(a, b):
    return a / b
