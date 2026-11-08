# Exercise: Json 7
# I AM NOT DONE
#
# A common job is: read JSON, change a value, then write it out again.
# Once decoded, `settings` is a normal dictionary, so you can change it with
# settings["key"] = value.
#
# Replace the ??? so that the theme becomes "dark". The last line then encodes
# the settings again for you.

import json

settings = json.loads('{"theme": "light", "font_size": 12}')
settings["theme"] = ???
encoded = json.dumps(settings, sort_keys=True)
