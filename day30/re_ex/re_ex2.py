# '*'와 '+'의 차이
# * - 앞문자 0번 이상 반복도 찾음
# + - 앞문자 1번 이상 반복
import re

p = re.compile("ca*t")   # 정규식

m1 = re.findall(p, "caat")
print(m1)

m2 = re.findall(p, "ct")
print(m2)

p2 = re.compile("ca+t")  # 정규식

m1 = re.findall(p2, "caat")
print(m1)

m2 = re.findall(p2, "ct")
print(m2)