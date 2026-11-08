# Exercise: Testing 7
# I AM NOT DONE
#
# You can also check the MESSAGE of an error. Catch it with `as e`, and use
# `str(e)` to get the message text:
#
#     except ValueError as e:
#         assert "some words" in str(e)
#
# Finish `test_divide_message` with two checks:
#     1. divide(10, 2) == 5.0
#     2. divide(5, 0) raises a ValueError whose message contains "zero"

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def test_divide_message():
    # 1. happy-path assertion
    # 2. catch ValueError and check its message contains "zero"
    pass
