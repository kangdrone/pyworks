# ralse 구문 - 예외 처리를 미뤄놓음
# 사용하는 쪽에서 예외 처리를 해야 함

class Animal:
    def cry(self):
        raise NotImplementedError   # 상속받는 클래스가 반드시 구현해야 함
    def breath(self):
        print("울음소리를 냅니다")

class Dog(Animal):
    # pass
    def cry(self):
        print("크르르 왈~ 왈~ ")

class Cat(Animal):
    # pass
    def cry(self):
        print("애옹 ~ 애옹")

dog = Dog()   # 상속
dog.cry()     # 부모 메서드 사용
dog.breath()

cat = Cat()
cat.cry()
cat.breath()

