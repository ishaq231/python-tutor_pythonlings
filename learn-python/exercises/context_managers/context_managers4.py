# Exercise: Context Managers 4
# I AM NOT DONE
#
# `__exit__` is the place for CLEAN-UP, the job you want done at the end no
# matter what. Think of it as turning off the lights as you leave.
#
# `ManagedList` already has an `__enter__`. Finish `__exit__` so it adds the
# string "done" to self.log.

class ManagedList:
    def __init__(self):
        self.items = []
        self.log = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Bug: cleanup is missing — append "done" to self.log.
        pass


ml = ManagedList()
with ml as resource:
    resource.items.append(1)
    resource.items.append(2)
