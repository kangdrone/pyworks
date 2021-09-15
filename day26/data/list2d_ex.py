# 2차원 리스트의 연산
# 학생 4명의 국어 점수의 합계와 평균
d2 = [[80], [90], [100]]

# 리스트 추가
d2.append([70])
print(d2)

# 합계 리스트 추가
# sum = d2[0][0] + d2[1][0] + d2[2][0] + d2[3][0]
sum_v = 0
n = len(d2)   # 4
for i in range(0, n):
    sum_v += d2[i][0]
    print('sum_v =', sum_v, ', d2[i][0] =', d2[i][0])

avg = sum_v / n
d2.append([sum_v])
d2.append([avg])
print(d2)
print("국어 점수의 평균 : %.1f" % avg)