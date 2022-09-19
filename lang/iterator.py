"""
watch -n 0.1 pytest -v iterator.py
"""


def test_iterator():
    sut = [1, 2, 3].__iter__()
    assert sut.__next__() == 1
    assert sut.__next__() == 2
    assert sut.__next__() == 3


def test_loop_iterator():
    sut = [1, 2, 3].__iter__()
    result = []

    for i in sut:
        result.append(i)

    assert result == [1, 2, 3]


def test_string_iterator():
    sut = "abc"
    methods = dir(sut)
    assert "__iter__" in methods

    iterator = sut.__iter__()
    assert iterator.__next__() == "a"
    assert iterator.__next__() == "b"
    assert iterator.__next__() == "c"


def test_dict_iterator():
    sut = {1: "one", 2: "two", 3: "three"}.__iter__()
    assert sut.__next__() == 1
    assert sut.__next__() == 2
    assert sut.__next__() == 3


def test_set_iterator():
    sut = {1, 2, 3}.__iter__()
    assert sut.__next__() == 1
    assert sut.__next__() == 2
    assert sut.__next__() == 3
