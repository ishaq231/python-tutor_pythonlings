# Exercise: Dataclasses 3
# I AM NOT DONE
#
# A field can have a DEFAULT value, written with `=`, just like a default
# parameter in a function. Fields with defaults must come AFTER the ones without.
#
#     unit: str = "m"
#
# Give `unit` a default of "m/s²" so that Measurement(9.8) works.

from dataclasses import dataclass


@dataclass
class Measurement:
    value: float
    unit: str  # Bug: no default — add = "m/s²" here


gravity = Measurement(9.8)
named = Measurement(100.0, "km/h")
