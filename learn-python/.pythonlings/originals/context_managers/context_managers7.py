# Exercise: Context Managers 7
# I AM NOT DONE
#
# What if an error happens inside the `with` block? Python calls `__exit__` and
# passes in details of the error. If `__exit__` returns True, the error is
# SUPPRESSED (silenced) and the program carries on after the block. Returning
# None means the error carries on as normal.
#
# `exc_type` is the type of the error (or None if there was no error).
#
# Finish `SilentZeroDivision.__exit__` so that a ZeroDivisionError is suppressed
# (return True), and every other error is left alone (return None).

class SilentZeroDivision:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Bug: always returns None, so ZeroDivisionError is not suppressed.
        return None


result = "not set"
with SilentZeroDivision():
    result = 1 / 0        # should be suppressed
    result = "unreachable"

# If suppression works, `result` stays "not set" because the exception
# aborts the rest of the block body before the second assignment.
