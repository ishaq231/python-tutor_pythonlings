# Exercise: Context Managers 5
# I AM NOT DONE
#
# Whatever `__enter__` returns becomes the variable after `as`:
#
#     with thing as x:      <- x is what thing.__enter__() returned
#
# Fix `DatabaseConnection.__enter__` so it returns `self.connection` (the
# dictionary set up in __init__) instead of None.

class DatabaseConnection:
    def __init__(self, dsn):
        self.dsn = dsn
        self.open = True
        self.connection = {"dsn": dsn, "active": True}

    def __enter__(self):
        # Bug: returns None instead of self.connection.
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open = False


db = DatabaseConnection("sqlite:///:memory:")
with db as conn:
    result = conn
