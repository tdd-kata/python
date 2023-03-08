import asyncio
import random


async def produce(queue):
    while True:
        # 임의의 데이터 생성
        data = random.randint(1, 100)
        # Queue에 데이터 추가
        await queue.put(data)
        # 1초 대기
        await asyncio.sleep(1)


async def consume(queue):
    while True:
        # Queue에서 데이터 가져오기
        data = await queue.get()
        if data % 2 == 0:
            print(f"Even number: {data}")
        else:
            print(f"Odd number: {data}")
        # Queue에서 데이터 삭제
        queue.task_done()


async def stream_processor():
    queue = asyncio.Queue()
    # 생산자 코루틴 실행
    producer = asyncio.create_task(produce(queue))
    # 소비자 코루틴 2개 실행
    consumers = [asyncio.create_task(consume(queue)) for _ in range(2)]
    # 생산자 코루틴이 완료될 때까지 대기
    await producer
    # 소비자 코루틴이 완료될 때까지 대기
    await queue.join()
    for c in consumers:
        c.cancel()


asyncio.run(stream_processor())
