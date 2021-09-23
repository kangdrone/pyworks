# threading, datetime 모듈 임포트

import threading
import datetime

def call():
    print("타이머 종료")
    print(datetime.datetime.now())   # call 호출 후 10초 후 시간 출력

print(datetime.datetime.now())   # 현재 시간
print(datetime.datetime.today())   # 현재 시간
timer = threading.Timer(10, call)
timer.start()