# Exercise: Regex 2
# I AM NOT DONE
#
# `re.match` only looks at the very start. `re.search` is more useful: it
# scans through the WHOLE text and finds the first place where the pattern
# matches. It gives back a match object, or None if there is no match.
#
# Replace the ??? with a pattern that finds the word "python" inside `text`.

import re

text = "I love python programming"
pattern = "???"
result = re.search(pattern, text)
