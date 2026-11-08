# Exercise: Regex 10
# I AM NOT DONE
#
# Let's put it all together by parsing a log line:
#
#     [ERROR] db.engine: connection refused
#
# Write a pattern with three named groups: `level`, `logger` and `message`.
# Some building blocks you will need:
#     \[ and \]   match real square brackets
#     [\w.]+      letters, digits, underscores or dots (for the logger name)
#     .+          anything at all, to the end of the line (for the message)
# Everything else in the pattern, like the colon and the space, matches itself.

import re

log_line = "[ERROR] db.engine: connection refused"
pattern = "???"
match = re.search(pattern, log_line)
level = match.group("level")
logger = match.group("logger")
message = match.group("message")
