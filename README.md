# Python

- [Python](#python)
  - [다운로드](#다운로드)
    - [macOS](#macos)
    - [Ubuntu 22.04](#ubuntu-2204)
    - [CentOS 7](#centos-7)
    - [Windows 11](#windows-11)
    - [pyenv](#pyenv)
  - [Python Code Formatter](#python-code-formatter)
  - [Package Installation](#package-installation)
  - [Virtual Environment (`venv`)](#virtual-environment-venv)
  - [더 읽을거리](#더-읽을거리)

Python 2는 2020년 1월 1일부터 더 이상 지원되지 않는다.
버그 수정, 보안 패치, 새로운 기능의 역포팅(backporting)이 이뤄지지 않는다.
Python 2를 사용하는 데 따른 책임은 본인에게 있다.

만약 Python 2 예제 코드 등을 확인할 일이 있다면 [2to3](https://docs.python.org/ko/3/library/2to3.html)를 사용할 수 있다.

```sh
2to3 -w .
```

## 다운로드

- [Download](https://www.python.org/downloads/)

### macOS

```sh
brew install python@3.12
```

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

### CentOS 7

기본적으로 2.7.5가 설치되어 있다.

```sh
python --version
# Python 2.7.5
```

YUM을 이용해 설치하면 3.6.8이 설치된다.

```sh
sudo yum install python3
```

```sh
python --version
# Python 3.6.8
```

3.10을 설치하기 위해서는 직접 설치해야 한다.

```sh
sudo yum install gcc openssl-devel bzip2-devel libffi-devel
```

```sh
cd /tmp
curl -LO https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tar.xz
tar xf Python-3.10.7.tar.xz
cd Python-3.10.7
```

ssl 모듈을 사용하려면 openssl 1.1.1을 설치해야 한다.

```sh
sudo yum install openssl-devel
openssl version
# OpenSSL 1.0.2k-fips  26 Jan 2017

sudo yum remove openssl-devel
```

```sh
yum install gcc gcc-c++ pcre-devel zlib-devel perl wget
cd /tmp
# https://www.boho.or.kr/data/secNoticeView.do?bulletin_writing_sequence=66719
# https://www.openssl.org/source/
curl -LO https://www.openssl.org/source/openssl-1.1.1q.tar.gz

sha256sum openssl-1.1.1q.tar.gz
curl https://www.openssl.org/source/openssl-1.1.1q.tar.gz.sha256

tar xf openssl-1.1.1q.tar.gz
cd openssl-1.1.1q

./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
make
sudo make install

echo "/usr/local/ssl/lib" | sudo tee /etc/ld.so.conf.d/openssl-1.1.1q.conf

which openssl
# /usr/bin/openssl
sudo mv /usr/bin/openssl /usr/bin/openssl-1.0.2k
sudo ldconfig -v

sudo ln -s /usr/local/ssl/bin/openssl /usr/bin/openssl
openssl version
# OpenSSL 1.1.1q  5 Jul 2022
```

openssl 경로와 함께 python을 설치한다.

```sh
# ./configure --enable-optimizations
# sudo make altinstall
# Could not build the ssl module!
# Python requires a OpenSSL 1.1.1 or newer

cd /tmp/Python-3.10.7
./configure --with-openssl=/usr/local/ssl
sudo make altinstall
```

```sh
python3.10 --version
# Python 3.10.7
```

python3라는 명령어를 사용하기 위해서는 심볼릭 링크를 생성한다.

```sh
which python3.10
# /usr/local/bin/python3.10

sudo ln /usr/local/bin/python3.10 /usr/local/bin/python3
python3 --version
# Python 3.10.7
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

### pyenv

- [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/) - Real Python

Build Dependencies

```sh
# Ubuntu/Debian
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl

# Fedora/CentOS/RHEL
sudo yum install gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite \
sqlite-devel openssl-devel xz xz-devel libffi-devel

# macOS
brew install openssl readline sqlite3 xz zlib
```

```sh
curl https://pyenv.run | bash
```

```sh
# ~/.zshrc
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

```sh
exec $SHELL
```

```sh
# 3.9.*, 3.10.*
pyenv install --list | egrep " 3\.(9|10)\."
```

```sh
pyenv install 3.9.16 -v
# /home/markruler/.pyenv/versions/3.9.16

pyenv versions                                                                                                ✭
* system (set by /home/markruler/.pyenv/version)
  3.9.16

pyenv install 3.10.9 -v
# /home/markruler/.pyenv/versions/3.10.10
```

## Python Code Formatter

- [Black](https://github.com/psf/black)

## Package Installation

- `python -m pip`를 사용해야 하는 이유
  - [BPO-22295](https://bugs.python.org/issue22295)
  - [Why you should use `python -m pip`](https://snarky.ca/why-you-should-use-python-m-pip/)
- [What's the difference between a Python module and a Python package?](https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-python-module-and-a-python-package#answer-7948672)

```sh
# https://bugs.python.org/issue22295
python3 -m pip install $PACKAGE
```

## Virtual Environment (`venv`)

- [venv](https://docs.python.org/3/library/venv.html)

> The virtual environment was not created successfully because ensurepip is not
> available.  On Debian/Ubuntu systems, you need to install the python3-venv
> package using the following command.

```sh
# 만약 커맨드가 없다면
apt install python3.11-venv
```

```sh
# python3 -m venv {venv_name}
python3 -m venv venv
echo "venv" >> .gitignore
```

```sh
# Unixlike
source venv/bin/activate

# Windows
venv\Scripts\activate
```

## 더 읽을거리

- 파이썬 스킬 업 (Supercharged Python)
- 고성능 파이썬 (High Performance Python)
- 전문가를 위한 파이썬 프로그래밍 (Expert Python Programming) 4/e
- 파이썬 코딩의 기술 (Effective Python) 2/e
- CPython 파헤치기
- [테스트 주도 개발](https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9788966261024) - 켄트 벡
- [클린 코드를 위한 테스트 주도 개발 (Django)](https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9788994774916) - 해리 J.W. 퍼시벌
- [파이썬 클린 코드](https://www.aladin.co.kr/shop/wproduct.aspx?ISBN=9791161340463) - 마리아노 아나야
- [우아하게 준비하는 테스트와 리팩토링](https://youtu.be/S5SY2pkmOy0) - 한성민, PyCon Korea
- [파이썬에서 편하게 테스트 케이스 작성하기](https://youtu.be/rxCjxX4tT1E) - 박종현, PyCon Korea
