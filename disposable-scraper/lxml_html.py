import lxml.html
import requests

from robots import robots

robot_url = "https://www.bobaedream.co.kr/robots.txt"
url = "https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=I"

parser = robots.exclusion_standard(robot_url)
if not parser.can_fetch(useragent="*", url=url):
    raise PermissionError("Cannot fetch")

get = requests.get(url, params={"key": "value"})
html = get.text

root = lxml.html.fromstring(html)
values = root.xpath('//*[@id="listCont"]/div[1]/ul/li[1]/div/div[2]/p[1]/a')
for val in values:
    print(val.text)

links = root.cssselect(
    '#listCont > div.wrap-thumb-list > ul > li:nth-child(1) > div > div.mode-cell.title > p.tit > a')
for link in links:
    print(link.attrib['href'])
