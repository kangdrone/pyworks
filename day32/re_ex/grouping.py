# 이름과 전화번호를 분리해서 추출하기
# 그룹은 ()로 구분 - 인덱스 붙이기

import re
str = "jang 010-1234-5678"
# p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")   # [0-9A-Za-z] 같은 형식 - \w+
p = re.compile("(\w+)\s([0-9]+[-]\d{4}[-]\d{4})")
m = p.search(str)
print(m.group())
print(m.group(1))   # jang
print(m.group(2))   # 010-1234-5678