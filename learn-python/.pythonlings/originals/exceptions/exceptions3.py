# Exercise: Exceptions 3
# I AM NOT DONE
#
# You can save the error itself in a variable using `as`. Printing or
# converting it with str() gives the error message that Python wrote:
#
#     except ValueError as e:
#         return str(e)
#
# Finish `describe_error(s)` so it tries to turn `s` into a float and returns
# it. If it fails, it should return the error message (str(e)), NOT a fixed text.

def describe_error(s):
    return float(s)
