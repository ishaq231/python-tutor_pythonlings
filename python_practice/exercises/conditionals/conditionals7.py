# Exercise: Conditionals 7
# I AM NOT DONE
#
# Nested `if` statements are an `if` inside another `if`. You only check the
# second condition after the first one has passed.
#
# Finish `ticket_price(age, is_member)` using a nested if/else:
#   - Younger than 5 -> free (0)
#   - 5 or older AND a member -> 8
#   - 5 or older AND NOT a member -> 12

def ticket_price(age, is_member):
    if age < 5:
        return 0
    else:
        if ???:
            return 8
        ???
