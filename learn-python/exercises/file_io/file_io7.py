# Exercise: File IO 7
# I AM NOT DONE
#
# .write() puts exactly what you give it into the file, and doesn't add a
# new line for you. To get each word on its own line, YOU must add the "\n"
# at the end of every word.
#
# Write the words so the file contains exactly "alpha\nbeta\ngamma\n".
# Fix the line so every word ends with "\n". A loop with fh.write(w + "\n")
# works well.

import tempfile

words_path = tempfile.mktemp()
words = ["alpha", "beta", "gamma"]

# Write each word to words_path on its own line.
with open(words_path, "w") as fh:
    fh.writelines(words)   # TODO: each word needs a newline at the end
