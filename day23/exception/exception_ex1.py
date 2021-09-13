# 예외(Exception) - 프로그램 실행 시 오류
# 예외 처리 : try ~ except
while True:
    try:
        x = input("숫자를 입력하세요 : ")
        num = int(x)
        print(num)
    except ValueError:
        print("유효한 숫자가 아닙니다. 다시 입력해주세요")