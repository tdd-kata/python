"""
watch -n 0.5 pytest -v set.py
"""


def test_len():
    # set은 {중괄호}를 사용한다.
    sut = {1, False, 2, 2}
    assert sut == {1, 2, False}
    assert len(sut) == 3


def test_list_to_set():
    sut = set([1, 2, 3, 3])
    assert sut == {1, 2, 3}
    assert len(sut) == 3


def test_add():
    sut = {1, 2}
    sut.add(None)
    assert sut == {1, 2, None}


def test_remove():
    sut = {"one", "two", 3}
    sut.remove("two")
    assert sut == {"one", 3}


def test_discard():
    sut = {"one", "two", 3}
    sut.discard("two")
    assert sut == {"one", 3}


def test_intersection():
    """
    교집합
    """
    s1 = {"one", "two", 3}
    s2 = {"two", 3, "five"}
    assert s1 & s2 == {"two", 3}
    assert s1.intersection(s2) == {"two", 3}


def test_union():
    """
    합집합
    """
    s1 = {"one", "two", 3}
    s2 = {3, "Four", "five"}
    assert s1 | s2 == {"one", "two", 3, "Four", "five"}
    assert s1.union(s2) == {"one", "two", 3, "Four", "five"}


def test_difference():
    """
    차집합
    """
    s1 = {"one", "two", 3}
    s2 = {3, "Four", "five"}
    assert s1 - s2 == {"one", "two"}
    assert s1.difference(s2) == {"one", "two"}


def test_add():
    sut = {1, 2}
    sut.add(None)
    assert sut == {1, 2, None}


def test_update():
    """
    add와 달리 여러개의 값을 추가할 수 있다.
    """
    sut = {1, 2}
    sut.update({3, 4})
    assert sut == {1, 2, 3, 4}


def test_remove():
    sut = {"one", "two", 3}
    sut.remove("two")
    assert sut == {"one", 3}
