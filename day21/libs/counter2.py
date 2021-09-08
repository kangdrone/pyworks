
class Counter:
    x = 0   # 클래스 변수

    def __init__(self):
        Counter.x += 1

    def __str__(self):
        return self.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

c3 = Counter()
print(c3.x)