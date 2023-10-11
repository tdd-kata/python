import json

import pdfkit
from flask import Flask, Response, request

app = Flask(__name__)


@app.route(rule='/pdf/url', methods=['GET'])
def get_pdf_from_url():
    # data: dict = request.json
    data: dict = request.args

    try:
        print(data['url'])
        binary_pdf = pdfkit.from_url(url=data['url'])
    except Exception as e:
        print(e)
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


@app.route(rule='/pdf/html', methods=['POST'])
def get_pdf_from_string_html():
    data: dict = request.json

    try:
        print(data['html'])
        binary_pdf = pdfkit.from_string(input=data['html'])
    except Exception as e:
        print(e)
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
app.run(
    port=5000,
    debug=True,
    use_reloader=True,
)
