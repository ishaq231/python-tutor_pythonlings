# Exercise: Functions 6
# I AM NOT DONE
#
# So far you gave arguments in order (this is called by POSITION). You can also
# give them by NAME, which are called KEYWORD arguments. Then the order
# doesn't matter, and it's easier to read:
#
#     describe_pet(animal_type="dog", name="Buddy")
#
# The call at the bottom has its arguments in the wrong order, so the answer
# comes out silly. Fix it using keyword arguments, and save the result in
# `description`.

def describe_pet(name, animal_type):
    return f"My {animal_type} is named {name}."

# This call has the arguments in the wrong order:
description = describe_pet("dog", "Buddy")
