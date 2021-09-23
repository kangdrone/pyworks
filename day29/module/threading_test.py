import time
import threading
# 멀티 스레드(실행된 프로세스가 2개 이상인 것)

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working : %s\n" % i)
print("Start")

threads = []   # [t1, t2, t3, t4, t5]
for i in range(5):
    t = threading.Thread(target = long_task)   # 실행할 작업 생성
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()   # 멀티(병렬) 스레드에서 사용되어야 함

print("End")