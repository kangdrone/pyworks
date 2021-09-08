# 학생의 시험점수 합격 판단
# 시험 점수가 60점 이상이면 '합격', 아니면 '불합격'
score = [90, 45, 67, 59, 85]
idx = 0

print("for ~ in 리스트 반복문")
for i in score:
    idx += 1
    if i >= 60:
        print(str(idx) + "번 학생은 합격입니다.")
    else:
        print(str(idx) + "번 학생은 불합격입니다.")
    #print(i)
print()

print("for ~ in range() 반복문")
n = len(score)
for i in range(0, n):
    if score[i] >= 60:
        print(str(i+1) + "번 학생은 합격입니다.")
    else:
        print(str(i+1) + "번 학생은 불합격입니다.")

# 성적의 합계, 평균
total = 0
avg = 0.0
for i in score:
    total += i

# 평균 = 합계 / 개수
avg = total / len(score)

print("합계 : " + str(total) + "점")
print("평균 : " + str(avg) + "점")
