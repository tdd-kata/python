# pytest -v tuple.py

"""
tuple은 list와 달리 값을 변경할 수 없다.
tuple은 list와 달리 소괄호를 사용한다.
"""

def length_tuple(tuple):
    """
    tuple 길이를 반환한다.

    :param tuple: Tuple
    :return: Length of tuple
    :rtype: int
    """
    return len(tuple)

def test_length_tuple():
    assert length_tuple((1, 3, 2, "", False)) == 5

def sorting_tuple(tuple):
    """
    tuple을 정렬한다.

    :param tuple: Tuple
    :return: Sorted tuple
    """
    return sorted(tuple)

def test_sorting_tuple():
    # 중복 허용
    assert sorting_tuple((1, 3, 2, 2)) == [1, 2, 2, 3]

def slice_tuple(tuple):
    """
    tuple의 1번째부터 3번째까지의 값을 반환한다.

    :param tuple: Tuple
    :return: Sliced tuple
    """
    return tuple[1:3]

def test_slice_tuple():
    # 순서 보장
    fixture = (1, 3, 2, 4)

    assert fixture[1] == 3
    assert (5 in fixture) == False
    assert slice_tuple(fixture) == (3, 2)

def others_element_in_unpacking_tuple(tuple):
    (one, two, *others) = tuple
    return others

def test_others_element_is_in_list():
    # others는 list
    assert others_element_in_unpacking_tuple((1, 3, 2, 4)) == [2, 4]
