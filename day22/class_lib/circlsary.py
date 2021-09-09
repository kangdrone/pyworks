# Calculator 클래스 정의   예제 1번 점프 투 파이썬 p.262
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

"""
cal1 = Calculator()
print(cal1.add(10))
"""
# UpgradeCalculator() 테스트

cal2 = UpgradeCalculator()
print(cal2.add(10))
print(cal2.minus(7))

print(cal2.value)