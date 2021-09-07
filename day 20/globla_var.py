# 전역변수 사용하기 - global 키워드 사용

def one_up():
    global x
    x += 1
    return x

x = 1  # x는 전역변수 : 프로그램이 종료되면 소멸
print(one_up())  # 2
print(one_up())  # 3
print(one_up())  # 4
