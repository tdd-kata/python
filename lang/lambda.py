"""
watch -n 0.1 pytest -v lambda.py
"""


# https://dojang.io/mod/page/view.php?id=2359
def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3
    assert add(3, 4) == 7


def test_add_lambda():
    assert (lambda x, y: x + y)(1, 2) == 3
    assert (lambda x, y: x + y)(3, 4) == 7


def test_add_lambda_function():
    # PEP 8 - E731 do not assign a lambda expression, use a def
    adder = lambda x, y: x + y
    assert adder(1, 2) == 3
    assert adder(3, 4) == 7


################################################
# 람다 표현식과 map, filter, reduce 함수 활용하기
# https://dojang.io/mod/page/view.php?id=2360
################################################

def test_map():
    m = map(lambda x: x + 10, [1, 2, 3])  # map object
    assert isinstance(m, map)
    assert list(m) == [11, 12, 13]


# 리스트(딕셔너리, 세트) 표현식으로 처리할 수 있는 경우에는
# map, filter와 람다 표현식 대신 리스트 표현식을 사용하는 것이 좋습니다.
def test_instead_lambda():
    sut = [1, 2, 3, 4, 5]
    assert [i * 2 for i in sut if i % 2 == 0] == [4, 8]


def test_map_conditional():
    # 람다 표현식에서 조건부 표현식 if를 사용했다면 반드시 else를 사용해야 합니다.
    # 람다 표현식에서 if, else를 사용할 때는 :(콜론)을 붙이지 않습니다.
    # 람다 표현식에서 elif를 사용할 수 없습니다.
    m = map(lambda x: x + 10 if x > 5 else x, [1, 2, 3, 4, 5, 6, 7])
    assert list(m) == [1, 2, 3, 4, 5, 16, 17]


def test_filter():
    sut = [3, 4, 5, 6, 7]
    f = filter(lambda x: x > 5, sut)  # filter object
    assert isinstance(f, filter)
    assert list(f) == [6, 7]


# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수입니다
# reduce는 파이썬 3부터 내장 함수가 아닙니다.
# functools 모듈에서 reduce 함수를 가져와야 합니다.

def test_reduce():
    from functools import reduce
    iterable_list = [1, 2, 3, 4, 5]
    assert reduce(lambda x, y: x + y, iterable_list) == 15


def test_reduce2():
    from functools import reduce
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) == 120


def test_reduce3():
    from functools import reduce
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 100) == 12000


def test_reduce4():
    from functools import reduce
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 1) == 120


def test_reduce5():
    from functools import reduce
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 0) == 0


def test_reduce6():
    from functools import reduce
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], -1) == -120


def test_reduce7():
    from functools import reduce
    assert reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], -100) == -12000
