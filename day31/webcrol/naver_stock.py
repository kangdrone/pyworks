# 네이버 > 증권 > 금융홈 > 우측 삼성전자
from urllib import request
from bs4 import BeautifulSoup

def getprice():
    url = request.urlopen("https://finance.naver.com/item/main.naver?code=005930")
    html = BeautifulSoup(url, 'html.parser')
    # content = html.find('p', {'class':'no_today'})
    content = html.select_one('p.no_today')   # 태그이름.클래스이름
    print(content)
    return content

content = getprice()
# price = content.find('span', {'class':'blind'})
price = content.select_one('span.blind')
print("삼성전자 주가 : {}원". format(price.text))