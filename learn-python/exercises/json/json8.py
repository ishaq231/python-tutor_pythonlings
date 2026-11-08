# Exercise: Json 8
# I AM NOT DONE
#
# A ROUND TRIP means converting data to JSON text and then back again and
# checking that nothing was lost. The data in `original` is nested, with a list
# and another dictionary inside it. `encoded` is the JSON text of it.
#
# Replace the ??? with the code that decodes `encoded` back into Python.
# The following lines read the tags and level out of it.

import json

original = {"project": "pythonlings", "tags": ["python", "practice"], "meta": {"level": 3}}
encoded = json.dumps(original, sort_keys=True)
decoded = ???
tag_count = len(decoded["tags"])
level = decoded["meta"]["level"]
