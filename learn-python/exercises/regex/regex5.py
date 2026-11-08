# Exercise: Regex 5
# I AM NOT DONE
#
# Some characters have a special job in a pattern, and the dot is one of
# them: `.` means "any character at all". To match an actual full stop you must
# ESCAPE it with a backslash: \.
#
# Version numbers look like 3.10: some digits, a dot, then some digits.
# Replace the ??? with a pattern that finds these in `text`. It must NOT
# match "1.x" or "42".

import re

text = "requires python 3.10 or 2.7, not 1.x or 42"
versions = re.findall("???", text)
