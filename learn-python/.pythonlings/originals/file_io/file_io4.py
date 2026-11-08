# Exercise: File IO 4
# I AM NOT DONE
#
# A file usually has many lines. .readlines() gives you a LIST with one string
# per line. The lines still have the invisible "\n" new-line character on the end.
#
#     lines = open(path).readlines()
#
# `poem_path` has a poem with three lines. The code currently uses .read(),
# which gives one big string. Change it so `lines` is a list of the lines.

import tempfile

poem_path = tempfile.mktemp()
with open(poem_path, "w") as f:
    f.write("roses are red\nviolets are blue\npython is great\n")

# Read all lines into `lines`.
lines = open(poem_path).read()   # TODO: use .readlines() instead of .read()
