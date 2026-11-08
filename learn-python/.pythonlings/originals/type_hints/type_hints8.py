# Exercise: Type Hints 8
# I AM NOT DONE
#
# Time to put everything together! Add full type hints to `summarise`:
#     records is a list[dict[str, int]]
#     key is a str
#     default is an int | None
#     it returns a dict[str, int | None]
#
# It should look like:
#     def summarise(
#         records: list[dict[str, int]],
#         key: str,
#         default: int | None,
#     ) -> dict[str, int | None]:
#
# Leave the `from __future__ import annotations` line as it is.

from __future__ import annotations


def summarise(records, key, default):
    return {
        "count": len(records),
        "total": sum(r.get(key, default or 0) for r in records),
        "missing": default,
    }
