# Exercise: Classes 12
# I AM NOT DONE
#
# Time to put classes together by building a bank account. Four things are
# broken or missing. Fix them so this all works:
#
#     account = BankAccount("Alice", 100)
#     account.deposit(50)      -> balance becomes 150
#     account.withdraw(30)     -> balance becomes 120
#     account.withdraw(200)    -> raises ValueError("insufficient funds")
#     str(account)             -> "BankAccount(Alice, balance=120)"
#
# To fix:
#  1. Add an `__init__` that stores `owner` and `balance`.
#  2. `deposit` should add `amount` to the balance.
#  3. `withdraw` should subtract `amount`, but raise a ValueError("insufficient
#     funds") if amount is more than the balance.
#  4. `__str__` should return the string shown above.

class BankAccount:
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def __str__(self):
        return ""


account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
