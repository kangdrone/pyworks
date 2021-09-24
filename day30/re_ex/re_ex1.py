# 정규 표현식
import re
# match()함수 -> find() 유사

p = re.compile("[a-z]+")   # [] - 매치되는 문자, + : 1번 이상 반복
m = p.match('2021 python')
print(m)

# search()
s = p.search("2021 python")
print(s)