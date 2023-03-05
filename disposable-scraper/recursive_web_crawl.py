import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from ansi_color import debug, info, meta, error
from robots import robots

VISITED = set()

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
        self.page = page
        self.size = size
        self.host = urlparse(url).netloc
        self.visited = set()

    def list_url(self) -> str:
        return \
            f"{self.url}/mycar/mycar_list.php" \
            f"?gubun={Car.IMPORTED}" \
            f"&order={Order.NEWEST_REGISTER}" \
            f"&page={self.page}" \
            f"&view_size={self.size}"

    # 각 URL에 대한 요청을 처리하는 함수
    def fetch_url(self, url: str):
        response = requests.get(url=url, verify=False)
        return response.content

    def crawl(self):
        # calculate total page
        # response = requests.get(
        #     self.list_url(),
        #     verify=False  # requests.exceptions.SSLError
        # )
        # soup = BeautifulSoup(response.text, "html.parser")
        # total_count: int = int(
        #     soup.find("span", {"id": "tot"}).text.replace(",", ""))
        # meta(f"total count: {total_count}")
        # total_page = total_count // self.size + 1
        # meta(f"total page: {total_page}")
        # for page in range(1, total_page):
        #     crawl_list(list_url(page, size))

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            urls = []
            for i in range(1, 20):
                self.page += 1
                urls.append(self.list_url())
            # futures.append(executor.submit(lambda: self.crawl_list(urls)))

            futures = [executor.submit(self.fetch_url, url) for url in urls]

            # 각 요청의 결과를 출력
            for future in as_completed(futures):
                content = future.result()
                print(len(content))
            # while futures:
            #     done, futures = self.check_futures(futures)
            #     for future in done:
            #         links = future.result()
            #         for link in links:
            #             if link not in self.visited and self.host in link:
            #                 futures.append(
            #                     executor.submit(self.crawl_list, link))

    def check_futures(self, futures):
        done = []
        for future in futures:
            if future.done():
                done.append(future)
        for future in done:
            futures.remove(future)
        return done, futures

    def crawl_list(self, url: str):
        time.sleep(1)
        if url in VISITED:
            return

        debug(f"Visiting {url}")
        try:
            response = requests.get(
                url,
                verify=False  # requests.exceptions.SSLError
            )
            pprint(response)
            content = response.text
            VISITED.add(url)
        except requests.exceptions.RequestException as e:
            error(f"Error scraping {url}: {e}")
            self.crawl_list(url)
            return

        soup = BeautifulSoup(content, "html.parser")

        product_list_by_page = soup.find_all("li", {"class": "product-item"})
        for product in product_list_by_page:
            product_path = product.find("a", {"class": "img w164"}).get("href")
            product_url = f"{self.url}{product_path}"
            self.crawl_product(product_url)

    def crawl_product(self, url: str):
        info(url)
        time.sleep(1)
        if url in VISITED:
            return

        debug(f"Visiting {url}")
        try:
            response = requests.get(
                url,
                verify=False  # requests.exceptions.SSLError
            )
            content = response.text
            VISITED.add(url)
        except Exception as e:
            error(f"Error: {e}")
            self.crawl_product(url)
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

    # validate robots.txt
    robot_url = f"{context}/robots.txt"
    if robots.validate(robot_url, scraper.list_url()):
        debug('validation success')

        # run crawler
        scraper.crawl()


if __name__ == "__main__":
    main()
