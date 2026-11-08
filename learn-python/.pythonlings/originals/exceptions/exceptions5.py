# Exercise: Exceptions 5
# I AM NOT DONE
#
# A `finally` part ALWAYS runs at the end, whether there was an error or not,
# even if a `return` has just happened. It's used for tidying up, like
# closing a file.
#
#     try:
#         ...
#     except SomeError:
#         ...
#     finally:
#         ...           <- always runs
#
# Finish `read_first(items)`: try to return items[0], and return None if
# the list is empty (an IndexError). In a `finally` part, use log.append("done")
# so "done" is added to the list `log` every time.

log = []

def read_first(items):
    try:
        return items[0]
    except IndexError:
        return None
    # TODO: add a finally clause that does log.append("done")
