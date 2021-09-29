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

def start():   # 스페이스 키를 누름
    global playing
    if playing == False:   # 게임이 중지되었다면
        playing = True     # 게임을 시작함
        t.clear()
        play()

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m1, False, "center", ("", 15))
    t.home()   # 거북이의 위치 좌표(0, 0)
    te.goto(0, 200)

def play():
    global playing
    global score

    if playing:   # playing == True 이면
        t.ontimer(play, 100)   # 0.1초 간격으로 play(콜백)

    t.forward(10)   # 주인공 거북이의 이동거리
    if random.randint(1, 5) == 2:   # 2를 뽑을 확률은 20%
        ang = te.towards(t.pos())  # 주인공 거북이 위치를 쫒아가는 적 거북이
        te.setheading(ang)
    speed = score + 5
    te.forward(speed)

    # 주인공 거북이가 먹이에 닿으면 먹이가 새 위치로 이동
    if t.distance(tf) < 12:
        score = score + 1
        t.write(score)
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        tf.goto(x, y)

    # 적 거북이가 주인공 거북이에게 닿으면 게임종료
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False   # 게임 종료
        score = 0         # 점수 초기화

# 메인(함수) 부분
playing = False   # 게임 스위치 전역변수 설정
score = 0         # 전역변수 (점수 누적 - 공유)

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
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")

t.mainloop()