# Exercise: Conditionals 5
# I AM NOT DONE
#
# Boolean operators join conditions together:
#   `and` - True only when BOTH sides are True
#   `or`  - True when AT LEAST ONE side is True
#
# Finish `can_ride(height, has_ticket)` so it returns True only when the rider
# is at least 120 cm tall AND has a ticket.
# Finish `gets_discount(is_student, is_senior)` so it returns True when the
# person is a student OR a senior.

def can_ride(height, has_ticket):
    return height >= 120 ??? has_ticket

def gets_discount(is_student, is_senior):
    return is_student ??? is_senior
