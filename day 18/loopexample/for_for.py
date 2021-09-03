# 중첩 for문

for i in range(0, 5):  # 0 ~ 4행
    for j in range(0, 5):
        print('가', end='')
    print()

for i in range(0, 5):  # 0 ~ 4행
    for j in range(1, 6):  # 1 ~ 5열
        num = i*5+j
        print(num, end=' ')
    print()
