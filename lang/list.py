# pytest -v list.py

def length_list(list):
    """
    list 길이를 반환한다.

    :param list: List
    :return: Length of list
    :rtype: int
    """
    return len(list)

def test_length_list():
    assert length_list([1, 3, 2, "", False]) == 5

def sorting_list(list):
    """
    list를 정렬한다.

    :param list: List
    :return: Sorted list
    """
    return sorted(list)

def test_sorting_list():
    assert sorting_list([1, 3, 2]) == [1, 2, 3]

def slice_list(list):
    """
    list의 1번째부터 3번째까지의 값을 반환한다.

    :param list: List
    :return: Sliced list
    """
    return list[1:3]

def test_slice_list():
    assert slice_list([1, 3, 2, 4]) == [3, 2]
