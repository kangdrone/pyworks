# 리스트 복사
li = [5, 8, 3, 2, 9]
li2 = []  # 빈 리스트
li3 = []
li4 = []

# li -> li2 원본 그대로 복사(저장)
"""
li2.append(5)
li2.append(8)
li2.append(3)
li2.append(2)
li2.append(9)
print(li2)
"""
for i in li:
    li2.append(i)

# 출력 - 리스트 형태로 출력
print(li2)
print()

# 전체 요소(값) 출력
for i in li2:
    print(i)
print()

# 짝수만 저장
for i in li:
    if i % 2 == 0:
        li3.append(i)

# 출력
print(li3)

print()

# li4에 3보다 큰 수 저장
for i in li:
    if i > 3:
        li4.append(i)

print(li4)
