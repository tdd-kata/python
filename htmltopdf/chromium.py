import asyncio
import shutil

from pyppeteer import launch


async def url_to_pdf(url, _output_path):
    # command_chrome = shutil.which('google-chrome')
    command_chrome = shutil.which('chromium-browser')
    print(f'which google-chrome: {command_chrome}')

    print('headless Chromium 브라우저 시작')
    browser = await launch(
        executablePath=command_chrome,
        headless=True,
    )

    print('새 페이지 열기')
    page = await browser.newPage()

    print('URL로 이동')
    await page.goto(url)

    print('PDF로 변환 및 저장')
    await page.pdf({
        'path': _output_path,
        'format': 'A4',
        # 'margin': {
        #     'top': '10mm'
        # },
    })

    print('브라우저 종료')
    await browser.close()


if __name__ == '__main__':
    webpage_url = 'https://www.google.com'
    output_path = 'output-chromium.pdf'

    # 비동기 함수 실행
    asyncio.get_event_loop().run_until_complete(
        url_to_pdf(webpage_url, output_path)
    )

    print(f'PDF 파일이 {output_path}로 생성되었습니다.')
