# Exercise: Datetime 3
# I AM NOT DONE
#
# Dates often arrive as text, like "2026-05-23 09:30". `datetime.strptime(text,
# format)` reads text into a datetime object (a date AND a time) using a format
# made of codes:
#     %Y  year (4 digits)    %m  month    %d  day
#     %H  hour (24-hour)     %M  minute
#
#     datetime.strptime("2026-05-23", "%Y-%m-%d")
#
# Replace the ??? so that `meeting` is `raw` parsed into a datetime.
# The format must match the text exactly (dashes, space and colon included).

from datetime import datetime

raw = "2026-05-23 09:30"
meeting = ???
