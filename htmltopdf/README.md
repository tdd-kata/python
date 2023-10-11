# pdfkit on Ubuntu

## Install `pdfkit`

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Install `wk<html>topdf`

```shell
sudo apt install wkhtmltopdf
python main.py
```

## 페이지 분리

table, div 태그 등에 해당 인라인 스타일을 넣어서 페이지 분리 필요.
margin 값 등으로 조정하려면 매우 힘듦.

```html

<!-- 첫 페이지부터 -> 마지막 페이지 -->
<!-- page-break-after:always; -> page-break-after:auto; -->
<!-- page-break-after:always; -> page-break-after:avoid; -->
<!-- page-break-before:auto; -> page-break-before:always; -->
<!-- page-break-before:avoid; -> page-break-before:always; -->
<div style="page-break-after: always;"></div>
<div style="page-break-after: avoid;"></div>
```

- 브라우저 프린트(`window.print()`) 기능과 동일한 출력물을 기대할 순 없나?

## 외부 URL 제거

- from_file() 사용 시 HTML 파일에 로컬 파일 참조 링크가 있으면 아래와 같은 에러가 발생함.
- CSS(`/style.css`), JS 파일과 같은 정적 파일 제거

```shell
Traceback (most recent call last):
  File "/home/markruler/playground/xpdojo/python/pdfkit/main.py", line 39, in <module>
    pdfkit.from_file(f, 'out.pdf', options={"enable-local-file-access": ""})
  File "/home/markruler/playground/xpdojo/python/pdfkit/venv/lib/python3.10/site-packages/pdfkit/api.py", line 51, in from_file
    return r.to_pdf(output_path)
  File "/home/markruler/playground/xpdojo/python/pdfkit/venv/lib/python3.10/site-packages/pdfkit/pdfkit.py", line 201, in to_pdf
    self.handle_error(exit_code, stderr)
  File "/home/markruler/playground/xpdojo/python/pdfkit/venv/lib/python3.10/site-packages/pdfkit/pdfkit.py", line 155, in handle_error
    raise IOError('wkhtmltopdf reported an error:\n' + stderr)
OSError: wkhtmltopdf reported an error:
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
QNetworkReplyImplPrivate::error: Internal problem, this method must only be called once.
QNetworkReplyImplPrivate::error: Internal problem, this method must only be called once.
Exit with code 1 due to network error: OperationCanceledError
```
