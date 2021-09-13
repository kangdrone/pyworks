from classlib.converter import ScaleConverter

# ScaleConverter를 상속한 Converter 클래스 정의
# 화씨 온도(F) = 섭씨온도 x 1.8 + 32
class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, factor2):
        super().__init__(units_from, units_to, factor)
        self.factor2 = factor2

    def conver(self, val):
        return super(). convert(val) + self.factor2

conv = Converter('C', 'F', 1.8, 32)
print("23C를 화씨 온도로 변환")
print(str(conv.convert(23)) + conv.units_to)