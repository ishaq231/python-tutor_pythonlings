# Exercise: Functions 5
# I AM NOT DONE
#
# You can give a parameter a DEFAULT value by writing `=` after it. If the
# caller doesn't give that argument, Python uses the default instead.
#
#     def power(base, exponent=2):
#         return base ** exponent
#
#     power(5)      <- uses the default, so 25
#     power(5, 3)   <- 125
#
# Parameters with defaults must come AFTER the ones without.
#
# Fix `make_greeting(name, greeting)` so that greeting is optional and
# defaults to "Hello". It returns "<greeting>, <name>!"
#     make_greeting("Alice")        gives   "Hello, Alice!"
#     make_greeting("Bob", "Hi")    gives   "Hi, Bob!"

def make_greeting(name, greeting):
    return f"{greeting}, {name}!"
