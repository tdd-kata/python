"""
watch -n 0.5 pytest -v list.py
"""

import pytest

def test_length():
    assert len([1, 3, 2, "", False]) == 5

def test_sorted():
    sut = [1, 3, 2]
    assert sorted(sut) == [1, 2, 3]

def test_sort():
    sut = [1, 3, 2]
    sut.sort()
    assert sut == [1, 2, 3]

def test_reverse():
    sut = [1, 3, 2]
    sut.reverse()
    assert sut == [2, 3, 1]

def test_index():
    sut = [1, 3, 2, 4]
    assert sut.index(3) == 1

def test_get():
    sut = [1, 3, 2, 4]
    assert sut[3] == 4

def test_slice():
    sut = [1, 3, 2, 4]
    assert sut[1:3] == [3, 2]

def last_element(list):
    """
    list의 마지막 값을 반환한다.

    :param list: List
    :return: Last element of list
    """
    return list[-1]

def test_last_element():
    assert last_element([1, 3, 2, 4]) == 4

def test_last_element2():
    assert last_element([1, 3, 2, ["a", "b"]]) == ["a", "b"]

def test_last_element3():
    assert last_element([1, 3, 2, None]) == None

def test_operator():
    a = [1, 2, 3]
    b = [4, 5, 6]

    assert a + b == [1, 2, 3, 4, 5, 6]
    assert a * 2 == [1, 2, 3, 1, 2, 3]

def test_append():
    a = [1, 2, 3]
    a.append(4)
    assert a == [1, 2, 3, 4]


def test_insert():
    a = [1, 2, 3, 4, 5]
    a.insert(2, 6)
    assert a == [1, 2, 6, 3, 4, 5]

def test_string_concatenation():
    assert "a" + "b" == "ab"

def test_string_concatenation_with_number():
    with pytest.raises(TypeError) as ex:
        "a" + 3
    assert "can only concatenate str (not \"int\") to str" in str(ex.value)

def test_delete():
    sut = [1, 2, 3, 4, 5]
    del sut[2]
    assert sut == [1, 2, 4, 5]

def test_remove():
    sut = [1, 2, 3, 4, 3]
    sut.remove(3)
    # 앞에서부터 1개 제거
    assert sut == [1, 2, 4, 3]

def test_pop():
    sut = [1, 2, 3, 4, 5]
    # sut.pop()
    element = sut.pop()
    assert element == 5
    assert sut == [1, 2, 3, 4]

def test_pop_index():
    sut = [1, 2, 3, 4, 5]
    # sut.pop(index)
    element = sut.pop(2)
    assert element == 3
    assert sut == [1, 2, 4, 5]

def test_count():
    sut = [1, 2, None, 3, False, "e", None]
    assert sut.count(None) == 2

def test_extend():
    sut = [1, 2, 3]
    sut.extend([4, 5, 6])
    assert sut == [1, 2, 3, 4, 5, 6]
