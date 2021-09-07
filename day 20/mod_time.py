# time 모듈 - 시간 관련 모듈

import time

print(time.time())  # 파이썬은 초로 계산
print(time.ctime())

# time.sleep(1) : 1초 간격으로 대기
for i in range(1, 11):
    time.sleep(0.5)  # 0.5초
    print(i)
