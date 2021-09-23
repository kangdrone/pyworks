# 매개변수가 2개 있는 람다 함수

def calc(x, y):   # 거듭 제곱 계산 함수
    return x ** y

print(calc(2, 3))   # 8

print("== lambda 함수로 구현 ==")
clac2 = lambda x, y : x ** y
print(clac2(2, 3))

print((lambda x, y : x ** y)(2, 3))