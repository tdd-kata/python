"""
watch -n 0.5 pytest -v set.py
"""

def test_len():
    # set은 {중괄호}를 사용한다.
    sut = {1, 3, 2, 2}
    assert sut == {1, 2, 3}
    assert len(sut) == 3
