# Exercise: Type Hints 5
# I AM NOT DONE
#
# Add type hints to the function `bounding_box`. It returns a tuple (a fixed-size group) of 4 numbers:
#   - the parameter `points` is a `list[tuple[float, float]]` (a list of x, y pairs)
#   - the function returns `tuple[float, float, float, float]`
#     (this stands for min_x, min_y, max_x, max_y)
#
# It should look like:
#   def bounding_box(points: list[tuple[float, float]]) -> tuple[float, float, float, float]:

def bounding_box(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return (min(xs), min(ys), max(xs), max(ys))
