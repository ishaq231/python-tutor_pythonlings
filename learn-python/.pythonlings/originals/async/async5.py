# Exercise: Async 5
# I AM NOT DONE
#
# A TASK is a coroutine that has been scheduled to start running in the
# background right away. `asyncio.create_task(coroutine)` makes one. You can
# then `await` the task later to get its result.
#
# Replace the ??? with a task made from compute() (remember to call it, so
# you have a coroutine to pass in).

import asyncio

async def compute():
    return 21 * 2

async def run_task():
    task = ???
    return await task
