# Exercise: Classes 7
# I AM NOT DONE
#
# A method can call the object's other methods too, again using `self`:
#
#     self.get_name()
#
# Replace the ??? so the `greet` method uses the `get_name` method to get
# the name for its greeting.

class Greeter:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        return f"Hello, {???}!"


g = Greeter("Alice")
