# 파이썬을 이용한 클린 코드를 위한 테스트 주도 개발

[해리 J.W. 퍼시벌](https://github.com/hjwp/Book-TDD-Web-Dev-Python/blob/master/book.asciidoc)

## The TDD process with functional and unit tests

![the-tdd-process-with-functional-and-unit-tests.png](../image/the-tdd-process-with-functional-and-unit-tests.png)

## 개발 환경

Ubuntu 20.04

- `HTMLParseError`가 Python 3.5에서 제거되었다.
- 책에서는 `django==1.7`을 설치하라고 하지만 1.8을 설치한다.

```bash
pip3 install django==1.8
```

```bash
pip3 install --upgrade selenium
```

```bash
# selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. 
cd /tmp
wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
tar zxvf geckodriver-v0.29.1-linux64.tar.gz
# geckodriver
sudo mv geckodriver /usr/local/bin/
```
