# 여러개의 원 그리기
import turtle as t

n = 50
t.speed(0)  # 최고 속도 (1 ~ 10)
t.bgcolor("black")
t.color("blue")
for x in range(n):
    t.circle(80)
    t.left(360/2.5)

for x in range(n):
    t.circle(140)
    t.left(360/2.3)

t.forward
t.color("pink")
for x in range(n):
    t.circle(140)
    t.left(360/2.1)
