# Exercise: Regex 4
# I AM NOT DONE
#
# Square brackets make a CHARACTER CLASS: "any ONE character from this set".
# Ranges are allowed:
#     [a-z]    any lowercase letter          [A-Z]   any capital letter
#     [0-9]    any digit                     [a-zA-Z]  any letter at all
#
# Add `+` after it to match a run of them: [a-z]+ is a whole lowercase word.
#
# Replace the ??? with a pattern that finds only the runs of lowercase
# letters in `text`, ignoring capitals, digits and punctuation.

import re

text = "Hello world 123 foo_bar baz!"
words = re.findall("???", text)
