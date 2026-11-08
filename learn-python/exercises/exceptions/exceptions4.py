# Exercise: Exceptions 4
# I AM NOT DONE
#
# try/except can have an `else` part too. It runs only if the `try` part
# finished with NO error. It's a tidy place for "and if all went well, then...".
#
#     try:
#         ...
#     except KeyError:
#         ...           <- runs if there was an error
#     else:
#         ...           <- runs if there was NO error
#
# Finish `load_value(data, key)`: if the key is missing, return "missing".
# Otherwise (in the `else` part) return the value doubled.

def load_value(data, key):
    try:
        value = data[key]
    except KeyError:
        return "missing"
    # TODO: add an else clause here that returns value * 2
