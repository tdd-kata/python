import time
from pprint import pprint

import requests
from bs4 import BeautifulSoup

from robots import robots

from ansi_color import debug, info, meta, error

VISITED = set()
CONTEXT = "https://www.bobaedream.co.kr"


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
        price: int,
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


def list_url(
    page: int,
    size: int,
) -> str:
    return \
        f"{CONTEXT}/mycar/mycar_list.php" \
        f"?gubun={Car.IMPORTED}" \
        f"&order={Order.NEWEST_REGISTER}" \
        f"&page={page}" \
        f"&view_size={size}"


def crawl_list(url: str):
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
    except Exception as e:
        error(f"Error: {e}")
        crawl_list(url)
        return

    soup = BeautifulSoup(content, "html.parser")

    product_list_by_page = soup.find_all("li", {"class": "product-item"})
    for product in product_list_by_page:
        product_path = product.find("a", {"class": "img w164"}).get("href")
        product_url = f"{CONTEXT}{product_path}"
        crawl_product(product_url)


def crawl_product(url: str):
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
        crawl_product(url)
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

    product = Product(
        name=soup.select("div.title-area h3.tit")[0].text.strip(),
        price=int(soup.select("div.price-area span.price b.cr")[0]
                  .text
                  .replace(",", "")),
        year=model_year,
        mileage=int(soup.select("p.state span.txt-bar")[1]
                    .text
                    .replace(",", "")
                    .replace("km", "")),
        displacement=displacement,
    )
    error(product)


def main():
    page: int = 1
    size: int = 20

    robot_url = f"{CONTEXT}/robots.txt"
    response = requests.get(
        list_url(page, size),
        verify=False  # requests.exceptions.SSLError
    )
    soup = BeautifulSoup(response.text, "html.parser")
    total_count: int = int(
        soup.find("span", {"id": "tot"}).text.replace(",", ""))
    meta(f"total count: {total_count}")
    total_page = total_count // size + 1
    meta(f"total page: {total_page}")

    if robots.validate(robot_url, list_url(page, size)):
        debug('validation success')
        for page in range(1, total_page):
            meta(
                f"crawl page:{page},\n"
                f"total_page:{total_page}"
            )
            crawl_list(list_url(page, size))


if __name__ == "__main__":
    main()
