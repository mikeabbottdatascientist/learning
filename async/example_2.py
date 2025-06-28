import asyncio
import itertools as it
import os
import random
import time


async def randsleep():
    i = random.randint(1, 5)
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    print(f"Producer {name} started creating a raw_num")
    await randsleep()
    raw_num = random.random()*100
    await q.put(raw_num)
    print(f"Producer {name} added <{raw_num}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    while True: 
        raw_num = await q.get()
        print(f"consumer {name} acquired {raw_num} from queue. starting to process")
        await randsleep()
        floor_num = int(raw_num)
        print(f"consumer {name} turned {raw_num} into {floor_num}")
        q.task_done()


async def main(nprod: int, ncon: int):
    # Create a queue
    q = asyncio.Queue()
    # Create producers, which will execute the produce task
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    # Create consumers, which will take tasks off the queue
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    await q.join() # Implicitly awaits consumers, too
    print("finished q.join()")
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    asyncio.run(main(5,5))
    print("completed")