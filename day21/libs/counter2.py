
class Counter:
    x = 0   # 클래스 변수

    def __init__(self):
        Counter.x += 1    # 클래스 이름으로 접근

    def __str__(self):
        return Counter.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

c3 = Counter()
print(c3.x)