# Exercise: Dictionaries 6
# I AM NOT DONE
#
# If you look up a key that isn't there, you get a KeyError. The method
# .get(key, default) is a safer way: it gives back the value if the key is
# there, or your `default` if it isn't. No error!
#
#     d.get("colour", "unknown")
#
# Using `config`, set:
#     timeout -> get "timeout", with a default of 30
#     retries -> get "retries", with a default of 3
#     verbose -> get "verbose", with a default of False
# ("timeout" is in config. "retries" and "verbose" aren't.)

config = {"host": "localhost", "port": 8080, "timeout": 60}

timeout = ???
retries = ???
verbose = ???
