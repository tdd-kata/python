import json
from functools import wraps
from time import process_time

import pdfkit
from flask import Flask, Response, request

app = Flask(__name__)


# logging decorator
def print_elapsed_time(func):
    @wraps(func)
    def wrapper(**kwargs):
        start = process_time()
        app.logger.info(start)

        # 함수 실행
        result = func(**kwargs)

        end = process_time()
        app.logger.info(end)
        app.logger.info("\tElapsed time for function: %.3f s" % (end - start))
        return result

    return wrapper


wkhtmltopdf_options = {
    'page-size': 'A4',  # A4, Letter, Legal
    'orientation': 'portrait',  # portrait, landscape
    'dpi': 1200,
    'encoding': "UTF-8",
}


@app.route(rule='/pdf/url', methods=['GET'])
@print_elapsed_time
def get_pdf_from_url():
    # data: dict = request.json
    data: dict = request.args

    try:
        app.logger.info(data['url'])
        binary_pdf = pdfkit.from_url(url=data['url'],
                                     options=wkhtmltopdf_options)
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
    filename = 'out'
    # elapsed time

    return Response(
        response=binary_pdf,
        mimetype='application/pdf',
        headers={
            'Content-Disposition': f'attachment;filename={filename}.pdf'
        }
    )


@app.route(rule='/pdf/html', methods=['POST'])
def get_pdf_from_string_html():
    data: dict = request.json

    try:
        app.logger.debug(data['html'])
        binary_pdf = pdfkit.from_string(input=data['html'],
                                        options=wkhtmltopdf_options)
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
    filename = 'out'
    return Response(
        response=binary_pdf,
        mimetype='application/pdf',
        headers={
            'Content-Disposition': f'attachment;filename={filename}.pdf'
        }
    )


# python3 -m flask --app api.py run --debug --reload
# python3 api.py
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",  # 명시하지 않으면 localhost만 인식함.
        port=5000,
        debug=True,
        use_reloader=True,
    )
