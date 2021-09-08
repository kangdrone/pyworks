# 최대값 함수 정의하고 사용하기

def find_max(li):
    max_v = li[0]
    for i in li:
        if max_v < i:
            max_v = i
    return max_v

def find_min(li):
     min_v = li[0]
     for i in li:
         if min_v > i:
             min_v = i
     return min_v


v = [70, 80, 55, 60, 90, 31, 100]
max_v = find_max(v)  # 함수 호출
min_v = find_min(v)

print("최대값 : ", max_v)
print("최소값 : ", min_v)
