# filter()함수와 lambda 함수 사용
# filter(함수, 리스트)
def negative2(v):
    v2 = []
    for i in v:
        if i < 0:
            v2.append(i)
    return v2

v = [-5, 1, 2, -11, 76]
print(negative2(v))

# lambda로 구현
negative = lambda x : x < 0   # 음수를 계산하는 함수
print(list(filter(negative, v)))
