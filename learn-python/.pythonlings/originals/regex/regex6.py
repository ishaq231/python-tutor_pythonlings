# Exercise: Regex 6
# I AM NOT DONE
#
# ANCHORS pin a pattern to the start or end of the text:
#     ^   the start of the text
#     $   the end of the text
# And {n} means "exactly n of the thing before it", so \d{3} is exactly three digits.
#
# `re.fullmatch` is like having both anchors: the WHOLE text must match.
# (`bool(...)` turns the match object into True or False.)
#
# Replace the ??? with a pattern for a valid code: exactly five capital
# letters followed by exactly three digits, like "ABCDE123".

import re

code = "ABCDE123"
pattern = "???"
is_valid = bool(re.fullmatch(pattern, code))
