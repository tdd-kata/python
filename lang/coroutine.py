"""
watch -n 0.1 pytest -v coroutine.py
"""


# https://dojang.io/mod/page/view.php?id=2418
# https://dojang.io/mod/page/view.php?id=2419
# https://dojang.io/mod/page/view.php?id=2420
# https://dojang.io/mod/page/view.php?id=2421
def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield total)  # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
            if x is None:  # 받아온 값이 None이면
                return total  # 합계 total을 반환, 코루틴을 끝냄
            total += x
    except RuntimeError as e:  # 코루틴에서 예외가 발생할 때 처리할 코드
        print(e)
        yield total  # 코루틴 바깥으로 값을 전달


def accumulate_coroutine():
    while True:
        total = yield from accumulate()
        print(total)
        yield total


def accumulate():
    total = 0
    while True:
        x = (yield total)  # 코루틴 바깥에서 값을 받아옴
        if x is None:  # 받아온 값이 None이면
            return total  # 합계 total을 반환, 코루틴을 끝냄
        total += x


def test_coroutine_methods():
    co = sum_coroutine()
    sut = dir(co)
    assert "__iter__" in sut
    assert "__next__" in sut
    assert "send" in sut


def test_sum_coroutine():
    co = sum_coroutine()

    """
    - next는 코루틴의 코드를 실행하지만 값을 보내지 않을 때 사용한다. == Generator
    - send는 값을 보내면서 코루틴의 코드를 실행할 때 사용한다.
    """
    # next(co)  # start coroutine - yield까지 코드 실행
    co.send(None)  # start coroutine - yield까지 코드 실행

    """
    - 제너레이터는 next 함수(__next__ 메서드)를 반복 호출하여 값을 얻어내는 방식
    - 코루틴은 next 함수(__next__ 메서드)를 한 번만 호출한 뒤 send로 값을 주고 받는 방식
    """
    assert co.send(1) == 1
    assert co.send(2) == 3
    assert co.send(0) == 3
    assert co.send(1) == 4

    closed_coroutine = co.throw(RuntimeError, "코루틴 종료")
    assert closed_coroutine == 4


def test_sum_coroutine_return():
    co = accumulate_coroutine()
    next(co)  # start coroutine - yield까지 코드 실행

    assert co.send(0) == 0
    assert co.send(2) == 2
    assert co.send(None) == 2
