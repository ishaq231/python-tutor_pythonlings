# Exercise: Regex 1
# I AM NOT DONE
#
# A REGULAR EXPRESSION (or "regex") is a mini-language for describing patterns
# in text, like "three digits then a dash". Python's `re` module uses them.
# It's very handy for searching and checking text.
#
# The simplest pattern is just plain letters, which match themselves, so the
# pattern "cat" matches the text "cat".
#
#     re.match(pattern, text)
#
# `re.match` checks whether the text STARTS with the pattern. It gives back a
# "match object" if it does, or None if it doesn't. (A match object counts as
# True in an `if`, and None counts as False, remember truthiness!)
#
# Replace the ??? with a pattern that matches the start of `text`, which is
# "hello world".

import re

text = "hello world"
pattern = "???"
result = re.match(pattern, text)
