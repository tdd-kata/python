"""
watch -n 1 pytest -v assert.py
"""

import pytest

def test_assert():
    assert 1 == 2-1

@pytest.mark.xfail(raises=TypeError)
def test_mark_xfail():
    "a" + 3

def test_raise():
    with pytest.raises(TypeError):
        "a" + 3

def test_raise_message():
    with pytest.raises(TypeError) as ex:
        "a" + 3
    assert "can only concatenate str (not \"int\") to str" in str(ex.value)
