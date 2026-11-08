# Exercise: Testing 8
# I AM NOT DONE
#
# When you want to test one function with lots of inputs, don't write a
# separate assert for each. Make a list of (input, expected answer) pairs, and
# loop through them. The loop is already written, so you only need to fill
# in the list.
#
# Fill in `cases` with these (fahrenheit, celsius) pairs:
#     (32, 0.0)   (212, 100.0)   (98.6, 37.0)   (-40, -40.0)

def fahrenheit_to_celsius(f):
    return round((f - 32) * 5 / 9, 10)


def test_fahrenheit_to_celsius():
    cases = []  # replace with a list of (fahrenheit, celsius) tuples
    for f, expected in cases:
        assert abs(fahrenheit_to_celsius(f) - expected) < 1e-6, (
            f"fahrenheit_to_celsius({f}) expected {expected}"
        )
