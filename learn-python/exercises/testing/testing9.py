# Exercise: Testing 9
# I AM NOT DONE
#
# Tests often need some data to work with. A FIXTURE is a helper function
# that builds that data fresh each time, so one test can't disturb another.
#
# `make_user` is the fixture. Finish `test_user_greeting` so it:
#     1. calls make_user() and saves the result in a variable
#     2. asserts that greet(user) is "Hello, Alice!"

def make_user():
    return {"name": "Alice", "age": 30}


def greet(user):
    return f"Hello, {user['name']}!"


def test_user_greeting():
    # 1. call make_user() to get the fixture
    # 2. assert greet(user) == "Hello, Alice!"
    pass
