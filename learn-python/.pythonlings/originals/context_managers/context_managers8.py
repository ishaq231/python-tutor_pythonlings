# Exercise: Context Managers 8
# I AM NOT DONE
#
# Challenge time! Use everything from this topic.
#
# Part 1, the `Resource` class (fill in the three methods marked "Bug"):
#     __init__   sets self.acquired = False and self.release_log = []
#     __enter__  sets self.acquired = True and returns self
#     __exit__   sets self.acquired = False and adds "released" to
#                self.release_log (and returns None)
#
# Part 2, `ManagedPool(resource)` using @contextmanager:
#     1. call resource.__enter__() to acquire it
#     2. yield the resource
#     3. call resource.__exit__(None, None, None) to release it

from contextlib import contextmanager


class Resource:
    def __init__(self):
        # Bug: attributes are missing — set acquired and release_log.
        pass

    def __enter__(self):
        # Bug: missing — set acquired, return self.
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Bug: missing — clear acquired, log "released".
        pass


@contextmanager
def ManagedPool(resource):
    # Bug: missing — acquire, yield resource, release.
    pass


r = Resource()
with ManagedPool(r) as res:
    in_block_acquired = res.acquired
