# 도형 그리기
import turtle as t

t.shape("turtle")

# 사각형
for i in range(4):
    t.forward(100)
    t.right(90)

# 삼각형
for i in range(3):
    t.forward(100)
    t.left(120)

# 원
t.circle(50)  # 반지름이 50px

t.mainloop()