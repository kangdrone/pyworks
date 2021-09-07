# 리스트 복사
li = [5, 8, 3, 2, 9]
li2 = []  # 빈 리스트
li3 = []

# li -> li2 원본 그대로 복사(저장)
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
