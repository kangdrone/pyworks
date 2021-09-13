# 터틀런 게임 만들기
import random
import turtle as t

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)   # 주인공 거북이의 이동거리
    te.forward(9)    # 적 거북이의 이동거리
    ang = te.towards(t.pos())  # 주인공 거북이 위치를 쫒아가는 적 거북이
    te.setheading(ang)

    # 적 거북이가 주인공 거북이에게 닿으면 게임종료
    if t.distance(te) >= 12:
        t.ontimer(play, 100)   # 0.1초 간격으로 계속 play(콜백함수)됨

    # 먹이에 닿으면 먹이가 새 위치로 이동
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)


# 적 거북이
te = t.Turtle()   # Turtle() 클래스의 생성자
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

# 주인공 거북이
t.setup(500, 500)  # 정사각형 무대
t.bgcolor('black')
t.shape('turtle')
t.speed(0)
t.up()
t.color('white')

# 먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('pink')
tf.speed(0)
tf.up()
tf.goto(0, -200)

# 키보드 방향키
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()

t.mainloop()