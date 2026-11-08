# Exercise: Regex 9
# I AM NOT DONE
#
# Numbered groups get confusing. You can NAME a group with ?P<name>
# right after the opening bracket:
#
#     (?P<year>\d{4})        <- a group called "year" holding four digits
#
# then ask for it by name: match.group("year")
#
# A date looks like "2024-07-15". Write a pattern with three named groups,
# "year", "month" and "day", with literal dashes between them.

import re

date_str = "2024-07-15"
pattern = "???"
match = re.search(pattern, date_str)
year = match.group("year")
month = match.group("month")
day = match.group("day")
