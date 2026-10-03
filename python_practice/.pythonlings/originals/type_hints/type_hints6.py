# Exercise: Type Hints 6
# I AM NOT DONE
#
# A type alias is a nickname for a long type. Make one called `Vector` that equals
# `list[float]`, then add type hints to the function `scale`:
#   - the parameter `v` is a `Vector`
#   - the parameter `factor` is a `float`
#   - the function returns a `Vector`
#
# Write:
#   Vector = list[float]
#
#   def scale(v: Vector, factor: float) -> Vector:

def scale(v, factor):
    return [x * factor for x in v]
