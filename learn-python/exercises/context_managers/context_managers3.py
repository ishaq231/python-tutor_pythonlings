# Exercise: Context Managers 3
# I AM NOT DONE
#
# You can make your OWN classes work with `with` by giving them two special
# methods:
#     __enter__   runs at the start of the block. Whatever it returns is what
#                 `as` gives you
#     __exit__    runs at the end, even if there was an error. It takes three
#                 extra parameters about any error that happened:
#                 def __exit__(self, exc_type, exc_val, exc_tb):
#
# Add both to `Timer`:
#     __enter__ returns self
#     __exit__ sets self.finished to True

class Timer:
    def __init__(self):
        self.finished = False

    # Bug: __enter__ and __exit__ are missing — add them.


t = Timer()
with t:
    pass
