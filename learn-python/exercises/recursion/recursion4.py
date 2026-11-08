# Exercise: Recursion 4
# I AM NOT DONE
#
# Same idea again: how long is a list? It's "1 plus the length of the rest of the
# list". The recursive case is already written.
#
# Replace the ??? with the right base-case answer: how many items are in an
# empty list?

def count_items(lst):
    if not lst:
        return ???
    return 1 + count_items(lst[1:])
