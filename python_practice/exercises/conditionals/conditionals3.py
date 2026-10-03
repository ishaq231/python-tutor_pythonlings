# Exercise: Conditionals 3
# I AM NOT DONE
#
# `elif` (short for "else if") lets you check lots of conditions one after the other.
# Python checks them in order and runs the FIRST one that is True.
#
# Finish `grade(score)` so it returns:
#   "A" if score is 90 or more
#   "B" if score is 80 or more
#   "C" if score is 70 or more
#   "F" for anything below 70

def grade(score):
    if score >= 90:
        return "A"
# add the other elif / else parts here

    return "F"
