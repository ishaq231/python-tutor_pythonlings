# Exercise: Type Hints 2
# I AM NOT DONE
#
# Add type hints to the function `greet` so that:
#   - the parameter `name` is a `str`
#   - the parameter `times` is an `int`
#   - the function returns a `str`
#
# It should look like:
#   def greet(name: str, times: int) -> str:

def greet(name, times):
    return (name + " ") * times
