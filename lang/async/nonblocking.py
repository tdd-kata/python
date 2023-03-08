import asyncio


async def nonblocking_function():
    print("Starting nonblocking function")
    await asyncio.sleep(3)  # 3초 동안 다른 작업 수행 가능
    print("Ending nonblocking function")


async def main():
    print("Before calling nonblocking function")
    task = asyncio.create_task(nonblocking_function())  # 함수를 비동기적으로 실행합니다.
    await task  # 함수의 실행이 완료될 때까지 대기하지 않고 다른 작업을 수행합니다.
    print("After calling nonblocking function")


asyncio.run(main())
