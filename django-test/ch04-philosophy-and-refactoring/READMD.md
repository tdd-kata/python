# 왜 테스트를 하는 것인가

[원문](https://github.com/hjwp/Book-TDD-Web-Dev-Python/blob/master/chapter_philosophy_and_refactoring.asciidoc)

```bash
# python3 manage.py help
python3 manage.py runserver
python3 functional_tests.py
```

```bash
mkdir -p lists/templates
```

```diff
# superlists/settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
+   'lists',
)
```

```bash
cd superlists
python3 manage.py test
```
