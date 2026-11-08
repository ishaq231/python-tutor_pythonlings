# Exercise: Exceptions 8
# I AM NOT DONE
#
# You can have several `except` parts, one for each type of error. Python
# checks them from the top and uses the first one that matches. A plain
# `except Exception:` at the bottom catches any other normal error. (`Exception`
# is the "parent" of almost all error types.)
#
# Finish `classify_error(func)`. It calls func() and returns:
#     "ok"           if nothing went wrong
#     "value error"  if a ValueError was raised
#     "type error"   if a TypeError was raised
#     "other error"  for any other exception

def classify_error(func):
    try:
        func()
        return "ok"
    # TODO: add except clauses for ValueError, TypeError, and a catch-all
