# Exercise: File IO 3
# I AM NOT DONE
#
# It is easy to forget to close a file. The `with` statement does it for
# you automatically as soon as the indented block finishes, even if an error
# happens. This is the proper way to work with files.
#
#     with open(path, "w") as fh:
#         fh.write(text)
#
# (`fh` is just a name for the open file. It stands for "file handle".)
#
# Replace the ??? so the `with` block writes "first entry".

import tempfile

log_path = tempfile.mktemp()

# Replace the ??? so the with-block writes "first entry".
with open(log_path, "w") as fh:
    fh.write(???)
