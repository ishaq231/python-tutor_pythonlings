# Exercise: File IO 6
# I AM NOT DONE
#
# You can loop straight over an open file and get one line at a time:
#
#     for line in fh:
#
# Each line is a string that ends with "\n". To use it as a number, remove
# the spaces and new-line with .strip() and then convert with int():
#     int(line.strip())
#
# The file contains five numbers, one per line. Fix the loop so `total`
# becomes the sum of them (10 + 20 + 30 + 40 + 50).

import tempfile

numbers_path = tempfile.mktemp()
with open(numbers_path, "w") as f:
    f.write("10\n20\n30\n40\n50\n")

total = 0
# Iterate over the file's lines and add each integer value to total.
with open(numbers_path) as fh:
    for line in fh:
        total += line   # TODO: convert line to int first (strip whitespace)
