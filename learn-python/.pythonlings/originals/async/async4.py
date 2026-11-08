# Exercise: Async 4
# I AM NOT DONE
#
# `asyncio.gather(a(), b())` runs several coroutines at the same time (well, it
# takes turns while each one waits) and collects the results in a list, in the
# order you gave them. You `await` the gather.
#
#     results = await asyncio.gather(job1(), job2())
#
# Replace the ??? so collect() returns the results of first() and second().

import asyncio

async def first():
    return "a"

async def second():
    return "b"

async def collect():
    return ???
