"""
watch -n 0.1 pytest -v generator.py
"""


# https://dojang.io/mod/page/view.php?id=2412
def number_generator():
    yield 0
    yield 1
    yield 3


def test_generator_is_iterator():
    gen = number_generator()
    sut = dir(gen)
    assert "__iter__" in sut
    assert "__next__" in sut


def test_loop_list():
    """
    https://youtu.be/B8TAMOk-iD0
    - 메모리 절약
    - Lazy evaluation
    """
    gen = number_generator()

    a = next(gen)
    assert a == 0

    b = next(gen)
    assert b == 1

    c = next(gen)
    assert c == 3
