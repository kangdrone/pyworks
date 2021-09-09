# 1 증가하는 Counter 클래스 정의
class Counter:
    def __init__(self):
        self.x = 0    # 인스턴스 변수
        self.x += 1

    def __str__(self):
        return self.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

c3 = Counter()
print(c3.x)