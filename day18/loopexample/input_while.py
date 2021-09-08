# 숫자를 입력받아 그 수까지 반복하는 프로그
x = input("몇 번 반복할까요? ")
n = int(x)

i = 0
while i < n:
    i += 1
    print(str(i) + "회 반복")
