# Exercise: Async 3
# I AM NOT DONE
#
# `asyncio.sleep(seconds)` is the async way to pause. While one coroutine sleeps,
# others can use the time (unlike the normal time.sleep(), which freezes
# everything). You must `await` it.
#
# Replace the ??? with a line that awaits a very short sleep, e.g. 0.
# (asyncio.sleep(0) means "yield control for a moment".)

import asyncio

async def wake_up():
    ???
    return "awake"
