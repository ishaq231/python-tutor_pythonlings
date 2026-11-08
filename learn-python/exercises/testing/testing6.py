# Exercise: Testing 6
# I AM NOT DONE
#
# Sometimes the RIGHT behaviour is for a function to raise an error (like
# for bad input). To test that, use try/except from the Exceptions topic. The
# trick is the line after the call: if no error happened, the test must fail.
#
#     try:
#         function_that_should_fail()
#         assert False, "expected an error but none came"
#     except ValueError:
#         pass      <- this is the good outcome
#
# Finish `test_parse_positive` with two checks:
#     1. parse_positive("42") == 42
#     2. parse_positive("-1") raises a ValueError

def parse_positive(s):
    n = int(s)
    if n < 0:
        raise ValueError(f"{n} is not positive")
    return n


def test_parse_positive():
    # 1. assert the happy path
    # 2. use try/except to verify ValueError is raised for "-1"
    pass
