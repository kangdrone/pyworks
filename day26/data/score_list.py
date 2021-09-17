# 학생 5명의 국어, 수학 점수 계산

score = [
    [90, 70],
    [85, 76],
    [80, 65],
    [95, 85],
    [85, 70]
]

# 리스트 추가
score.append([90, 80])
print(score)

for x, y in score:
    print(x, y)
"""
# 합계와 평균
sum_kor = 0
sum_math = 0
n = len(score)
for i in range(0, n):   # 0 ~ 4
    sum_kor += score[i][0]
    sum_math += score[i][1]

avg_kor = sum_kor / n    # 국어 평군
avg_math = sum_math / n  # 수학 평균

print("국어 합계 : %d점" % sum_kor)
print("수학 합계 : %d점" % sum_math)
print("국어 평균 : %.1f점" % avg_kor)
print("수학 평균 : %.1f점" % avg_math)
"""