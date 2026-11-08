# Exercise: Context Managers 2
# I AM NOT DONE
#
# A file object has a `closed` attribute that tells you if it's closed. With
# `with`, it's True as soon as the indented block ends. Without `with`,
# the file stays open.
#
# Rewrite the code with a `with` statement that opens `data_path` for writing and
# writes "closed check". Keep the file variable called `f`, so that after the
# `with` block `f.closed` is True.

import tempfile

data_path = tempfile.mktemp()

# Bug: no with-statement — the file stays open until garbage-collected.
f = open(data_path, "w")
f.write("closed check")
# .close() is intentionally omitted to illustrate the problem.
