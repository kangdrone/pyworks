# 주민번호 뒷자리를 -******* 처리하기

import re

data = '''
kim 871212-1234567
park 900101-2345678
'''

p = re.compile("(\d{6})[-]\d{7}")
s = p.sub("\g<1>-*******", data)
print(s)