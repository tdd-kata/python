# Associative array
# Dictionary
# Hash
"""_summary_
watch -n 0.5 pytest -v dict.py
"""

from pytest import raises

def test_add():
    sut = {1: "one", 2: "two"}
    sut[3] = "three"
    assert sut == {1: "one", 2: "two", 3: "three"}

def test_del():
    sut = {1: "one", 2: "two"}
    del sut[1]
    assert sut == {2: "two"}

def test_duplication():
    sut = {
        1: "one",
        2: "two",
        1: "onee",
    }
    assert sut == {1: "onee", 2: "two"}

def test_dict_keys():
    sut = {1: "one", 2: "two"}

    keys = sut.keys()
    assert keys == {1, 2}
    assert type(keys) is not list # dict_keys

    key_list = list(keys)
    assert type(key_list) is list

def test_dict_values():
    sut = {1: "one", 2: "two"}

    values = sut.values()
    assert type(values) is not list # dict_values

    key_list = list(values)
    assert type(key_list) is list
    assert key_list == ["one", "two"]

def test_dict_items():
    sut = {1: "one", 2: "two"}

    items = sut.items()
    assert type(items) is not list # dict_items

    item_list = list(items)
    assert type(item_list) is list
    assert item_list == [(1, "one"), (2, "two")]
    assert type(item_list[0]) is tuple

def test_clear():
    sut = {1: "one", 2: "two"}
    sut.clear()
    assert sut == {}

def test_get():
    sut = {1: "one", 2: "two"}
    empty = sut.get(3)
    assert empty == None

    with raises(KeyError) as ex:
        sut["invalid_key"]
    assert "invalid_key" in str(ex.value)

def test_in():
    sut = {1: "one", 2: "two"}
    assert 1 in sut
    assert 2 in sut
    assert 3 not in sut
