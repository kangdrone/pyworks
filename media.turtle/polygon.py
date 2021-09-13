# 다각형 그리기
import turtle as t

t. shape("turtle")

def polygon(n):
    for i in range(n):
        t.forward(50)     # 거리(변의 길이)
        t.left(360 / n)   # 각도

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360 / n)

polygon(3)
polygon(5)

t.up()  # 펜 올리기
t.forward(150)
t.down()  # 펜 내리기

polygon2(4, 70)
polygon2(8, 100)

t.mainloop()
