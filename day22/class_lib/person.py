# person 클래스

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {0}, 나이 : {1}".format(self.name, self.age)

class Employee(Person):    # Person을 상속받음 자식클래스 이름(부모클래스)
    pass

# main()
p1 = Person("손흥민", 30)   # p1(인스턴스, 객체)
print(p1)
p2 = Person("김연아", 31)
print(p2)

emp1 = Employee("흥부", 30)
print(emp1.name)   # name이 Person의 소속인데 Employee 객체가 사용
print(emp1.age)
print(emp1)

emp2 = Employee("놀부", 32)
print(emp2)