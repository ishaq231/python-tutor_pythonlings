# Exercise: Pathlib 1
# I AM NOT DONE
#
# `pathlib` is the modern way to work with file and folder locations (called
# PATHS). A `Path` object knows about the parts of a path. Its attributes
# include `.name`, the final part (the file name).
#
#     Path("photos/cat.jpg").name      gives   "cat.jpg"
#
# Replace the ??? so that `path` is the path "notes/today.txt".

from pathlib import Path

path = ???
filename = path.name
