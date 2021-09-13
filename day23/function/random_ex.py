
import math
import random

# 0.0 <= r < 1.0
print(random.random())

# random.randint(1, 10) - 1부터 10까지의 무작위 수
rand1 = random.randint(1, 10)
rand2 = math.floor(random.random() * 10 ) + 1

print(rand1)
print(rand2)

# 문자 추출
fruit = ['포도', '오렌지', '딸기']
# rnd = math.floor(random.random() * len(fruit))  # 0 ~ 2
# print(rnd)
# print(fruit[rnd])
print(random.choice(fruit))