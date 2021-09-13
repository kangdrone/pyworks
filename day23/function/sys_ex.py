# sys모듈 : 운영체제 관련 모듈
# 명령행에서 인수 전달하기

import sys

args = sys.argv[1:]
print(args)   # 리스트 형태로 출력

for i in args:  # 값 전체 출력
    print(i)

# 수의 합계
# args = [ '1', '2', '3']
total = 0
for i in args:
    total += int(i)
avg = total / len(args)
print("합계 : " + str(total))
print("평균 : " + str(avg))