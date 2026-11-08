# Exercise: Lists 8
# I AM NOT DONE
#
# Very often you want to build a NEW list from an old one, changing every
# item. The recipe is: start with an empty list, loop through the old list,
# and append the changed item each time.
#
# You have temperatures in Celsius. Make a new list called `fahrenheit` with
# each temperature changed using this formula:  F = C * 9 / 5 + 32
# Fill in the loop (the line with `pass` is just a place-holder, so replace it).
# Do not change the `temperatures` list.
#
# (Extra for later: there is a shorter way to do this in one line, called a
# "list comprehension". You don't need it here.)

temperatures = [0, 100, -40, 37, 212, -273]

fahrenheit = []
for temp in temperatures:
    pass  # replace this line with the conversion and append
