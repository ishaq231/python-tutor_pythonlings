# Exercise: Async 10
# I AM NOT DONE
#
# Putting it together: make one coroutine call for each name, run them all with
# gather (remember the * trick from the last exercise), then join the
# results into one string.
#
# Replace the ??? so that `upper_names` is the list of the results of
# fetch_name() for every name in `names`.

import asyncio

async def fetch_name(name):
    await asyncio.sleep(0)
    return name.upper()

async def fetch_all(names):
    upper_names = ???
    return ",".join(upper_names)
