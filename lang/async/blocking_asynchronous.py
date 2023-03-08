import asyncio
import concurrent.futures
import time

"""
https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/
https://developer.ibm.com/articles/l-async/
https://stackoverflow.com/questions/74145286/python-run-non-blocking-async-function-from-sync-function

- 이 차이는 파일 입출력 응용 프로그램을 만들면 명확하게 알 수 있다.
비동기 호출을 했지만 Blocking 입출력을 할 경우 응용 프로그램이 멈춘다.
- 마찬가지로 웹 애플리케이션에서 비동기 호출을 했지만
DB에서 데이터 조회 시 Blocking I/O를 수행할 경우 해당 트랜잭션에서 계속 대기한다.
따라서 DB에서 데이터 조회 시 Non-blocking I/O를 수행해야 한다.

[Blocking vs. Non-blocking]
호출되는 함수가 바로 리턴하느냐 마느냐가 관심사다.

쉽게 말하면:
Blocking은 작업이 완료될 때까지 다른 작업을 수행하지 않는 것을 의미합니다.
Non-blocking은 작업이 완료되지 않아도 다른 작업을 수행할 수 있는 것을 의미합니다.

명확하게 말하면:
Blocking은 호출된 함수가 자신의 작업을 모두 마칠 때까지 호출한 함수에게
`제어권`을 넘겨주지 않고 대기하게 만든다.
Non-Blocking은 호출된 함수가 바로 리턴해서 호출한 함수에게
`제어권`을 넘겨주고 호출한 함수가 다른 일을 할 수 있게 한다.

예를 들어, Blocking I/O는 데이터가 도착하기 전까지
응용 프로그램이 멈추고 대기해야 한다.
반면, Non-blocking I/O는 데이터가 도착하기를 기다리지 않고
계속 실행된다.

[Synchronous vs. Asynchronous]
호출되는 함수의 작업 완료 여부를 누가 신경쓰냐가 관심사다.

쉽게 말하면:
Synchronous는 호출된 함수가 결과를 반환할 때까지
호출하는 함수가 대기해야 하는 것을 의미합니다.
Asynchronous는 호출된 함수가 결과를 반환하기를 기다리지 않고
호출하는 함수가 다른 작업을 수행할 수 있는 것을 의미합니다.

명확하게 말하면:
Synchronous는
호출하는 함수가 호출되는 함수의 작업 완료 후 리턴을 기다리거나,
또는 호출되는 함수로부터 바로 리턴 받더라도 작업 완료 여부를
호출하는 함수 스스로 계속 확인하며 신경쓴다.
Asynchronous는
호출되는 함수에게 callback을 전달해서 호출되는 함수의 작업이 완료되면
호출되는 함수가 전달받은 callback을 실행하고,
호출하는 함수는 작업 완료 여부를 신경쓰지 않는다.

예를 들어, Synchronous 함수는 호출자가 함수가 반환할 때까지 기다려야 합니다.
반면, Asynchronous 함수는 호출자가 반환하기를 기다리지 않고 다른 작업을 수행할 수 있습니다.
"""


def blocking(delay):
    time.sleep(delay)
    print('Completed.')


async def non_blocking(executor):
    loop = asyncio.get_running_loop()
    # Run three of the blocking tasks concurrently.
    # asyncio.wait will automatically wrap these in Tasks.
    # If you want explicit access to the tasks themselves,
    # use asyncio.ensure_future,
    # or add a "done, pending = asyncio.wait..." assignment
    await asyncio.wait(
        fs={
            loop.run_in_executor(executor, blocking, 2),
            loop.run_in_executor(executor, blocking, 4),
            loop.run_in_executor(executor, blocking, 6)
        },
        return_when=asyncio.ALL_COMPLETED
    )


_executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
asyncio.run(non_blocking(_executor))
