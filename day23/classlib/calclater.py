
# 계산기 클래스
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

# minus()를 추가함
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

# add() 함수 객체 변수가 100이상의 값을 가질 수 없도록 제한하는 클래스
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100
        return self.value

cal = MaxLimitCalculator()
cal.add(50)   # 50 더하기
cal.add(60)   # 60 더하기
print(cal.value)   # 100 출력하기