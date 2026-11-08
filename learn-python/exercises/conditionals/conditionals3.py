# Exercise: Conditionals 3
# I AM NOT DONE
#
# What if you have more than two choices? Use `elif` (short for "else if").
# Python checks the conditions from the top, and runs the FIRST one that is
# True. After that it ignores the rest, so the order matters!
#
# Finish `grade(score)` so it returns:
#     "A" if score is 90 or more
#     "B" if score is 80 or more
#     "C" if score is 70 or more
#     "F" for anything below 70

def grade(score):
    if score >= 90:
        return "A"
    # add the remaining elif / else branches

    return "F"
