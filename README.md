# Python

## 다운로드

- [Download](https://www.python.org/downloads/)

### Ubuntu 22.04

```sh
sudo apt install python3-pip
```

```sh
python --version
# command not found: python

python3 --version
# Python 3.10.4

pip --version
# pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

pip3 --version
# pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
```

```sh
python3 -m pip3 install --upgrade pytest
```

```sh
pytest --version
# command not found: pytest
```

일반적으로 설치했을 경우 `$HOME/.local/bin`에 설치되기 때문에
전역적으로 사용하려면 `python3` 명령어를 사용하거나
`$HOME/.local/bin`을 `$PATH`에 추가한다.
혹은 간단하게 심볼릭 링크를 생성한다.

```sh
python3 -m pytest --version
# pytest 7.1.3
```

```sh
sudo ln $HOME/.local/bin/pytest /usr/local/bin/pytest
pytest --version
# pytest 7.1.3
```

### Windows 11

```ps1
wsl
```

```sh
sudo apt update
sudo apt upgrade
sudo apt autoremove
```

```sh
sudo apt install python3-pip
pip install --upgrade pytest

echo "export PATH=\$PATH:/home/markruler/.local/bin" >> .bashrc
source .bashrc
pytest --version
# pytest 7.1.3
```

```sh
pytest
```

## Python Code Formatter

- [Black](https://github.com/psf/black)

## 참조

- [테스트 주도 개발](https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9788966261024) - 켄트 벡
- [클린 코드를 위한 테스트 주도 개발 (Django)](https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9788994774916) - 해리 J.W. 퍼시벌
- [파이썬 클린 코드](https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9791161340463) - 마리아노 아나야
- [우아하게 준비하는 테스트와 리팩토링](https://youtu.be/S5SY2pkmOy0) - 한성민, PyCon Korea
- [파이썬에서 편하게 테스트 케이스 작성하기](https://youtu.be/rxCjxX4tT1E) - 박종현, PyCon Korea
