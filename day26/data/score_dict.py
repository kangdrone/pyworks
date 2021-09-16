# 학생 5명의 개인별 국어, 수학 점수 계산
score = [
    {'name': '디바', 'Korean': 90, 'math': 70, 'science': 65},
    {'name': '파라', 'Korean': 85, 'math': 76, 'science': 75},
    {'name': '메르시', 'Korean': 80, 'math': 65, 'science': 85},
    {'name': '윈스턴', 'Korean': 95, 'math': 85, 'science': 55},
    {'name': '솔저-76', 'Korean': 85, 'math': 70, 'science': 35}
]

print('이름 총점 평균')
for s in score:
    sum_v = s['Korean'] + s['math'] + s['science']
    avg = sum_v / 3
    print("%s %d %.1f" % (s['name'], sum_v, avg))


# 과목별 국어 수학 점수 계산
sum_korean = 0
sum_math = 0
sum_science = 0

for c2 in score:
    sum_korean += c2['Korean']
    sum_math += c2['math']
    sum_science += c2['science']

    avg_korean = sum_korean / len(score)
    avg_math = sum_math / len(score)
    avg_science = sum_science / len(score)

    print("국어 합계 : %d점" % sum_korean)
    print("수학 합계 : %d점" % sum_math)
    print("과학 합계 : %d점" % sum_science)
    print("국어 평균 : %.1f점" % avg_korean)
    print("수학 평균 : %.1f점" % avg_math)
    print("과학 평균 : %.1f점" % avg_science)
