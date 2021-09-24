import re

str = "123?45yy7890 hi 999 hello"
pat = re.compile("\d{1,3}")  # \d : 0~9, {최소, 최대}
m = re.findall(pat, str)
print(m)

m2 = re.findall('[^\s\w]+', str)   # '\s - 공백문자, '\w'-0-9A-Za-z
print(m2)

m3 = re.findall('[1-5]{1,2}', str)
print(m3)