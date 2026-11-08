# Exercise: Regex 8
# I AM NOT DONE
#
# `re.sub(pattern, replacement, text)` finds every match and REPLACES it,
# giving back a new string. It's like .replace() but far more powerful.
#
# The vertical bar | means "or", so spam|junk matches either "spam" or "junk".
#
# Replace the ??? with a pattern that matches either bad word, so both get
# changed to "***".

import re

text = "This email is full of spam and junk, total spam!"
pattern = "???"
clean = re.sub(pattern, "***", text)
