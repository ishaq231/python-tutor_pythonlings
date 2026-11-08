# Exercise: Testing 10
# I AM NOT DONE
#
# EDGE CASES are the unusual inputs most likely to break your code: empty
# lists, zero, negative numbers, and so on. Good testers actively try to
# break things.
#
# Finish `test_sum_list` with five asserts:
#     sum_list([])         == 0     (empty list)
#     sum_list([0])        == 0     (a single zero)
#     sum_list([-1, -2])   == -3    (all negative)
#     sum_list([1, -1])    == 0     (they cancel out)
#     sum_list([1, 2, 3])  == 6     (a normal list)

def sum_list(numbers):
    return sum(numbers)


def test_sum_list():
    # write five assertions covering the edge cases above
    pass
