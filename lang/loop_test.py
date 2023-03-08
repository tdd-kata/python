"""
watch -n 0.1 pytest -v loop.py
"""


def test_loop_list():
    sut = [1, 2, 3]
    result = []

    for i in sut:
        result.append(i)

    assert result == [1, 2, 3]


def test_loop_set():
    sut = {1, 2, 3}
    result = []

    for i in sut:
        result.append(i)

    assert result == [1, 2, 3]


def test_loop_tuple_list():
    sut = [(1, "one"), (2, "two"), (3, "three")]
    lefts = []
    rights = []

    for (first, last) in sut:
        lefts.append(first)
        rights.append(last)

    assert lefts == [1, 2, 3]
    assert rights == ["one", "two", "three"]


def test_loop_dict():
    sut = {1: "one", 2: "two", 3: "three"}
    keys = []
    values = []

    # dict_keys, dict_values, dict_items
    for (key, value) in sut.items():
        keys.append(key)
        values.append(value)

    assert keys == [1, 2, 3]
    assert values == ["one", "two", "three"]
