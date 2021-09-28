# 네이버 > 증권 > 금융홈 > 우측 삼성전자
from urllib import request
from bs4 import BeautifulSoup

def getprice():
    url = request.urlopen("https://finance.naver.com/item/main.naver?code=005930")
    html = BeautifulSoup(url, 'html.parser')
    no_today = html.find('p', {'class':'no_today'})
    # print(no_today)
    return no_today

content = getprice()
price = content.find('span', {'class':'blind'})
print("삼성전자 주가 : {}원". format(price.text))