# 단위 변환 클래스 만들기 1inch -> 25mm
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):
        return self.factor * val

if __name__=="__main__":
    c = ScaleConverter("inch", "mm", 25)
    print("== inch를 mm로 변환 ==")
    # print(c.units_from)
    # print(c.units_to)
    print(str(c.convert(1)) + c.units_to)

    c2 = ScaleConverter("KB", 'Byte', 1024)
    print("KB를 B로 환산")
    print("1KB는 " + str(c2.convert(1)) + c2.units_to)