
d2 = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print("리스트의 크기(행) : ", len(d2))      # 3
print("리스트의 크기(열) : ", len(d2[0]))   # 2
print("리스트의 크기(열) : ", len(d2[1]))   # 2

# 전체 요소 출력
for i in range(len(d2)):
    for j in range(len(d2[i])):
        print(d2[i][j], end=' ')
    print()

# 합계와 평균
sum_v = 0
count = 0   # 개수를 기억할 변수 선언
for i in range(len(d2)):
    for j in range(len(d2[i])):
        sum_v += d2[i][j]
        count += 1    # 1번 반복할 때마다 1증가
        print('sum_v =', sum_v, ', d2[i][j] =', d2[i][j], ', count =', count)
    print()

avg = sum_v / count
print("합계 : %d" % sum_v)
print("개수 : %d" % count)
print("평균 : %.1f" % avg)