# Exercise: Pathlib 3
# I AM NOT DONE
#
# Paths can be taken apart:
#     .parent   the folder it's in (as a Path)
#     .stem     the file name without the ending
#     .suffix   the ending, including the dot
#
#     Path("photos/cat.jpg")   ->   parent: photos, stem: cat, suffix: .jpg
#
# Replace the three ??? with those attributes of `path`.

from pathlib import Path

path = Path("docs/guide.md")
parent = ???
stem = ???
suffix = ???
