from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("http://www.naver.com")
html = BeautifulSoup(url, "html.parser")

div = html.find('div', {'class' : 'service_area'})
first_a = div.find('a')
print(first_a.text)

all_a = div.findAll('a')   # a 요소를 전체 리스트로 반환
print(all_a)
print(all_a[1].text)
for i in all_a:
    print(i.text)