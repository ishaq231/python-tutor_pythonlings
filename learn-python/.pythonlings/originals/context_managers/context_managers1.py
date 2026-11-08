# Exercise: Context Managers 1
# I AM NOT DONE
#
# You have already met the `with` statement in File I/O. It's a safety net
# that makes sure something is tidied up (like closing a file) even if
# an error happens. Anything that works with `with` is called a CONTEXT MANAGER.
#
#     with open(path, "w") as f:
#         f.write("hi")
#     # the file is closed automatically here
#
# Rewrite the code below using a `with` statement to open `data_path` for
# writing and write "hello, context!". Don't call .close() yourself.

import tempfile

data_path = tempfile.mktemp()

# Replace the bare open/write/close below with a with-statement.
f = open(data_path, "w")
f.write("hello, context!")
# Bug: .close() is missing — but the real fix is to use `with`.
