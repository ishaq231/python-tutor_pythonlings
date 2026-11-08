# Exercise: File IO 9
# I AM NOT DONE
#
# To count the words in a text: .split() with nothing in the brackets chops a
# string into a list of words (at any spaces), and len() counts the list.
# Right now the code counts letters instead of words. Fix it so `word_count`
# is the number of words in the file.

import tempfile

essay_path = tempfile.mktemp()
with open(essay_path, "w") as f:
    f.write("the quick brown fox jumps over the lazy dog")

# Count the words in essay_path and store in `word_count`.
with open(essay_path) as fh:
    word_count = len(fh.read())   # TODO: split into words before taking len()
