# Exercise: Type Hints 4
# I AM NOT DONE
#
# Sometimes a function might give back a value OR nothing at all (None). Use
# the vertical bar `|` to mean "or":
#
#     int | None       a whole number, or None
#
# `find_index` returns the position of an item, or None if it isn't in the
# list. Add type hints:
#     items is a list[str],  target is a str,  and it returns int | None
#
# It should look like:
#     def find_index(items: list[str], target: str) -> int | None:
#
# Leave the `from __future__ import annotations` line as it is. It makes the
# `int | None` style work on older versions of Python.

from __future__ import annotations


def find_index(items, target):
    try:
        return items.index(target)
    except ValueError:
        return None
