# Exercise: Type Hints 5
# I AM NOT DONE
#
# A TUPLE is a fixed group of values, like the pair returned in the Functions
# exercises. In a hint you list the type of EACH position:
#
#     tuple[float, float]       exactly two decimals, like (1.5, 2.0)
#
# `bounding_box` takes a list of (x, y) points and returns a tuple of four
# numbers: (min_x, min_y, max_x, max_y). Add type hints:
#     points is a list[tuple[float, float]]
#     it returns tuple[float, float, float, float]
#
# It should look like:
#     def bounding_box(points: list[tuple[float, float]]) -> tuple[float, float, float, float]:

def bounding_box(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (min(xs), min(ys), max(xs), max(ys))
