# Exercise: Json 6
# I AM NOT DONE
#
# A JSON array becomes a Python list, and in this one each item is a dictionary.
# JSON's `true` and `false` become Python's True and False.
#
# Replace the ??? so that `active_names` is a list of the names of the users
# that are active, in order. A list comprehension with an `if` is perfect.

import json

raw = '[{"name": "Ada", "active": true}, {"name": "Lin", "active": false}, {"name": "Guido", "active": true}]'
users = json.loads(raw)
active_names = ???
