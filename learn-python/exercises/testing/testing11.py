# Exercise: Testing 11
# I AM NOT DONE
#
# Testing a class: make an instance, call its methods, and assert that its
# attributes have the right values after each step.
#
# Finish `test_counter` so it:
#     1. creates a Counter and asserts its value is 0
#     2. calls increment() and asserts the value is 1
#     3. calls increment() again and asserts the value is 2
#     4. calls reset() and asserts the value is 0

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


def test_counter():
    # 1. create a Counter instance
    # 2-4. assert state after each method call
    pass
