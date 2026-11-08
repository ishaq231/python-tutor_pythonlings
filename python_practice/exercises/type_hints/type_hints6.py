# Exercise: Type Hints 6
# I AM NOT DONE
#
# Long hints get hard to read, so you can give one a nickname. This is called
# a TYPE ALIAS. It's just a variable that holds a type:
#
#     Names = list[str]
#     def shout(names: Names) -> Names:
#
# Make an alias `Vector` that equals `list[float]`, then add hints to `scale`:
#     v is a Vector,  factor is a float,  and it returns a Vector
#
# It should look like:
#     Vector = list[float]
#     def scale(v: Vector, factor: float) -> Vector:

def scale(v, factor):
    return [x * factor for x in v]
