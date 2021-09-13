# 좌표 이동 : goto(x, y)
# 시작시에 랜덤한 좌표에서 나타나기
import random
import turtle as t

t.shape("turtle")

t.speed(0)
t.up()
# t.goto(0,-200)  # x : 0  y : 100px
x = random.randint(-250, 250)
y = random.randint(-250, 250)
print(x, y)
t.goto(x, y)

t.mainloop()