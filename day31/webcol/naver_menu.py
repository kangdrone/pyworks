from urllib import request
from bs4 import BeautifulSoup

url = request.urlopen("http://www.naver.com")
html = BeautifulSoup(url, "html.parser")

ul = html. find('ul', {'class' : 'list_nav type_fix'})
# ul > li > a 로 찾아 들어감
"""
all_li = ul.findAll('li')
for li in all_li:
    a = li.find('a')
    print(a.text)
"""
# a로 찾기 ul > a
all_a = ul.find_all('a')
for a in all_a:
    print(a.text)

# print(all_li)
# print(all_li[0].text)   # 메일
# print(all_li[1].text)   # 카페