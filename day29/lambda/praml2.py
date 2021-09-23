# 매개변수가 없는 lambda 함수
# 안녕하세요를 10번 반복 -> 콜백함수(매개변수가 함수인 것)
def call_10(func):
    for i in range(10):
        func()

def say_hello():
    print("안녕하세요")

# say_hello()
call_10(say_hello)

print("lambda로 구현")
say_hello2 = lambda : print("안녕하세요")
call_10(say_hello2)
call_10(lambda : print("안녕하세요"))