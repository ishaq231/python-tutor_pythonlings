# Exercise: Json 4
# I AM NOT DONE
#
# The same functions without the `s` work with files instead of strings:
#     json.dump(obj, file)     write JSON to a file
#     json.load(file)          read JSON from a file
#
# A StringIO buffer here is a pretend file that lives in memory, so we don't
# have to make a real one. `buffer.seek(0)` moves back to the start so it
# can be read again.
#
# Replace the ??? with the object that should be written to the buffer.

import io
import json

payload = {"ok": True, "count": 3}
buffer = io.StringIO()
json.dump(???, buffer)
buffer.seek(0)
restored = json.load(buffer)
