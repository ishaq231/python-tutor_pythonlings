# Exercise: Async 6
# I AM NOT DONE
#
# An ASYNC GENERATOR is like a normal generator (it uses `yield`), but it's
# inside an `async def`. To loop over one, you write `async for`:
#
#     async for item in some_async_generator():
#         ...
#
# Replace the ??? so each value is added to the `result` list.

async def numbers():
    for value in [1, 2, 3]:
        yield value

async def collect_numbers():
    result = []
    async for value in numbers():
        ???
    return result
