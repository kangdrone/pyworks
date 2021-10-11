# 온도 변환기
class Converter:
    def __init__(self, units_from, units_to, factor, offset):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor
        self.offset = offset

    def convert(self, val):
        return self.factor * val + self.offset

if __name__ == "__name__":
    c1 = Converter("C", 'F', 1.8, 32)
    print(str(c1.convert(23)) + c1.units_to)