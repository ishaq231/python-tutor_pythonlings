# Exercise: Json 1
# I AM NOT DONE
#
# JSON is a popular text format for storing and sharing data. It looks very
# like Python dictionaries and lists, so it's used all over the internet. In
# JSON, true/false are lowercase and the empty value is `null`. Python's
# `json` module converts between JSON text and Python objects.
#
#     json.loads(text)      JSON text -> Python object   (the s is for "string")
#
# Replace the ??? so that `data` is the parsed version of the JSON text `raw`.

import json

raw = '{"name": "Ada", "language": "Python"}'
data = ???
name = data["name"]
