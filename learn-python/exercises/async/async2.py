# Exercise: Async 2
# I AM NOT DONE
#
# Calling a coroutine doesn't run it. It just gives you a coroutine
# object. To actually run it and get the result, you `await` it, which is only
# allowed inside another `async def`:
#
#     result = await get_message()
#
# `await` means "wait here until this finishes. Meanwhile, other things are free
# to run".
#
# Replace the ??? so that main() awaits get_message() and returns its value.

async def get_message():
    return "ready"

async def main():
    return ???
