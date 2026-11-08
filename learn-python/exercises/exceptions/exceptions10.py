# Exercise: Exceptions 10
# I AM NOT DONE
#
# Time to put it all together! Validation means checking that data makes
# sense before using it. Check the rules in this order, raising an error with
# the exact message given for the first rule that is broken:
#
#     1. name must be a str      -> TypeError("username must be a str")
#        (check with isinstance(name, str))
#     2. 3 to 20 characters long -> ValueError("username must be 3–20 characters")
#     3. only letters and digits -> ValueError("username must be alphanumeric")
#        (name.isalnum() tells you this)
#
# If everything is fine, return name.lower().

def validate_username(name):
    # TODO: check type (raise TypeError if not str)
    # TODO: check length (raise ValueError if out of 3–20 range)
    # TODO: check alphanumeric (raise ValueError if not .isalnum())
    return name.lower()
