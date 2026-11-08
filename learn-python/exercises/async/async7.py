# Exercise: Async 7
# I AM NOT DONE
#
# What if something takes too long? `asyncio.wait_for(coroutine, timeout=seconds)`
# waits for a coroutine, but gives up with an error if it takes more than the
# given time. It must be awaited too.
#
# Replace the ??? so with_timeout() awaits quick() with a timeout of 1 second
# and returns its result.

import asyncio

async def quick():
    await asyncio.sleep(0)
    return "done"

async def with_timeout():
    return ???
