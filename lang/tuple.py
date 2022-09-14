"""
watch -n 0.1 pytest -v tuple.py
"""

from pytest import raises


def test_length():
    # tuple은 (소괄호)를 사용한다.
    sut = (1, 3, 2, "", False)
    assert len(sut) == 5


def test_sort():
    # 중복 가능
    sut = (1, 3, 2, 2)
    assert sorted(sut) == [1, 2, 2, 3]


def test_slice():
    # 순서 보장
    sut = (1, 3, 2, 4)

    assert sut[1] == 3
    assert (5 in sut) == False
    assert sut[1:3] == (3, 2)


def test_unpacking():
    sut = (1, 3, 2, 4)
    (one, two, *others) = sut  # unpacking 시 others는 tuple이 아닌 list로 반환된다.

    assert one == 1
    assert two == 3
    assert others == [2, 4]


def test_delete():
    sut = (1, 3, 2, 4)
    with raises(TypeError) as ex:
        del sut[1]  # tuple은 list와 달리 immutable하다.
    assert "'tuple' object doesn't support item deletion" in str(ex.value)


def test_assign():
    sut = (1, 3, 2, 4)
    with raises(TypeError) as ex:
        sut[1] = 5  # tuple은 list와 달리 immutable하다.
    assert "'tuple' object does not support item assignment" in str(ex.value)
