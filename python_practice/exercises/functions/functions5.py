# Exercise: Functions 5
# I AM NOT DONE
#
# Make a function called `make_greeting` that takes a `name` and an optional
# `greeting`. If no greeting is given, it should use "Hello" as the default.
# It should return the string "<greeting>, <name>!".
# Example: make_greeting("Alice") gives "Hello, Alice!"
# Example: make_greeting("Bob", "Hi") gives "Hi, Bob!"
# (Hint: a default looks like this: greeting="Hello")

def make_greeting(name, greeting):
    return f"{greeting}, {name}!"
