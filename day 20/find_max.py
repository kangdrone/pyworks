# 최대값 계산하기

v = [70, 80, 55, 60, 90]
max = v[0]  # 최대값 설정
for i in v:
    if max < i:
        max = i

'''
max = 70
max = 80  70 < 80
max = 90  80 < 90
'''

print("최대값 : ", max)

min = v[0]
for i in v:
    if min > i:
        min = i

print("최소값 : ", min)
