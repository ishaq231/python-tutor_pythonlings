# Exercise: Conditionals 7
# I AM NOT DONE
#
# You can put an `if` INSIDE another `if`. This is called NESTING. Python only
# looks at the inner question if the outer one let it through. Each level of
# nesting is indented a little bit further.
#
# Finish `ticket_price(age, is_member)` using a nested if/else:
#     younger than 5                -> free (0)
#     5 or older AND a member       -> 8
#     5 or older AND NOT a member   -> 12

def ticket_price(age, is_member):
    if age < 5:
        return 0
    else:
        if ???:
            return 8
        ???
