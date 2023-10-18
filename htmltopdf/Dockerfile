#FROM python:3.12-slim-bookworm
FROM python:3.11-bookworm

COPY . /app
WORKDIR /app

RUN apt-get update

# 한국어 처리 시 폰트 필요
RUN apt-get -y install fonts-nanum

# Locale 설정
#RUN apt-get -y install locales
#RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8
#ENV LANG ko_KR.UTF-8
#ENV LANGUAGE ko_KR.UTF-8
#ENV LC_ALL ko_KR.utf8
#ENV PYTHONIOENCODING utf-8

# Timezone: KST 설정
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# wkhtmltopdf: HTML to PDF converter
RUN apt-get -y install wkhtmltopdf

RUN pip3 install -r requirements.txt
CMD ["python3", "api.py"]

