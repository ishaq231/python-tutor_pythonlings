# Exercise: Loops 10
# I AM NOT DONE
#
# Time to use lots of loop skills together! You are going through a list of bank `transactions`.
# Each transaction is a dictionary with an "amount" (a number) and a "type" ("credit" means money in, "debit" means money out).
# Make `summary`, a list of dictionaries (one for each transaction) with these keys:
#   "index"   : the position counting from 1 (use enumerate)
#   "amount"  : the amount of the transaction
#   "balance" : how much money there is so far (credits add on, debits take away)
# Skip any transaction where the amount is 0 (use continue).
# The balance starts at 0.

transactions = [
    {"amount": 100, "type": "credit"},
    {"amount": 0,   "type": "debit"},
    {"amount": 40,  "type": "debit"},
    {"amount": 200, "type": "credit"},
    {"amount": 60,  "type": "debit"},
]
summary = []
balance = 0
# write your for loop here (use enumerate, continue, and keep updating balance)
