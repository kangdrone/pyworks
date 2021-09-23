import threading
# threading.Timer : 일정 주기마다 함수를 실행하는 클래스
# threading.Timer(시간, 함수)
# 싱글 스레드 - 작업 1개 실행

def repeat():
    print("3초 간격으로 반복 실행")
    timer = threading.Timer(3, repeat)
    timer.start()

repeat()