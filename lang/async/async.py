"""
python3 async.py

ref: https://dojang.io/mod/page/view.php?id=2469
ref: Using Asyncio in Python
"""
import asyncio
import time


class AsyncAdd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self.a + self.b  # __aenter__에서 값을 반환하면 as에 지정한 변수에 들어감

    async def __aexit__(self, exc_type, exc_value, traceback):
        pass


class AsyncCounter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.stop:
            await asyncio.sleep(1.0)
            r = self.current
            self.current += 1
            return r
        else:
            raise StopAsyncIteration


async def async_counter(stop):  # 제너레이터 방식으로 만들기
    n = 0
    while n < stop:
        yield n
        n += 1
        await asyncio.sleep(1.0)


async def say_native_coroutine(delay, what):
    """
    파이썬에서는 제너레이터 기반의 코루틴과 구분하기 위해
    async def로 만든 코루틴은 네이티브 코루틴이라고 합니다.
    async def 키워드는 파이썬 3.5 이상부터 사용 가능
    """
    await asyncio.sleep(delay)
    print(what)


@asyncio.coroutine
def say_old_coroutine(delay, what):
    """
    async def와 await는 파이썬 3.5에서 추가되었습니다.
    따라서 3.5 미만 버전에서는 사용할 수 없습니다.
    파이썬 3.4에서는 다음과 같이 @asyncio.coroutine 데코레이터로 네이티브 코루틴을 만듭니다.
    파이썬 3.4에서는 await가 아닌 yield from을 사용합니다.

    파이썬 3.3에서 asyncio는 pip install asyncio로 asyncio를 설치한 뒤
    @asyncio.coroutine 데코레이터와 yield from을 사용하면 됩니다.
    단, 3.3 미만 버전에서는 asyncio를 지원하지 않습니다.
    """
    yield from asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    """
    이번에는 await로 네이티브 코루틴을 실행하는 방법입니다.
    다음과 같이 await 뒤에 코루틴 객체, 퓨처 객체, 태스크 객체를 지정하면
    해당 객체가 끝날 때까지 기다린 뒤 결과를 반환합니다.
    await는 단어 뜻 그대로 특정 객체가 끝날 때까지 기다립니다.
    await 키워드는 파이썬 3.5 이상부터 사용 가능, 3.4에서는 yield from을 사용

    여기서 주의할 점이 있는데 await는 네이티브 코루틴 안에서만 사용할 수 있습니다.
    """
    await say_native_coroutine(1, 'hello')
    await say_old_coroutine(2, 'world')

    print(f"finished at {time.strftime('%X')}")

    async with AsyncAdd(1, 2) as result:  # async with에 클래스의 인스턴스 지정
        print(result)  # 3

    async for i in AsyncCounter(3):  # for 앞에 async를 붙임
        print(i, end=' ')

    async for i in async_counter(3):    # for 앞에 async를 붙임
        print(i, end=' ')


"""
The asyncio.run() function is a new high-level entry point for asyncio
"""
# asyncio.run(main())
loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
loop.run_until_complete(main())  # print_add가 끝날 때까지 이벤트 루프를 실행
loop.close()  # 이벤트 루프를 닫음
