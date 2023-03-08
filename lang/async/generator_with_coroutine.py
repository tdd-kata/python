"""
Generators produce data
Coroutines consume data
"""
import asyncio
import time

start_time = time.time()


async def generator(stop):  # 제너레이터 방식으로 만들기
    n = 0
    while n < stop:
        yield n
        n += 1
        await asyncio.sleep(1.0)


async def coroutine():
    async for i in generator(stop=3):  # for 앞에 async를 붙임
        print(i, end=' ')


asyncio.run(coroutine())

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
