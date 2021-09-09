class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        if self.y == 0:
            print("0으로 나눌 수 없습니다.")
            return 0
        else:
            return self.x / self.y


cal = calculator(5, 0)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())