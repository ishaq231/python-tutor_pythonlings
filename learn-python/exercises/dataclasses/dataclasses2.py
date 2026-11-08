# Exercise: Dataclasses 2
# I AM NOT DONE
#
# The fields of a dataclass are ordinary attributes, so you read them with a
# dot, e.g. orange.red. The values go in the same order as the fields were listed.
#
# 1. Create `orange` with red=255, green=128, blue=0.
# 2. Fix `description` so the ??? are replaced by the real field values and the
#    result is "R=255 G=128 B=0". In an f-string, put the attribute in curly
#    brackets, like {orange.red}.

from dataclasses import dataclass


@dataclass
class Color:
    red: int
    green: int
    blue: int


orange = Color(0, 0, 0)  # Bug: wrong values — use 255, 128, 0

description = f"R=??? G=??? B=???"  # Bug: replace ??? with the field values
