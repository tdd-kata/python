# 단위 테스트를 이용한 간단한 홈페이지 테스트

## 개요

- 기능 테스트(Functional Test)는 사용자 관점에서 애플리케이션 외부를 테스트하는 것이고, 단위 테스트(Unit Test)는 프로그래머 관점에서 그 내부를 테스트한다는 것이다.
- 작업 순서
  - 기능 테스트를 작성해서 사용자 관점의 새로운 기능성을 정의하는 것부터 시작한다.
  - 기능 테스트가 실패하고 나면 어떻게 코드를 작성해야 테스트를
    통과할지(또는 적어도 현재 문제를 해결할 수 있는 방법)를 생각해보도록 한다.
    이 시점에서 하나 또는 그 이상의 단위 테스트를 이용해서 어떻게 코드가 동작해야 하는지
    정의한다(기본적으로 모든 코드가 (적어도) 하나 이상의 단위 테스트에 의해 테스트돼야 한다).
  - 단위 테스트가 실패하고 나면 단위 테스트를 통과할 수 있을 정도의 최소한의 코드만 작성한다.
    기능 테스트가 완전해질 때까지 과정 2와 3을 반복해야 할 수도 있다.
  - 기능 테스트를 재실행해서 통과하는지 또는 제대로 동작하는지 호가인한다. 이 과정에서 새로운 단위 테스트를 작성해야 할 수도 있다.

## 실습

```bash
django-admin.py startproject superlists
cd superlists
```

### 의도적인 실패 테스트와 함께 lists 앱을 추가

```bash
python3 manage.py startapp lists
```

```python
from django.test import TestCase


class SmokeTest(TestCase):

  def test_bad_maths(self):
    self.assertEqual(1 + 1, 3)
```

```bash
python3 manage.py test
# Creating test database for alias 'default'...
# F
# ======================================================================
# FAIL: test_bad_maths (lists.tests.SmokeTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "[...]/tests.py", line 7, in test_bad_maths
#     self.assertEqual(1 + 1, 3)
# AssertionError: 2 != 3
# 
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
```

### ㅇ
