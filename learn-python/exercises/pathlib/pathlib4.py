# Exercise: Pathlib 4
# I AM NOT DONE
#
# Putting what you know together: keep only the paths whose `.suffix` is
# ".py". A list comprehension with an `if` does it nicely.
#
# Replace the ??? so that `python_files` holds only the Python files from
# `files`, in order.

from pathlib import Path

files = [Path("app.py"), Path("README.md"), Path("tests.py")]
python_files = ???
