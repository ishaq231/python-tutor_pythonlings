# Exercise: Type Hints 2
# I AM NOT DONE
#
# You can add type hints to a function too. Each parameter gets `: type`, and
# `->` followed by a type says what the function returns:
#
#     def add(x: int, y: int) -> int:
#
# Add type hints to `greet` so that:
#     name is a str, times is an int, and the function returns a str.
#
# It should look like:  def greet(name: str, times: int) -> str:

def greet(name, times):
    return (name + " ") * times
