# Exercise: File IO 10
# I AM NOT DONE
#
# You can have two files open at once. Here one is read and the other
# is written. This is a "copy" with a twist: every line is changed to UPPERCASE
# on the way across. (.upper() makes capital letters, as you saw in Strings.)
#
# Fix the code so that `dst_path` ends up containing the uppercase version
# of the text in `src_path`.

import tempfile

src_path = tempfile.mktemp()
dst_path = tempfile.mktemp()

with open(src_path, "w") as f:
    f.write("hello world\npython is fun\nfile io rocks\n")

# Copy src_path to dst_path, converting each line to uppercase.
with open(src_path) as src:
    with open(dst_path, "w") as dst:
        for line in src:
            dst.write(line)   # TODO: write line.upper() instead of line
