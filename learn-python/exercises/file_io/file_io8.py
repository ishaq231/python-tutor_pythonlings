# Exercise: File IO 8
# I AM NOT DONE
#
# Text read from a file can have unwanted spaces around it. You already know
# the fix from the Strings exercises: .strip().
#
# `source_path` contains "  Hello, World!  " with spaces at each end. Fix the code
# so `result` has the spaces removed.

import tempfile

source_path = tempfile.mktemp()
with open(source_path, "w") as f:
    f.write("  Hello, World!  ")

# Read the file and strip whitespace; store in `result`.
with open(source_path) as fh:
    result = fh.read()   # TODO: call .strip() on the result
