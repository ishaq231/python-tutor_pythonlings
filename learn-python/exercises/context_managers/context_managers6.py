# Exercise: Context Managers 6
# I AM NOT DONE
#
# Writing a whole class is a lot of work. The `contextmanager` decorator (the
# @ line above the function) lets you write a context manager as a single
# generator function with ONE `yield`:
#
#     @contextmanager
#     def thing():
#         ...setup (this is like __enter__)...
#         yield value       <- the value that `as` receives
#         ...clean-up (this is like __exit__)...
#
# Fill in the body of `managed_counter`:
#     1. make an empty list called `counter`
#     2. yield `counter`
#     3. after the yield, append the string "finished" to `counter`

from contextlib import contextmanager


@contextmanager
def managed_counter():
    # Bug: body is missing — add counter, yield, then cleanup.
    pass


with managed_counter() as counter:
    counter.append(1)
    counter.append(2)
