# 고객 클래스 정의
class Customer:
    def __init__(self, cid, cname):
        self._cid = cid          # 고객 아이디 (private - 접근제한)
        self._cname = cname      # 고객 이름 (private - 접근제한)
        self.cgraed = "Silver"   # 고객 등급
        self.bonus_point = 0     # 보너스 포인트
        self.bonus_ratio = 0.01  # 보너스 적립율 - 1%

    def getname(self):    # cname이 접근 불가이므로 함수로 가져옴
        return self._cname

    def calc_price(self, price):   # 보너스 포인트 = 상품가격 x 보너스 적립율
        self.bonus_point += int(price * self.bonus_ratio)   # 포인트 정수로 변환
        return price

    def showInfo(self):
        print(self.getname() + " 님의 등급은 < " + self.cgraed + " > 이고, 보너스 포인트는 "+
              str(self.bonus_point) + "점 입니다.")

class GoldCustomer(Customer):
    def __init__(self,cid, cname):
        super().__init__(cid, cname)   # Customer 멤버(cid, cname) 상속
        self.cgraed = "Gold"      # 고객 등급
        self.sale_ratio = 0.1     # 구매 할인율 - 10%
        self.bonus_ratio = 0.02   # 보너스 적립율 - 2%

    def calc_prcie(self, price):   # 메서드 재정의(오버라이드)
        price = price - int(price * self.sale_ratio)   # 상품 가격 = 상품 가격 - 할인된 가격
        self.bonus_point += int(price * self.bonus_ratio)  # 포인트 정수로 변환
        return price

class VIPCustomer(Customer):
    def __init__(self, cid, cname, agent):
        super().__init__(cid, cname)
        self.agent = agent        # 전문 상담원 설정
        self.cgraed = "VIP"       # 고객 등급
        self.sale_ratio = 0.1     # 구매 할인율 - 10%
        self.bonus_ratio = 0.05   # 보너스 적립율 - 2%

    def calc_prcie(self, price):   # 메서드 재정의(오버라이드)
        price = price - int(price * self.sale_ratio)   # 상품 가격 = 상품 가격 - 할인된 가격
        self.bonus_point += int(price * self.bonus_ratio)  # 포인트 정수로 변환
        return price

    def showInfo(self):
        super().showInfo()
        print("상담원 ID는 " + str(self.agent) + "입니다.")