import asyncio
import json
import logging
import os
import shutil
from datetime import datetime, timedelta
from functools import wraps

from flask import Flask, Response, request
from pyppeteer import launch

app = Flask(__name__)
loop = asyncio.get_event_loop()


# logging decorator
def print_elapsed_time(func):
    @wraps(func)
    def wrapper(**kwargs):
        start = datetime.now()
        app.logger.info(f"start: {start}")

        # 함수 실행
        result = func(**kwargs)

        # 현재 Epoch time 얻기
        end = datetime.now()
        app.logger.info(f"end: {end}")

        elapsed_time: timedelta = (end - start)
        formatted_elapsed_time = "{:.3f}".format(elapsed_time.total_seconds())
        app.logger.info(
            f"Elapsed time for function: {formatted_elapsed_time} s")

        return result

    return wrapper


async def url_to_pdf(url):
    print(os.environ["PATH"])
    # GUI(gtk)
    command_chrome = shutil.which('google-chrome')
    # command_chrome = shutil.which('chromium-browser')
    # CLI
    # command_chrome = shutil.which('chromium')
    app.logger.debug(f'which chrome: {command_chrome}')

    app.logger.debug('headless Chromium 브라우저 시작')
    browser = await launch(
        executablePath=command_chrome,
        headless=True,
        args=[
            "--no-sandbox",
            "--single-process",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--no-zygote",
        ],
        # avoid "signal only works in main thread of the main interpreter"
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
    )

    app.logger.debug('새 페이지 열기')
    page = await browser.newPage()

    app.logger.debug('URL로 이동')
    await page.goto(url)

    app.logger.debug('PDF로 변환 및 저장')
    pdf = await page.pdf({
        'format': 'A4',
        # 'path': _output_path,
        # 'margin': {
        #     'top': '10mm'
        # },
    })

    app.logger.debug('브라우저 종료')
    await browser.close()

    return pdf


@app.route(rule='/pdf/url', methods=['GET'])
@print_elapsed_time
def get_pdf_from_url():
    # req_param: dict = request.json
    req_param: dict = request.args

    try:
        app.logger.info(req_param['url'])
        pdf_binary_data = loop.run_until_complete(
            url_to_pdf(url=req_param['url'])
        )

    except Exception as e:
        app.logger.error(e)
        res: dict[str, str] = {
            "message": "Something went wrong. Please try again later."
        }
        return Response(
            response=json.dumps(res),
            mimetype='application/json',
            status=500,
        )
    filename = req_param.get('filename', 'output')

    return Response(
        response=pdf_binary_data,
        mimetype='application/pdf',
        headers={
            'Content-Disposition': f'attachment;filename={filename}.pdf'
        }
    )


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)

    app.run(
        host="0.0.0.0",  # 명시하지 않으면 `localhost`만 인식함.
        port=5000,
        # use_reloader=True,
        debug=False,  # 개발 시 `True`로 설정
    )
