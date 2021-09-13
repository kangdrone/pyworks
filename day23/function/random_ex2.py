# 주사위 10번 던지기
import random

for x in range(1, 11):
    dice = random.randint(1, 6)
    print(dice,end='')
print()

"""
# 주사위 2개를 10번 더지기
# 두 눈의 합이 7이면 "Seven Thrown!!"
# 두 눈의 합이 11이면 "Eleven Thrown!!"
# 두 눈의 수가 같으면 "Double Thrown!!"
"""

for x in range(1, 11):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 = dice2    # 두 눈의 합
    print(total)
    if total == 7:
        print("Seven Thrown!!")
    if total == 11:
        print("Eleven Thrown!!")
    if dice1 == dice2:
        print("Double Thrown!!")