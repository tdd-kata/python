import pdfkit

# config = pdfkit.configuration(wkhtmltopdf="path_to_exe")

# margin 값은 CSS로 조정
margin = '0mm'

options = {
    'page-size': 'A4',  # A4, Letter, Legal
    'orientation': 'portrait',  # portrait, landscape
    'dpi': 1200,
    'margin-top': margin,
    'margin-bottom': margin,
    'margin-right': margin,
    'margin-left': margin,
    'encoding': "UTF-8",
}

url = 'https://www.google.com'

# wkhtmltopdf --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 "https://google.com" test.pdf
pdfkit.from_url(url=url, output_path='out.pdf', options=options)

# return 'application/pdf'
# t = pdfkit.from_url(url=url, options=options)
# print(t)

# pdfkit.from_file(input='demo.html', output_path='out.pdf', options=options)

# pdfkit.from_string(input='Hello!', output_path='out.pdf', options=options)
