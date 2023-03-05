import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from ansi_color import debug, info, meta, error
from robots import robots

# response = requests.get(URL, verify=False)
requests.packages.urllib3.disable_warnings()  # 인증서 경고 메시지 무시


class Car:
    IMPORTED = "I"
    DOMESTIC = "K"


class Order:
    NEWEST_REGISTER = "S11"
    OLDEST_REGISTER = "S12"
    NEWEST_MODEL_YEAR = "S21"
    OLDEST_MODEL_YEAR = "S22"
    CHEAP = "S41"
    EXPENSIVE = "S42"
    LOW_MILEAGE = "S51"
    HIGH_MILEAGE = "S52"


class Product:
    def __init__(
        self,
        name: str,
        price: str,
        mileage: int,
        year: str,
        displacement: str,
    ):
        self.name = name
        self.price = price
        self.mileage = mileage
        self.year = year
        self.displacement = displacement

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, mileage={self.mileage}, year={self.year}, displacement={self.displacement})"


class WebScraper:
    def __init__(self,
                 url: str,
                 page: int,
                 size: int):
        self.url = url
        self.total_page = 0
        self.page = page
        self.size = size
        self.host = urlparse(url).netloc
        self.visited = set()

    def get_url(self) -> str:
        return \
            f"{self.url}/mycar/mycar_list.php" \
            f"?gubun={Car.IMPORTED}" \
            f"&order={Order.NEWEST_REGISTER}" \
            f"&page={self.page}" \
            f"&view_size={self.size}"

    def calculate_total_page(self):
        """
        전체 페이지 수를 계산한다.
        """
        response = requests.get(
            url=self.get_url(),
            headers={
                # navigator.userAgent
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
            },
            verify=False  # requests.exceptions.SSLError
        )
        soup = BeautifulSoup(response.text, "html.parser")
        total_count = int(
            soup.find("span", {"id": "tot"}).text.replace(",", ""))
        meta(f"total count: {total_count}")
        self.total_page = total_count // self.size + 1
        meta(f"total page: {self.total_page}")

    def fetch_url(self, url: str):
        """
        각 URL에 대한 요청을 처리한다.
        """
        response = requests.get(
            url=url,
            headers={
                # navigator.userAgent
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
            },
            verify=False
        )
        return response.content

    def crawl(self):
        """
        크롤링을 수행한다.
        """
        interval = 0.5
        """
        Rate Limiting을 피하기 위해 interval을 설정한다.
        `ssl.SSLZeroReturnError: TLS/SSL connection has been closed (EOF) (_ssl.c:997)` 에러가 발생하는데
        이 오류는 "일반적으로 서버에서 SSL/TLS 연결을 닫았지만, 클라이언트 측에서 이를 처리하지 못하고 추가 데이터를 보낼려고 시도할 때 발생한다"고 한다.
        서버가 연결을 닫았기 때문에 클라이언트가 데이터를 보내려고 할 때 `SSLZeroReturnError` 예외가 발생한다.
        """

        with ThreadPoolExecutor(max_workers=3) as executor:
            urls = []
            for i in range(1, self.total_page):
                self.page = i
                urls.append(self.get_url())
            # futures.append(executor.submit(lambda: self.crawl_list(urls)))

            futures = [executor.submit(self.fetch_url, url) for url in urls]

            # 각 요청의 결과를 출력
            for future in as_completed(futures):
                time.sleep(interval)
                content = future.result()
                # print(len(content))
                soup = BeautifulSoup(content, "html.parser")

                product_elements = soup.find_all("li",
                                                 {"class": "product-item"})
                product_url = []
                for product in product_elements:
                    product_path = product.find("a", {"class": "img w164"}).get(
                        "href")
                    product_url.append(f"{self.url}{product_path}")
                    # self.crawl_product(product_url)
                # return product_url
                print(product_url)
            # while futures:
            #     done, futures = self.check_futures(futures)
            #     for future in done:
            #         links = future.result()
            #         for link in links:
            #             if link not in self.visited and self.host in link:
            #                 futures.append(
            #                     executor.submit(self.crawl_list, link))

    def check_futures(self, futures):
        """
        완료된 future를 제거한다.
        """
        done = []
        for future in futures:
            if future.done():
                done.append(future)
        for future in done:
            futures.remove(future)
        return done, futures

    def scrap_list(self, url: str):
        """
        상품 목록 페이지를 스크랩한다.
        """
        time.sleep(1)
        if url in self.visited:
            return

        debug(f"Visiting {url}")
        try:
            response = requests.get(
                url=url,
                headers={
                    # navigator.userAgent
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
                },
                verify=False  # requests.exceptions.SSLError
            )
            pprint(response)
            content = response.text
            self.visited.add(url)
        except requests.exceptions.RequestException as e:
            error(f"Error scraping {url}: {e}")
            self.scrap_list(url)
            return

        soup = BeautifulSoup(content, "html.parser")

        product_list_by_page = soup.find_all("li", {"class": "product-item"})
        product_url = []
        for product in product_list_by_page:
            product_path = product.find("a", {"class": "img w164"}).get("href")
            product_url.append(f"{self.url}{product_path}")
            # self.crawl_product(product_url)
        return product_url

    def scrap_product(self, product_url: str):
        """
        상품 페이지를 스크랩한다.
        """
        info(product_url)
        time.sleep(1)
        if product_url in self.visited:
            return

        debug(f"Visiting {product_url}")
        try:
            response = requests.get(
                url=product_url,
                headers={
                    # navigator.userAgent
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
                },
                verify=False  # requests.exceptions.SSLError
            )
            content = response.text
            self.visited.add(product_url)
        except Exception as e:
            error(f"Error: {e}")
            self.scrap_product(product_url)
            return

        soup = BeautifulSoup(content, "html.parser")
        tbody_children = soup.find_all('tbody')[0].find_all(recursive=True)
        model_year = ""
        displacement = ""
        for node in tbody_children:
            if node.text == "연식":
                model_year = node.find_next_siblings("td")[0].text
            elif node.text == "배기량":
                displacement = node.find_next_siblings("td")[0].text

        _price = soup.select("div.price-area span.price b.cr")
        if len(_price) == 0:
            _price = soup.select("div.price-area span.price b")
        else:
            _price = _price[0].text.strip().replace(",", "")

        product = Product(
            name=soup.select("div.title-area h3.tit")[0].text.strip(),
            price=_price,
            year=model_year,
            mileage=int(soup.select("p.state span.txt-bar")[1]
                        .text
                        .replace(",", "")
                        .replace("km", "")),
            displacement=displacement,
        )
        error(product)


def main():
    context = "https://www.bobaedream.co.kr"
    scraper = WebScraper(url=context, page=1, size=20)
    scraper.calculate_total_page()

    # validate robots.txt
    robot_url = f"{context}/robots.txt"
    if robots.validate(robot_url, scraper.get_url()):
        debug('validation success')

        # run crawler
        scraper.crawl()


if __name__ == "__main__":
    main()
