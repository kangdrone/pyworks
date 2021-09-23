# map(함수, 리스트)함수와 함께 사용
# list([리스트]) -> 리스트로 반환(출력)

def times2(a):
    a2 = []   # 3의배수를 저장할 빈 리스트
    for i in a:
        a2.append(i * 3)
    return a2

v = [1, 2, 3, 4]
print(times2(v))

# 람다 함수
times = lambda x : x * 3
print(list(map(times, v)))