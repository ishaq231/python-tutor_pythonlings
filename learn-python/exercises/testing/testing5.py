# Exercise: Testing 5
# I AM NOT DONE
#
# Good tests try a function with a variety of inputs, especially at the
# BOUNDARIES (the edges), because that's where bugs love to hide.
#
# `clamp(value, lo, hi)` keeps a number between a lowest and highest value.
# Write five asserts, one for each case:
#     clamp(5, 0, 10)   == 5      (inside the range)
#     clamp(-3, 0, 10)  == 0      (below the range)
#     clamp(15, 0, 10)  == 10     (above the range)
#     clamp(0, 0, 10)   == 0      (exactly on the low edge)
#     clamp(10, 0, 10)  == 10     (exactly on the high edge)

def clamp(value, lo, hi):
    return max(lo, min(value, hi))


def test_clamp():
    # write five assertions here
    pass
