# Exercise: File IO 5
# I AM NOT DONE
#
# Writing with "w" wipes the file first! To ADD to a file without losing what is
# already there, open it in append mode: "a".
#
# `journal_path` already contains "day 1: sunny". Fix the code so that
# "day 2: rainy" is added after it, and both lines end up in the file.

import tempfile

journal_path = tempfile.mktemp()
with open(journal_path, "w") as f:
    f.write("day 1: sunny\n")

# Append "day 2: rainy\n" to journal_path.
with open(journal_path, "w") as fh:   # TODO: change "w" to "a"
    fh.write("day 2: rainy\n")
