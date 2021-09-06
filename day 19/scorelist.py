# 리스트 생성 및 사용
# 리스트 5개의 자료 저장

score = [90, 80, 70, 60, 85]

# 인덱싱(요소 접근)
print(score[0])  # 첫 요소
print(score[-1])  # 끝 요소
print(score)  # 리스트 형태로 출력
# 슬라이싱
print(score[0:3])  # 0 ~ 2 (3-1)
print(score[:3])  # 0 ~ 2
print(score[1:4])  # 1 ~ 3
print(score[2:])  # 2번 인덱스 ~ 끝
print('='*20)

# 값으로 출력
for i in score:
    print(i, end=' ')
print()
print('='*20)

# 70 이상인 값
for i in score:
    if i >= 70:
        print(i, end=' ')
print('\n' + '=' *20)

#  홀수 값만 출력
for i in score:
    if i % 2 == 1:
        print(i, end=' ')
