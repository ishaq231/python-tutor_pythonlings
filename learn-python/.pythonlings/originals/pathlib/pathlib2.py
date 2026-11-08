# Exercise: Pathlib 2
# I AM NOT DONE
#
# The `/` sign has a special meaning for paths: it JOINS parts together, adding
# the right slash for your computer (Windows uses backslashes!).
#
#     Path("photos") / "cat.jpg"       gives   Path("photos/cat.jpg")
#
# Replace the ??? so that `source` is the path "pythonlings/src/main.py",
# built from `project` using / for the rest.

from pathlib import Path

project = Path("pythonlings")
source = ???
