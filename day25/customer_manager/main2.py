# 객체(인스턴스)를 리스트로 관리

from customer_class import Customer, GoldCustomer, VipCustomer

c1 = Customer(101, "흥부")
c2 = Customer(102, "놀부")
gold1 = GoldCustomer(201, "콩쥐")
gold2 = GoldCustomer(202, "팥쥐")
vip1 = VipCustomer(301, "심청", 777)

# 리스트로 관리

customer = []   # 빈 리스트 생성
customer.append(c1)
customer.append(c2)
customer.append(gold1)
customer.append(gold2)
customer.append(vip1)

print("============ 구매가격과 보너스 포인트 계산 ============")
price = 10000   # 상품 - 10000원
for c in customer:
    cost = c.calc_price(price)   # 구매 가격(할인 적용)
    print(c.getname() + "님의 지불 금액은 " + format(cost, ',d') + "원 입니다.")

print("================== 고객 정보 출력 ==================")
for c in customer:
    c.showInfo()