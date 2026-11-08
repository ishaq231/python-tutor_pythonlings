# Exercise: Pathlib 6
# I AM NOT DONE
#
# Similarly, `.with_suffix(".new")` swaps the ending, and `.parts` gives the
# path as a tuple of its pieces, e.g. ("data", "raw.json").
#
# Replace the ??? so that `processed` is "data/raw.json", made from `source`
# by changing its suffix to ".json".

from pathlib import Path

source = Path("data/raw.csv")
processed = ???
parts = processed.parts
