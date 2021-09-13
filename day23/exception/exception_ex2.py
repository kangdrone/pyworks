
# 다중 예외 - except를 여러번 사용

try:
    date = [59, 8, 4, 114, 383]
    x = input("정수 입력(0~4까지 입력해주세요)")
    num = int(x)
    print(date[num])
except IndexError as exception:  # IndexError as exception- 생략가능
    print("0~4까지 입력해주세요")
except ValueError:
    print("값에 문제가 있습니다")