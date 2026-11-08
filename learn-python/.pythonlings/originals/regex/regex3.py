# Exercise: Regex 3
# I AM NOT DONE
#
# `re.findall(pattern, text)` finds EVERY match, and gives them to you as a list
# of strings.
#
# Special codes make patterns more powerful:
#     \d    any one digit (0 to 9)
#     +     "one or more" of the thing just before it
# So \d+ means "one or more digits in a row", like 12 or 450.
#
# Tip: patterns are full of backslashes, so write an `r` just before the
# opening quote, like r"\d+". This "raw string" tells Python to leave the
# backslashes alone.
#
# Replace the ??? with a pattern that finds all the numbers in `text`.

import re

text = "order 12 has 3 items and 450 points"
numbers = re.findall("???", text)
