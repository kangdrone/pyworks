# 이차원 리스트 - 문자열 함께 사용
e = [7, 3, ['chicken', 'cow', 'pig', 'horse']]

# chicken에 접근
print(e[0])
print(e[1])
print(e[2])
print(e[2][0])

# pig에 접근
print(e[2][2])
print(e[2][-1])

# 슬라이싱
print(e[2][1:])
print(e[2][:3])