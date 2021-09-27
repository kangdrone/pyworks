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
first_ul = html.find('ul')   # find() 첫 요소를 찾음
print(first_ul)
print(first_ul.text)