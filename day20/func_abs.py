# 절대값 계산하는 함수 정의
# 조건 - 음수는 양수로 변환되고, 양수는 그대로 양수

def abs_v(x):
    if x < 0:
        return -x
    else:
        return x

print(abs_v(-5)) # 3
print(abs_v(3))  # 3
