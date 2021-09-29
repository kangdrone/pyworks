# 이름과 전화번호를 분리해서 추출하기
# 그룹핑된 문자열에 이름 붙이기 - (?P<그룹이름>)

import re
str = "jang 010-1234-5678"
# p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")   # [0-9A-Za-z] 같은 형식 - \w+
p = re.compile("(?P<name>\w+)\s+(?P<phone>[0-9]+[-]\d{4}[-]\d{4})")
m = p.search(str)
print(m.group())
print(m.group("phone"))   # 010-1234-5678
print(m.group("name"))    # jang
