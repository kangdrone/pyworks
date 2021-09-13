# 장바구니 클래스 만들기
class Cart:
    li = []  # 클래스 빈 리스트 선언

    def __init__(self, goods):
        Cart.li.append(goods)  # 클래스 이름으로 접근

    def __str__(self):
        print(Cart.li)


c1 = Cart("계란")
print(c1.li)
c2 = Cart("두부")
print(c2.li)
c3 = Cart("커피")
print(c3.li)