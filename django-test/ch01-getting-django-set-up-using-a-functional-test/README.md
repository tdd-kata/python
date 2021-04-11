# 기능 테스트를 이용한 Django 설치

```bash
python3 functional_test.py
Traceback (most recent call last):
#   File "functional_test.py", line 4, in <module>
#     browser.get('http://localhost:8000')
#   File "/home/changsu/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 333, in get
#     self.execute(Command.GET, {'url': url})
#   File "/home/changsu/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
#     self.error_handler.check_response(response)
#   File "/home/changsu/.local/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
#     raise exception_class(message, screen, stacktrace)
# selenium.common.exceptions.WebDriverException: Message: Reached error page: about:neterror?e=connectionFailure&u=http%3A//localhost%3A8000/[...]
```

```bash
django-admin.py startproject superlists
python3 ./superlists/manage.py runserver
```
