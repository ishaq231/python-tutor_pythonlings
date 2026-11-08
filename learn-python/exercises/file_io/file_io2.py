# Exercise: File IO 2
# I AM NOT DONE
#
# To get a file's text back, open it for reading and use .read(), which gives
# the whole file as one string.
#
#     text = open(path).read()
#
# `note_path` points to a file that contains the text "remember". Read the
# whole file and save its text in `contents`.

import tempfile

note_path = tempfile.mktemp()
with open(note_path, "w") as f:
    f.write("remember")

# Read the whole file into `contents`.
contents = ???
