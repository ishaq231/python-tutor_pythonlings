# Exercise: Loops 10
# I AM NOT DONE
#
# Time to use all your loop skills together! You are going through a list of
# bank `transactions`. Each one is a dictionary, and you read a value from it
# using its key in square brackets, like  transaction["amount"].
#
# Each has an "amount" (a number) and a "type": "credit" means money going in
# and "debit" means money coming out.
#
# Make `summary`, a list of dictionaries (one for each transaction) with:
#     "index"   -> the position counting from 1 (use enumerate)
#     "amount"  -> the amount of the transaction
#     "balance" -> the money there is so far (credits add on, debits take away)
# Skip any transaction with an amount of 0 (use continue). The balance starts
# at 0. A new dictionary looks like {"index": 1, "amount": 100, "balance": 100}.

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
