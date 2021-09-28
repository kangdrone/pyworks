# 네이버 > 증권 > 금융홈 > 우측 삼성전자
from urllib import request
from bs4 import BeautifulSoup

def getcontent(item_code):
    url = request.urlopen("https://finance.naver.com/item/main.naver?code=" + item_code)
    html = BeautifulSoup(url, 'html.parser')
    content = html.find('p', {'class':'no_today'})
    # print(no_today)
    return content

def getprice(item_code):
    content = getcontent(item_code)
    price = content.find('span', {'class': 'blind'})
    return price

삼성전자 = getprice('005930')
카카오 = getprice('035720')

print("삼성전자 주가 : {}원". format(삼성전자.text))
print("카카오 주가 : {}원". format(카카오.text))