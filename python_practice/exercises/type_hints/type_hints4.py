# Exercise: Type Hints 4
# I AM NOT DONE
#
# Add type hints to the function `find_index`. It might return a number, or it might
# return nothing (None) if the item isn't found:
#   - the parameter `items` is a `list[str]`
#   - the parameter `target` is a `str`
#   - the function returns `int | None` (a number OR None)
#
# It should look like:
#   def find_index(items: list[str], target: str) -> int | None:
#
# Leave the `from __future__ import annotations` line below as it is.
# It makes the `int | None` style work on older versions of Python.

from __future__ import annotations


def find_index(items, target):
    try:
        return items.index(target)
    except ValueError:
        return None
