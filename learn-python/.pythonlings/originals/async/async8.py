# Exercise: Async 8
# I AM NOT DONE
#
# Where does the first `await` come from? Normal (non-async) code can't use
# `await`. `asyncio.run(coroutine)` is the bridge. It starts everything running,
# waits for the coroutine to finish, and returns its result.
#
#     result = asyncio.run(some_coroutine())
#
# Replace the ??? so that `result` is what you get from running answer().

import asyncio

async def answer():
    return 42

result = ???
