# Exercise: Async 9
# I AM NOT DONE
#
# You can use a comprehension to make a bunch of coroutines, then `gather`
# them all. The star `*` unpacks a list into separate arguments:
#
#     await asyncio.gather(*[job(x) for x in things])
#
# Replace the ??? so double_all(values) returns the doubled values, using
# gather to run double() for each value.

import asyncio

async def double(value):
    await asyncio.sleep(0)
    return value * 2

async def double_all(values):
    return ???
