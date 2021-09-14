"""
 - 숫자 추측 게임
컴퓨터의 랜덤 수(1 ~ 30)와 사용자가 생각하는 수가 일치하면 " 정답 "
컴퓨터가 크면"너무 커요", 아니면 "너무 작아요"출력
문자 입력시 예외처리 : try ~ except
입력 범위 초과시 : '입력 범위를 초과했습니다. 다시 입력해 주세요'
"""
import random

com = random.randint(1, 30) # 컴푸터의 랜덤 수

while True:
    try:
        user = int(input("맞혀보세요(1 ~ 30) : "))

    # 논리연산 코드 작성
        if user > 30 or user < 1:
            print("입력 범위를 초과했습니다.")
        elif com == user:
            print("정답")
            break
        elif com > user:
            print("너무 커요")
        else:
            print("너무 작아요")
    except ValueError:
        print("숫자를 입력해 주세여")