# Exercise: Regex 7
# I AM NOT DONE
#
# Round brackets make a GROUP, which remembers the part of the text it matched.
# You can then pull that part out with match.group(1) (the first group, groups
# count from 1).
#
# Because ( and ) are used for groups, matching real brackets in the text
# needs a backslash: \( and \)
#
# Phone numbers look like "(415) 555-2671". Replace the ??? with a pattern
# that matches the whole format, with the three-digit area code inside a
# group. Then `area_code` will be "415".

import re

phone = "(415) 555-2671"
pattern = "???"
match = re.search(pattern, phone)
area_code = match.group(1)
