# 시간 추측 게임

import time

input("엔터를 누르고 20초를 셉니다.")  # input()이 엔터이다.
start = time.time()  # 1970. 1. 1 자정이후 지금까지 초로 환산 시간

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

et = end-start
print("실제 시간 : %.2f초" % (et))
print("차이 : %.2f초" % abs(et-20))


