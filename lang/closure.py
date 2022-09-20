"""
watch -n 0.1 pytest -v closure.py
"""

# https://dojang.io/mod/page/view.php?id=2364
# https://shoark7.github.io/programming/python/closure-in-python
# https://wikidocs.net/134789

x = 1


def global_scope(x):
    def inner():
        global x
        return x

    return inner()


def test_global_scope():
    assert global_scope(100) == 1


def local_scope(x):
    def inner():
        x = 100
        return x

    return inner()


def test_local_scope():
    assert local_scope(1) == 100


def nonlocal_scope(x):
    def inner():
        nonlocal x
        x += 1
        return x

    return inner()


def test_nonlocal_scope():
    assert nonlocal_scope(3) == 4


# https://shoark7.github.io/programming/python/closure-in-python
def first_class_citizen(a, b):
    return a + b


def execute(func, *args):
    return func(*args)


def test_first_class_citizen():
    assert execute(first_class_citizen, 1, 2) == 3


# 파이썬에서 클로저는 '자신을 둘러싼 스코프(네임스페이스)의 상태값을 기억하는 함수'다.
# 그리고 어떤 함수가 클로저이기 위해서는 다음의 세 가지 조건을 만족해야 한다.
# - 해당 함수는 어떤 함수 내의 중첩된 함수여야 한다.
# - 해당 함수는 자신을 둘러싼(enclose) 함수 내의 상태값을 반드시 참조해야 한다.
# - 해당 함수를 둘러싼 함수는 이 함수를 반환해야 한다.

def in_cache(func):
    cache = {}

    def wrapper(n):
        print("cache: ", cache)
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return wrapper


def test_fibonacci():
    @in_cache  # decorator
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    assert fib(9) == 34
    assert fib(10) == 55


def test_in_cache():
    def factorial(n):
        ret = 1
        for i in range(1, n + 1):
            ret *= i
        return ret

    cached_factorial = in_cache(factorial)
    # 원본 함수에 어떤 변화(심지어는 삭제)가 발생되어도 자신의 스코프는 지킨다.
    del factorial

    assert cached_factorial(1) == 1
    assert cached_factorial(2) == 2
    assert cached_factorial(3) == 6
    assert cached_factorial(5) == 120
    assert cached_factorial(10) == 3628800
    # assert False # print() 출력을 확인하려면 테스트가 실패해야 한다.
