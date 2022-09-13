def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def test_factorial():
    assert factorial(3) == 6

# pytest -v factorial.py
