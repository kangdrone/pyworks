# BeautifulSoup 사용하기 - html 태그 및 데이터 추출 라이브러리

from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <ul class="item">
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇공학</li>
        </ul>
        <ul class="lang">
            <li>python</li>
            <li>C/C++</li>
            <li>Java</li>
    </body>
</html>
"""

html = BeautifulSoup(html_str, 'html.parser')
ul = html.find('ul', {'class':'lang'})   # 딕셔너리 구조(선택자:값)
# print(ul)
# print(ul.text)
li = ul.find('li')   # 첫 요소만 찾음
# print(li.text)

all_li = ul.findAll('li')
print(all_li)
print(all_li[2].text)