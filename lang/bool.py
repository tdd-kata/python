"""
watch -n 0.1 pytest -v bool.py
"""

def test_true():
    assert bool("string") is True
    assert bool('string') is True
    assert bool(2) is True
    assert bool([1]) is True
    assert bool((1)) is True
    assert bool({1}) is True

def test_false():
    assert bool("") is False
    assert bool('') is False
    assert bool(0) is False
    assert bool([]) is False
    assert bool(()) is False
    assert bool({}) is False
    assert bool(None) is False
