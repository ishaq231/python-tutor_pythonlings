# Exercise: Json 3
# I AM NOT DONE
#
# JSON data often has things nested inside other things. After `loads`, it's
# just normal dictionaries, so you dig in with square brackets, one level
# at a time (like the nested dictionary exercise earlier).
#
# Replace the ??? with the code to get the user's city out of `profile`.

import json

raw = '{"user": {"name": "Grace", "address": {"city": "London"}}}'
profile = json.loads(raw)
city = ???
