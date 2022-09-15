"""
watch -n 0.1 pytest -v generator.py
"""

# https://dojang.io/mod/page/view.php?id=2412
def number_generator():
    yield 0
    yield 1
    yield 3

def test_loop_list():
    gen = number_generator()

    a = next(gen)
    assert a == 0

    b = next(gen)
    assert b == 1

    c = next(gen)
    assert c == 3
