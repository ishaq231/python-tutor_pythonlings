# Exercise: Type Hints 8
# I AM NOT DONE
#
# Add full type hints to the function `summarise`:
#   - the parameter `records` is a `list[dict[str, int]]`
#   - the parameter `key` is a `str`
#   - the parameter `default` is an `int | None`
#   - the function returns a `dict[str, int | None]`
#
# It should look like:
#   def summarise(
#       records: list[dict[str, int]],
#       key: str,
#       default: int | None,
#   ) -> dict[str, int | None]:
#
# Leave the `from __future__ import annotations` line below as it is.
# It makes the `int | None` style work on older versions of Python.

from __future__ import annotations


def summarise(records, key, default):
    return {
        "count": len(records),
        "total": sum(r.get(key, default or 0) for r in records),
        "missing": default,
    }
