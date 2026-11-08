# Exercise: Pathlib 5
# I AM NOT DONE
#
# `.with_name("new.txt")` gives a new path in the same folder but with a
# different file name. The original is never changed.
#
# Replace the ??? so that `final` is "reports/final.txt", using `original`
# and .with_name().

from pathlib import Path

original = Path("reports/draft.txt")
final = ???
