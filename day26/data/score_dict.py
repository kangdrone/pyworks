# 학생 5명의 국어, 수학 점수 계산
score = [
    {'name': '디바', 'Korean': 90, 'math': 70},
    {'name': '파라', 'Korean': 85, 'math': 76},
    {'name': '메르시', 'Korean': 80, 'math': 65},
    {'name': '윈스턴', 'Korean': 95, 'math': 85},
    {'name': '솔저-76', 'Korean': 85, 'math': 70}
]

print('이름 총점 평균')
sum_v = 0
for s in score:
    sum_v = s['Korean'] + s['math']
    avg = sum_v / 2
    print(s['name'], sum_v, avg)


# 과목별 국어 수학 점수 계산
sum_korean = 0
sum_math = 0

for c2 in score:
    sum_korean += c2['Korean']
    sum_math += c2['math']
    avg_korean = sum_korean / len(score)
    avg_math = sum_math / len(score)

    print("국어 합계 : %d점" % sum_korean)
    print("수학 합계 : %d점" % sum_math)
    print("국어 평균 : %.1f" % avg_korean)
    print("수학 평균 : %.1f점" % avg_math)