import feedparser

from robots import robots

robot_url = "http://aladin.co.kr/robots.txt"
url = "http://aladin.co.kr/rss/special_new/351"

parser = robots.exclusion_standard(robot_url)
if not parser.can_fetch(useragent="*", url=url):
    raise PermissionError("Cannot fetch")

rss = feedparser.parse(url)
print(rss)
