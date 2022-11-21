"""
watch -n 0.1 pytest -v str.py
"""


def test_string_slicing_1():
    """
    인덱스 1에서 4까지 (뒷쪽 숫자는 포함하지 않는다)
    """
    assert "Hello World"[1:5] == "ello"


def test_string_slicing_2():
    assert "Hello World"[1:-2] == "ello Wor"


def test_string_slicing_3():
    assert "Hello World"[1:] == "ello World"


def test_string_slicing_4():
    world = "Hello World"
    world_ = world[:]
    assert world == world_
    assert id(world) == id(world_)


def test_string_slicing_5():
    assert "Hello World"[1:100] == "ello World"


def test_string_slicing_6():
    """
    마지막 문자(뒤에서 첫 번째)
    :return:
    """
    assert "Hello World"[-1] == "d"


def test_string_slicing_7():
    assert "Hello World"[-4] == "o"


def test_string_slicing_8():
    """
    (앞)부터 (뒤에서 3개 글자)까지
    :return:
    """
    assert "Hello World"[:-3] == "Hello Wo"


def test_string_slicing_9():
    """
    뒤에서 3번째 문자부터 마지막까지
    :return:
    """
    assert "Hello World"[-3:] == "rld"


def test_string_slicing_10():
    assert "Hello World"[::1] == "Hello World"


def test_string_slicing_11():
    """
    뒤집는다.
    :return:
    """
    assert "Hello World"[::-1] == "dlroW olleH"


def test_string_slicing_12():
    """
    2칸씩 앞으로 이동한다.
    :return:
    """
    assert "Hello World"[::2] == "HloWrd"
