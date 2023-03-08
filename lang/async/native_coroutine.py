import asyncio


async def process_data(data):
    print(f"Processing {data}...")
    await asyncio.sleep(1)  # 데이터 처리하는 동안 1초 대기
    result = data * 2
    print(f"Processed {data}, result={result}")
    return result


async def main():
    # 비동기적으로 데이터를 처리합니다.
    tasks = [asyncio.create_task(process_data(data)) for data in range(1, 6)]
    # 처리 결과를 기다립니다.
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")


asyncio.run(main())
