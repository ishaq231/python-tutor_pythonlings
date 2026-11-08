# Exercise: Json 5
# I AM NOT DONE
#
# Real data can have missing fields. Remember `.get(key, default)` from the
# Dictionaries topic? It gives a default instead of raising a KeyError.
#
# `data` has no "timezone" field. Replace the ??? so that `timezone` is the
# data's "timezone" if there is one, or "UTC" if there isn't.

import json

data = json.loads('{"name": "Pythonlings"}')
timezone = ???
