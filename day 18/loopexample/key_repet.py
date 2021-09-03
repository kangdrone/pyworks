# key 반복
# 'y' : "계속 반복합니다.", 'n':반복을 중단합니다.
# 다른 키는 "기능을 지원하지 않습니다."

while True:
    answer = input("반복을 계속할까요?(y/n) ")

    if answer == 'y' or  answer == 'Y':
        print("계속 반복합니다.")
    elif answer == 'n' or answer == 'X':
        print("반복을 중단합니다")
        break
    else:
        print("지원하지 않는 키입니다. 다시 입력해주세요")
