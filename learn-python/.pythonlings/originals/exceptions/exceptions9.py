# Exercise: Exceptions 9
# I AM NOT DONE
#
# You can invent your own error types! They are made as CLASSES (a class is a
# blueprint for making things; you'll learn about them very soon). For now,
# this recipe is all you need, where `pass` just means "nothing more to add":
#
#     class MyError(Exception):
#         pass
#
# A custom error with a clear name makes your code easier to understand.
#
# 1. Define an error called `InsufficientFundsError` that inherits
#    from Exception (that's the bit in brackets).
# 2. Finish `withdraw(balance, amount)`: if amount is more than balance, raise
#    InsufficientFundsError with the message
#    "cannot withdraw <amount> from balance of <balance>".
#    Otherwise return balance - amount.

def withdraw(balance, amount):
    # TODO: raise InsufficientFundsError when amount > balance
    return balance - amount
