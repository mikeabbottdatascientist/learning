## Imports
# Built-in
import asyncio

# Installed

# Local
##


async def my_coroutine(name:str):
    print(f"{name} did step 1")
    # await tells the coordinator that this is a spot where we can pause
    # this function and work on other stuff.
    await asyncio.sleep(1)
    print(f"{name} did step 2")

async def main():
    await asyncio.gather(my_coroutine('A'), my_coroutine('B'), my_coroutine('C'))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    