import asyncio
import random


async def generate_data(n):
    for i in range(n):
        await asyncio.sleep(random.uniform(0, 1))
        yield i


async def process_data(data):
    for i in data:
        await asyncio.sleep(random.uniform(0, 1))
        print(f"Processing: {i}")


async def main():
    data = [i async for i in generate_data(10)]
    await asyncio.gather(
        *[process_data(data[i:i + 2]) for i in range(0, len(data), 2)])


asyncio.run(main())
