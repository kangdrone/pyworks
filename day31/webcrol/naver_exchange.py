# 네이버 > 증권 > 시장지표 > 환전 고시 환율

from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("https://finance.naver.com/marketindex/")
html = BeautifulSoup(url, "html.parser")
lis = html.select("div.market1 ul li")
print(lis)
for li in lis:
    exchange = li.select_one("span.blind")
    value = li.select_one("span.value")
    print(exchange.string.split(' ')[-1], ':', value.string)