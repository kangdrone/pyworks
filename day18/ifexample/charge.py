# 놀이공원 입장료 계산하기
print("♣ 놀이공원 입장료 ♣")
x = input("나이를 입력하세요.")
age = int(x)
charge = 0;

if age < 8:
    print("미취학 아동입니다")
    charge = 1000
elif age >= 8 and age < 14:
    print("초.중학생입니다")
    charge = 2000
elif age >= 14 and age < 20:
    print("고등학생입니다")
    charge = 2500
else:
    print("일반인입니다")
    charge = 3000

print("입장료는 " + str(charge) + "원 입니다.")
print("입장료는 " + format(charge, ',d') + "원 입니다.")
# format(value, "서식문자") - 천단위 구분기호 표시
# d - 정수형 , s - 문자형


