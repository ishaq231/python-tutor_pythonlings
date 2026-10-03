# Exercise: Functions 6
# I AM NOT DONE
#
# The function `describe_pet` takes a `name` and an `animal_type`.
# It returns "My <animal_type> is named <name>."
#
# The call at the bottom has the arguments in the wrong order.
# Fix it by using keyword arguments (like name="Buddy") so it works
# whatever order you write them in.
# Save the answer in `description`.

def describe_pet(name, animal_type):
    return f"My {animal_type} is named {name}."

# This call has the arguments in the wrong order:
description = describe_pet("dog", "Buddy")
