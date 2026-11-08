# Exercise: Datetime 8
# I AM NOT DONE
#
# `date.fromisoformat("2026-05-23")` reads dates written the standard
# YEAR-MONTH-DAY way (called ISO format). It's done for you here.
#
# Dates can be compared, so Python's min() and max() work on them too, and
# they give the earliest and latest. Replace the ??? so that `earliest` and
# `latest` are the earliest and latest dates in `parsed`.

from datetime import date

raw_dates = ["2026-05-23", "2024-01-01", "2025-12-31"]
parsed = [date.fromisoformat(value) for value in raw_dates]
earliest = ???
latest = ???
